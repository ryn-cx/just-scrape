from typing import Any

from just_scrape.protocol import JustWatchProtocol
from just_scrape.season_episodes import query
from just_scrape.season_episodes.request import models as request_models
from just_scrape.season_episodes.response import models as response_models

DEFAULT_LIMIT = 20


class SeasonEpisodesMixin(JustWatchProtocol):
    def download_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> dict[str, Any]:
        variables = request_models.Variables(
            nodeId=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )
        return self._download_graphql_request(
            operation_name="GetSeasonEpisodes",
            query=query.QUERY,
            variables=variables,
        )

    def parse_season_episodes(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> response_models.SeasonEpisodesResponse:
        if update:
            return self.parse_response(
                response_models.SeasonEpisodesResponse,
                data,
                "season_episodes/response",
            )

        return response_models.SeasonEpisodesResponse.model_validate(data)

    def get_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> response_models.SeasonEpisodesResponse:
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
        response = self.download_season_episodes(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )

        return self.parse_season_episodes(response)

    def get_all_season_episodes(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[response_models.SeasonEpisodesResponse]:
        """Get all of the episodes for a specific season.

        This API request occurs when visiting a specific season page for a TV show.

        Args:
            node_id: The ID of the season.
            country: ???
            language: ???
            platform: ???
        """
        offset = 0
        all_episodes: list[response_models.SeasonEpisodesResponse] = []

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

    def extract_season_episodes_episodes(
        self,
        all_episodes: response_models.SeasonEpisodesResponse
        | list[response_models.SeasonEpisodesResponse],
    ) -> list[response_models.Episode]:
        """Combine SeasonEpisodesResponse responses into a single list of Episodes."""
        if isinstance(all_episodes, dict):
            all_episodes = self.parse_season_episodes(all_episodes)

        if isinstance(all_episodes, response_models.SeasonEpisodesResponse):
            return all_episodes.data.node.episodes

        return [
            episode
            for episode_page in all_episodes
            for episode in self.extract_season_episodes_episodes(episode_page)
        ]
