# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.title_detail_article import TitleDetailArticle

MOVIE_PATH = "/us/movie/the-thursday-murder-club"
"""URL path for a movie title."""
MOVIE_NAME = MOVIE_PATH.strip("/").replace("/", "_")
"""Filesystem-safe cache name for MOVIE_PATH."""
INVALID_MOVIE_PATH = "/us/movie/invalid-movie"
INVALID_MOVIE_NAME = INVALID_MOVIE_PATH.strip("/").replace("/", "_")
"""Filesystem-safe cache name for INVALID_MOVIE_PATH."""


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> TitleDetailArticle:
    return client.title_detail_article


class TestTitleDetailArticle:
    def test_download(self, endpoint: TitleDetailArticle) -> None:
        download_and_save(
            endpoint,
            MOVIE_NAME,
            lambda: endpoint.download(MOVIE_PATH),
        )

    def test_parse(self, endpoint: TitleDetailArticle) -> None:
        data = parse_json(endpoint, MOVIE_NAME)
        assert data is not None

    def test_invalid_download(self, endpoint: TitleDetailArticle) -> None:
        assert_error(
            endpoint,
            INVALID_MOVIE_NAME,
            lambda: endpoint.download(INVALID_MOVIE_PATH),
            GraphQLError,
        )


@pytest.mark.parametrize("country", [None, "CA"])
def test_log_id(endpoint: TitleDetailArticle, country: str | None) -> None:
    expected = f"TitleDetailArticle full_path={MOVIE_PATH!r}"
    if country is not None:
        expected += f" country={country!r}"
    assert endpoint.get_log_id(MOVIE_PATH, country=country or "US") == expected
