from typing import Any

from just_scrape.lib import graphql_request, parse_response

from .query import QUERY
from .request import Variables
from .response import Episode, ModelItem, Node

DEFAULT_LIMIT = 20


def get_variables(  # noqa: PLR0913
    *,
    node_id: str,
    country: str = "US",
    language: str = "en",
    platform: str = "WEB",
    limit: int = DEFAULT_LIMIT,
    offset: int = 0,
) -> Variables:
    return Variables(
        nodeId=node_id,
        country=country,
        language=language,
        platform=platform,
        limit=limit,
        offset=offset,
    )


def download(variables: Variables) -> dict[str, Any]:
    return graphql_request(
        operation_name="GetSeasonEpisodes",
        query=QUERY,
        variables=variables.model_dump(by_alias=True),
    )


def parse(data: dict[str, Any]) -> Node:
    return parse_response(ModelItem, data, "get_season_episodes").data.node


def get_season_episodes(  # noqa: PLR0913
    *,
    node_id: str,
    country: str = "US",
    language: str = "en",
    platform: str = "WEB",
    limit: int = DEFAULT_LIMIT,
    offset: int = 0,
) -> Node:
    variables = get_variables(
        node_id=node_id,
        country=country,
        language=language,
        platform=platform,
        limit=limit,
        offset=offset,
    )

    data = download(variables=variables)

    return parse(data)


def get_all_season_episodes(
    *,
    node_id: str,
    country: str = "US",
    language: str = "en",
    platform: str = "WEB",
) -> list[Episode]:
    # Check if more pages need to be downloaded and if so download them and concat the
    # data
    variables = get_variables(
        node_id=node_id,
        country=country,
        language=language,
        platform=platform,
    )

    data = download(variables=variables)
    result = parse(data)
    combined_results = result.episodes

    while len(result.episodes) == DEFAULT_LIMIT:
        variables.offset += DEFAULT_LIMIT
        data = download(variables=variables)
        result = parse(data)
        combined_results.extend(result.episodes)

    return combined_results
