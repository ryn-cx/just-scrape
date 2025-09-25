import datetime
import json
from typing import Any

from just_scrape.api.just_watch_protocol import JustWatchProtocol
from just_scrape.models.request.get_new_titles import Filter, Variables
from just_scrape.models.response.get_new_titles import Edge, Model, NewTitles
from just_scrape.queries.get_new_titles import QUERY


class GetNewTitles(JustWatchProtocol):
    """Mixin for GraphQL clients that implement JustWatchProtocol."""

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
        return self.graphql_request(
            operation_name="GetNewTitles",
            query=QUERY,
            variables=dumped_variables,
        )

    def parse_get_new_titles(self, data: dict[str, Any]) -> NewTitles:
        return self.parse_response(Model, data, "get_new_titles").data.new_titles

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
    ) -> NewTitles:
        data = self.download_get_new_titles(
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

        return self.parse_get_new_titles(data)

    def get_all_new_titles(  # noqa: PLR0913
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
    ) -> list[Edge]:
        after = None
        all_edges: list[Edge] = []

        while True:
            response = self.get_new_titles(
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

            all_edges.extend(response.edges)

            if not response.page_info.has_next_page:
                return all_edges

            after = response.page_info.end_cursor

    def get_all_new_titles_since(  # noqa: PLR0913
        self,
        *,
        first: int = 10,
        page_type: str = "NEW",
        start_date: datetime.date | None = None,
        end_date: datetime.date,
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
    ) -> list[Edge]:
        """Get new titles for a range of dates.

        Downloads all paginated data for each date from start_date down to end_date.
        """
        current_date = start_date or datetime.datetime.now(tz=datetime.UTC).date()
        all_edges: list[Edge] = []

        while current_date >= end_date:
            day_edges = self.get_all_new_titles(
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

            all_edges.extend(day_edges)

            current_date -= datetime.timedelta(days=1)

        return all_edges
