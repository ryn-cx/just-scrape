"""Custom Season Episodes API endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, override

from good_ass_pydantic_integrator import CustomSerializer

from just_scrape.base_client import BaseEndpoint
from just_scrape.custom_season_episodes import query
from just_scrape.custom_season_episodes.response_models import (
    CustomSeasonEpisodesResponse,
)

if TYPE_CHECKING:
    from just_scrape.custom_season_episodes.response_models import Episode

DEFAULT_LIMIT = 20


class CustomSeasonEpisodes(
    BaseEndpoint[CustomSeasonEpisodesResponse],
):
    """Provides methods to download, parse, and retrieve custom season episodes data."""

    _response_model = CustomSeasonEpisodesResponse

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="Episode",
                field_name="max_offer_updated_at",
                serializer_code=(
                    "if value is None:\n"
                    "    return None\n"
                    "if isinstance(value, str):\n"
                    "    return value\n"
                    'return value.strftime("%Y-%m-%dT%H:%M:%S.%f")'
                    '.rstrip("0").rstrip(".") + "Z"'
                ),
                output_type="str | None",
            ),
        ]

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
        """Downloads custom season episodes data for a given node ID.

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
    ) -> CustomSeasonEpisodesResponse:
        """Downloads and parses custom season episodes data for a given node ID.

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
