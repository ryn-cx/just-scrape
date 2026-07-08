# TODO: Validate
"""Tests for just_scrape."""

from __future__ import annotations

import json
from datetime import datetime, timedelta

import pytest
from dotenv import load_dotenv

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError

load_dotenv()

client = JustScrape(
    # get_around_server=os.environ["GET_AROUND_SERVER"],
    # get_around_password=os.environ["GET_AROUND_PASSWORD"],
)


class TestGet:
    """Test live get requests across every endpoint."""

    def test_get_buy_box_offers(self) -> None:
        """Test getting buy box offers."""
        model = client.buy_box_offers.get(node_id="tse9298997")
        client.buy_box_offers.save_new_json_file(
            client.buy_box_offers.original_input(model)
        )

    def test_get_custom_buy_box_offers(self) -> None:
        """Test getting custom buy box offers."""
        model = client.custom_buy_box_offers.get(node_id="tse9298997")
        client.custom_buy_box_offers.save_new_json_file(
            client.custom_buy_box_offers.original_input(model),
        )

    def test_get_custom_season_episodes(self) -> None:
        """Test getting custom season episodes."""
        model = client.custom_season_episodes.get("tss466559")
        client.custom_season_episodes.save_new_json_file(
            client.custom_season_episodes.original_input(model),
        )

    def test_get_custom_season_episodes_all(self) -> None:
        """Test getting all custom season episodes with pagination."""
        season_episodes = client.custom_season_episodes.get_all("tss23744")
        for model in season_episodes:
            client.custom_season_episodes.save_new_json_file(
                client.custom_season_episodes.original_input(model),
            )
        episodes = client.custom_season_episodes.extract_episodes(season_episodes)
        assert len(episodes) == 23  # noqa: PLR2004

    def test_get_new_title_buckets(self) -> None:
        """Test getting new title buckets."""
        model = client.new_title_buckets.get()
        client.new_title_buckets.save_new_json_file(
            client.new_title_buckets.original_input(model),
        )

    def test_get_new_title_buckets_all_since_date(self) -> None:
        """Test getting all new title buckets since a date with pagination."""
        today = datetime.now().astimezone().date()
        end_date = today - timedelta(days=5)

        all_buckets = client.new_title_buckets.get_all_since_date(end_date)
        for model in all_buckets:
            client.new_title_buckets.save_new_json_file(
                client.new_title_buckets.original_input(model),
            )
        all_edges = client.new_title_buckets.extract_edges(all_buckets)

        assert len(all_buckets) >= 1
        assert len(all_edges) >= 1

        if len(all_buckets) > 1:
            assert len(all_edges) > 3  # noqa: PLR2004

    def test_get_new_titles(self) -> None:
        """Test getting new titles."""
        model = client.new_titles.get(
            filter_packages=["net"],
            available_to_packages=["net"],
        )
        client.new_titles.save_new_json_file(client.new_titles.original_input(model))

    def test_get_new_titles_all_for_date(self) -> None:
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
            for model in new_titles:
                client.new_titles.save_new_json_file(
                    client.new_titles.original_input(model)
                )
            expected_episodes = new_titles[0].data.new_titles.total_count
            all_edges = client.new_titles.extract_edges(new_titles)
            assert len(all_edges) == expected_episodes

            if expected_episodes > 10:  # noqa: PLR2004
                break

    def test_get_new_titles_all_since_date(self) -> None:
        """Test getting all new titles since a date with pagination."""
        today = datetime.now().astimezone().date()
        new_titles = client.new_titles.get_all_since_date(
            today - timedelta(days=1),
            filter_packages=["amp"],
            available_to_packages=["amp"],
            end_date=today - timedelta(days=2),
        )
        for page in new_titles:
            for model in page:
                client.new_titles.save_new_json_file(
                    client.new_titles.original_input(model)
                )
        assert len(new_titles) == 2  # noqa: PLR2004
        assert new_titles[0] != new_titles[1]

        expected_edges = 0
        for responses in new_titles:
            expected_edges += responses[0].data.new_titles.total_count

        assert len(client.new_titles.extract_edges(new_titles)) == expected_edges

    def test_get_search(self) -> None:
        """Test searching for titles."""
        model = client.search.get(search_query="Breaking")
        client.search.save_new_json_file(client.search.original_input(model))

    def test_get_season_episodes(self) -> None:
        """Test getting season episodes."""
        model = client.season_episodes.get("tss337460")
        client.season_episodes.save_new_json_file(
            client.season_episodes.original_input(model)
        )

    def test_get_season_episodes_all(self) -> None:
        """Test getting all season episodes with pagination."""
        season_episodes = client.season_episodes.get_all("tss23744")
        for model in season_episodes:
            client.season_episodes.save_new_json_file(
                client.season_episodes.original_input(model),
            )
        episodes = client.season_episodes.extract_episodes(season_episodes)
        assert len(episodes) == 23  # noqa: PLR2004

    def test_get_title_detail_article(self) -> None:
        """Test getting a title detail article."""
        model = client.title_detail_article.get("/us/movie/the-thursday-murder-club")
        client.title_detail_article.save_new_json_file(
            client.title_detail_article.original_input(model),
        )

    def test_get_url_title_details_movie(self) -> None:
        """Test getting URL title details for a movie."""
        model = client.url_title_details.get("/us/movie/the-thursday-murder-club")
        client.url_title_details.save_new_json_file(
            client.url_title_details.original_input(model),
        )

    def test_get_url_title_details_tv_show(self) -> None:
        """Test getting URL title details for a TV show."""
        model = client.url_title_details.get("/us/tv-show/strip-law")
        client.url_title_details.save_new_json_file(
            client.url_title_details.original_input(model),
        )

    def test_get_url_title_details_unavailable_movie(self) -> None:
        """Test getting URL title details for an unavailable movie."""
        model = client.url_title_details.get(
            "/us/movie/code-geass-akito-the-exiled-5-to-beloved-ones",
        )
        client.url_title_details.save_new_json_file(
            client.url_title_details.original_input(model),
        )

    def test_get_url_title_details_unavailable_tv_show(self) -> None:
        """Test getting URL title details for an unavailable TV show."""
        model = client.url_title_details.get("/us/tv-show/darker-than-black")
        client.url_title_details.save_new_json_file(
            client.url_title_details.original_input(model),
        )


