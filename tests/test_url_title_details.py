# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.url_title_details import UrlTitleDetails

INVALID_URL_PATH = "/us/tv-show/invalid-url"

PATHS = [
    "/us/movie/the-thursday-murder-club",
    "/us/tv-show/strip-law",
    "/us/movie/code-geass-akito-the-exiled-5-to-beloved-ones",
    "/us/tv-show/darker-than-black",
    "/us/tv-show/aria-the-animation",
    "/us/tv-show/frieren-beyond-journeys-end",
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
        data = parsed_json(endpoint, _name(full_path))
        assert data.data.url_v2.node.content.full_path == full_path

    def test_invalid_download(self, endpoint: UrlTitleDetails) -> None:
        assert_error(
            endpoint,
            _name(INVALID_URL_PATH),
            lambda: endpoint.download(INVALID_URL_PATH),
            GraphQLError,
        )
