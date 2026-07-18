# TODO: Validate
"""Contains the CustomSeasonEpisodes class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.custom_season_episodes import query
from just_scrape.custom_season_episodes.models import (
    CustomSeasonEpisodesResponse,
)

if TYPE_CHECKING:
    from just_scrape.custom_season_episodes.models import Episode

logger = getLogger(__name__)
logger.addHandler(NullHandler())

DEFAULT_LIMIT = 20


class CustomSeasonEpisodes(
    BaseEndpoint[CustomSeasonEpisodesResponse],
):
    """Manage the custom season episodes file."""

    _response_model = CustomSeasonEpisodesResponse

    # PLR0913 - Each parameter maps to an API parameter.
    def get_log_id(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {node_id=}",
            country=(country, "US"),
            language=(language, "en"),
            platform=(platform, "WEB"),
            limit=(limit, DEFAULT_LIMIT),
            offset=(offset, 0),
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def download(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Downloads the custom season episodes file."""
        return self._client.download(
            operation_name="GetSeasonEpisodes",
            query=query.QUERY,
            variables={
                "nodeId": node_id,
                "country": country,
                "language": language,
                "platform": platform,
                "limit": limit,
                "offset": offset,
            },
            log_id=self.get_log_id(
                node_id,
                country=country,
                language=language,
                platform=platform,
                limit=limit,
                offset=offset,
            ),
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def download_and_parse(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> CustomSeasonEpisodesResponse:
        """Downloads and parses the custom season episodes file."""
        data = self.download(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )
        return self.parse(data)

    def download_and_parse_all(
        self,
        node_id: str,
        *,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[CustomSeasonEpisodesResponse]:
        """Downloads and parses all custom season episodes for a given node ID."""
        offset = 0
        all_episodes: list[CustomSeasonEpisodesResponse] = []

        while True:
            response = self.download_and_parse(
                node_id=node_id,
                country=country,
                language=language,
                platform=platform,
                limit=DEFAULT_LIMIT,
                offset=offset,
            )

            all_episodes.append(response)
            # TODO(YBR): This can download one more page  # noqa: TD003, FIX002
            # than needed, there may be a better way to do this.
            if len(response.data.node.episodes) < DEFAULT_LIMIT:
                return all_episodes

            offset += DEFAULT_LIMIT

    def extract_episodes(
        self,
        all_episodes: CustomSeasonEpisodesResponse | list[CustomSeasonEpisodesResponse],
    ) -> list[Episode]:
        """Combine CustomSeasonEpisodesResponse responses into a single list."""
        if isinstance(all_episodes, list):
            return [
                episode
                for episode_page in all_episodes
                for episode in self.extract_episodes(episode_page)
            ]

        return all_episodes.data.node.episodes
