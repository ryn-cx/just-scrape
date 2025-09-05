from typing import Any

from just_scrape.lib import graphql_request, parse_response

from .query import QUERY
from .request import Variables
from .response import ModelItem, Node


def get_variables(  # noqa: PLR0913
    node_id: str,
    *,
    platform: str = "WEB",
    fallback_to_foreign_offers: bool = False,
    exclude_packages: list[str] | None = None,
    country: str = "US",
    language: str = "en",
) -> Variables:
    exclude_packages = exclude_packages or [
        "3ca",
        "als",
        "amo",
        "bfi",
        "cgv",
        "chi",
        "cnv",
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
        "yot",
        "yrk",
        "jpc",
        "thl",
    ]

    return Variables(
        platform=platform,
        fallbackToForeignOffers=fallback_to_foreign_offers,
        excludePackages=exclude_packages,
        nodeId=node_id,
        country=country,
        language=language,
    )


def download(variables: Variables) -> dict[str, Any]:
    return graphql_request(
        operation_name="GetBuyBoxOffers",
        query=QUERY,
        variables=variables.model_dump(by_alias=True),
    )


def parse(data: dict[str, Any]) -> Node:
    return parse_response(ModelItem, data, "get_buy_box_offers").data.node


def get_buy_box_offers(  # noqa: PLR0913
    node_id: str,
    *,
    platform: str = "WEB",
    fallback_to_foreign_offers: bool = False,
    exclude_packages: list[str] | None = None,
    country: str = "US",
    language: str = "en",
) -> Node:
    variables = get_variables(
        node_id=node_id,
        platform=platform,
        fallback_to_foreign_offers=fallback_to_foreign_offers,
        exclude_packages=exclude_packages,
        country=country,
        language=language,
    )

    data = download(variables=variables)

    return parse(data)
