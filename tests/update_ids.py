# TODO: Validate
"""Recomputes which ids the tests actually need.

For each endpoint: downloads every id in ``tests/ids``, drops the recorded
responses that are redundant for schema generation, then rewrites the list from
whatever survived. Ids left out of the file are neither downloaded nor tested,
so this is the only way to add one.

Usage::

    uv run python -m tests.update_ids                        # every endpoint
    uv run python -m tests.update_ids ENDPOINT [NEW_ID ...]

Ids given on the command line are downloaded alongside the recorded ones and
kept only if they turn out to add something the others do not cover, so
proposing an id and pruning the list is a single command.
"""

from __future__ import annotations

import json
import logging
import sys
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from get_around import build_client_automatically

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError, InvalidFileError
from tests.utils import json_path, load_ids, path_name, save_ids

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from pathlib import Path

    from just_scrape.base_client import BaseEndpoint

logger = logging.getLogger(__name__)

DEPRIORITIZE_PREFIX = "zzz_"
"""Sorts after every recorded id, so prefixed files are pruned first."""


def _identity(id_: str) -> str:
    return id_


@dataclass(frozen=True)
class EndpointIds:
    """How to refresh the id list of one endpoint.

    Attributes:
        name: Both the ``JustScrape`` attribute and the id list file stem.
        dead_id_error: Raised by ``download`` for an id the API no longer
            serves, which is then dropped from the list.
        file_name: Maps an id to the stem of the file it is recorded under.
        protected: Stems of files in the same folder that other tests assert on
            individually. They are moved aside while pruning so they can neither
            be deleted nor keep a listed id from being needed.
    """

    name: str
    dead_id_error: type[Exception]
    file_name: Callable[[str], str] = _identity
    protected: tuple[str, ...] = field(default=())


# new_titles and new_title_buckets are absent on purpose: neither download()
# takes an id, so each records a single file and there is nothing to prune.
ENDPOINTS = (
    EndpointIds("buy_box_offers", InvalidFileError),
    EndpointIds("season_episodes", InvalidFileError),
    EndpointIds("url_title_details", GraphQLError, file_name=path_name),
    EndpointIds("title_detail_article", GraphQLError, file_name=path_name),
    # An unmatched query is recorded and asserted on rather than raising.
    EndpointIds("search", GraphQLError, protected=("zxcvbbnm",)),
)


@contextmanager
def _renamed(moves: list[tuple[Path, Path]]) -> Iterator[None]:
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
    spec: EndpointIds,
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


def update_endpoint(
    client: JustScrape,
    spec: EndpointIds,
    extra_ids: list[str],
) -> None:
    """Download every id, prune the redundant ones, rewrite the id list."""
    endpoint: BaseEndpoint[Any] = getattr(client, spec.name)
    ids = sorted(set(load_ids(spec.name)) | set(extra_ids))

    # An id the API no longer serves cannot contribute to the schema, so it is
    # dropped rather than retried on every run.
    downloaded: list[str] = []
    for id_ in ids:
        path = json_path(endpoint, spec.file_name(id_))
        if not path.exists():
            logger.info("%s: downloading %s.", spec.name, id_)
            try:
                data = endpoint.download(id_)
            except spec.dead_id_error:
                logger.warning("%s: dropping %s, the API rejects it.", spec.name, id_)
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(data, indent=2))
        downloaded.append(id_)

    stems = {spec.file_name(id_): id_ for id_ in downloaded}
    with _listed_ids_preferred(endpoint, spec, set(stems)):
        endpoint.remove_redundant_json_files()
        survivors = {file.stem for file in endpoint.json_files()}

    required = [stems[stem] for stem in stems if stem in survivors]

    save_ids(spec.name, required)
    logger.info(
        "%s: %s of %s ids required.",
        spec.name,
        len(required),
        len(downloaded),
    )


def main(argv: list[str]) -> None:
    """Update one named endpoint, or every endpoint when given no arguments."""
    if argv:
        wanted, extra_ids = argv[0], argv[1:]
        specs = [spec for spec in ENDPOINTS if spec.name == wanted]
        if not specs:
            names = ", ".join(spec.name for spec in ENDPOINTS)
            message = f"Unknown endpoint {wanted!r}. Known endpoints: {names}."
            raise SystemExit(message)
    else:
        specs, extra_ids = list(ENDPOINTS), []

    client = JustScrape(get_around_client=build_client_automatically())
    for spec in specs:
        update_endpoint(client, spec, extra_ids)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main(sys.argv[1:])
