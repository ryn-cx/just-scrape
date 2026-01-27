import logging
from pathlib import Path
from typing import Any

import requests
from gapi import AbstractGapiClient
from pydantic import BaseModel

from just_scrape.buy_box_offers import BuyBoxOffersMixin
from just_scrape.constants import JUST_SCRAPE_PATH
from just_scrape.custom_season_episodes import CustomSeasonEpisodesMixin
from just_scrape.exceptions import GraphQLError, HTTPError
from just_scrape.new_title_buckets import NewTitleBucketsMixin
from just_scrape.new_titles import NewTitlesMixin
from just_scrape.season_episodes import SeasonEpisodesMixin
from just_scrape.title_detail_article import TitleDetailArticleMixin
from just_scrape.url_title_details import UrlTitleDetailsMixin

logger = logging.getLogger(__name__)


class JustScrape(
    AbstractGapiClient,
    BuyBoxOffersMixin,
    NewTitleBucketsMixin,
    NewTitlesMixin,
    SeasonEpisodesMixin,
    TitleDetailArticleMixin,
    UrlTitleDetailsMixin,
    CustomSeasonEpisodesMixin,
):
    def client_path(self) -> Path:
        return JUST_SCRAPE_PATH

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
        super().__init__()

    def _headers(self) -> dict[str, str]:
        return {
            "User-Agent": self.user_agent,
            "Referer": self.referer,
            "Origin": self.origin,
        }

    def _download_graphql_request(
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
            timeout=30,
        )

        if response.status_code != 200:  # noqa: PLR2004
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        output = response.json()

        if output.get("errors"):
            msg = f"GraphQL errors occurred: {output['errors']}"
            raise GraphQLError(msg)

        return response.json()
