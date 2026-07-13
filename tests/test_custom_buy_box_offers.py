# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from tests.utils import download_if_missing

if TYPE_CHECKING:
    from just_scrape.custom_buy_box_offers import CustomBuyBoxOffers

client = JustScrape(get_around_client=build_client_automatically())

BUY_BOX_NODE_ID = "tse9298997"
"""node_id used for buy box offer lookups."""
INVALID_NODE_ID = "tse9999999"


@pytest.fixture(scope="session")
def endpoint() -> CustomBuyBoxOffers:
    return client.custom_buy_box_offers


class TestCustomBuyBoxOffers:
    def test_download(self, endpoint: CustomBuyBoxOffers) -> None:
        download_if_missing(
            endpoint,
            BUY_BOX_NODE_ID,
            lambda: endpoint.download(BUY_BOX_NODE_ID),
        )

    def test_invalid(self, endpoint: CustomBuyBoxOffers) -> None:
        # This endpoint does not raise for an unknown node_id.
        path = download_if_missing(
            endpoint,
            INVALID_NODE_ID,
            lambda: endpoint.download(INVALID_NODE_ID),
        )
        data = endpoint.parse(json.loads(path.read_text()))
        assert data is not None
