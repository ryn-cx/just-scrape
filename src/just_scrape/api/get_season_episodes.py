from typing import Any

from just_scrape.api.just_watch_protocol import JustWatchProtocol
from just_scrape.models.request.get_season_episodes import Variables
from just_scrape.models.response.get_season_episodes import Episode, Model, Node
from just_scrape.queries.get_season_episodes import QUERY

DEFAULT_LIMIT = 20


class GetSeasonEpisodes(JustWatchProtocol):
    """Mixin for GraphQL clients that implement JustWatchProtocol."""

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

    def download_get_season_episodes(  # noqa: PLR0913
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

    def parse_get_season_episodes(self, data: dict[str, Any]) -> Node:
        return self.parse_response(Model, data, "get_season_episodes").data.node

    def get_season_episodes(  # noqa: PLR0913
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
    ) -> Node:
        data = self.download_get_season_episodes(
            node_id=node_id,
            country=country,
            language=language,
            platform=platform,
            limit=limit,
            offset=offset,
        )

        return self.parse_get_season_episodes(data)

    def get_all_season_episodes(
        self,
        *,
        node_id: str,
        country: str = "US",
        language: str = "en",
        platform: str = "WEB",
    ) -> list[Episode]:
        offset = 0
        combined_results: Node | None = None

        while True:
            data = self.download_get_season_episodes(
                node_id=node_id,
                country=country,
                language=language,
                platform=platform,
                limit=DEFAULT_LIMIT,
                offset=offset,
            )
            result = self.parse_get_season_episodes(data)

            if combined_results is None:
                combined_results = result
            else:
                combined_results.episodes.extend(result.episodes)

            # TODO: This can download one more page than needed, there may be a better
            # way to do this.
            if len(result.episodes) < DEFAULT_LIMIT:
                break

            offset += DEFAULT_LIMIT

        return combined_results.episodes if combined_results else []
