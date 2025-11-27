import json
import logging
import uuid
from pathlib import Path
from typing import Any, override

import requests
from gapi import (
    AbstractGapiClient,
    GapiCustomizations,
    apply_customizations,
    update_json_schema_and_pydantic_model,
)
from pydantic import BaseModel

from .constants import FILES_PATH, JUST_SCRAPE_PATH
from .custom_get_buy_box_offers import CustomGetBuyBoxOffersMixin
from .custom_get_buy_box_offers.response import CustomGetBuyBoxOffers
from .exceptions import GraphQLError, HTTPError
from .get_buy_box_offers import BuyBoxOffersMixin
from .get_buy_box_offers.response import GetBuyBoxOffers
from .new_title_buckets import NewTitleBucketsMixin
from .new_title_buckets.response import NewTitleBuckets
from .new_titles import NewTitlesMixin
from .new_titles.response import NewTitles
from .season_episodes import SeasonEpisodesMixin
from .season_episodes.response import SeasonEpisodes
from .title_detail_article import TitleDetailArticleMixin
from .title_detail_article.response import TitleDetailArticle
from .url_title_details import UrlTitleDetailsMixin
from .url_title_details.response import UrlTitleDetails

RESPONSE_MODELS = (
    GetBuyBoxOffers
    | NewTitles
    | NewTitleBuckets
    | SeasonEpisodes
    | TitleDetailArticle
    | UrlTitleDetails
    | CustomGetBuyBoxOffers
)
RESPONSE_MODELS_LIST = list[NewTitles] | list[SeasonEpisodes]
RESPONSE_MODELS_LIST_LIST = list[list[NewTitles]]

logger = logging.getLogger(__name__)


class JustScrape(
    AbstractGapiClient,
    BuyBoxOffersMixin,
    NewTitleBucketsMixin,
    NewTitlesMixin,
    SeasonEpisodesMixin,
    TitleDetailArticleMixin,
    UrlTitleDetailsMixin,
    CustomGetBuyBoxOffersMixin,
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

    @override
    def save_file(
        self,
        name: str,
        data: dict[str, Any],
        model_type: str,
    ) -> None:
        input_folder = FILES_PATH / name / model_type
        new_json_path = input_folder / f"{uuid.uuid4()}.json"
        new_json_path.parent.mkdir(parents=True, exist_ok=True)
        new_json_path.write_text(json.dumps(data, indent=2))

    @override
    def update_model(
        self,
        name: str,
        model_type: str,
        customizations: GapiCustomizations | None = None,
    ) -> None:
        schema_path = JUST_SCRAPE_PATH / f"{name}/{model_type}.schema.json"
        model_path = JUST_SCRAPE_PATH / f"{name}/{model_type}.py"
        files_path = FILES_PATH / name / model_type
        update_json_schema_and_pydantic_model(files_path, schema_path, model_path, name)
        apply_customizations(model_path, customizations)

    def files_path(self) -> Path:
        return FILES_PATH
