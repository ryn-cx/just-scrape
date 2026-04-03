"""Tests for just_scrape."""

from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from just_scrape import JustScrape
from just_scrape.base_client import BaseEndpoint
from just_scrape.exceptions import GraphQLError

if TYPE_CHECKING:
    from pydantic import BaseModel

client = JustScrape()

LOGGED_FILES_PATH = Path(__file__).parent / "logged_files"

_run_timestamp = datetime.now().astimezone().strftime("%Y-%m-%dT%H_%M_%S")
RUN_FOLDER = LOGGED_FILES_PATH / _run_timestamp


def save_responses(folder_name: str, *responses: BaseModel) -> None:
    """Save API responses to disk for manual analysis."""
    folder = RUN_FOLDER / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().astimezone().strftime("%Y-%m-%dT%H_%M_%S")
    subfolder = folder / timestamp
    subfolder.mkdir(exist_ok=True)

    for i, response in enumerate(responses):
        dumped = BaseEndpoint.dump_response(response)
        file_path = subfolder / f"{i}.json"
        file_path.write_text(json.dumps(dumped, indent=2))


class TestParse:
    """Tests parsing files."""

    def test_parse_buy_box_offers(self) -> None:
        """Test parsing buy box offers files."""
        for json_file in client.buy_box_offers.json_files():
            file_content = json.loads(json_file.read_text())
            client.buy_box_offers.parse(file_content)

    def test_parse_custom_buy_box_offers(self) -> None:
        """Test parsing custom buy box offers files."""
        for json_file in client.custom_buy_box_offers.json_files():
            file_content = json.loads(json_file.read_text())
            client.custom_buy_box_offers.parse(file_content)

    def test_parse_new_titles(self) -> None:
        """Test parsing new titles files."""
        for json_file in client.new_titles.json_files():
            file_content = json.loads(json_file.read_text())
            client.new_titles.parse(file_content)

    def test_parse_new_title_buckets(self) -> None:
        """Test parsing new title buckets files."""
        for json_file in client.new_title_buckets.json_files():
            file_content = json.loads(json_file.read_text())
            client.new_title_buckets.parse(file_content)

    def test_parse_url_title_details(self) -> None:
        """Test parsing URL title details files."""
        for json_file in client.url_title_details.json_files():
            file_content = json.loads(json_file.read_text())
            client.url_title_details.parse(file_content)

    def test_parse_title_detail_article(self) -> None:
        """Test parsing title detail article files."""
        for json_file in client.title_detail_article.json_files():
            file_content = json.loads(json_file.read_text())
            client.title_detail_article.parse(file_content)

    def test_parse_season_episodes(self) -> None:
        """Test parsing season episodes files."""
        for json_file in client.season_episodes.json_files():
            file_content = json.loads(json_file.read_text())
            client.season_episodes.parse(file_content)

    def test_parse_custom_season_episodes(self) -> None:
        """Test parsing custom season episodes files."""
        for json_file in client.custom_season_episodes.json_files():
            file_content = json.loads(json_file.read_text())
            client.custom_season_episodes.parse(file_content)

    def test_parse_search(self) -> None:
        """Test parsing search files."""
        for json_file in client.search.json_files():
            file_content = json.loads(json_file.read_text())
            client.search.parse(file_content)


