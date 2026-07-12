# TODO: Validate
import json

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError

client = JustScrape(get_around_client=build_client_automatically())

MOVIE_PATH = "/us/movie/the-thursday-murder-club"
"""URL path for a movie title."""
TV_SHOW_PATH = "/us/tv-show/strip-law"
"""URL path for a TV show title."""
UNAVAILABLE_MOVIE_PATH = "/us/movie/code-geass-akito-the-exiled-5-to-beloved-ones"
"""URL path for a movie that is not available."""
UNAVAILABLE_TV_SHOW_PATH = "/us/tv-show/darker-than-black"
"""URL path for a TV show that is not available."""
INVALID_URL_PATH = "/us/tv-show/invalid-url"


class TestUrlTitleDetails:
    def test_get_movie(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(MOVIE_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_tv_show(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(TV_SHOW_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_unavailable_movie(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(UNAVAILABLE_MOVIE_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_unavailable_tv_show(self) -> None:
        endpoint = client.url_title_details
        model = endpoint.get(UNAVAILABLE_TV_SHOW_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(GraphQLError, match="URL not found"):
            client.url_title_details.get(INVALID_URL_PATH)

    def test_parse(self) -> None:
        endpoint = client.url_title_details
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
