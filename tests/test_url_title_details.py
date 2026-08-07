# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError
from tests.update_ids import full_path_from_response, update_ids
from tests.utils import (
    assert_error,
    download_and_save,
    load_ids,
    parsed_json,
    path_name,
)

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.url_title_details import UrlTitleDetails

INVALID_URL_PATH = "/us/tv-show/invalid-url"

PATHS = load_ids("url_title_details")
"""Rewritten by ``test_update_ids``; add an id here and run the tests."""


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> UrlTitleDetails:
    return client.url_title_details


@pytest.fixture(params=PATHS)
def full_path(request: pytest.FixtureRequest) -> str:
    return request.param


def test_download(endpoint: UrlTitleDetails, full_path: str) -> None:
    download_and_save(
        endpoint,
        path_name(full_path),
        lambda: endpoint.download(full_path),
    )


def test_parse(endpoint: UrlTitleDetails, full_path: str) -> None:
    data = parsed_json(endpoint, path_name(full_path))
    assert data.data.url_v2.node.content.full_path == full_path


def test_invalid_download(endpoint: UrlTitleDetails) -> None:
    assert_error(
        endpoint,
        path_name(INVALID_URL_PATH),
        lambda: endpoint.download(INVALID_URL_PATH),
        GraphQLError,
    )


def test_update_ids(endpoint: UrlTitleDetails) -> None:
    assert update_ids(
        endpoint,
        "url_title_details",
        GraphQLError,
        file_name=path_name,
        id_from_response=full_path_from_response,
    )
