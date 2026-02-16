"""Custom Season Episodes API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import Any, override

from gapi import CustomSerializer
from gapi.customizer import ReplacementField

from just_scrape.base_client import BaseEndpoint
from just_scrape.constants import DATETIME_SERIALIZER
from just_scrape.custom_season_episodes import query
from just_scrape.custom_season_episodes.response.models import (
    CustomSeasonEpisodesResponse,
    Episode,
)
from just_scrape.season_episodes.request.models import Variables

DEFAULT_LIMIT = 20


class CustomSeasonEpisodes(
    BaseEndpoint[CustomSeasonEpisodesResponse],
):
    """Provides methods to download, parse, and retrieve custom season episodes data."""

    @cached_property
    @override
    def _response_model(self) -> type[CustomSeasonEpisodesResponse]:
        return CustomSeasonEpisodesResponse

    @cached_property
    @override
    def _response_model_folder_name(self) -> str:
        return "custom_season_episodes/response"

    @cached_property
    @override
    def _custom_serializers(self) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="Episode",
                field_name="max_offer_updated_at",
                serializer_code=DATETIME_SERIALIZER,
                input_type="AwareDatetime",
                output_type="str",
            ),
        ]

    def download(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Downloads custom season episodes data for a given node ID.

        Args:
            node_id: The ID of the season.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        variables = Variables(
            nodeId=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )
        return self._client.download_graphql_request(
            operation_name="GetSeasonEpisodes",
            query=query.QUERY,
            variables=variables,
        )

    def get(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> CustomSeasonEpisodesResponse:
        """Downloads and parses custom season episodes data for a given node ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            node_id: The ID of the season.
        """
        data = self.download(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )
        return self.parse(data)

    def get_all(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[CustomSeasonEpisodesResponse]:
        """Downloads and parses all custom season episodes for a given node ID."""
        offset = 0
        all_episodes: list[CustomSeasonEpisodesResponse] = []

        while True:
            response = self.get(
                node_id=node_id,
                country=country,
                language=language,
                platform=platform,
                limit=DEFAULT_LIMIT,
                offset=offset,
            )

            all_episodes.append(response)
            # TODO: This can download one more page than needed, there may be a better
            # way to do this.
            if len(response.data.node.episodes) < DEFAULT_LIMIT:
                return all_episodes

            offset += DEFAULT_LIMIT

    def extract_episodes(
        self,
        all_episodes: CustomSeasonEpisodesResponse | list[CustomSeasonEpisodesResponse],
    ) -> list[Episode]:
        """Combine CustomSeasonEpisodesResponse responses into a single list."""
        if isinstance(all_episodes, CustomSeasonEpisodesResponse):
            return all_episodes.data.node.episodes

        return [
            episode
            for episode_page in all_episodes
            for episode in self.extract_episodes(episode_page)
        ]
