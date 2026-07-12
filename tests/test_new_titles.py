# TODO: Validate
import json
from datetime import datetime, timedelta

from get_around import build_client_automatically

from just_scrape import JustScrape

client = JustScrape(get_around_client=build_client_automatically())


class TestNewTitles:
    def test_get(self) -> None:
        endpoint = client.new_titles
        model = endpoint.get(
            filter_packages=["net"],
            available_to_packages=["net"],
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_all_for_date(self) -> None:
        # This test needs more than 10 entries in the response for it to show it
        # is working correctly. Amazon usually has 10 entries, but sometimes it
        # doesn't, so this test walks back through the last week until one is
        # found with more than 10 entries.

        # Always start 1 day behind the current day because the current day may
        # have incomplete data and is less likely to have 10+ entries.
        endpoint = client.new_titles
        for i in range(1, 10):
            new_titles = endpoint.get_all_for_date(
                filter_packages=["amp"],
                available_to_packages=["amp"],
                date=datetime.now().astimezone().date() - timedelta(days=i),
            )
            for model in new_titles:
                endpoint.save_new_json_file(endpoint.original_input(model))
            expected_episodes = new_titles[0].data.new_titles.total_count
            all_edges = endpoint.extract_edges(new_titles)
            assert len(all_edges) == expected_episodes

            if expected_episodes > 10:  # noqa: PLR2004
                break

    def test_get_all_since_date(self) -> None:
        endpoint = client.new_titles
        today = datetime.now().astimezone().date()
        new_titles = endpoint.get_all_since_date(
            today - timedelta(days=1),
            filter_packages=["amp"],
            available_to_packages=["amp"],
            end_date=today - timedelta(days=2),
        )
        for page in new_titles:
            for model in page:
                endpoint.save_new_json_file(endpoint.original_input(model))
        assert len(new_titles) == 2  # noqa: PLR2004
        assert new_titles[0] != new_titles[1]

        expected_edges = 0
        for responses in new_titles:
            expected_edges += responses[0].data.new_titles.total_count

        assert len(endpoint.extract_edges(new_titles)) == expected_edges

    def test_parse(self) -> None:
        endpoint = client.new_titles
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_edges(self) -> None:
        endpoint = client.new_titles
        for json_file in endpoint.json_files():
            parsed = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_edges(parsed)
