from datetime import UTC, datetime
from typing import Any

from just_scrape.lib import graphql_request, parse_response

from .query import QUERY
from .request import Filter, Variables
from .response import Edge, ModelItem, NewTitles


def get_variables(  # noqa: PLR0913
    *,
    first: int = 10,
    page_type: str = "NEW",
    date: str | None = None,
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
    date = date or datetime.now(tz=UTC).date().strftime("%Y-%m-%d")
    available_to_packages = available_to_packages or []
    filter_age_certifications = filter_age_certifications or []
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


def download(variables: Variables) -> dict[str, Any]:
    return graphql_request(
        operation_name="GetNewTitles",
        query=QUERY,
        variables=variables.model_dump(by_alias=True),
    )


def parse(data: dict[str, Any]) -> NewTitles:
    return parse_response(ModelItem, data).data.new_titles


def get_new_titles(  # noqa: PLR0913
    *,
    first: int = 10,
    page_type: str = "NEW",
    date: str | None = None,
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
    variables = get_variables(
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

    data = download(variables=variables)

    return parse(data)


def get_all_new_titles(  # noqa: PLR0913
    *,
    available_to_packages: list[str] | None = None,
    country: str = "US",
    date: str | None = None,
    filter_age_certifications: list[Any] | None = None,
    filter_exclude_genres: list[Any] | None = None,
    filter_exclude_irrelevant_titles: bool = False,
    filter_exclude_production_countries: list[Any] | None = None,
    filter_genres: list[Any] | None = None,
    filter_monetization_types: list[Any] | None = None,
    filter_object_types: list[Any] | None = None,
    filter_packages: list[str] | None = None,
    filter_presentation_types: list[Any] | None = None,
    filter_production_countries: list[Any] | None = None,
    filter_subgenres: list[Any] | None = None,
    language: str = "en",
    page_type: str = "NEW",
    platform: str = "WEB",
    price_drops: bool = False,
    show_date_badge: bool = False,
) -> list[Edge]:
    all_edges: list[Edge] = []
    after = None

    while True:
        response = get_new_titles(
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
            break

        after = response.page_info.end_cursor

    return all_edges
