# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError

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
@pytest.mark.parametrize("node_id", NODE_IDS)
def test_download(client: JustScrape, node_id: str) -> None:
    episode = client.episode_offers(node_id)
    assert episode.id == node_id


# TODO: Validate
def test_download_invalid(client: JustScrape) -> None:
    with pytest.raises(GraphQLError):
        client.episode_offers.download("0000000")
