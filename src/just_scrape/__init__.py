import logging
from typing import Any, overload

import requests
from pydantic import BaseModel, ValidationError

from .buy_box_offers import BuyBoxOffersMixin
from .buy_box_offers.response import BuyBoxOffers
from .custom_buy_box_offers import CustomBuyBoxOffersMixin
from .custom_buy_box_offers.response import CustomBuyBoxOffers
from .exceptions import GraphQLError, HTTPError
from .new_title_buckets import NewTitleBucketsMixin
from .new_title_buckets.response import NewTitleBuckets
from .new_titles import NewTitlesMixin
from .new_titles.response import NewTitles
from .season_episodes import SeasonEpisodesMixin
from .season_episodes.response import SeasonEpisodes
from .title_detail_article import TitleDetailArticleMixin
from .title_detail_article.response import TitleDetailArticle
from .update_files import add_test_file, update_model
from .url_title_details import UrlTitleDetailsMixin
from .url_title_details.response import UrlTitleDetails

RESPONSE_MODELS = (
    BuyBoxOffers
    | NewTitles
    | NewTitleBuckets
    | SeasonEpisodes
    | TitleDetailArticle
    | UrlTitleDetails
    | CustomBuyBoxOffers
)
RESPONSE_MODELS_LIST = list[NewTitles] | list[SeasonEpisodes]
RESPONSE_MODELS_LIST_LIST = list[list[NewTitles]]

logger = logging.getLogger(__name__)


class JustScrape(
    BuyBoxOffersMixin,
    NewTitleBucketsMixin,
    NewTitlesMixin,
    SeasonEpisodesMixin,
    TitleDetailArticleMixin,
    UrlTitleDetailsMixin,
    CustomBuyBoxOffersMixin,
):
    def __init__(
        self,
        user_agent: str = "Mozilla/5.0 (Windows NT 11.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/134.0.6998.166 Safari/537.36",
        referer: str = "https://www.justwatch.com/",
        origin: str = "https://www.justwatch.com",
    ) -> None:
        self.user_agent = user_agent
        self.referer = referer
        self.origin = origin

    def _headers(self) -> dict[str, str]:
        return {
            "User-Agent": self.user_agent,
            "Referer": self.referer,
            "Origin": self.origin,
        }

    def _graphql_request(
        self,
        operation_name: str,
        query: str,
        variables: BaseModel,
    ) -> dict[str, Any]:
        logger.info("Downloading %s: %s", operation_name, variables)

        response = requests.post(
            "https://apis.justwatch.com/graphql",
            json={
                "operationName": operation_name,
                "query": query,
                "variables": variables.model_dump(mode="json", by_alias=True),
            },
            headers=self._headers(),
            timeout=60,
        )

        if response.status_code != 200:  # noqa: PLR2004
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        output = response.json()

        if output.get("errors"):
            msg = f"GraphQL errors occurred: {output['errors']}"
            raise GraphQLError(msg)

        return response.json()

    def _parse_response[T: BaseModel](
        self,
        response_model: type[T],
        response: dict[str, Any],
        name: str,
    ) -> T:
        try:
            return response_model.model_validate(response)
        except ValidationError as e:
            add_test_file(name, "response", response)
            update_model(name, "response")
            msg = "Parsing error, models updated, try again."
            raise ValueError(msg) from e

    @overload
    def dump_response(
        self,
        data: RESPONSE_MODELS_LIST_LIST,
    ) -> list[list[dict[str, Any]]]: ...
    @overload
    def dump_response(self, data: RESPONSE_MODELS_LIST) -> list[dict[str, Any]]: ...
    @overload
    def dump_response(self, data: RESPONSE_MODELS) -> dict[str, Any]: ...
    def dump_response(
        self,
        data: RESPONSE_MODELS | RESPONSE_MODELS_LIST | RESPONSE_MODELS_LIST_LIST,
    ) -> dict[str, Any] | list[dict[str, Any]] | list[list[dict[str, Any]]]:
        """Dump an API response to a JSON serializable object."""
        if isinstance(data, list):
            return [self.dump_response(response) for response in data]

        return data.model_dump(mode="json", by_alias=True, exclude_unset=True)
