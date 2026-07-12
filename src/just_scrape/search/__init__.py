# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.search import query
from just_scrape.search.models import SearchResponse


class Search(BaseEndpoint[SearchResponse]):
    """Manage the search file."""

    _response_model = SearchResponse

    # PLR0913 - Each parameter maps to an API parameter.
    def download(  # noqa: PLR0913
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
    ) -> dict[str, Any]:
        """Downloads the search file."""
        return self._client.download(
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
                    "includeTitlesWithoutUrl": (include_titles_without_url),
                },
                "language": language,
                "country": country,
                "location": location,
            },
            log_id=f"{self.__class__.__name__} {search_query}",
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def get(  # noqa: PLR0913
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
    ) -> SearchResponse:
        """Downloads and parses the search file."""
        data = self.download(
            search_query=search_query,
            first=first,
            search_titles_sort_by=search_titles_sort_by,
            sort_random_seed=sort_random_seed,
            search_after_cursor=search_after_cursor,
            include_titles_without_url=include_titles_without_url,
            person_id=person_id,
            language=language,
            country=country,
            location=location,
        )
        return self.parse(data)
