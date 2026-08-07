# TODO: Validate
"""Utils."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from just_scrape.constants import FILES_PATH

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any

    from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

    from just_scrape.base_client import BaseEndpoint

IDS_PATH = Path(__file__).parent / "ids"
"""Folder holding the per-endpoint id lists.

Each file lists the ids whose recorded responses are needed to completely build
that endpoint's model, and so the ids the tests parametrize over. An "id" is
whatever ``download`` takes to identify one response: a node id, a URL path or a
search query, depending on the endpoint. Each list is rewritten by its own
endpoint's ``test_update_ids``; add an id to the file to have it downloaded and
kept if it covers a shape the others do not.
"""


def ids_path(endpoint_name: str) -> Path:
    return IDS_PATH / f"{endpoint_name}.json"


def load_ids(endpoint_name: str) -> list[str]:
    """Load the required ids for an endpoint."""
    content: list[str] = json.loads(ids_path(endpoint_name).read_text())
    return content


def save_ids(endpoint_name: str, ids: list[str]) -> None:
    """Write the required ids for an endpoint back to disk, sorted and deduplicated."""
    path = ids_path(endpoint_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(sorted(set(ids)), indent=2) + "\n")


def path_name(full_path: str) -> str:
    """Filesystem-safe cache name for a URL path id."""
    return full_path.strip("/").replace("/", "_")


def json_path(
    endpoint: GAPIClient[Any],
    name: str,
    *,
    folder: str | None = None,
) -> Path:
    if folder is not None:
        return FILES_PATH / folder / f"{name}.json"
    return endpoint.json_files_folder() / f"{name}.json"


def parsed_json[T: GAPIBaseModel](endpoint: BaseEndpoint[T], name: str) -> T:
    path = json_path(endpoint, name)
    return endpoint.parse(json.loads(path.read_text()))


# The loaders below produce each input shape that an extract helper accepts,
# so extraction tests can parametrize over a single load callable.
def single_dict(endpoint: BaseEndpoint[Any], name: str) -> dict[str, Any]:
    """A single recorded page as a raw dict."""
    return json.loads(json_path(endpoint, name).read_text())


def page_dicts(
    endpoint: BaseEndpoint[Any],
    name: str,
    *,
    folder: str | None = None,
) -> list[dict[str, Any]]:
    """Recorded page(s) as a list of raw dicts, wrapping a single page."""
    content: list[dict[str, Any]] | dict[str, Any] = json.loads(
        json_path(endpoint, name, folder=folder).read_text(),
    )
    return content if isinstance(content, list) else [content]


def page_models[T: GAPIBaseModel](
    endpoint: BaseEndpoint[T],
    name: str,
    *,
    folder: str | None = None,
) -> list[T]:
    """Recorded page(s) as a list of parsed models, wrapping a single page."""
    return [endpoint.parse(page) for page in page_dicts(endpoint, name, folder=folder)]


def download_and_save(
    endpoint: GAPIClient[Any],
    name: str,
    get: Callable[[], dict[str, Any] | list[dict[str, Any]]],
    *,
    folder: str | None = None,
) -> Path:
    path = json_path(endpoint, name, folder=folder)
    if path.exists():
        pytest.skip(f"File already recorded for {type(endpoint).__name__}/{name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(get(), indent=2))
    return path


def assert_error(
    endpoint: GAPIClient[Any],
    name: str,
    download: Callable[[], object],
    error: type[Exception],
) -> None:
    if get_error_path(endpoint, name).exists():
        pytest.skip(f"File already recorded for {type(endpoint).__name__}/{name}")
    with pytest.raises(error) as excinfo:
        download()
    record_error(endpoint, name, getattr(excinfo.value, "response", None))


def get_error_path(endpoint: GAPIClient[Any], name: str) -> Path:
    folder = f"Errors/{endpoint.json_files_folder().name}"
    return json_path(endpoint, name, folder=folder)


def record_error(
    endpoint: GAPIClient[Any],
    name: str,
    data: Any = None,  # noqa: ANN401 - A recorded response can be any JSON value.
) -> None:
    path = get_error_path(endpoint, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(data, indent=2) if data is not None else ""
    path.write_text(content)
