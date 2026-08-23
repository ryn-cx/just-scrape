# TODO: Validate
"""Contains the JustScrape class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic, sleep
from typing import Any

from get_around import GetAround

from just_scrape.episode_offers import EpisodeOffers
from just_scrape.exceptions import GraphQLError, HTTPError, ResourceNotFoundError
from just_scrape.new_title_buckets import NewTitleBuckets
from just_scrape.new_titles import NewTitles
from just_scrape.search import Search
from just_scrape.season_episodes import SeasonEpisodes
from just_scrape.title_detail_article import TitleDetailArticle
from just_scrape.url_title_details import UrlTitleDetails

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_URL = "https://apis.justwatch.com/graphql"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/134.0.6998.166 Safari/537.36"
)


# TODO: Validate
class JustScrape:
    """JustWatch API wrapper."""

    # TODO: Validate
    def __init__(  # noqa: PLR0913 - Every request header is settable.
        self,
        get_around_client: GetAround | None = None,
        user_agent: str = USER_AGENT,
        referer: str = "https://www.justwatch.com/",
        origin: str = "https://www.justwatch.com",
        sleep_time: float = 0,
        timeout: float = 30,
    ) -> None:
        """Initializes the JustScrape client.

        The client holds one attribute per endpoint, so `client.search(query)`
        runs a search and `client.search.download(query)` and
        `client.search.load(data)` are the halves of it.
        """
        self.get_around_client = get_around_client or GetAround()
        self.user_agent = user_agent
        self.referer = referer
        self.origin = origin
        self.sleep_time = sleep_time
        self.timeout = timeout

        self.episode_offers = EpisodeOffers(self)
        self.new_title_buckets = NewTitleBuckets(self)
        self.new_titles = NewTitles(self)
        self.search = Search(self)
        self.season_episodes = SeasonEpisodes(self)
        self.title_detail_article = TitleDetailArticle(self)
        self.url_title_details = UrlTitleDetails(self)

    # TODO: Validate
    def download(
        self,
        operation_name: str,
        query: str,
        variables: dict[str, Any],
        log_id: str,
    ) -> str:
        """Downloads from the API.

        What comes back is the body as it was served, which the endpoint reads
        into its model.

        Raises:
            HTTPError: If the request is answered with anything but a 200.
            ResourceNotFoundError: If the API says the thing does not exist.
            GraphQLError: If the response carries any other errors.
        """
        logger.debug("Downloading: %s", log_id)
        start = monotonic()
        response = self.get_around_client.post(
            API_URL,
            json={
                "operationName": operation_name,
                "query": query,
                "variables": variables,
            },
            headers={
                "User-Agent": self.user_agent,
                "Referer": self.referer,
                "Origin": self.origin,
            },
            timeout=self.timeout,
        )

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        self._validate_download(response.text)
        sleep(self.sleep_time)
        return response.text

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str) -> None:
        """Raise if the response carries errors instead of the data asked for."""
        errors = json.loads(response).get("errors")
        if not errors:
            return
        codes = {error.get("extensions", {}).get("code") for error in errors}
        if "NOT_FOUND" in codes:
            raise ResourceNotFoundError(errors, response)
        raise GraphQLError(errors, response)
