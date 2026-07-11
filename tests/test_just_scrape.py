# TODO: Validate
from __future__ import annotations

import json
from datetime import datetime, timedelta

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError

client = JustScrape(get_around_client=build_client_automatically())

BUY_BOX_NODE_ID = "tse9298997"
"""node_id used for buy box offer lookups."""
CUSTOM_SEASON_ID = "tss466559"
"""season_id for custom season episodes."""
SEASON_ID = "tss337460"
"""season_id for season episodes."""
PAGINATED_SEASON_ID = "tss23744"
"""season_id with enough episodes to exercise pagination."""
EXPECTED_EPISODE_COUNT = 23
"""Number of episodes in PAGINATED_SEASON_ID."""
SEARCH_QUERY = "Breaking"
"""A search term that matches titles."""
MOVIE_PATH = "/us/movie/the-thursday-murder-club"
"""URL path for a movie title."""
TV_SHOW_PATH = "/us/tv-show/strip-law"
"""URL path for a TV show title."""
UNAVAILABLE_MOVIE_PATH = "/us/movie/code-geass-akito-the-exiled-5-to-beloved-ones"
"""URL path for a movie that is not available."""
UNAVAILABLE_TV_SHOW_PATH = "/us/tv-show/darker-than-black"
"""URL path for a TV show that is not available."""
INVALID_NODE_ID = "tse9999999"
INVALID_SEASON_ID = "tss999999"
INVALID_SEARCH_QUERY = "zxcvbbnm"
INVALID_MOVIE_PATH = "/us/movie/invalid-movie"
INVALID_URL_PATH = "/us/tv-show/invalid-url"


