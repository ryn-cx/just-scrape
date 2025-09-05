from typing import Any

from just_scrape.lib import graphql_request, parse_response

from .query import QUERY
from .request import Variables
from .response import ModelItem, UrlV2


def get_variables(
    *,
    full_path: str,
    language: str = "en",
    country: str = "US",
) -> Variables:
    return Variables(
        fullPath=full_path,
        language=language,
        country=country,
    )


def download(variables: Variables) -> dict[str, Any]:
    return graphql_request(
        operation_name="GetTitleDetailArticle",
        query=QUERY,
        variables=variables.model_dump(by_alias=True),
    )


def parse(data: dict[str, Any]) -> UrlV2:
    return parse_response(ModelItem, data).data.url_v2


def get_title_detail_article(
    *,
    full_path: str,
    language: str = "en",
    country: str = "US",
) -> UrlV2:
    variables = get_variables(
        full_path=full_path,
        language=language,
        country=country,
    )

    data = download(variables=variables)

    return parse(data)
