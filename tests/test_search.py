# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from just_scrape import JustScrape

QUERIES = [
    pytest.param("Frieren", id="query with matches"),
    # A query nothing matches is answered with an empty page rather than an error.
    pytest.param("zxcvbbnm", id="query with no matches"),
]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: JustScrape, query: str) -> None:
    titles = client.search(query)
    assert bool(titles.edges) == bool(titles.total_count)
