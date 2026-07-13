# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from tests.utils import download_if_missing

if TYPE_CHECKING:
    from just_scrape.search import Search

client = JustScrape(get_around_client=build_client_automatically())

SEARCH_QUERY = "Breaking"
"""A search term that matches titles."""
INVALID_SEARCH_QUERY = "zxcvbbnm"


@pytest.fixture(scope="session")
def endpoint() -> Search:
    return client.search


class TestSearch:
    def test_download(self, endpoint: Search) -> None:
        download_if_missing(
            endpoint,
            SEARCH_QUERY,
            lambda: endpoint.download(SEARCH_QUERY),
        )

    def test_invalid(self, endpoint: Search) -> None:
        path = download_if_missing(
            endpoint,
            INVALID_SEARCH_QUERY,
            lambda: endpoint.download(INVALID_SEARCH_QUERY),
        )
        data = endpoint.parse(json.loads(path.read_text()))
        assert data.data.search_titles.total_count == 0
        assert data.data.search_titles.edges == []
