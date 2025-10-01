from typing import Any

from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import NewTitlesFilter, Variables
from .response import Model


class GetNewTitleBuckets(JustWatchProtocol):
    def _new_title_buckets_variables(  # noqa: PLR0913
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
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> Variables:
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

        new_titles_filter = NewTitlesFilter(
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
            first=first,
            bucketSize=bucket_size,
            groupBy=group_by,
            pageType=page_type,
            country=country,
            newAfterCursor=new_after_cursor,
            newTitlesFilter=new_titles_filter,
            priceDrops=price_drops,
        )

    def _download_new_title_buckets(  # noqa: PLR0913
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
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> dict[str, Any]:
        variables = self._new_title_buckets_variables(
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

        return self._graphql_request(
            operation_name="GetNewTitleBuckets",
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_new_title_buckets(
        self,
        response: dict[str, Any],
        *,
        update: bool = False,
    ) -> Model:
        if update:
            return self._parse_response(Model, response, "buy_box_offers")

        return Model.model_validate(response)

    def get_new_title_buckets(  # noqa: PLR0913
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
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> Model:
        """Get websites with new episodes.

        This API request normally occurs when visiting the new episodes page
        (https://www.justwatch.com/us/new). It has a list of websites with new episodes.

        Args:
            first: ???
            bucket_size: ???
            group_by: ???
            page_type: ???
            country: ???
            new_after_cursor: ???
            price_drops: ???
            filter_age_certifications: ???
            filter_exclude_genres: ???
            filter_exclude_production_countries: ???
            filter_object_types: ???
            filter_production_countries: ???
            filter_subgenres: ???
            filter_genres: ???
            filter_packages: ???
            filter_exclude_irrelevant_titles: ???
            filter_presentation_types: ???
            filter_monetization_types: ???
        """
        response = self._download_new_title_buckets(
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

        return self.parse_new_title_buckets(response, update=True)
