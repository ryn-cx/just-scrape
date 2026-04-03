"""Tests for just_scrape using the Cloudflare Worker proxy."""

from __future__ import annotations

import os
from datetime import datetime, timedelta

import pytest
from dotenv import load_dotenv

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError
from tests.test_just_scrape import save_responses

load_dotenv()

client = JustScrape(
    proxy_url=os.environ["PROXY_URL"],
    proxy_auth_token=os.environ["PROXY_AUTH_TOKEN"],
)


class TestGet:
    """Tests getting data through the proxy."""

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
            for i in range(1, 10):
                all_new_titles_for_date = client.new_titles.get_all_for_date(
                    filter_packages=["amp"],
                    available_to_packages=["amp"],
                    date=datetime.now().astimezone().date() - timedelta(days=i),
                )
                expected_episodes = all_new_titles_for_date[
                    0
                ].data.new_titles.total_count
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
            assert len(responseses) == 2  # noqa: PLR2004
            assert responseses[0] != responseses[1]

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
