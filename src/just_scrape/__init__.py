"""JustScrape is a client for downloading and parsing data from JustWatch."""

from __future__ import annotations

from datetime import datetime
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from get_around import GetAround

from just_scrape.buy_box_offers import BuyBoxOffers
from just_scrape.custom_buy_box_offers import CustomBuyBoxOffers
from just_scrape.custom_season_episodes import CustomSeasonEpisodes
from just_scrape.exceptions import GraphQLError, HTTPError
from just_scrape.new_title_buckets import NewTitleBuckets
from just_scrape.new_titles import NewTitles
from just_scrape.season_episodes import SeasonEpisodes
from just_scrape.title_detail_article import TitleDetailArticle
from just_scrape.url_title_details import UrlTitleDetails

if TYPE_CHECKING:
    from just_scrape.base_client import BaseEndpoint

logger = getLogger(__name__)
logger.addHandler(NullHandler())


def response_models() -> list[BaseEndpoint[Any]]:
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
        get_around_server: str | None = None,
        get_around_password: str | None = None,
    ) -> None:
        """Initialize the JustScrape client."""
        self.get_around_client = GetAround(
            server=get_around_server,
            password=get_around_password,
        )
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

    def download(
        self,
        operation_name: str,
        query: str,
        variables: dict[str, Any],
    ) -> dict[str, Any]:
        """Make a GraphQL request to the JustWatch API."""
        logger.info("Downloading %s: %s", operation_name, variables)

        response = self.get_around_client.post(
            "https://apis.justwatch.com/graphql",
            json={
                "operationName": operation_name,
                "query": query,
                "variables": variables,
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
        output["just_scrape"]["variables"] = variables
        output["just_scrape"]["operationName"] = operation_name
        output["just_scrape"]["headers"] = self._headers()
        output["just_scrape"]["timestamp"] = (
            datetime.now().astimezone().isoformat().replace("+00:00", "Z")
        )

        return output
