import json

import pytest

from just_scrape import JustScrape
from just_scrape.constants import TEST_FILE_DIR
from just_scrape.exceptions import GraphQLError


class TestParsing:
    def test_get_buy_box_offers(self) -> None:
        for file in (TEST_FILE_DIR / "get_buy_box_offers" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            JustScrape().parse_get_buy_box_offers(file_content)

    def test_get_new_titles(self) -> None:
        for file in (TEST_FILE_DIR / "get_new_titles" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            JustScrape().parse_get_new_titles(file_content)

    def test_get_new_title_buckets(self) -> None:
        for file in (TEST_FILE_DIR / "get_new_title_buckets" / "response").glob(
            "*.json",
        ):
            file_content = json.loads(file.read_text())
            JustScrape().parse_get_new_title_buckets(file_content)

    def test_get_url_title_details(self) -> None:
        for file in (TEST_FILE_DIR / "get_url_title_details" / "response").glob(
            "*.json",
        ):
            file_content = json.loads(file.read_text())
            JustScrape().parse_get_url_title_details(file_content)

    def test_get_title_detail_article(self) -> None:
        for file in (TEST_FILE_DIR / "get_title_detail_article" / "response").glob(
            "*.json",
        ):
            file_content = json.loads(file.read_text())
            JustScrape().parse_get_title_detail_article(file_content)

    def test_get_season_episodes(self) -> None:
        for file in (TEST_FILE_DIR / "get_season_episodes" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            JustScrape().parse_get_season_episodes(file_content)


class TestGetAll:
    def test_get_all_new_titles(self) -> None:
        new_titles = JustScrape().get_all_new_titles(
            filter_packages=["amp"],
            available_to_packages=["amp"],
        )
        # Amazon seems to always have at least 10 new episode every day so this will
        # probably always be true without looking weird hitting JustWatch's backlog.
        assert len(new_titles) > 10  # noqa: PLR2004

    def test_get_all_season_episodes(self) -> None:
        # https://www.justwatch.com/us/tv-show/king-of-the-hill/season-2
        season_id = "tss23744"
        number_of_episodes = 23
        season_episodes = JustScrape().get_all_season_episodes(node_id=season_id)
        assert len(season_episodes) == number_of_episodes


class TestGet:
    def test_get_movie_details(self) -> None:
        path = "/us/movie/the-thursday-murder-club"
        JustScrape().get_url_title_details(full_path=path)

    def test_get_tv_show_details(self) -> None:
        path = "/us/tv-show/south-park"
        JustScrape().get_url_title_details(full_path=path)

    def test_invalid_url(self) -> None:
        path = "/us/tv-show/a"
        with pytest.raises(GraphQLError, match="URL not found"):
            JustScrape().get_url_title_details(full_path=path)
