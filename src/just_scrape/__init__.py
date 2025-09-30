from typing import Any

import requests
from pydantic import BaseModel, ValidationError

from just_scrape.exceptions import GraphQLError, HTTPError
from just_scrape.get_buy_box_offers import GetBuyBoxOffers
from just_scrape.get_new_title_buckets import GetNewTitleBuckets
from just_scrape.get_new_titles import GetNewTitles
from just_scrape.get_season_episodes import GetSeasonEpisodes
from just_scrape.get_title_detail_article import GetTitleDetailArticle
from just_scrape.get_url_title_details import GetUrlTitleDetails
from just_scrape.utils.update_files import Updater


class JustScrape(
    GetBuyBoxOffers,
    GetNewTitleBuckets,
    GetNewTitles,
    GetSeasonEpisodes,
    GetTitleDetailArticle,
    GetUrlTitleDetails,
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

    def headers(self) -> dict[str, str]:
        return {
            "User-Agent": self.user_agent,
            "Referer": self.referer,
            "Origin": self.origin,
        }

    def graphql_request(
        self,
        operation_name: str,
        query: str,
        variables: dict[str, Any],
    ) -> dict[str, Any]:
        response = requests.post(
            "https://apis.justwatch.com/graphql",
            json={
                "operationName": operation_name,
                "query": query,
                "variables": variables,
            },
            headers=self.headers(),
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

    def parse_response[T: BaseModel](
        self,
        response_model: type[T],
        response: dict[str, Any],
        name: str,
    ) -> T:
        try:
            return response_model.model_validate(response)
        except ValidationError as e:
            updater = Updater(name, "response")
            updater.add_test_file(response)
            updater.generate_schema()
            updater.remove_redundant_files()
            msg = "Parsing error, models updated, try again."
            raise ValueError(msg) from e
