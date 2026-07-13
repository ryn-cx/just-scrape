# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from tests.utils import assert_graphql_error, data_path, download_if_missing

if TYPE_CHECKING:
    from just_scrape.url_title_details import UrlTitleDetails

client = JustScrape(get_around_client=build_client_automatically())

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


@pytest.fixture(scope="session")
def endpoint() -> UrlTitleDetails:
    return client.url_title_details


class TestUrlTitleDetails:
    @pytest.mark.parametrize("full_path", PATHS)
    def test_download(self, endpoint: UrlTitleDetails, full_path: str) -> None:
        name = full_path.strip("/").replace("/", "_")
        download_if_missing(
            endpoint,
            name,
            lambda: endpoint.download(full_path),
        )

    @pytest.mark.parametrize("full_path", PATHS)
    def test_parse(self, endpoint: UrlTitleDetails, full_path: str) -> None:
        name = full_path.strip("/").replace("/", "_")
        data = endpoint.parse(json.loads(data_path(endpoint, name).read_text()))
        assert data is not None

    def test_invalid(self, endpoint: UrlTitleDetails) -> None:
        name = INVALID_URL_PATH.strip("/").replace("/", "_")
        assert_graphql_error(
            endpoint,
            name,
            lambda: endpoint.download(INVALID_URL_PATH),
        )
