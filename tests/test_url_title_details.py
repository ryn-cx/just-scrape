# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.url_title_details import UrlTitleDetails

MOVIE_PATH = "/us/movie/the-thursday-murder-club"
"""URL path for a movie title."""
TV_SHOW_PATH = "/us/tv-show/strip-law"
"""URL path for a TV show title."""
UNAVAILABLE_MOVIE_PATH = "/us/movie/code-geass-akito-the-exiled-5-to-beloved-ones"
"""URL path for a movie that is not available."""
UNAVAILABLE_TV_SHOW_PATH = "/us/tv-show/darker-than-black"
"""URL path for a TV show that is not available."""
INVALID_URL_PATH = "/us/tv-show/invalid-url"

PATHS = [
    pytest.param(MOVIE_PATH, id="movie"),
    pytest.param(TV_SHOW_PATH, id="tv-show"),
    pytest.param(UNAVAILABLE_MOVIE_PATH, id="unavailable-movie"),
    pytest.param(UNAVAILABLE_TV_SHOW_PATH, id="unavailable-tv-show"),
]


def _name(full_path: str) -> str:
    return full_path.strip("/").replace("/", "_")


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> UrlTitleDetails:
    return client.url_title_details


class TestUrlTitleDetails:
    @pytest.mark.parametrize("full_path", PATHS)
    def test_download(self, endpoint: UrlTitleDetails, full_path: str) -> None:
        download_and_save(
            endpoint,
            _name(full_path),
            lambda: endpoint.download(full_path),
        )

    @pytest.mark.parametrize("full_path", PATHS)
    def test_parse(self, endpoint: UrlTitleDetails, full_path: str) -> None:
        data = parse_json(endpoint, _name(full_path))
        assert data is not None

    def test_invalid_download(self, endpoint: UrlTitleDetails) -> None:
        assert_error(
            endpoint,
            _name(INVALID_URL_PATH),
            lambda: endpoint.download(INVALID_URL_PATH),
            GraphQLError,
        )


@pytest.mark.parametrize("country", [None, "CA"])
def test_log_id(endpoint: UrlTitleDetails, country: str | None) -> None:
    expected = f"UrlTitleDetails full_path={MOVIE_PATH!r}"
    if country is not None:
        expected += f" country={country!r}"
    assert endpoint.get_log_id(MOVIE_PATH, country=country or "US") == expected