class TestGet:
    """Tests getting data."""

    class TestValid:
        """Tests getting data with valid inputs."""

        def test_get_buy_box_offers(self) -> None:
            """Test getting buy box offers."""
            response = client.buy_box_offers.get(node_id="tse9298997")
            save_responses("buy_box_offers", response)

        def test_get_custom_buy_box_offers(self) -> None:
            """Test getting custom buy box offers."""
            response = client.custom_buy_box_offers.get(
                node_id="tse9298997",
            )
            save_responses("custom_buy_box_offers", response)

        def test_get_new_title_buckets(self) -> None:
            """Test getting new title buckets."""
            response = client.new_title_buckets.get()
            save_responses("new_title_buckets", response)

        def test_get_new_titles(self) -> None:
            """Test getting new titles."""
            response = client.new_titles.get(
                filter_packages=["net"],
                available_to_packages=["net"],
            )
            save_responses("new_titles", response)

        def test_get_season_episodes(self) -> None:
            """Test getting season episodes."""
            response = client.season_episodes.get(node_id="tss337460")
            save_responses("season_episodes", response)

        def test_get_title_detail_article(self) -> None:
            """Test getting a title detail article."""
            response = client.title_detail_article.get(
                full_path="/us/movie/the-thursday-murder-club",
            )
            save_responses("title_detail_article", response)

        def test_get_url_title_details_movie(self) -> None:
            """Test getting URL title details for a movie."""
            response = client.url_title_details.get(
                full_path="/us/movie/the-thursday-murder-club",
            )
            save_responses("url_title_details", response)

        def test_get_url_title_details_tv_show(self) -> None:
            """Test getting URL title details for a TV show."""
            response = client.url_title_details.get(
                "/us/tv-show/strip-law",
            )
            save_responses("url_title_details", response)

        def test_get_url_title_details_unavailable_movie(self) -> None:
            """Test getting URL title details for an unavailable movie."""
            response = client.url_title_details.get(
                full_path="/us/movie/code-geass-akito-the-exiled-5-to-beloved-ones",
            )
            save_responses("url_title_details", response)

        def test_get_url_title_details_unavailable_tv_show(self) -> None:
            """Test getting URL title details for an unavailable TV show."""
            response = client.url_title_details.get(
                "/us/tv-show/darker-than-black",
            )
            save_responses("url_title_details", response)

        def test_get_custom_season_episodes(self) -> None:
            """Test getting custom season episodes."""
            response = client.custom_season_episodes.get(
                node_id="tss466559",
            )
            save_responses("custom_season_episodes", response)

        def test_get_search(self) -> None:
            """Test searching for titles."""
            response = client.search.get(search_query="jojo")
            save_responses("search", response)

        def test_get_all_new_titles_for_date(self) -> None:
            """Test getting all new titles for a date with pagination."""
            # This test needs more than 10 entries in the response for it
            # to show it is working correctly, Amazon usually has 10
            # entries, but sometimes it doesn't. So this test will go
            # through all entries in the last week until one is found with
            # more than 10 entries.

            # Always start 1 day behind current day because current day may have
            # incomplete data and is less likely to have at least 10 entries.
            for i in range(1, 10):
                all_new_titles_for_date = client.new_titles.get_all_for_date(
                    filter_packages=["amp"],
                    available_to_packages=["amp"],
                    date=datetime.now().astimezone().date() - timedelta(days=i),
                )
                expected_episodes = all_new_titles_for_date[
                    0
                ].data.new_titles.total_count
                # Amazon seems to usually have at least 10 new episodes
                # every day so this will USUALLY test true on the first
                # iteration but sometimes extra loops are required.
                all_edges = client.new_titles.extract_edges(all_new_titles_for_date)
                assert len(all_edges) == expected_episodes

                save_responses("new_titles", *all_new_titles_for_date)

                if expected_episodes > 10:  # noqa: PLR2004
                    break

        def test_get_all_new_titles_since_date(self) -> None:
            """Test getting all new titles since a date."""
            today = datetime.now().astimezone().date()
            responseses = client.new_titles.get_all_since_date(
                filter_packages=["amp"],
                available_to_packages=["amp"],
                start_date=today - timedelta(days=1),
                end_date=today - timedelta(days=2),
            )
            # There should be 2 days worth of responses and the data from the days
            # should be different.
            assert len(responseses) == 2  # noqa: PLR2004
            assert responseses[0] != responseses[1]

            # total_count is the total number of entries for the day, not the number
            # returned, so using just the first response will get the correct value for
            # expected_edges.
            expected_edges = 0
            for responses in responseses:
                expected_edges += responses[0].data.new_titles.total_count

            assert len(client.new_titles.extract_edges(responseses)) == expected_edges

            for responses in responseses:
                save_responses("new_titles", *responses)

        def test_get_all_new_title_buckets_since_date(self) -> None:
            """Test getting all new title buckets since a date."""
            today = datetime.now().astimezone().date()
            end_date = today - timedelta(days=5)

            all_buckets = client.new_title_buckets.get_all_since_date(
                first=3,
                end_date=end_date,
            )
            all_edges = client.new_title_buckets.extract_edges(all_buckets)

            assert len(all_buckets) >= 1
            assert len(all_edges) >= 1

            # If pagination occurred, verify we got more edges than
            # a single page would return.
            if len(all_buckets) > 1:
                assert len(all_edges) > 3  # noqa: PLR2004

            save_responses("new_title_buckets", *all_buckets)

        def test_get_all_season_episodes(self) -> None:
            """Test getting all season episodes with pagination."""
            season_id = "tss23744"
            number_of_episodes = 23
            season_episodes = client.season_episodes.get_all(node_id=season_id)
            episodes = client.season_episodes.extract_episodes(season_episodes)
            assert len(episodes) == number_of_episodes

            save_responses("season_episodes", *season_episodes)

        def test_get_all_custom_season_episodes(self) -> None:
            """Test getting all custom season episodes with pagination."""
            season_id = "tss23744"
            number_of_episodes = 23
            season_episodes = client.season_episodes.get_all(node_id=season_id)
            episodes = client.season_episodes.extract_episodes(season_episodes)
            assert len(episodes) == number_of_episodes

            save_responses("custom_season_episodes", *season_episodes)

    class TestInvalid:
        """Tests getting data with invalid inputs."""

        def test_get_buy_box_offers_invalid_id(self) -> None:
            """Test getting buy box offers with an invalid ID."""
            client.buy_box_offers.get(node_id="tse9999999")

        def test_get_custom_buy_box_offers_invalid_id(self) -> None:
            """Test getting custom buy box offers with an invalid ID."""
            client.custom_buy_box_offers.get(node_id="tse9999999")

        def test_get_season_episodes_invalid_id(self) -> None:
            """Test getting season episodes with an invalid ID."""
            client.season_episodes.get(node_id="tss999999")

        def test_get_custom_season_episodes_invalid_id(self) -> None:
            """Test getting custom season episodes with an invalid ID."""
            client.custom_season_episodes.get(node_id="tss999999")

        def test_get_title_detail_article_invalid_path(self) -> None:
            """Test getting a title detail article with an invalid path."""
            with pytest.raises(GraphQLError):
                client.title_detail_article.get(full_path="/us/movie/invalid-movie")

        def test_get_url_title_details_invalid_url(self) -> None:
            """Test getting URL title details with an invalid URL."""
            with pytest.raises(GraphQLError, match="URL not found"):
                client.url_title_details.get("/us/tv-show/invalid-url")
