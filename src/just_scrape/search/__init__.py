"""Search API endpoint."""

from __future__ import annotations

from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.search import query
from just_scrape.search.response_models import SearchResponse


class Search(BaseEndpoint[SearchResponse]):
    """Provides methods to download, parse, and retrieve search results."""

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
        """Downloads search results for a given query.

        Args:
            search_query: The search string.
            first: Number of results to return.
            search_titles_sort_by: Sort order.
            sort_random_seed: Random seed for sorting.
            search_after_cursor: Cursor for pagination.
            include_titles_without_url: Include titles without a URL.
            person_id: Filter by person ID.
            language: Language code.
            country: Country code.
            location: Source location.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
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
        """Downloads and parses search results for a given query.

        Convenience method that calls ``download()`` then ``parse()``.
        """
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
