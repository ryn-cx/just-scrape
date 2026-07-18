# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.search import Search

SEARCH_QUERY = "Breaking"
"""A search term that matches titles."""
INVALID_SEARCH_QUERY = "zxcvbbnm"


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> Search:
    return client.search


class TestSearch:
    def test_download(self, endpoint: Search) -> None:
        download_and_save(
            endpoint,
            SEARCH_QUERY,
            lambda: endpoint.download(SEARCH_QUERY),
        )

    def test_parse(self, endpoint: Search) -> None:
        data = parse_json(endpoint, SEARCH_QUERY)
        assert data is not None

    # This endpoint does not raise for an unmatched query; it returns an empty
    # result set that is recorded and parsed like any other download.
    def test_invalid_download(self, endpoint: Search) -> None:
        download_and_save(
            endpoint,
            INVALID_SEARCH_QUERY,
            lambda: endpoint.download(INVALID_SEARCH_QUERY),
        )

    def test_invalid_parse(self, endpoint: Search) -> None:
        data = parse_json(endpoint, INVALID_SEARCH_QUERY)
        assert data.data.search_titles.total_count == 0
        assert data.data.search_titles.edges == []


@pytest.mark.parametrize("country", [None, "CA"])
def test_log_id(endpoint: Search, country: str | None) -> None:
    expected = f"Search search_query={SEARCH_QUERY!r}"
    if country is not None:
        expected += f" country={country!r}"
    assert endpoint.get_log_id(SEARCH_QUERY, country=country or "US") == expected