class TestGet:
    def test_get_buy_box_offers(self) -> None:
        endpoint = client.buy_box_offers
        model = endpoint.get(node_id=BUY_BOX_NODE_ID)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_custom_buy_box_offers(self) -> None:
        endpoint = client.custom_buy_box_offers
        model = endpoint.get(node_id=BUY_BOX_NODE_ID)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_custom_season_episodes(self) -> None:
        endpoint = client.custom_season_episodes
        model = endpoint.get(CUSTOM_SEASON_ID)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_custom_season_episodes_all(self) -> None:
        endpoint = client.custom_season_episodes
        season_episodes = endpoint.get_all(PAGINATED_SEASON_ID)
        for model in season_episodes:
            endpoint.save_new_json_file(endpoint.original_input(model))
        episodes = endpoint.extract_episodes(season_episodes)
        assert len(episodes) == EXPECTED_EPISODE_COUNT

    def test_get_new_title_buckets(self) -> None:
        endpoint = client.new_title_buckets
        model = endpoint.get()
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_new_title_buckets_all_since_date(self) -> None:
        endpoint = client.new_title_buckets
        today = datetime.now().astimezone().date()
        end_date = today - timedelta(days=5)

        all_buckets = endpoint.get_all_since_date(end_date)
        for model in all_buckets:
            endpoint.save_new_json_file(endpoint.original_input(model))
        all_edges = endpoint.extract_edges(all_buckets)

        assert len(all_buckets) >= 1
        assert len(all_edges) >= 1

        if len(all_buckets) > 1:
            assert len(all_edges) > 3  # noqa: PLR2004

    def test_get_new_titles(self) -> None:
        endpoint = client.new_titles
        model = endpoint.get(
            filter_packages=["net"],
            available_to_packages=["net"],
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_new_titles_all_for_date(self) -> None:
        # This test needs more than 10 entries in the response for it to show it
        # is working correctly. Amazon usually has 10 entries, but sometimes it
        # doesn't, so this test walks back through the last week until one is
        # found with more than 10 entries.

        # Always start 1 day behind the current day because the current day may
        # have incomplete data and is less likely to have 10+ entries.
        endpoint = client.new_titles
        for i in range(1, 10):
            new_titles = endpoint.get_all_for_date(
                filter_packages=["amp"],
                available_to_packages=["amp"],
                date=datetime.now().astimezone().date() - timedelta(days=i),
            )
            for model in new_titles:
                endpoint.save_new_json_file(endpoint.original_input(model))
            expected_episodes = new_titles[0].data.new_titles.total_count
            all_edges = endpoint.extract_edges(new_titles)
            assert len(all_edges) == expected_episodes

            if expected_episodes > 10:  # noqa: PLR2004
                break

    def test_get_new_titles_all_since_date(self) -> None:
        endpoint = client.new_titles
        today = datetime.now().astimezone().date()
        new_titles = endpoint.get_all_since_date(
            today - timedelta(days=1),
            filter_packages=["amp"],
            available_to_packages=["amp"],
            end_date=today - timedelta(days=2),
        )
        for page in new_titles:
            for model in page:
                endpoint.save_new_json_file(endpoint.original_input(model))
        assert len(new_titles) == 2  # noqa: PLR2004
        assert new_titles[0] != new_titles[1]

        expected_edges = 0
        for responses in new_titles:
            expected_edges += responses[0].data.new_titles.total_count

        assert len(endpoint.extract_edges(new_titles)) == expected_edges

    def test_get_search(self) -> None:
        endpoint = client.search
        model = endpoint.get(search_query=SEARCH_QUERY)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_season_episodes(self) -> None:
        endpoint = client.season_episodes
        model = endpoint.get(SEASON_ID)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_season_episodes_all(self) -> None:
        endpoint = client.season_episodes
        season_episodes = endpoint.get_all(PAGINATED_SEASON_ID)
        for model in season_episodes:
            endpoint.save_new_json_file(endpoint.original_input(model))
        episodes = endpoint.extract_episodes(season_episodes)
        assert len(episodes) == EXPECTED_EPISODE_COUNT

    def test_get_title_detail_article(self) -> None:
        endpoint = client.title_detail_article
        model = endpoint.get(MOVIE_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_url_title_details_movie(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(MOVIE_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_url_title_details_tv_show(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(TV_SHOW_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_url_title_details_unavailable_movie(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(UNAVAILABLE_MOVIE_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_url_title_details_unavailable_tv_show(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(UNAVAILABLE_TV_SHOW_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))


class TestInvalidGet:
    def test_invalid_get_buy_box_offers(self) -> None:
        # This endpoint does not raise for an unknown node_id.
        client.buy_box_offers.get(INVALID_NODE_ID)

    def test_invalid_get_custom_buy_box_offers(self) -> None:
        # This endpoint does not raise for an unknown node_id.
        client.custom_buy_box_offers.get(INVALID_NODE_ID)

    def test_invalid_get_custom_season_episodes(self) -> None:
        # This endpoint does not raise for an unknown season_id.
        client.custom_season_episodes.get(INVALID_SEASON_ID)

    def test_invalid_get_search(self) -> None:
        response = client.search.get(search_query=INVALID_SEARCH_QUERY)
        assert response.data.search_titles.total_count == 0
        assert response.data.search_titles.edges == []

    def test_invalid_get_season_episodes(self) -> None:
        # This endpoint does not raise for an unknown season_id.
        client.season_episodes.get(INVALID_SEASON_ID)

    def test_invalid_get_title_detail_article(self) -> None:
        with pytest.raises(GraphQLError):
            client.title_detail_article.get(INVALID_MOVIE_PATH)

    def test_invalid_get_url_title_details(self) -> None:
        with pytest.raises(GraphQLError, match="URL not found"):
            client.url_title_details.get(INVALID_URL_PATH)


class TestParse:
    @pytest.mark.parametrize(
        "endpoint_name",
        [
            "buy_box_offers",
            "custom_buy_box_offers",
            "custom_season_episodes",
            "new_title_buckets",
            "new_titles",
            "search",
            "season_episodes",
            "title_detail_article",
            "url_title_details",
        ],
    )
    def test_parse(self, endpoint_name: str) -> None:
        endpoint = getattr(client, endpoint_name)
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))


class TestExtract:
    def test_extract_custom_season_episodes_episodes(self) -> None:
        endpoint = client.custom_season_episodes
        for json_file in endpoint.json_files():
            parsed = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_episodes(parsed)

    def test_extract_new_title_buckets_edges(self) -> None:
        endpoint = client.new_title_buckets
        for json_file in endpoint.json_files():
            parsed = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_edges(parsed)

    def test_extract_new_titles_edges(self) -> None:
        endpoint = client.new_titles
        for json_file in endpoint.json_files():
            parsed = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_edges(parsed)

    def test_extract_season_episodes_episodes(self) -> None:
        endpoint = client.season_episodes
        for json_file in endpoint.json_files():
            parsed = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_episodes(parsed)
