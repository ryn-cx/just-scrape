# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.buy_box_offers import BuyBoxOffers

BUY_BOX_NODE_ID = "tse9298997"
"""node_id used for buy box offer lookups."""
ANIME_NODE_ID = "tse87753"
"""node_id whose offers carry audio languages and nested plan children."""
INVALID_NODE_ID = "tse9999999"
"""This endpoint does not raise for an unknown node_id, so the invalid case is
recorded and parsed like any other node_id."""

NODE_IDS = [BUY_BOX_NODE_ID, ANIME_NODE_ID, INVALID_NODE_ID]


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> BuyBoxOffers:
    return client.buy_box_offers


@pytest.fixture(params=NODE_IDS)
def node_id(request: pytest.FixtureRequest) -> str:
    return request.param


class TestBuyBoxOffers:
    def test_download(self, endpoint: BuyBoxOffers, node_id: str) -> None:
        download_and_save(
            endpoint,
            node_id,
            lambda: endpoint.download(node_id),
        )

    def test_parse(self, endpoint: BuyBoxOffers, node_id: str) -> None:
        data = parsed_json(endpoint, node_id)
        assert data.data.node.id == node_id
