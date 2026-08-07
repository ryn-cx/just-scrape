# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import InvalidFileError
from tests.update_ids import node_id_from_response, update_ids
from tests.utils import download_and_save, load_ids, parsed_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.season_episodes import SeasonEpisodes

PAGINATED_NODE_ID = "tss23744"
"""node_id with enough episodes to exercise pagination."""
EXPECTED_EPISODE_COUNT = 23
"""Number of episodes in PAGINATED_NODE_ID."""

NODE_IDS = load_ids("season_episodes")
"""Rewritten by ``test_update_ids``; add an id here and run the tests."""


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> SeasonEpisodes:
    return client.season_episodes


@pytest.fixture(params=NODE_IDS)
def node_id(request: pytest.FixtureRequest) -> str:
    return request.param


def test_download(endpoint: SeasonEpisodes, node_id: str) -> None:
    download_and_save(
        endpoint,
        node_id,
        lambda: endpoint.download(node_id),
    )


def test_extract_episodes(endpoint: SeasonEpisodes, node_id: str) -> None:
    data = parsed_json(endpoint, node_id)
    assert data.data.node.id == node_id
    assert endpoint.extract_episodes(data)


# Live pagination test: walks every page of the season over the network and has no
# clean cached-file equivalent.
def test_download_and_parse_all(endpoint: SeasonEpisodes) -> None:
    season_episodes = endpoint.download_and_parse_all(PAGINATED_NODE_ID)
    episodes = endpoint.extract_episodes(season_episodes)
    assert len(episodes) == EXPECTED_EPISODE_COUNT


def test_update_ids(endpoint: SeasonEpisodes) -> None:
    assert update_ids(
        endpoint,
        "season_episodes",
        InvalidFileError,
        id_from_response=node_id_from_response,
    )
