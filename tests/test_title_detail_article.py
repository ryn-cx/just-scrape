# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from tests.utils import assert_graphql_error, data_path, download_if_missing

if TYPE_CHECKING:
    from just_scrape.title_detail_article import TitleDetailArticle

client = JustScrape(get_around_client=build_client_automatically())

MOVIE_PATH = "/us/movie/the-thursday-murder-club"
"""URL path for a movie title."""
MOVIE_NAME = MOVIE_PATH.strip("/").replace("/", "_")
"""Filesystem-safe cache name for MOVIE_PATH."""
INVALID_MOVIE_PATH = "/us/movie/invalid-movie"
INVALID_MOVIE_NAME = INVALID_MOVIE_PATH.strip("/").replace("/", "_")
"""Filesystem-safe cache name for INVALID_MOVIE_PATH."""


@pytest.fixture(scope="session")
def endpoint() -> TitleDetailArticle:
    return client.title_detail_article


class TestTitleDetailArticle:
    def test_download(self, endpoint: TitleDetailArticle) -> None:
        download_if_missing(
            endpoint,
            MOVIE_NAME,
            lambda: endpoint.download(MOVIE_PATH),
        )

    def test_parse(self, endpoint: TitleDetailArticle) -> None:
        data = endpoint.parse(
            json.loads(data_path(endpoint, MOVIE_NAME).read_text()),
        )
        assert data is not None

    def test_invalid(self, endpoint: TitleDetailArticle) -> None:
        assert_graphql_error(
            endpoint,
            INVALID_MOVIE_NAME,
            lambda: endpoint.download(INVALID_MOVIE_PATH),
        )
