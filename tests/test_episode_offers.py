# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.episode_offers.models import EpisodeOffersModel
from just_scrape.exceptions import GraphQLError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from just_scrape import JustScrape

NODE_IDS = [
    pytest.param("tse1126259", id="episode carried by netflix"),
    pytest.param("tse1610421", id="episode carried in a disney plus bundle"),
    # An id nothing is under is echoed back as an episode with no offers, which
    # is the same answer a real episode nobody carries gives.
    pytest.param("tse0000000", id="episode that does not exist"),
]


# TODO: Validate
class EpisodeOffersTest(RecordedEndpoint):
    MODEL = EpisodeOffersModel
    SAME_TYPE = ("Node.max_offer_updated_at",)


# TODO: Validate
@pytest.mark.parametrize("node_id", NODE_IDS)
def test_download(client: JustScrape, node_id: str) -> None:
    EpisodeOffersTest.download_test(
        node_id,
        lambda: client.episode_offers.download(node_id),
    )


# TODO: Validate
@pytest.mark.parametrize("node_id", NODE_IDS)
def test_parse(client: JustScrape, node_id: str) -> None:
    data = client.episode_offers.load(EpisodeOffersTest.recorded_content(node_id))
    assert data.data.node.id == node_id


# TODO: Validate
@pytest.mark.parametrize(
    "node_id",
    [pytest.param("0000000", id="node id that is not shaped like one")],
)
def test_download_invalid(client: JustScrape, node_id: str) -> None:
    EpisodeOffersTest.error_test(
        node_id,
        lambda: client.episode_offers.download(node_id),
        GraphQLError,
    )
