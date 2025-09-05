from typing import Any

from just_scrape.lib import graphql_request, parse_response

from .query import QUERY
from .request import Variables
from .response import ModelItem, UrlV2


def get_variables(  # noqa: PLR0913
    *,
    platform: str = "WEB",
    exclude_text_recommendation_title: bool = True,
    first: int = 10,
    fallback_to_foreign_offers: bool = False,
    exclude_packages: list[str] | None = None,
    full_path: str,
    language: str = "en",
    country: str = "US",
    episode_max_limit: int = 20,
) -> Variables:
    if exclude_packages is None:
        exclude_packages = [
            "3ca",
            "als",
            "amo",
            "bfi",
            "cgv",
            "chi",
            "cnv",
            "cut",
            "daf",
            "kod",
            "koc",
            "mrp",
            "mte",
            "mvt",
            "nxp",
            "org",
            "ply",
            "rvl",
            "tak",
            "tbv",
            "tf1",
            "uat",
            "vld",
            "wa4",
            "wdt",
            "yot",
            "yrk",
            "jpc",
            "thl",
        ]

    return Variables(
        platform=platform,
        excludeTextRecommendationTitle=exclude_text_recommendation_title,
        first=first,
        fallbackToForeignOffers=fallback_to_foreign_offers,
        excludePackages=exclude_packages,
        fullPath=full_path,
        language=language,
        country=country,
        episodeMaxLimit=episode_max_limit,
    )


def download(variables: Variables) -> dict[str, Any]:
    return graphql_request(
        operation_name="GetUrlTitleDetails",
        query=QUERY,
        variables=variables.model_dump(by_alias=True),
    )


def parse(data: dict[str, Any]) -> UrlV2:
    return parse_response(ModelItem, data, "get_url_title_details").data.url_v2


def get_url_title_details(  # noqa: PLR0913
    *,
    full_path: str,
    platform: str = "WEB",
    exclude_text_recommendation_title: bool = True,
    first: int = 10,
    fallback_to_foreign_offers: bool = False,
    exclude_packages: list[str] | None = None,
    language: str = "en",
    country: str = "US",
    episode_max_limit: int = 20,
) -> UrlV2:
    variables = get_variables(
        platform=platform,
        exclude_text_recommendation_title=exclude_text_recommendation_title,
        first=first,
        fallback_to_foreign_offers=fallback_to_foreign_offers,
        exclude_packages=exclude_packages,
        full_path=full_path,
        language=language,
        country=country,
        episode_max_limit=episode_max_limit,
    )

    data = download(variables=variables)

    return parse(data)
