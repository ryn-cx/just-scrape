# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError
from tests.update_ids import update_ids
from tests.utils import download_and_save, load_ids, parsed_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.search import Search

INVALID_SEARCH_QUERY = "zxcvbbnm"

SEARCH_QUERIES = load_ids("search")
"""Search terms that match titles.

Rewritten by ``test_update_ids``; add an id here and run the tests.
"""


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> Search:
    return client.search


@pytest.fixture(params=SEARCH_QUERIES)
def search_query(request: pytest.FixtureRequest) -> str:
    return request.param


def test_download(endpoint: Search, search_query: str) -> None:
    download_and_save(
        endpoint,
        search_query,
        lambda: endpoint.download(search_query),
    )


def test_parse(endpoint: Search, search_query: str) -> None:
    data = parsed_json(endpoint, search_query)
    assert data is not None


# This endpoint does not raise for an unmatched query; it returns an empty result
# set that is recorded and parsed like any other download.
def test_invalid_download(endpoint: Search) -> None:
    download_and_save(
        endpoint,
        INVALID_SEARCH_QUERY,
        lambda: endpoint.download(INVALID_SEARCH_QUERY),
    )


def test_invalid_parse(endpoint: Search) -> None:
    data = parsed_json(endpoint, INVALID_SEARCH_QUERY)
    assert data.data.search_titles.total_count == 0
    assert data.data.search_titles.edges == []


# No id_from_response: the response carries no echo of the query it answered.
# The unmatched query is protected because test_invalid_parse asserts on it by
# name, so pruning must neither delete it nor count its shapes against a listed id.
def test_update_ids(endpoint: Search) -> None:
    assert update_ids(
        endpoint,
        "search",
        GraphQLError,
        protected=(INVALID_SEARCH_QUERY,),
    )
