# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from just_scrape.base_api_endpoint import BaseEndpoint
from just_scrape.exceptions import InvalidFileError, JustScrapeError
from just_scrape.search import query
from just_scrape.search.models import SearchModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_titles(response: str) -> dict[str, Any]:
    """Extract the search results from the Search response."""
    if titles := json.loads(response)["data"]["searchTitles"]:
        return titles

    msg = "The response has no search results in it"
    raise JustScrapeError(msg)


# TODO: Validate
class Search(BaseEndpoint):
    """Contains the search.

    Source: https://www.justwatch.com/us/search?q={query}

    Example request:
        - POST /graphql HTTP/2
        - Host: apis.justwatch.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Content-Type: application/json
        - Referer: https://www.justwatch.com/
        - Origin: https://www.justwatch.com
        - Body:
            - operationName: GetSearchTitles
            - query: the document in `query.py`
            - variables:
                - searchTitlesFilter.searchQuery={query}
                - first=5
                - searchTitlesSortBy=POPULAR
                - country=US
                - language=en
                - location=SearchPage
    """

    # TODO: Validate
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        search_query: str,
        *,
        first: int = 5,
        search_titles_sort_by: str = "POPULAR",
        sort_random_seed: int = 0,
        search_after_cursor: str = "",
        include_titles_without_url: bool = True,
        person_id: str | None = None,
        language: str = "en",
        country: str = "US",
        location: str = "SearchPage",
    ) -> SearchModel:
        """Download and parse the search file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                search_query,
                first=first,
                search_titles_sort_by=search_titles_sort_by,
                sort_random_seed=sort_random_seed,
                search_after_cursor=search_after_cursor,
                include_titles_without_url=include_titles_without_url,
                person_id=person_id,
                language=language,
                country=country,
                location=location,
            ),
            log_id,
        )

    # TODO: Validate
    def download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        search_query: str,
        *,
        first: int = 5,
        search_titles_sort_by: str = "POPULAR",
        sort_random_seed: int = 0,
        search_after_cursor: str = "",
        include_titles_without_url: bool = True,
        person_id: str | None = None,
        language: str = "en",
        country: str = "US",
        location: str = "SearchPage",
    ) -> str:
        """Download the search file."""
        log_id = self.get_log_id(self.download, locals())
        response = self._client.download(
            "GetSearchTitles",
            query.QUERY,
            {
                "first": first,
                "searchTitlesSortBy": search_titles_sort_by,
                "sortRandomSeed": sort_random_seed,
                "searchAfterCursor": search_after_cursor,
                "searchTitlesFilter": {
                    "searchQuery": search_query,
                    "personId": person_id,
                    "includeTitlesWithoutUrl": include_titles_without_url,
                },
                "language": language,
                "country": country,
                "location": location,
            },
            log_id,
        )
        return self._validate_download(response)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str) -> str:
        # The response carries no echo of the query, so only its shape is
        # checked. A query nothing matches is answered with an empty page.
        search_titles = json.loads(response).get("data", {}).get("searchTitles", {})
        if search_titles.get("edges") is None:
            raise InvalidFileError(field="search titles", response=response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchModel:
        """Load a search file into its model."""
        return model_validate_json(
            extract_titles(data),
            log_id or self.default_log_id,
        )
