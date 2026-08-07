# TODO: Validate
"""Recomputes which ids an endpoint's tests actually need.

Every ``test_*.py`` for an endpoint that takes an id calls :func:`update_ids`
from a single test, so a plain ``pytest`` run keeps that endpoint's list in step
with the responses on disk. The call describes only its own endpoint; nothing
here knows the full set.

One pass over an endpoint: adopt any recorded response the list does not mention,
download whatever is still missing, drop the responses that are redundant for
schema generation, then rewrite the list from whatever survived.

To propose an id, add it to ``tests/ids/<endpoint>.json`` and run the tests. It
is downloaded alongside the recorded ones and kept only if it turns out to cover
a shape the others do not, so an id that earns its place stays and one that does
not is removed again.
"""

from __future__ import annotations

import json
import logging
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, cast

from tests.utils import json_path, load_ids, save_ids

if TYPE_CHECKING:
    from collections.abc import Callable, Generator
    from pathlib import Path

    from just_scrape.base_client import BaseEndpoint

logger = logging.getLogger(__name__)

DEPRIORITIZE_PREFIX = "zzz_"
"""Sorts after every recorded id, so prefixed files are pruned first."""


def _identity(id_: str) -> str:
    return id_


def _dig(data: Any, *keys: str) -> Any:  # noqa: ANN401 - Walks arbitrary JSON.
    """Follow a chain of keys, stopping at the first one that is not a mapping."""
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key)
    return data


def node_id_from_response(data: dict[str, Any]) -> str | None:
    """Read back the ``node_id`` an endpoint keyed on ``data.node`` was asked for."""
    node_id = _dig(data, "data", "node", "id")
    return node_id if isinstance(node_id, str) else None


def full_path_from_response(data: dict[str, Any]) -> str | None:
    """Read back the ``full_path`` a ``urlV2`` endpoint was asked for."""
    full_path = _dig(data, "data", "urlV2", "node", "content", "fullPath")
    return full_path if isinstance(full_path, str) else None


@dataclass(frozen=True)
class _EndpointIds:
    """How to refresh the id list of one endpoint.

    Attributes:
        name: Both the endpoint's own name and the id list file stem.
        dead_id_error: Raised by ``download`` for an id the API no longer
            serves, which is then dropped from the list.
        file_name: Maps an id to the stem of the file it is recorded under.
        protected: Stems of files in the same folder that other tests assert on
            individually. They are moved aside while pruning so they can neither
            be deleted nor keep a listed id from being needed.
        id_from_response: Reads an id back out of a recorded response, or None
            when the response does not echo one. This is what lets a response
            recorded under a timestamp rather than an id join the list instead
            of being pruned; see ``_adopt_recorded_ids``.
    """

    name: str
    dead_id_error: type[Exception]
    file_name: Callable[[str], str] = _identity
    protected: tuple[str, ...] = field(default=())
    id_from_response: Callable[[dict[str, Any]], str | None] | None = None


@contextmanager
def _renamed(moves: list[tuple[Path, Path]]) -> Generator[None]:
    """Rename files for the duration of the block, restoring any that survive."""
    for original, temporary in moves:
        temporary.parent.mkdir(parents=True, exist_ok=True)
        original.rename(temporary)
    try:
        yield
    finally:
        for original, temporary in moves:
            if temporary.exists():
                temporary.rename(original)
        # Drop the holding folder, but never the endpoint's own folder, which
        # is where the in-place renames live.
        holders = {
            temporary.parent
            for original, temporary in moves
            if temporary.parent != original.parent
        }
        for holder in holders:
            if holder.is_dir() and not any(holder.iterdir()):
                holder.rmdir()


def _listed_ids_preferred(
    endpoint: BaseEndpoint[Any],
    spec: _EndpointIds,
    listed_stems: set[str],
) -> ExitStack:
    """Set the folder up so pruning only ever decides between listed ids.

    The pruner walks a folder in reverse name order and deletes the first
    redundant file it finds, with no notion of which files the tests depend on.
    Two kinds of file need handling first:

    * Protected files, which other tests assert on by name, are moved out of the
      folder entirely so they neither get deleted nor cover a listed id's shapes.
    * Timestamped responses, recorded automatically whenever the model is
      updated, are renamed to sort last so they are pruned before any listed id.
    """
    folder = endpoint.json_files_folder()
    protected = [
        (folder / f"{stem}.json", folder / "_protected" / f"{stem}.json")
        for stem in spec.protected
        if (folder / f"{stem}.json").exists()
    ]
    deprioritized = [
        (file, file.with_name(DEPRIORITIZE_PREFIX + file.name))
        for file in endpoint.json_files()
        if file.stem not in listed_stems and file.stem not in spec.protected
    ]

    stack = ExitStack()
    stack.enter_context(_renamed(protected))
    stack.enter_context(_renamed(deprioritized))
    return stack


