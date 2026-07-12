# TODO: Validate
import json

from get_around import build_client_automatically

from just_scrape import JustScrape

client = JustScrape(get_around_client=build_client_automatically())

SEASON_ID = "tss337460"
"""season_id for season episodes."""
PAGINATED_SEASON_ID = "tss23744"
"""season_id with enough episodes to exercise pagination."""
EXPECTED_EPISODE_COUNT = 23
"""Number of episodes in PAGINATED_SEASON_ID."""
INVALID_SEASON_ID = "tss999999"


class TestSeasonEpisodes:
    def test_get(self) -> None:
        endpoint = client.season_episodes
        model = endpoint.get(SEASON_ID)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_all(self) -> None:
        endpoint = client.season_episodes
        season_episodes = endpoint.get_all(PAGINATED_SEASON_ID)
        for model in season_episodes:
            endpoint.save_new_json_file(endpoint.original_input(model))
        episodes = endpoint.extract_episodes(season_episodes)
        assert len(episodes) == EXPECTED_EPISODE_COUNT

    def test_invalid_get(self) -> None:
        # This endpoint does not raise for an unknown season_id.
        client.season_episodes.get(INVALID_SEASON_ID)

    def test_parse(self) -> None:
        endpoint = client.season_episodes
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_episodes(self) -> None:
        endpoint = client.season_episodes
        for json_file in endpoint.json_files():
            parsed = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_episodes(parsed)
