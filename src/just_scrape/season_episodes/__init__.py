# TODO: Validate
"""Contains the SeasonEpisodes class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from just_scrape.base_api_endpoint import BaseEndpoint
from just_scrape.exceptions import (
    InvalidFileError,
    ResourceNotFoundError,
    SeasonNotFoundError,
)
from just_scrape.season_episodes import query
from just_scrape.season_episodes.models import SeasonEpisodesModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LIMIT = 20


# TODO: Validate
class SeasonEpisodes(BaseEndpoint):
    """Manage the season episodes file.

    Source: https://www.justwatch.com/us/tv-show/{slug}/season-{n}

    Example request:
        - POST /graphql HTTP/2
        - Host: apis.justwatch.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Content-Type: application/json
        - Referer: https://www.justwatch.com/
        - Origin: https://www.justwatch.com
        - Body:
            - operationName: GetSeasonEpisodes
            - query: the document in `query.py`
            - variables:
                - nodeId={node_id}
                - country=US
                - language=en
                - platform=WEB
                - limit=20
                - offset=0
    """

    # TODO: Validate
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = LIMIT,
        offset: int = 0,
    ) -> SeasonEpisodesModel:
        """Look the season episodes up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                node_id,
                country=country,
                language=language,
                platform=platform,
                limit=limit,
                offset=offset,
            ),
            log_id,
        )

    # TODO: Validate
    def download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = LIMIT,
        offset: int = 0,
    ) -> str:
        """Download one page of the season episodes file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                "GetSeasonEpisodes",
                query.QUERY,
                {
                    "nodeId": node_id,
                    "country": country,
                    "language": language,
                    "platform": platform,
                    "limit": limit,
                    "offset": offset,
                },
                log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonNotFoundError(node_id, err.errors, err.response) from err
        return self._validate_download(response, node_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, node_id: str) -> str:
        # An unknown node id is not an error to the API: it echoes the id back in
        # a node holding no episodes, which is the same answer a real season with
        # nothing listed gives.
        node = json.loads(response).get("data", {}).get("node", {})
        if node.get("id") != node_id:
            raise InvalidFileError(field="node id", expected=node_id, response=response)
        return response

    # TODO: Validate
    def download_all(
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[str]:
        """Download every page of a season's episodes."""
        pages: list[str] = []
        offset = 0

        while True:
            page = self.download(
                node_id,
                country=country,
                language=language,
                platform=platform,
                limit=LIMIT,
                offset=offset,
            )
            pages.append(page)

            episodes = json.loads(page)["data"]["node"]["episodes"]
            if len(episodes) < LIMIT:
                return pages
            offset += LIMIT

    # TODO: Validate
    def download_merged(
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> str:
        """Download every page of a season's episodes as a single file.

        The pages are put together into one file holding every episode, which is
        the whole season written the way one page of it is, rather than the
        pages themselves.
        """
        return self.merge_pages(
            self.download_all(
                node_id,
                country=country,
                language=language,
                platform=platform,
            ),
        )

    # TODO: Validate
    @staticmethod
    def merge_pages(pages: list[str]) -> str:
        """Return the pages of one season written out as a single file.

        The first page is what the merged file is built on, since everything it
        says around the episodes is what the season is, and its episodes are
        replaced by the episodes of every page in the order they were served.

        Raises:
            ValueError: If there are no pages, since there is nothing to say the
                season was answered with.
        """
        if not pages:
            msg = "Expected at least one page, got none."
            raise ValueError(msg)

        documents: list[dict[str, Any]] = [json.loads(page) for page in pages]
        merged = json.loads(pages[0])
        merged["data"]["node"]["episodes"] = [
            episode
            for document in documents
            for episode in document["data"]["node"]["episodes"]
        ]
        return json.dumps(merged)

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SeasonEpisodesModel:
        """Read a downloaded season episodes file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    def load_pages(self, pages: list[str]) -> list[SeasonEpisodesModel]:
        """Read the pages `download_all` returns into their models."""
        return [self.load(page) for page in pages]