def _adopt_recorded_ids(
    endpoint: BaseEndpoint[Any],
    spec: _EndpointIds,
    listed_stems: set[str],
) -> list[str]:
    """Recover the ids of recorded responses that the id list does not mention.

    A response is recorded automatically whenever it grows the endpoint's model,
    and is named after the moment it arrived rather than after the id it was
    fetched with. Those shapes are exactly the ones worth keeping, but an unlisted
    file is pruned on the next run, so the id is read back out of the response and
    added to the list, with the file renamed to the stem that id maps to.

    Files whose id cannot be recovered are left alone for the pruner to deal with.
    """
    if spec.id_from_response is None:
        return []

    adopted: list[str] = []
    for file in endpoint.json_files():
        if file.stem in listed_stems or file.stem in spec.protected:
            continue
        try:
            data = json.loads(file.read_text())
        except json.JSONDecodeError:
            logger.warning("%s: skipping %s, it is not valid JSON.", spec.name, file)
            continue
        if not isinstance(data, dict):
            continue
        id_ = spec.id_from_response(cast("dict[str, Any]", data))
        if id_ is None:
            continue

        target = json_path(endpoint, spec.file_name(id_))
        # A file already recorded under the id holds the same response, so the
        # duplicate is left for the pruner rather than overwriting it.
        if not target.exists():
            file.rename(target)
        logger.info("%s: adopting %s from %s.", spec.name, id_, file.name)
        adopted.append(id_)

    return adopted


def update_ids(  # noqa: PLR0913 - Each parameter describes one endpoint trait.
    endpoint: BaseEndpoint[Any],
    name: str,
    dead_id_error: type[Exception],
    *,
    file_name: Callable[[str], str] = _identity,
    protected: tuple[str, ...] = (),
    id_from_response: Callable[[dict[str, Any]], str | None] | None = None,
) -> list[str]:
    """Rewrite one endpoint's id list from the responses it actually needs.

    Called from a single test per endpoint, so the list is refreshed by an
    ordinary test run. The rewritten list only takes effect on the next run:
    the tests read it at import time to parametrize over.

    Args:
        endpoint: The endpoint whose recorded responses are being pruned.
        name: The endpoint's name, and the stem of its file in ``tests/ids``.
        dead_id_error: See :class:`_EndpointIds`.
        file_name: See :class:`_EndpointIds`.
        protected: See :class:`_EndpointIds`.
        id_from_response: See :class:`_EndpointIds`.

    Returns:
        The ids that were written back, in sorted order.
    """
    spec = _EndpointIds(
        name=name,
        dead_id_error=dead_id_error,
        file_name=file_name,
        protected=protected,
        id_from_response=id_from_response,
    )

    listed = set(load_ids(name))
    listed_stems = {file_name(id_) for id_ in listed}
    adopted = _adopt_recorded_ids(endpoint, spec, listed_stems)
    ids = sorted(listed | set(adopted))

    # An id the API no longer serves cannot contribute to the schema, so it is
    # dropped rather than retried on every run.
    downloaded: list[str] = []
    for id_ in ids:
        path = json_path(endpoint, file_name(id_))
        if not path.exists():
            logger.info("%s: downloading %s.", name, id_)
            try:
                data = endpoint.download(id_)
            except dead_id_error:
                logger.warning("%s: dropping %s, the API rejects it.", name, id_)
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(data, indent=2))
        downloaded.append(id_)

    stems = {file_name(id_): id_ for id_ in downloaded}
    with _listed_ids_preferred(endpoint, spec, set(stems)):
        endpoint.remove_redundant_json_files()
        survivors = {file.stem for file in endpoint.json_files()}

    required = sorted(stems[stem] for stem in stems if stem in survivors)

    save_ids(name, required)
    logger.info("%s: %s of %s ids required.", name, len(required), len(downloaded))
    return required
