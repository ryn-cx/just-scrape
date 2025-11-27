from typing import Any

from just_scrape.protocol import JustWatchProtocol
from just_scrape.season_episodes import query, request, response

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
    ) -> request.Variables:
        return request.Variables(
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
            query=query.QUERY,
            variables=variables,
        )

    def parse_season_episodes(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> response.SeasonEpisodes:
        if update:
            return self.parse_response(response.SeasonEpisodes, data, "season_episodes")

        return response.SeasonEpisodes.model_validate(data)

    def get_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> response.SeasonEpisodes:
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
        resp = self._download_season_episodes(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )

        return self.parse_season_episodes(resp, update=True)

    def get_all_season_episodes(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[response.SeasonEpisodes]:
        """Get all of the episodes for a specific season.

        This API request occurs when visiting a specific season page for a TV show.

        Args:
            node_id: The ID of the season.
            country: ???
            language: ???
            platform: ???
        """
        offset = 0
        all_episodes: list[response.SeasonEpisodes] = []

        while True:
            resp = self.get_season_episodes(
                node_id=node_id,
                country=country,
                language=language,
                platform=platform,
                limit=DEFAULT_LIMIT,
                offset=offset,
            )

            all_episodes.append(resp)
            # TODO: This can download one more page than needed, there may be a better
            # way to do this.
            if len(resp.data.node.episodes) < DEFAULT_LIMIT:
                return all_episodes

            offset += DEFAULT_LIMIT

    def parse_all_season_episodes(
        self,
        all_episodes: response.SeasonEpisodes
        | list[response.SeasonEpisodes]
        | list[dict[str, Any]]
        | dict[str, Any],
        *,
        update: bool = False,
    ) -> list[response.Episode]:
        """Combine multiple GetSeasonEpisodes responses into a single response."""
        if isinstance(all_episodes, dict):
            all_episodes = self.parse_season_episodes(all_episodes, update=update)

        if isinstance(all_episodes, response.SeasonEpisodes):
            return all_episodes.data.node.episodes

        return [
            episode
            for episode_page in all_episodes
            for episode in self.parse_all_season_episodes(episode_page)
        ]
