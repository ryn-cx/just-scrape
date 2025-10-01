import datetime
import json
from typing import Any

from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Filter, Variables
from .response import Edge, Model


class GetNewTitles(JustWatchProtocol):
    def _variables_get_new_titles(  # noqa: PLR0913
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
    ) -> Variables:
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

        return Variables(
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

    def _download_get_new_titles(  # noqa: PLR0913
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
        variables = self._variables_get_new_titles(
            first=first,
            page_type=page_type,
            date=date,
            language=language,
            country=country,
            price_drops=price_drops,
            platform=platform,
            after=after,
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

        # The object passed to variables needs to be dumpable by JSON, the easiest way
        # to achieve this is to dump it to a JSON string and then load it back.
        dumped_variables = json.loads(variables.model_dump_json(by_alias=True))
        return self._graphql_request(
            operation_name="GetNewTitles",
            query=QUERY,
            variables=dumped_variables,
        )

    def parse_new_titles(
        self,
        response: dict[str, Any],
        *,
        update: bool = False,
    ) -> Model:
        if update:
            return self._parse_response(Model, response, "buy_box_offers")

        return Model.model_validate(response)

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
    ) -> Model:
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
        response = self._download_get_new_titles(
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
        return self.parse_new_titles(response, update=True)

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
    ) -> list[Model]:
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
        output: list[Model] = []

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
    ) -> list[list[Model]]:
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
        output: list[list[Model]] = []

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

    def new_titles_entries(
        self,
        responses: Model
        | list[Model]
        | list[list[Model]]
        | dict[str, Any]
        | list[dict[str, Any]],
    ) -> list[Edge]:
        """Get all of the edges for a new titles input."""
        if isinstance(responses, list):
            result: list[Edge] = []
            for response in responses:
                result.extend(self.new_titles_entries(response))
            return result

        if isinstance(responses, dict):
            responses = self.parse_new_titles(responses)

        return responses.data.new_titles.edges
