"""New Title Buckets API endpoint."""

from __future__ import annotations

from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.new_title_buckets import query
from just_scrape.new_title_buckets.response_models import NewTitleBucketsResponse


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
