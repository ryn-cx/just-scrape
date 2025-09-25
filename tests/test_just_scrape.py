import json
from collections.abc import Iterator
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError
from just_scrape.utils.update_files import Updater

client = JustScrape()


class TestParsing:
    def get_test_files(self, endpoint: str) -> Iterator[Path]:
        """Get all JSON test files for a given endpoint."""
        updater = Updater("response", endpoint)
        dir_path = updater.input_folder()
        if not dir_path.exists():
            pytest.fail(f"{dir_path} not found")

        return dir_path.glob("*.json")

    def test_get_buy_box_offers(self) -> None:
        for json_file in self.get_test_files("get_buy_box_offers"):
            file_content = json.loads(json_file.read_text())
            client.parse_get_buy_box_offers(file_content)

    def test_get_new_titles(self) -> None:
        for json_file in self.get_test_files("get_new_titles"):
            file_content = json.loads(json_file.read_text())
            client.parse_get_new_titles(file_content)

    def test_get_new_title_buckets(self) -> None:
        for json_file in self.get_test_files("get_new_title_buckets"):
            file_content = json.loads(json_file.read_text())
            client.parse_get_new_title_buckets(file_content)

    def test_get_url_title_details(self) -> None:
        for json_file in self.get_test_files("get_url_title_details"):
            file_content = json.loads(json_file.read_text())
            client.parse_get_url_title_details(file_content)

    def test_get_title_detail_article(self) -> None:
        for json_file in self.get_test_files("get_title_detail_article"):
            file_content = json.loads(json_file.read_text())
            client.parse_get_title_detail_article(file_content)

    def test_get_season_episodes(self) -> None:
        for json_file in self.get_test_files("get_season_episodes"):
            file_content = json.loads(json_file.read_text())
            client.parse_get_season_episodes(file_content)


class TestGetAll:
    def test_get_all_new_titles(self) -> None:
        new_titles = client.get_all_new_titles(
            filter_packages=["amp"],
            available_to_packages=["amp"],
        )
        # Amazon seems to always have at least 10 new episode every day so this will
        # probably always be true without looking weird hitting JustWatch's backlog.
        assert len(new_titles) > 10  # noqa: PLR2004

    def test_get_all_new_titles_since(self) -> None:
        new_titles = client.get_all_new_titles_since(
            filter_packages=["cru"],
            available_to_packages=["cru"],
            end_date=datetime.now().astimezone().date() - timedelta(days=7),
        )
        # There will probably always be at least 10 new titles on a weekly basis
        assert len(new_titles) > 10  # noqa: PLR2004

    def test_get_all_season_episodes(self) -> None:
        # https://www.justwatch.com/us/tv-show/king-of-the-hill/season-2
        season_id = "tss23744"
        number_of_episodes = 23
        season_episodes = client.get_all_season_episodes(node_id=season_id)
        assert len(season_episodes) == number_of_episodes


class TestGet:
    def test_get_movie_details(self) -> None:
        client.get_url_title_details(full_path="/us/movie/the-thursday-murder-club")

    def test_get_tv_show_details(self) -> None:
        client.get_url_title_details("/us/tv-show/south-park")

    def test_invalid_url(self) -> None:
        with pytest.raises(GraphQLError, match="URL not found"):
            client.get_url_title_details("/us/tv-show/invalid-url")
