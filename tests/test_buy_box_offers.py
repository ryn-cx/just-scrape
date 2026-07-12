# TODO: Validate
import json

from get_around import build_client_automatically

from just_scrape import JustScrape

client = JustScrape(get_around_client=build_client_automatically())

BUY_BOX_NODE_ID = "tse9298997"
"""node_id used for buy box offer lookups."""
INVALID_NODE_ID = "tse9999999"


class TestBuyBoxOffers:
    def test_get(self) -> None:
        endpoint = client.buy_box_offers
        model = endpoint.get(node_id=BUY_BOX_NODE_ID)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        # This endpoint does not raise for an unknown node_id.
        client.buy_box_offers.get(INVALID_NODE_ID)

    def test_parse(self) -> None:
        endpoint = client.buy_box_offers
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
