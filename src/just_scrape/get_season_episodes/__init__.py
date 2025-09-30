from typing import Any

from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Variables
from .response import Episode, Model

DEFAULT_LIMIT = 20


class GetSeasonEpisodes(JustWatchProtocol):
    def _variables_get_season_episodes(  # noqa: PLR0913
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

    def _download_get_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> dict[str, Any]:
        variables = self._variables_get_season_episodes(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )
        return self.graphql_request(
            operation_name="GetSeasonEpisodes",
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_get_season_episodes(self, response: dict[str, Any]) -> Model:
        return self.parse_response(Model, response, "get_season_episodes")

    def get_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> Model:
        response = self._download_get_season_episodes(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )

        return self.parse_get_season_episodes(response)

    def get_all_season_episodes(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[Model]:
        offset = 0
        all_episodes: list[Model] = []

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

    def get_all_season_episodes_get_episodes(
        self,
        all_episodes: list[Model],
    ) -> list[Episode]:
        """Combine multiple GetSeasonEpisodes responses into a single response."""
        return [
            episode
            for response in all_episodes
            for episode in response.data.node.episodes
        ]
