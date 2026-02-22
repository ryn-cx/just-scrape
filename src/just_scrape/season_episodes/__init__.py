"""Season Episodes API endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.season_episodes import query
from just_scrape.season_episodes.response_models import SeasonEpisodesResponse

if TYPE_CHECKING:
    from just_scrape.season_episodes.response_models import Episode

DEFAULT_LIMIT = 20


class SeasonEpisodes(BaseEndpoint[SeasonEpisodesResponse]):
    """Provides methods to download, parse, and retrieve season episodes data."""

    _response_model = SeasonEpisodesResponse

    # PLR0913 - Each parameter maps to an API parameter.
    def download(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Downloads season episodes data for a given node ID.

        Args:
            node_id: The ID of the season.
            country: ???
            language: ???
            platform: ???
            limit: ???
            offset: ???

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
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
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def get(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> SeasonEpisodesResponse:
        """Downloads and parses season episodes data for a given node ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            node_id: The ID of the season.
            country: ???
            language: ???
            platform: ???
            limit: ???
            offset: ???
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
    ) -> list[SeasonEpisodesResponse]:
        """Downloads and parses all season episodes for a given node ID."""
        offset = 0
        all_episodes: list[SeasonEpisodesResponse] = []

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
            # TODO(YBR): This can download one more page  # noqa: TD003, FIX002
            # than needed, there may be a better way to do this.
            if len(response.data.node.episodes) < DEFAULT_LIMIT:
                return all_episodes

            offset += DEFAULT_LIMIT

    def extract_episodes(
        self,
        all_episodes: SeasonEpisodesResponse | list[SeasonEpisodesResponse],
    ) -> list[Episode]:
        """Combine SeasonEpisodesResponse responses into a single list of Episodes."""
        if isinstance(all_episodes, dict):
            all_episodes = self.parse(all_episodes)

        if isinstance(all_episodes, SeasonEpisodesResponse):
            return all_episodes.data.node.episodes

        return [
            episode
            for episode_page in all_episodes
            for episode in self.extract_episodes(episode_page)
        ]
