"""Tests for just_scrape."""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta

import pytest
from dotenv import load_dotenv

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError

load_dotenv()

client = JustScrape(
    get_around_server=os.environ["GET_AROUND_SERVER"],
    get_around_password=os.environ["GET_AROUND_PASSWORD"],
)


class TestParse:
    """Tests parsing files."""

    def test_parse_buy_box_offers(self) -> None:
        """Test parsing buy box offers files."""
        for json_file in client.buy_box_offers.json_files():
            client.buy_box_offers.parse(json.loads(json_file.read_text()))

    def test_parse_custom_buy_box_offers(self) -> None:
        """Test parsing custom buy box offers files."""
        for json_file in client.custom_buy_box_offers.json_files():
            client.custom_buy_box_offers.parse(json.loads(json_file.read_text()))

    def test_parse_new_titles(self) -> None:
        """Test parsing new titles files."""
        for json_file in client.new_titles.json_files():
            client.new_titles.parse(json.loads(json_file.read_text()))

    def test_parse_new_title_buckets(self) -> None:
        """Test parsing new title buckets files."""
        for json_file in client.new_title_buckets.json_files():
            client.new_title_buckets.parse(json.loads(json_file.read_text()))

    def test_parse_url_title_details(self) -> None:
        """Test parsing URL title details files."""
        for json_file in client.url_title_details.json_files():
            client.url_title_details.parse(json.loads(json_file.read_text()))

    def test_parse_title_detail_article(self) -> None:
        """Test parsing title detail article files."""
        for json_file in client.title_detail_article.json_files():
            client.title_detail_article.parse(json.loads(json_file.read_text()))

    def test_parse_season_episodes(self) -> None:
        """Test parsing season episodes files."""
        for json_file in client.season_episodes.json_files():
            client.season_episodes.parse(json.loads(json_file.read_text()))

    def test_parse_custom_season_episodes(self) -> None:
        """Test parsing custom season episodes files."""
        for json_file in client.custom_season_episodes.json_files():
            client.custom_season_episodes.parse(json.loads(json_file.read_text()))

    def test_parse_search(self) -> None:
        """Test parsing search files."""
        for json_file in client.search.json_files():
            client.search.parse(json.loads(json_file.read_text()))


