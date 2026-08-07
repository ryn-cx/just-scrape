# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError
from tests.update_ids import update_ids
from tests.utils import (
    assert_error,
    download_and_save,
    load_ids,
    parsed_json,
    path_name,
)

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.title_detail_article import TitleDetailArticle

INVALID_MOVIE_PATH = "/us/movie/invalid-movie"

PATHS = load_ids("title_detail_article")
"""Rewritten by ``test_update_ids``; add an id here and run the tests."""


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> TitleDetailArticle:
    return client.title_detail_article


@pytest.fixture(params=PATHS)
def full_path(request: pytest.FixtureRequest) -> str:
    return request.param


def test_download(endpoint: TitleDetailArticle, full_path: str) -> None:
    download_and_save(
        endpoint,
        path_name(full_path),
        lambda: endpoint.download(full_path),
    )


def test_parse(endpoint: TitleDetailArticle, full_path: str) -> None:
    data = parsed_json(endpoint, path_name(full_path))
    assert data is not None


def test_invalid_download(endpoint: TitleDetailArticle) -> None:
    assert_error(
        endpoint,
        path_name(INVALID_MOVIE_PATH),
        lambda: endpoint.download(INVALID_MOVIE_PATH),
        GraphQLError,
    )


# No id_from_response: the response echoes back neither the path it was fetched
# with nor anything else an id could be rebuilt from.
def test_update_ids(endpoint: TitleDetailArticle) -> None:
    assert update_ids(
        endpoint,
        "title_detail_article",
        GraphQLError,
        file_name=path_name,
    )
