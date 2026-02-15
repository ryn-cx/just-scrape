"""JustScrape is a client for downloading and parsing data from JustWatch."""

import logging
from datetime import datetime
from logging import Logger
from typing import Any

import requests
from pydantic import BaseModel

from just_scrape.base_client import BaseExtractor
from just_scrape.buy_box_offers import BuyBoxOffers
from just_scrape.custom_buy_box_offers import CustomBuyBoxOffers
from just_scrape.custom_season_episodes import CustomSeasonEpisodes
from just_scrape.exceptions import GraphQLError, HTTPError
from just_scrape.new_title_buckets import NewTitleBuckets
from just_scrape.new_titles import NewTitles
from just_scrape.season_episodes import SeasonEpisodes
from just_scrape.title_detail_article import TitleDetailArticle
from just_scrape.url_title_details import UrlTitleDetails

default_logger = logging.getLogger(__name__)


def response_models() -> list[BaseExtractor[Any]]:
    """Returns a list of all of the response models for JustScrape."""
    client = JustScrape()

    return [
        client.buy_box_offers,
        client.custom_buy_box_offers,
        client.custom_season_episodes,
        client.new_title_buckets,
        client.new_titles,
        client.season_episodes,
        client.title_detail_article,
        client.url_title_details,
    ]


class JustScrape:
    """Interface for downloading and parsing data from JustWatch."""

    def __init__(
        self,
        user_agent: str = "Mozilla/5.0 (Windows NT 11.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/134.0.6998.166 Safari/537.36",
        referer: str = "https://www.justwatch.com/",
        origin: str = "https://www.justwatch.com",
        logger: Logger = default_logger,
    ) -> None:
        """Initialize the JustScrape client."""
        self.logger = logger

        self.buy_box_offers = BuyBoxOffers(self)
        self.custom_buy_box_offers = CustomBuyBoxOffers(self)
        self.custom_season_episodes = CustomSeasonEpisodes(self)
        self.new_title_buckets = NewTitleBuckets(self)
        self.new_titles = NewTitles(self)
        self.season_episodes = SeasonEpisodes(self)
        self.title_detail_article = TitleDetailArticle(self)
        self.url_title_details = UrlTitleDetails(self)

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

    def download_graphql_request(
        self,
        operation_name: str,
        query: str,
        variables: BaseModel,
    ) -> dict[str, Any]:
        """Make a GraphQL request to the JustWatch API."""
        self.logger.info("Downloading %s: %s", operation_name, variables)

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

        output["just_scrape"] = {}
        output["just_scrape"]["variables"] = variables.model_dump(
            mode="json",
            by_alias=True,
        )
        output["just_scrape"]["operationName"] = operation_name
        output["just_scrape"]["headers"] = self._headers()
        output["just_scrape"]["timestamp"] = (
            datetime.now().astimezone().isoformat().replace("+00:00", "Z")
        )

        return output
