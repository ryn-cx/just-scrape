# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from tests.utils import data_path, download_if_missing

if TYPE_CHECKING:
    from just_scrape.custom_season_episodes import CustomSeasonEpisodes

client = JustScrape(get_around_client=build_client_automatically())

CUSTOM_SEASON_ID = "tss466559"
"""season_id for custom season episodes."""
PAGINATED_SEASON_ID = "tss23744"
"""season_id with enough episodes to exercise pagination."""
EXPECTED_EPISODE_COUNT = 23
"""Number of episodes in PAGINATED_SEASON_ID."""
INVALID_SEASON_ID = "tss999999"


@pytest.fixture(scope="session")
def endpoint() -> CustomSeasonEpisodes:
    return client.custom_season_episodes


class TestCustomSeasonEpisodes:
    def test_download(self, endpoint: CustomSeasonEpisodes) -> None:
        download_if_missing(
            endpoint,
            CUSTOM_SEASON_ID,
            lambda: endpoint.download(CUSTOM_SEASON_ID),
        )

    def test_extract_episodes(self, endpoint: CustomSeasonEpisodes) -> None:
        data = endpoint.parse(
            json.loads(data_path(endpoint, CUSTOM_SEASON_ID).read_text()),
        )
        episodes = endpoint.extract_episodes(data)
        assert episodes is not None
        # TODO: assert expected value (needs live data)

    def test_invalid(self, endpoint: CustomSeasonEpisodes) -> None:
        # This endpoint does not raise for an unknown season_id.
        path = download_if_missing(
            endpoint,
            INVALID_SEASON_ID,
            lambda: endpoint.download(INVALID_SEASON_ID),
        )
        data = endpoint.parse(json.loads(path.read_text()))
        assert data is not None

    # Live pagination test: walks every page of the season over the network and
    # has no clean cached-file equivalent.
    def test_get_all(self, endpoint: CustomSeasonEpisodes) -> None:
        season_episodes = endpoint.get_all(PAGINATED_SEASON_ID)
        episodes = endpoint.extract_episodes(season_episodes)
        assert len(episodes) == EXPECTED_EPISODE_COUNT
