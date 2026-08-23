# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.search.models import SearchModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from just_scrape import JustScrape

QUERIES = [
    pytest.param("Frieren", id="query with matches"),
    # A query nothing matches is answered with an empty page rather than an error.
    pytest.param("zxcvbbnm", id="query with no matches"),
]


# TODO: Validate
class SearchTest(RecordedEndpoint):
    MODEL = SearchModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: JustScrape, query: str) -> None:
    SearchTest.download_test(query, lambda: client.search.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(client: JustScrape, query: str) -> None:
    data = client.search.load(SearchTest.recorded_content(query))
    search_titles = data.data.search_titles
    assert bool(search_titles.edges) == bool(search_titles.total_count)
