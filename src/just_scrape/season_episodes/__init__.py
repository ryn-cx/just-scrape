from typing import Any

from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Variables
from .response import Episode, SeasonEpisodes

DEFAULT_LIMIT = 20


class SeasonEpisodesMixin(JustWatchProtocol):
    def _season_episodes_variables(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> Variables:
        return Variables(
            nodeId=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )

    def _download_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> dict[str, Any]:
        variables = self._season_episodes_variables(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )
        return self._graphql_request(
            operation_name="GetSeasonEpisodes",
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_season_episodes(
        self,
        response: dict[str, Any],
        *,
        update: bool = False,
    ) -> SeasonEpisodes:
        if update:
            return self._parse_response(SeasonEpisodes, response, "season_episodes")

        return SeasonEpisodes.model_validate(response)

    def get_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> SeasonEpisodes:
        """Get episodes for a specific season.

        This API request occurs when visiting a specific season page for a TV show.

        Args:
            node_id: The ID of the season.
            country: ???
            language: ???
            platform: ???
            limit: Number of episodes to return.
            offset: Offset to start getting episodes from.
        """
        response = self._download_season_episodes(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )

        return self.parse_season_episodes(response, update=True)

    def get_all_season_episodes(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[SeasonEpisodes]:
        """Get all of the episodes for a specific season.

        This API request occurs when visiting a specific season page for a TV show.

        Args:
            node_id: The ID of the season.
            country: ???
            language: ???
            platform: ???
        """
        offset = 0
        all_episodes: list[SeasonEpisodes] = []

        while True:
            response = self.get_season_episodes(
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

    def season_episodes_entries(
        self,
        all_episodes: SeasonEpisodes | list[SeasonEpisodes],
    ) -> list[Episode]:
        """Combine multiple GetSeasonEpisodes responses into a single response."""
        if isinstance(all_episodes, SeasonEpisodes):
            return all_episodes.data.node.episodes

        return [
            episode
            for episode_page in all_episodes
            for episode in self.season_episodes_entries(episode_page)
        ]
