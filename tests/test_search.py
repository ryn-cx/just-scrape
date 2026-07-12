# TODO: Validate
import json

from get_around import build_client_automatically

from just_scrape import JustScrape

client = JustScrape(get_around_client=build_client_automatically())

SEARCH_QUERY = "Breaking"
"""A search term that matches titles."""
INVALID_SEARCH_QUERY = "zxcvbbnm"


class TestSearch:
    def test_get(self) -> None:
        endpoint = client.search
        model = endpoint.get(search_query=SEARCH_QUERY)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        response = client.search.get(search_query=INVALID_SEARCH_QUERY)
        assert response.data.search_titles.total_count == 0
        assert response.data.search_titles.edges == []

    def test_parse(self) -> None:
        endpoint = client.search
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
