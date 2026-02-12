"""New Titles API endpoint."""

from __future__ import annotations

import datetime
from functools import cached_property
from typing import Any, override

from just_scrape.base_client import BaseEndpoint
from just_scrape.new_titles import query
from just_scrape.new_titles.request.models import Filter, Variables
from just_scrape.new_titles.response.models import Edge, NewTitlesResponse


class NewTitles(BaseEndpoint[NewTitlesResponse]):
    """Provides methods to download, parse, and retrieve new titles data."""

    @cached_property
    @override
    def _response_model(self) -> type[NewTitlesResponse]:
        return NewTitlesResponse

    @cached_property
    @override
    def _response_model_folder_name(self) -> str:
        return "new_titles/response"

    def download(
        self,
        *,
        first: int = 10,
        page_type: str = "NEW",
        date: datetime.date | None = None,
        language: str = "en",
        country: str = "US",
        price_drops: bool = False,
        platform: str = "WEB",
        after: str | None = None,
        show_date_badge: bool = False,
        available_to_packages: list[str] | None = None,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> dict[str, Any]:
        """Downloads new titles data.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        date = date or datetime.datetime.now(tz=datetime.UTC).date()
        available_to_packages = available_to_packages or []
        filter_age_certifications = filter_age_certifications or []
        filter_exclude_genres = filter_exclude_genres or []
        filter_exclude_production_countries = filter_exclude_production_countries or []
        filter_object_types = filter_object_types or []
        filter_production_countries = filter_production_countries or []
        filter_subgenres = filter_subgenres or []
        filter_genres = filter_genres or []
        filter_packages = filter_packages or []
        filter_presentation_types = filter_presentation_types or []
        filter_monetization_types = filter_monetization_types or []

        filter_obj = Filter(
            ageCertifications=filter_age_certifications,
            excludeGenres=filter_exclude_genres,
            excludeProductionCountries=filter_exclude_production_countries,
            objectTypes=filter_object_types,
            productionCountries=filter_production_countries,
            subgenres=filter_subgenres,
            genres=filter_genres,
            packages=filter_packages,
            excludeIrrelevantTitles=filter_exclude_irrelevant_titles,
            presentationTypes=filter_presentation_types,
            monetizationTypes=filter_monetization_types,
        )

        variables = Variables(
            after=after,
            first=first,
            pageType=page_type,
            date=date,
            filter=filter_obj,
            language=language,
            country=country,
            priceDrops=price_drops,
            platform=platform,
            showDateBadge=show_date_badge,
            availableToPackages=available_to_packages,
        )

        return self._client.download_graphql_request(
            "GetNewTitles",
            query.QUERY,
            variables,
        )

    def get(
        self,
        *,
        first: int = 10,
        page_type: str = "NEW",
        date: datetime.date | None = None,
        language: str = "en",
        country: str = "US",
        price_drops: bool = False,
        platform: str = "WEB",
        show_date_badge: bool = False,
        available_to_packages: list[str] | None = None,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
        after: str | None = None,
    ) -> NewTitlesResponse:
        """Downloads and parses new titles data.

        Convenience method that calls ``download()`` then ``parse()``.
        """
        data = self.download(
            first=first,
            page_type=page_type,
            date=date,
            language=language,
            after=after,
            country=country,
            price_drops=price_drops,
            platform=platform,
            show_date_badge=show_date_badge,
            available_to_packages=available_to_packages,
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

    def get_all_for_date(
        self,
        *,
        first: int = 10,
        page_type: str = "NEW",
        language: str = "en",
        country: str = "US",
        price_drops: bool = False,
        platform: str = "WEB",
        show_date_badge: bool = False,
        available_to_packages: list[str] | None = None,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
        date: datetime.date | None = None,
    ) -> list[NewTitlesResponse]:
        """Downloads and parses all new titles for a specific date."""
        after = None
        output: list[NewTitlesResponse] = []

        while True:
            parsed = self.get(
                first=first,
                after=after,
                available_to_packages=available_to_packages,
                country=country,
                date=date,
                filter_age_certifications=filter_age_certifications,
                filter_exclude_genres=filter_exclude_genres,
                filter_exclude_irrelevant_titles=filter_exclude_irrelevant_titles,
                filter_exclude_production_countries=filter_exclude_production_countries,
                filter_genres=filter_genres,
                filter_monetization_types=filter_monetization_types,
                filter_object_types=filter_object_types,
                filter_packages=filter_packages,
                filter_presentation_types=filter_presentation_types,
                filter_production_countries=filter_production_countries,
                filter_subgenres=filter_subgenres,
                language=language,
                page_type=page_type,
                platform=platform,
                price_drops=price_drops,
                show_date_badge=show_date_badge,
            )
            output.append(parsed)

            if not parsed.data.new_titles.page_info.has_next_page:
                return output

            after = parsed.data.new_titles.page_info.end_cursor

    def get_all_since_date(
        self,
        *,
        first: int = 10,
        page_type: str = "NEW",
        language: str = "en",
        country: str = "US",
        price_drops: bool = False,
        platform: str = "WEB",
        show_date_badge: bool = False,
        available_to_packages: list[str] | None = None,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
        # Specialized parameters for this function.
        start_date: datetime.date | None = None,
        end_date: datetime.date,
    ) -> list[list[NewTitlesResponse]]:
        """Downloads and parses all new titles for a specific date range."""
        current_date = start_date or datetime.datetime.now(tz=datetime.UTC).date()
        output: list[list[NewTitlesResponse]] = []

        while current_date >= end_date:
            response = self.get_all_for_date(
                first=first,
                page_type=page_type,
                date=current_date,
                language=language,
                country=country,
                price_drops=price_drops,
                platform=platform,
                show_date_badge=show_date_badge,
                available_to_packages=available_to_packages,
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

            output.append(response)

            current_date -= datetime.timedelta(days=1)

        return output

    def extract_edges(
        self,
        data: NewTitlesResponse | list[NewTitlesResponse],
    ) -> list[Edge]:
        """Get all of the edges for a new titles input."""
        if isinstance(data, list):
            result: list[Edge] = []
            for resp in data:
                result.extend(self.extract_edges(resp))
            return result

        if isinstance(data, dict):
            data = self.parse(data)

        return data.data.new_titles.edges
