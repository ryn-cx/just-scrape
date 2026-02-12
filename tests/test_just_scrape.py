import json
from datetime import datetime, timedelta

import pytest

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError

client = JustScrape()


class TestParsing:
    def test_parse_buy_box_offers(self) -> None:
        """Parse all saved buy box offers JSON files."""
        for json_file in client.buy_box_offers.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.buy_box_offers.parse(file_content)

    def test_parse_custom_buy_box_offers(self) -> None:
        """Parse all saved custom buy box offers JSON files."""
        for json_file in client.custom_buy_box_offers.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.custom_buy_box_offers.parse(file_content)

    def test_parse_new_titles(self) -> None:
        """Parse all saved new titles JSON files."""
        for json_file in client.new_titles.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.new_titles.parse(file_content)

    def test_parse_new_title_buckets(self) -> None:
        """Parse all saved new title buckets JSON files."""
        for json_file in client.new_title_buckets.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.new_title_buckets.parse(file_content)

    def test_parse_url_title_details(self) -> None:
        """Parse all saved URL title details JSON files."""
        for json_file in client.url_title_details.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.url_title_details.parse(file_content)

    def test_parse_title_detail_article(self) -> None:
        """Parse all saved title detail article JSON files."""
        for json_file in client.title_detail_article.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.title_detail_article.parse(file_content)

    def test_parse_season_episodes(self) -> None:
        """Parse all saved season episodes JSON files."""
        for json_file in client.season_episodes.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.season_episodes.parse(file_content)

    def test_parse_custom_season_episodes(self) -> None:
        """Parse all saved custom season episodes JSON files."""
        for json_file in client.custom_season_episodes.json_files_folder.glob("*.json"):
            file_content = json.loads(json_file.read_text())
            client.custom_season_episodes.parse(file_content)


class TestGet:
    def test_get_buy_box_offers(self) -> None:
        client.buy_box_offers.get(node_id="tse9298997")

    def test_get_custom_buy_box_offers(self) -> None:
        client.custom_buy_box_offers.get(node_id="tse9298997")

    def test_get_new_title_buckets(self) -> None:
        client.new_title_buckets.get()

    def test_get_new_titles(self) -> None:
        client.new_titles.get(filter_packages=["net"], available_to_packages=["net"])

    def test_get_season_episodes(self) -> None:
        client.season_episodes.get(node_id="tss337460")

    def test_get_title_detail_article(self) -> None:
        client.title_detail_article.get(full_path="/us/movie/the-thursday-murder-club")

    def test_get_url_title_details_movie(self) -> None:
        client.url_title_details.get(full_path="/us/movie/the-thursday-murder-club")

    def test_get_url_title_details_tv_show(self) -> None:
        client.url_title_details.get("/us/tv-show/south-park")

    def test_get_url_title_details_invalid_url(self) -> None:
        with pytest.raises(GraphQLError, match="URL not found"):
            client.url_title_details.get("/us/tv-show/invalid-url")

    def test_custom_season_episodes(self) -> None:
        client.custom_season_episodes.get(node_id="tss466559")


class TestCustomGet:
    def test_get_all_new_titles_for_date(self) -> None:
        # This test needs more than 10 entries in the response for it to show it is
        # working correctly, Amazon usually has 10 entries, but sometimes it doesn't. So
        # this test will go through all entries in the last week until one is found
        # with more than 10 entries.

        # Always start 1 day behind current day because current day may have incomplete
        # data and is less likely to have at least 10 entries.
        for i in range(1, 10):
            all_new_titles_for_date = client.new_titles.get_all_for_date(
                filter_packages=["amp"],
                available_to_packages=["amp"],
                date=datetime.now().astimezone().date() - timedelta(days=i),
            )
            expected_episodes = all_new_titles_for_date[0].data.new_titles.total_count
            # Amazon seems to usually have at least 10 new episode every day so this
            # will USUALLY test true on the first iteration but sometimes extra loops
            # are required.
            all_edges = client.new_titles.extract_edges(all_new_titles_for_date)
            assert len(all_edges) == expected_episodes

            if expected_episodes > 10:  # noqa: PLR2004
                break

    def test_get_all_new_titles_since_date(self) -> None:
        responseses = client.new_titles.get_all_since_date(
            filter_packages=["amp"],
            available_to_packages=["amp"],
            start_date=datetime.now().astimezone().date() - timedelta(days=1),
            end_date=datetime.now().astimezone().date() - timedelta(days=2),
        )
        # There should be 2 days worth of responses and the data from the days should be
        # different.
        assert len(responseses) == 2  # noqa: PLR2004
        assert responseses[0] != responseses[1]

        # total_count is the total number of entries for the day, not the number
        # returned, so using just the first response will get the correct value for
        # expected_edges.
        expected_edges = 0
        for responses in responseses:
            expected_edges += responses[0].data.new_titles.total_count

        assert len(client.new_titles.extract_edges(responseses)) == expected_edges

    def test_get_all_season_episodes(self) -> None:
        season_id = "tss23744"
        number_of_episodes = 23
        season_episodes = client.season_episodes.get_all(node_id=season_id)
        episodes = client.season_episodes.extract_episodes(season_episodes)
        assert len(episodes) == number_of_episodes

    def test_get_custom_all_season_episodes(self) -> None:
        season_id = "tss23744"
        number_of_episodes = 23
        season_episodes = client.season_episodes.get_all(node_id=season_id)
        episodes = client.season_episodes.extract_episodes(season_episodes)
        assert len(episodes) == number_of_episodes
