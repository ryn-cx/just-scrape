# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.season_episodes import SeasonEpisodes

SEASON_ID = "tss337460"
"""season_id for season episodes."""
PAGINATED_SEASON_ID = "tss23744"
"""season_id with enough episodes to exercise pagination."""
EXPECTED_EPISODE_COUNT = 23
"""Number of episodes in PAGINATED_SEASON_ID."""
INVALID_SEASON_ID = "tss999999"


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> SeasonEpisodes:
    return client.season_episodes


class TestSeasonEpisodes:
    def test_download(self, endpoint: SeasonEpisodes) -> None:
        download_and_save(
            endpoint,
            SEASON_ID,
            lambda: endpoint.download(SEASON_ID),
        )

    def test_extract_episodes(self, endpoint: SeasonEpisodes) -> None:
        data = parse_json(endpoint, SEASON_ID)
        episodes = endpoint.extract_episodes(data)
        assert episodes is not None
        # TODO: assert expected value (needs live data)

    # This endpoint does not raise for an unknown season_id, so the invalid case
    # is recorded and parsed like any other download.
    def test_invalid_download(self, endpoint: SeasonEpisodes) -> None:
        download_and_save(
            endpoint,
            INVALID_SEASON_ID,
            lambda: endpoint.download(INVALID_SEASON_ID),
        )

    def test_invalid_parse(self, endpoint: SeasonEpisodes) -> None:
        data = parse_json(endpoint, INVALID_SEASON_ID)
        assert data is not None

    # Live pagination test: walks every page of the season over the network and
    # has no clean cached-file equivalent.
    def test_download_and_parse_all(self, endpoint: SeasonEpisodes) -> None:
        season_episodes = endpoint.download_and_parse_all(PAGINATED_SEASON_ID)
        episodes = endpoint.extract_episodes(season_episodes)
        assert len(episodes) == EXPECTED_EPISODE_COUNT


@pytest.mark.parametrize("country", [None, "CA"])
def test_log_id(endpoint: SeasonEpisodes, country: str | None) -> None:
    expected = f"SeasonEpisodes node_id={SEASON_ID!r}"
    if country is not None:
        expected += f" country={country!r}"
    assert endpoint.get_log_id(SEASON_ID, country=country or "US") == expected
