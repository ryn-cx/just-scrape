import json
from pathlib import Path

import pytest

import just_scrape.wrappers.get_buy_box_offers_ as get_buy_box_offers
import just_scrape.wrappers.get_new_title_buckets_ as get_new_title_buckets
import just_scrape.wrappers.get_new_titles_ as get_new_titles
import just_scrape.wrappers.get_season_episodes_ as get_season_episodes
import just_scrape.wrappers.get_title_detail_article_ as get_title_detail_article
import just_scrape.wrappers.get_url_title_details_ as get_url_title_details

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_DIR = ROOT_DIR / "src/just_scrape/schema"
TEST_FILE_DIR = ROOT_DIR / "tests/files"


class TestParsing:
    def test_get_buy_box_offers(self) -> None:
        for file in (SCHEMA_DIR / "get_buy_box_offers" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_buy_box_offers.parse(file_content)

    def test_get_new_titles(self) -> None:
        for file in (SCHEMA_DIR / "get_new_titles" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_new_titles.parse(file_content)

    def test_get_new_title_buckets(self) -> None:
        for file in (SCHEMA_DIR / "get_new_title_buckets" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_new_title_buckets.parse(file_content)

    def test_get_url_title_details(self) -> None:
        for file in (SCHEMA_DIR / "get_url_title_details" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_url_title_details.parse(file_content)

    def test_get_title_detail_article(self) -> None:
        for file in (SCHEMA_DIR / "get_title_detail_article" / "response").glob(
            "*.json",
        ):
            file_content = json.loads(file.read_text())
            get_title_detail_article.parse(file_content)

    def test_get_season_episodes(self) -> None:
        for file in (SCHEMA_DIR / "get_season_episodes" / "response").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_season_episodes.parse(file_content)


class TestGetAll:
    def test_get_all_new_titles(self) -> None:
        new_titles = get_new_titles.get_all_new_titles(
            filter_packages=["amp"],
            available_to_packages=["amp"],
        )
        # Amazon seems to always have at least 10 new episode every day so this will
        # probably always be true without looking weird hitting JustWatch's backlog.
        assert len(new_titles) > get_new_titles.get_variables().first

    def test_get_all_season_episodes(self) -> None:
        # https://www.justwatch.com/us/tv-show/king-of-the-hill/season-2
        season_id = "tss23744"
        number_of_episodes = 23
        season_episodes = get_season_episodes.get_all_season_episodes(node_id=season_id)
        assert len(season_episodes) == number_of_episodes


class TestGet:
    def test_get_movie_details(self) -> None:
        path = "/us/movie/the-thursday-murder-club"
        get_url_title_details.get_url_title_details(full_path=path)

    def test_get_tv_show_details(self) -> None:
        path = "/us/tv-show/south-park"
        get_url_title_details.get_url_title_details(full_path=path)

    def test_invalid_url(self) -> None:
        path = "/us/tv-show/a"
        with pytest.raises(ValueError, match="URL not found"):
            get_url_title_details.get_url_title_details(full_path=path)