class TestInvalidGet:
    """Test get requests for missing or invalid resources."""

    def test_invalid_get_buy_box_offers(self) -> None:
        """Test getting buy box offers with an invalid ID."""
        client.buy_box_offers.get("tse9999999")

    def test_invalid_get_custom_buy_box_offers(self) -> None:
        """Test getting custom buy box offers with an invalid ID."""
        client.custom_buy_box_offers.get("tse9999999")

    def test_invalid_get_custom_season_episodes(self) -> None:
        """Test getting custom season episodes with an invalid ID."""
        client.custom_season_episodes.get("tss999999")

    def test_invalid_get_search(self) -> None:
        """Test searching with a query that returns no results."""
        response = client.search.get(search_query="zxcvbbnm")
        assert response.data.search_titles.total_count == 0
        assert response.data.search_titles.edges == []

    def test_invalid_get_season_episodes(self) -> None:
        """Test getting season episodes with an invalid ID."""
        client.season_episodes.get("tss999999")

    def test_invalid_get_title_detail_article(self) -> None:
        """Test getting a title detail article with an invalid path."""
        with pytest.raises(GraphQLError):
            client.title_detail_article.get("/us/movie/invalid-movie")

    def test_invalid_get_url_title_details(self) -> None:
        """Test getting URL title details with an invalid URL."""
        with pytest.raises(GraphQLError, match="URL not found"):
            client.url_title_details.get("/us/tv-show/invalid-url")


class TestParse:
    """Test parsing every saved file for each endpoint."""

    def test_parse_buy_box_offers(self) -> None:
        """Test parsing buy box offers files."""
        for json_file in client.buy_box_offers.json_files():
            client.buy_box_offers.parse(json.loads(json_file.read_text()))

    def test_parse_custom_buy_box_offers(self) -> None:
        """Test parsing custom buy box offers files."""
        for json_file in client.custom_buy_box_offers.json_files():
            client.custom_buy_box_offers.parse(json.loads(json_file.read_text()))

    def test_parse_custom_season_episodes(self) -> None:
        """Test parsing custom season episodes files."""
        for json_file in client.custom_season_episodes.json_files():
            client.custom_season_episodes.parse(json.loads(json_file.read_text()))

    def test_parse_new_title_buckets(self) -> None:
        """Test parsing new title buckets files."""
        for json_file in client.new_title_buckets.json_files():
            client.new_title_buckets.parse(json.loads(json_file.read_text()))

    def test_parse_new_titles(self) -> None:
        """Test parsing new titles files."""
        for json_file in client.new_titles.json_files():
            client.new_titles.parse(json.loads(json_file.read_text()))

    def test_parse_search(self) -> None:
        """Test parsing search files."""
        for json_file in client.search.json_files():
            client.search.parse(json.loads(json_file.read_text()))

    def test_parse_season_episodes(self) -> None:
        """Test parsing season episodes files."""
        for json_file in client.season_episodes.json_files():
            client.season_episodes.parse(json.loads(json_file.read_text()))

    def test_parse_title_detail_article(self) -> None:
        """Test parsing title detail article files."""
        for json_file in client.title_detail_article.json_files():
            client.title_detail_article.parse(json.loads(json_file.read_text()))

    def test_parse_url_title_details(self) -> None:
        """Test parsing URL title details files."""
        for json_file in client.url_title_details.json_files():
            client.url_title_details.parse(json.loads(json_file.read_text()))


class TestExtract:
    """Test extracting typed entries from saved responses."""

    def test_extract_custom_season_episodes_episodes(self) -> None:
        """Test extracting episodes from saved custom season episodes files."""
        for json_file in client.custom_season_episodes.json_files():
            parsed = client.custom_season_episodes.parse(
                json.loads(json_file.read_text()),
            )
            client.custom_season_episodes.extract_episodes(parsed)

    def test_extract_new_title_buckets_edges(self) -> None:
        """Test extracting edges from saved new title buckets files."""
        for json_file in client.new_title_buckets.json_files():
            parsed = client.new_title_buckets.parse(json.loads(json_file.read_text()))
            client.new_title_buckets.extract_edges(parsed)

    def test_extract_new_titles_edges(self) -> None:
        """Test extracting edges from saved new titles files."""
        for json_file in client.new_titles.json_files():
            parsed = client.new_titles.parse(json.loads(json_file.read_text()))
            client.new_titles.extract_edges(parsed)

    def test_extract_season_episodes_episodes(self) -> None:
        """Test extracting episodes from saved season episodes files."""
        for json_file in client.season_episodes.json_files():
            parsed = client.season_episodes.parse(json.loads(json_file.read_text()))
            client.season_episodes.extract_episodes(parsed)
