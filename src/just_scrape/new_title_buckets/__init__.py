# As of 3/13/2026 API is broken server side and returns a truncated set of results if
# objectTypes is empty. Set to "SHOW_SEASON" or "MOVIE" to fix pagination. This is a
# server side bug because the website itself is broken
# https://www.justwatch.com/us/tv-shows/new
"""New Title Buckets API endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.new_title_buckets import query
from just_scrape.new_title_buckets.response_models import NewTitleBucketsResponse

if TYPE_CHECKING:
    import datetime

    from just_scrape.new_title_buckets.response_models import Edge


class NewTitleBuckets(BaseEndpoint[NewTitleBucketsResponse]):
    """Provides methods to download, parse, and retrieve new title buckets data."""

    _response_model = NewTitleBucketsResponse

    # PLR0913 - Each parameter maps to an API parameter.
    def download(  # noqa: PLR0913
        self,
        *,
        first: int = 8,
        bucket_size: int = 0,
        group_by: str = "DATE_PACKAGE",
        page_type: str = "NEW",
        country: str = "US",
        new_after_cursor: str = "",
        price_drops: bool = False,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[None] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> dict[str, Any]:
        """Downloads new title buckets data.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        return self._client.download(
            "GetNewTitleBuckets",
            query.QUERY,
            {
                "first": first,
                "bucketSize": bucket_size,
                "groupBy": group_by,
                "pageType": page_type,
                "country": country,
                "newAfterCursor": new_after_cursor,
                "newTitlesFilter": {
                    "ageCertifications": filter_age_certifications or [],
                    "excludeGenres": filter_exclude_genres or [],
                    "excludeProductionCountries": (
                        filter_exclude_production_countries or []
                    ),
                    "objectTypes": filter_object_types or [],
                    "productionCountries": filter_production_countries or [],
                    "subgenres": filter_subgenres or [],
                    "genres": filter_genres or [],
                    "packages": filter_packages or [],
                    "excludeIrrelevantTitles": filter_exclude_irrelevant_titles,
                    "presentationTypes": filter_presentation_types or [],
                    "monetizationTypes": filter_monetization_types or [],
                },
                "priceDrops": price_drops,
            },
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def get(  # noqa: PLR0913
        self,
        *,
        first: int = 8,
        bucket_size: int = 0,
        group_by: str = "DATE_PACKAGE",
        page_type: str = "NEW",
        country: str = "US",
        new_after_cursor: str = "",
        price_drops: bool = False,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[None] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> NewTitleBucketsResponse:
        """Downloads and parses new title buckets data.

        Convenience method that calls ``download()`` then ``parse()``.
        """
        data = self.download(
            first=first,
            bucket_size=bucket_size,
            group_by=group_by,
            page_type=page_type,
            country=country,
            new_after_cursor=new_after_cursor,
            price_drops=price_drops,
            filter_age_certifications=filter_age_certifications,
            filter_exclude_genres=filter_exclude_genres,
            filter_exclude_production_countries=filter_exclude_production_countries,
            filter_object_types=filter_object_types,
            filter_production_countries=filter_production_countries,
            filter_subgenres=filter_subgenres,
            filter_genres=filter_genres,
            filter_packages=filter_packages,
            filter_exclude_irrelevant_titles=filter_exclude_irrelevant_titles,
            filter_presentation_types=filter_presentation_types,
            filter_monetization_types=filter_monetization_types,
        )
        return self.parse(data)

    # PLR0913 - Each parameter maps to an API parameter.
    def get_all_since_date(  # noqa: PLR0913
        self,
        end_date: datetime.date,
        *,
        first: int = 8,
        bucket_size: int = 0,
        group_by: str = "DATE_PACKAGE",
        page_type: str = "NEW",
        country: str = "US",
        price_drops: bool = False,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[None] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> list[NewTitleBucketsResponse]:
        """Downloads and parses all new title buckets since a date."""
        new_after_cursor = ""
        output: list[NewTitleBucketsResponse] = []

        while True:
            parsed = self.get(
                first=first,
                bucket_size=bucket_size,
                group_by=group_by,
                page_type=page_type,
                country=country,
                new_after_cursor=new_after_cursor,
                price_drops=price_drops,
                filter_age_certifications=filter_age_certifications,
                filter_exclude_genres=filter_exclude_genres,
                filter_exclude_production_countries=filter_exclude_production_countries,
                filter_object_types=filter_object_types,
                filter_production_countries=filter_production_countries,
                filter_subgenres=filter_subgenres,
                filter_genres=filter_genres,
                filter_packages=filter_packages,
                filter_exclude_irrelevant_titles=filter_exclude_irrelevant_titles,
                filter_presentation_types=filter_presentation_types,
                filter_monetization_types=filter_monetization_types,
            )
            output.append(parsed)

            last_edge = parsed.data.new_title_buckets.edges[-1]
            if last_edge.key.date < end_date:
                return output

            if not parsed.data.new_title_buckets.page_info.has_next_page:
                return output

            new_after_cursor = parsed.data.new_title_buckets.page_info.end_cursor

    def extract_edges(
        self,
        data: NewTitleBucketsResponse | list[NewTitleBucketsResponse],
    ) -> list[Edge]:
        """Get all of the edges for a new title buckets input."""
        if isinstance(data, list):
            result: list[Edge] = []
            for resp in data:
                result.extend(self.extract_edges(resp))
            return result

        if isinstance(data, dict):
            data = self.parse(data)

        return data.data.new_title_buckets.edges
