# TODO: Validate
import json
from datetime import datetime, timedelta

from get_around import build_client_automatically

from just_scrape import JustScrape

client = JustScrape(get_around_client=build_client_automatically())


class TestNewTitleBuckets:
    def test_get(self) -> None:
        endpoint = client.new_title_buckets
        model = endpoint.get()
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_all_since_date(self) -> None:
        endpoint = client.new_title_buckets
        today = datetime.now().astimezone().date()
        end_date = today - timedelta(days=5)

        all_buckets = endpoint.get_all_since_date(end_date)
        for model in all_buckets:
            endpoint.save_new_json_file(endpoint.original_input(model))
        all_edges = endpoint.extract_edges(all_buckets)

        assert len(all_buckets) >= 1
        assert len(all_edges) >= 1

        if len(all_buckets) > 1:
            assert len(all_edges) > 3  # noqa: PLR2004

    def test_parse(self) -> None:
        endpoint = client.new_title_buckets
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_edges(self) -> None:
        endpoint = client.new_title_buckets
        for json_file in endpoint.json_files():
            parsed = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_edges(parsed)
