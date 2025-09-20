import json
import tempfile
from pathlib import Path
from typing import Any

import requests
from pydantic import BaseModel, ValidationError

from just_scrape.api.get_buy_box_offers import GetBuyBoxOffers
from just_scrape.api.get_new_title_buckets import GetNewTitleBuckets
from just_scrape.api.get_new_titles import GetNewTitles
from just_scrape.api.get_season_episodes import GetSeasonEpisodes
from just_scrape.api.get_title_detail_article import GetTitleDetailArticle
from just_scrape.api.get_url_title_details import GetUrlTitleDetails
from just_scrape.constants import TEST_FILE_DIR
from just_scrape.exceptions import GraphQLError, HTTPError
from just_scrape.utils.update_files import update_response


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
        data: dict[str, Any],
        name: str,
    ) -> T:
        try:
            return response_model.model_validate(data)
        except ValidationError as e:
            with tempfile.NamedTemporaryFile(
                delete=False,
                delete_on_close=False,
                suffix=".json",
            ) as file:
                file.write(json.dumps(data).encode("utf-8"))
            endpoint_folder = TEST_FILE_DIR / name
            response_folder = endpoint_folder / "response"
            temp_file = Path(file.name)
            new_json_path = response_folder / temp_file.name
            new_json_path.parent.mkdir(parents=True, exist_ok=True)
            temp_file.rename(new_json_path)
            update_response(endpoint_folder)

            msg = "Parsing error, Pydantic updated, try again."
            raise ValueError(msg) from e
