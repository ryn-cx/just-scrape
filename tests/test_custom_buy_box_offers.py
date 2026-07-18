# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.custom_buy_box_offers import CustomBuyBoxOffers

BUY_BOX_NODE_ID = "tse9298997"
"""node_id used for buy box offer lookups."""
INVALID_NODE_ID = "tse9999999"


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> CustomBuyBoxOffers:
    return client.custom_buy_box_offers


class TestCustomBuyBoxOffers:
    def test_download(self, endpoint: CustomBuyBoxOffers) -> None:
        download_and_save(
            endpoint,
            BUY_BOX_NODE_ID,
            lambda: endpoint.download(BUY_BOX_NODE_ID),
        )

    def test_parse(self, endpoint: CustomBuyBoxOffers) -> None:
        data = parse_json(endpoint, BUY_BOX_NODE_ID)
        assert data is not None

    # This endpoint does not raise for an unknown node_id, so the invalid case is
    # recorded and parsed like any other download.
    def test_invalid_download(self, endpoint: CustomBuyBoxOffers) -> None:
        download_and_save(
            endpoint,
            INVALID_NODE_ID,
            lambda: endpoint.download(INVALID_NODE_ID),
        )

    def test_invalid_parse(self, endpoint: CustomBuyBoxOffers) -> None:
        data = parse_json(endpoint, INVALID_NODE_ID)
        assert data is not None


@pytest.mark.parametrize("country", [None, "CA"])
def test_log_id(endpoint: CustomBuyBoxOffers, country: str | None) -> None:
    expected = f"CustomBuyBoxOffers node_id={BUY_BOX_NODE_ID!r}"
    if country is not None:
        expected += f" country={country!r}"
    assert endpoint.get_log_id(BUY_BOX_NODE_ID, country=country or "US") == expected
