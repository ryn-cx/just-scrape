import json
from pathlib import Path

import just_scrape.wrappers._get_buy_box_offers as get_buy_box_offers
import just_scrape.wrappers._get_content_providers as get_content_providers
import just_scrape.wrappers._get_new_title_buckets as get_new_title_buckets
import just_scrape.wrappers._get_new_titles as get_new_titles
import just_scrape.wrappers._get_season_episodes as get_season_episodes
import just_scrape.wrappers._get_title_detail_article as get_title_detail_article
import just_scrape.wrappers._get_url_title_details as get_url_title_details

ROOT_DIR = Path(__file__).parent.parent
SCHEMAS_DIR = ROOT_DIR / "schemas"
TEST_FILE_DIR = ROOT_DIR / "tests/files"


# TODO: Downloading tests
class TestGetBuyBoxOffers:
    def test_parsing(self) -> None:
        for file in (SCHEMAS_DIR / "get_buy_box_offers").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_buy_box_offers.parse(file_content)


class TestGetNewTitles:
    def test_parsing(self) -> None:
        for file in (SCHEMAS_DIR / "get_new_titles").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_new_titles.parse(file_content)


class TestGetNewTitleBuckets:
    def test_parsing(self) -> None:
        for file in (SCHEMAS_DIR / "get_new_title_buckets").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_new_title_buckets.parse(file_content)


class TestGetUrlTitleDetails:
    def test_parsing(self) -> None:
        for file in (SCHEMAS_DIR / "get_url_title_details").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_url_title_details.parse(file_content)

    def test_get_movie_details(self) -> None:
        path = "/us/movie/the-thursday-murder-club"
        get_url_title_details.get_url_title_details(full_path=path)

    def test_get_tv_show_details(self) -> None:
        path = "/us/tv-show/south-park"
        get_url_title_details.get_url_title_details(full_path=path)


class TestGetTitleDetailArticle:
    def test_parsing(self) -> None:
        for file in (SCHEMAS_DIR / "get_title_detail_article").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_title_detail_article.parse(file_content)


class TestGetContentProviders:
    def test_parsing(self) -> None:
        for file in (SCHEMAS_DIR / "get_content_providers").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_content_providers.parse(file_content)


class TestGetSeasonEpisodes:
    def test_parsing(self) -> None:
        for file in (SCHEMAS_DIR / "get_season_episodes").glob("*.json"):
            file_content = json.loads(file.read_text())
            get_season_episodes.parse(file_content)

    def test_get_all_season_episodes(self) -> None:
        # https://www.justwatch.com/us/tv-show/king-of-the-hill/season-2
        season_id = "tss23744"
        number_of_episodes = 23
        season_episodes = get_season_episodes.get_all_season_episodes(node_id=season_id)
        assert len(season_episodes) == number_of_episodes
