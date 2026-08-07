# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import InvalidFileError
from tests.update_ids import node_id_from_response, update_ids
from tests.utils import download_and_save, load_ids, parsed_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.buy_box_offers import BuyBoxOffers

NODE_IDS = load_ids("buy_box_offers")
"""Rewritten by ``test_update_ids``; add an id here and run the tests."""


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> BuyBoxOffers:
    return client.buy_box_offers


@pytest.fixture(params=NODE_IDS)
def node_id(request: pytest.FixtureRequest) -> str:
    return request.param


def test_download(endpoint: BuyBoxOffers, node_id: str) -> None:
    download_and_save(
        endpoint,
        node_id,
        lambda: endpoint.download(node_id),
    )


def test_parse(endpoint: BuyBoxOffers, node_id: str) -> None:
    data = parsed_json(endpoint, node_id)
    assert data.data.node.id == node_id


def test_update_ids(endpoint: BuyBoxOffers) -> None:
    assert update_ids(
        endpoint,
        "buy_box_offers",
        InvalidFileError,
        id_from_response=node_id_from_response,
    )
