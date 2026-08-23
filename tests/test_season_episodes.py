# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError
from just_scrape.season_episodes.models import SeasonEpisodesModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from just_scrape import JustScrape

NODE_IDS = [
    pytest.param("tss486285", id="frieren beyond journeys end season 2"),
    # An id nothing is under is echoed back as a season with no episodes, which
    # is the same answer a real season with nothing listed gives.
    pytest.param("tss0000000", id="season that does not exist"),
]


# TODO: Validate
class SeasonEpisodesTest(RecordedEndpoint):
    MODEL = SeasonEpisodesModel


# TODO: Validate
@pytest.mark.parametrize("node_id", NODE_IDS)
def test_download(client: JustScrape, node_id: str) -> None:
    SeasonEpisodesTest.download_test(
        node_id,
        lambda: client.season_episodes.download(node_id),
    )


# TODO: Validate
@pytest.mark.parametrize("node_id", NODE_IDS)
def test_parse(client: JustScrape, node_id: str) -> None:
    data = client.season_episodes.load(SeasonEpisodesTest.recorded_content(node_id))
    assert data.data.node.id == node_id


# TODO: Validate
@pytest.mark.parametrize(
    "node_id",
    [pytest.param("0000000", id="node id that is not shaped like one")],
)
def test_download_invalid(client: JustScrape, node_id: str) -> None:
    SeasonEpisodesTest.error_test(
        node_id,
        lambda: client.season_episodes.download(node_id),
        GraphQLError,
    )
