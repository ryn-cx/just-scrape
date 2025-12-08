import datetime
from typing import Any

from just_scrape.new_titles import query
from just_scrape.new_titles.request import models as request_models
from just_scrape.new_titles.response import models as response_models
from just_scrape.protocol import JustWatchProtocol


class NewTitlesMixin(JustWatchProtocol):
    def download_get_new_titles(  # noqa: PLR0913
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

        filter_obj = request_models.Filter(
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

        variables = request_models.Variables(
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

        return self._download_graphql_request("GetNewTitles", query.QUERY, variables)

    def parse_new_titles(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> response_models.NewTitlesResponse:
        if update:
            return self.parse_response(
                response_models.NewTitlesResponse,
                data,
                "new_titles/response",
            )

        return response_models.NewTitlesResponse.model_validate(data)

    def get_new_titles(  # noqa: PLR0913
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
    ) -> response_models.NewTitlesResponse:
        """Get new episodes for a specific website and date.

        This API request normally occurs when visiting the new episodes page
        (https://www.justwatch.com/us/new).

        Args:
            first: Number of titles to return.
            date: The date to get new titles for.
            filter_packages: What websites to include, uses the shortName like "amz",
            "nfx", etc. This values should probably always match available_to_packages.
            available_to_packages: What websites to include, uses the shortName like
            "amz", "nfx", etc. This values should probably always match filter_packages
            after: Cursor to start getting titles from.

            page_type: ???
            language: ???
            country: ???
            price_drops: ???
            platform: ???
            show_date_badge: ???
            available_to_packages.
            filter_age_certifications: ???
            filter_exclude_genres: ???
            filter_exclude_production_countries: ???
            filter_object_types: ???
            filter_production_countries: ???
            filter_subgenres: ???
            filter_genres: ???
            filter_exclude_irrelevant_titles: ???
            filter_presentation_types: ???
            filter_monetization_types: ???

        """
        response = self.download_get_new_titles(
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
        return self.parse_new_titles(response)

    def get_all_new_titles_for_date(  # noqa: PLR0913
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
    ) -> list[response_models.NewTitlesResponse]:
        """Get all of the new titles for a specific date.

        Args:
            first: Number of titles to return.
            date: The date to get new titles for.
            filter_packages: What websites to include, uses the shortName like "amz",
            "nfx", etc. This values should probably always match available_to_packages.
            available_to_packages: What websites to include, uses the shortName like
            "amz", "nfx", etc. This values should probably always match filter_packages

            page_type: ???
            language: ???
            country: ???
            price_drops: ???
            platform: ???
            show_date_badge: ???
            available_to_packages.
            filter_age_certifications: ???
            filter_exclude_genres: ???
            filter_exclude_production_countries: ???
            filter_object_types: ???
            filter_production_countries: ???
            filter_subgenres: ???
            filter_genres: ???
            filter_exclude_irrelevant_titles: ???
            filter_presentation_types: ???
            filter_monetization_types: ???
        """
        after = None
        output: list[response_models.NewTitlesResponse] = []

        while True:
            parsed = self.get_new_titles(
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

    def get_all_new_titles_since_date(  # noqa: PLR0913
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
    ) -> list[list[response_models.NewTitlesResponse]]:
        """Get all of the new titles for a specific date range.

        Args:
            start_date: The earliest date to get new titles for.
            end_date: The latest date to get new titles for.

            first: Number of titles to return.
            filter_packages: What websites to include, uses the shortName like "amz",
            "nfx", etc. This values should probably always match available_to_packages.
            available_to_packages: What websites to include, uses the shortName like
            "amz", "nfx", etc. This values should probably always match filter_packages

            page_type: ???
            language: ???
            country: ???
            price_drops: ???
            platform: ???
            show_date_badge: ???
            available_to_packages.
            filter_age_certifications: ???
            filter_exclude_genres: ???
            filter_exclude_production_countries: ???
            filter_object_types: ???
            filter_production_countries: ???
            filter_subgenres: ???
            filter_genres: ???
            filter_exclude_irrelevant_titles: ???
            filter_presentation_types: ???
            filter_monetization_types: ???
        """
        current_date = start_date or datetime.datetime.now(tz=datetime.UTC).date()
        output: list[list[response_models.NewTitlesResponse]] = []

        while current_date >= end_date:
            response = self.get_all_new_titles_for_date(
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

    def extract_get_new_titles_edges(
        self,
        data: response_models.NewTitlesResponse
        | list[response_models.NewTitlesResponse],
    ) -> list[response_models.Edge]:
        """Get all of the edges for a new titles input."""
        if isinstance(data, response_models.NewTitlesResponse):
            return data.data.new_titles.edges

        return [
            edge
            for response in data
            for edge in self.extract_get_new_titles_edges(response)
        ]
