import json
from collections.abc import Iterator
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError
from just_scrape.update_files import Updater

client = JustScrape()


class TestParsing:
    def get_test_files(self, endpoint: str) -> Iterator[Path]:
        """Get all JSON test files for a given endpoint."""
        updater = Updater(endpoint, "response")
        dir_path = updater.input_folder()
        if not dir_path.exists():
            pytest.fail(f"{dir_path} not found")

        return dir_path.glob("*.json")

    def test_get_buy_box_offers(self) -> None:
        for json_file in self.get_test_files("buy_box_offers"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_buy_box_offers(file_content)
            dumped = parsed.model_dump(mode="json", by_alias=True, exclude_unset=True)
            assert file_content == dumped

    def test_get_new_titles(self) -> None:
        for json_file in self.get_test_files("new_titles"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_new_titles(file_content)
            dumped = parsed.model_dump(mode="json", by_alias=True, exclude_unset=True)
            assert file_content == dumped

    def test_get_new_title_buckets(self) -> None:
        for json_file in self.get_test_files("new_title_buckets"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_new_title_buckets(file_content)
            dumped = parsed.model_dump(mode="json", by_alias=True, exclude_unset=True)
            assert file_content == dumped

    def test_get_url_title_details(self) -> None:
        for json_file in self.get_test_files("url_title_details"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_url_title_details(file_content)
            dumped = parsed.model_dump(mode="json", by_alias=True, exclude_unset=True)
            assert file_content == dumped

    def test_get_title_detail_article(self) -> None:
        for json_file in self.get_test_files("title_detail_article"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_get_title_detail_article(file_content)
            dumped = parsed.model_dump(mode="json", by_alias=True, exclude_unset=True)
            assert file_content == dumped

    def test_get_season_episodes(self) -> None:
        for json_file in self.get_test_files("season_episodes"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_season_episodes(file_content)
            dumped = parsed.model_dump(mode="json", by_alias=True, exclude_unset=True)
            assert file_content == dumped


class TestGet:
    def test_get_buy_box_offers(self) -> None:
        client.get_buy_box_offers(node_id="tse9298997")

    def test_get_new_title_buckets(self) -> None:
        client.get_new_title_buckets()

    def test_get_new_titles(self) -> None:
        client.get_new_titles(filter_packages=["net"], available_to_packages=["net"])

    def test_get_season_episodes(self) -> None:
        client.get_season_episodes(node_id="tss337460")

    def test_get_title_detail_article(self) -> None:
        client.get_title_detail_article(full_path="/us/movie/the-thursday-murder-club")

    def test_get_url_title_details_movie(self) -> None:
        client.get_url_title_details(full_path="/us/movie/the-thursday-murder-club")

    def test_get_url_title_details_tv_show(self) -> None:
        client.get_url_title_details("/us/tv-show/south-park")

    def test_get_url_title_details_invalid_url(self) -> None:
        with pytest.raises(GraphQLError, match="URL not found"):
            client.get_url_title_details("/us/tv-show/invalid-url")


class TestCustomGet:
    def test_get_all_new_titles_for_date(self) -> None:
        # This test needs more than 10 entries in the response for it to show it is
        # working correctly, Amazon usually has 10 entries, but sometimes it doesn't. So
        # this test will go through all entries in the last week until one is found
        # with more than 10 entries.

        # Always start 1 day behind current day because current day may have incomplete
        # data and is less likely to have at least 10 entries.
        for i in range(1, 10):
            all_new_titles_for_date = client.get_all_new_titles_for_date(
                filter_packages=["amp"],
                available_to_packages=["amp"],
                date=datetime.now().astimezone().date() - timedelta(days=i),
            )
            expected_episodes = all_new_titles_for_date[0].data.new_titles.total_count
            # Amazon seems to usually have at least 10 new episode every day so this
            # will USUALLY test true on the first iteration but sometimes extra loops
            # are required.
            all_edges = client.new_titles_edges(all_new_titles_for_date)
            assert len(all_edges) == expected_episodes

            if expected_episodes > 10:  # noqa: PLR2004
                break

    def test_get_all_new_titles_since_date(self) -> None:
        responseses = client.get_all_new_titles_since_date(
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

        actual_edges = len(client.new_titles_edges(responseses))

        assert expected_edges == actual_edges

    def test_get_all_season_episodes(self) -> None:
        season_id = "tss23744"
        number_of_episodes = 23
        season_episodes = client.get_all_season_episodes(node_id=season_id)
        episodes = client.get_actual_season_episodes(season_episodes)
        assert len(episodes) == number_of_episodes