class TestGet:
    """Tests getting data."""

    class TestValid:
        """Tests getting data with valid inputs."""

        def test_get_buy_box_offers(self) -> None:
            """Test getting buy box offers."""
            client.buy_box_offers.get(node_id="tse9298997")

        def test_get_custom_buy_box_offers(self) -> None:
            """Test getting custom buy box offers."""
            client.custom_buy_box_offers.get(node_id="tse9298997")

        def test_get_new_title_buckets(self) -> None:
            """Test getting new title buckets."""
            client.new_title_buckets.get()

        def test_get_new_titles(self) -> None:
            """Test getting new titles."""
            client.new_titles.get(
                filter_packages=["net"],
                available_to_packages=["net"],
            )

        def test_get_season_episodes(self) -> None:
            """Test getting season episodes."""
            client.season_episodes.get("tss337460")

        def test_get_title_detail_article(self) -> None:
            """Test getting a title detail article."""
            client.title_detail_article.get("/us/movie/the-thursday-murder-club")

        def test_get_url_title_details_movie(self) -> None:
            """Test getting URL title details for a movie."""
            client.url_title_details.get("/us/movie/the-thursday-murder-club")

        def test_get_url_title_details_tv_show(self) -> None:
            """Test getting URL title details for a TV show."""
            client.url_title_details.get("/us/tv-show/strip-law")

        def test_get_url_title_details_unavailable_movie(self) -> None:
            """Test getting URL title details for an unavailable movie."""
            client.url_title_details.get(
                "/us/movie/code-geass-akito-the-exiled-5-to-beloved-ones",
            )

        def test_get_url_title_details_unavailable_tv_show(self) -> None:
            """Test getting URL title details for an unavailable TV show."""
            client.url_title_details.get("/us/tv-show/darker-than-black")

        def test_get_custom_season_episodes(self) -> None:
            """Test getting custom season episodes."""
            client.custom_season_episodes.get("tss466559")

        def test_get_search(self) -> None:
            """Test searching for titles."""
            client.search.get(search_query="Breaking")

        def test_get_all_new_titles_for_date(self) -> None:
            """Test getting all new titles for a date with pagination."""
            # This test needs more than 10 entries in the response for it
            # to show it is working correctly, Amazon usually has 10
            # entries, but sometimes it doesn't. So this test will go
            # through all entries in the last week until one is found with
            # more than 10 entries.

            # Always start 1 day behind current day because current day may
            # have incomplete data and is less likely to have 10+ entries.
            for i in range(1, 10):
                new_titles = client.new_titles.get_all_for_date(
                    filter_packages=["amp"],
                    available_to_packages=["amp"],
                    date=datetime.now().astimezone().date() - timedelta(days=i),
                )
                expected_episodes = new_titles[0].data.new_titles.total_count
                all_edges = client.new_titles.extract_edges(new_titles)
                assert len(all_edges) == expected_episodes

                if expected_episodes > 10:  # noqa: PLR2004
                    break

        def test_get_all_new_titles_since_date(self) -> None:
            """Test getting all new titles since a date."""
            today = datetime.now().astimezone().date()
            new_titles = client.new_titles.get_all_since_date(
                today - timedelta(days=1),
                filter_packages=["amp"],
                available_to_packages=["amp"],
                end_date=today - timedelta(days=2),
            )
            assert len(new_titles) == 2  # noqa: PLR2004
            assert new_titles[0] != new_titles[1]

            expected_edges = 0
            for responses in new_titles:
                expected_edges += responses[0].data.new_titles.total_count

            assert len(client.new_titles.extract_edges(new_titles)) == expected_edges

        def test_get_all_new_title_buckets_since_date(self) -> None:
            """Test getting all new title buckets since a date."""
            today = datetime.now().astimezone().date()
            end_date = today - timedelta(days=5)

            all_buckets = client.new_title_buckets.get_all_since_date(end_date)
            all_edges = client.new_title_buckets.extract_edges(all_buckets)

            assert len(all_buckets) >= 1
            assert len(all_edges) >= 1

            if len(all_buckets) > 1:
                assert len(all_edges) > 3  # noqa: PLR2004

        def test_get_all_season_episodes(self) -> None:
            """Test getting all season episodes with pagination."""
            season_episodes = client.season_episodes.get_all("tss23744")
            episodes = client.season_episodes.extract_episodes(season_episodes)
            assert len(episodes) == 23  # noqa: PLR2004

        def test_get_all_custom_season_episodes(self) -> None:
            """Test getting all custom season episodes with pagination."""
            season_episodes = client.season_episodes.get_all("tss23744")
            episodes = client.season_episodes.extract_episodes(season_episodes)
            assert len(episodes) == 23  # noqa: PLR2004

    class TestInvalid:
        """Tests getting data with invalid inputs."""

        def test_get_buy_box_offers_invalid_id(self) -> None:
            """Test getting buy box offers with an invalid ID."""
            client.buy_box_offers.get("tse9999999")

        def test_get_custom_buy_box_offers_invalid_id(self) -> None:
            """Test getting custom buy box offers with an invalid ID."""
            client.custom_buy_box_offers.get("tse9999999")

        def test_get_season_episodes_invalid_id(self) -> None:
            """Test getting season episodes with an invalid ID."""
            client.season_episodes.get("tss999999")

        def test_get_custom_season_episodes_invalid_id(self) -> None:
            """Test getting custom season episodes with an invalid ID."""
            client.custom_season_episodes.get("tss999999")

        def test_get_title_detail_article_invalid_path(self) -> None:
            """Test getting a title detail article with an invalid path."""
            with pytest.raises(GraphQLError):
                client.title_detail_article.get("/us/movie/invalid-movie")

        def test_get_url_title_details_invalid_url(self) -> None:
            """Test getting URL title details with an invalid URL."""
            with pytest.raises(GraphQLError, match="URL not found"):
                client.url_title_details.get("/us/tv-show/invalid-url")

        def test_get_search_no_results(self) -> None:
            """Test searching with a query that returns no results."""
            response = client.search.get(search_query="zxcvbbnm")
            assert response.data.search_titles.total_count == 0
            assert response.data.search_titles.edges == []
