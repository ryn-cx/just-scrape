# TODO: Validate
import json

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from just_scrape.exceptions import GraphQLError

client = JustScrape(get_around_client=build_client_automatically())

MOVIE_PATH = "/us/movie/the-thursday-murder-club"
"""URL path for a movie title."""
INVALID_MOVIE_PATH = "/us/movie/invalid-movie"


class TestTitleDetailArticle:
    def test_get(self) -> None:
        endpoint = client.title_detail_article
        model = endpoint.get(MOVIE_PATH)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(GraphQLError):
            client.title_detail_article.get(INVALID_MOVIE_PATH)

    def test_parse(self) -> None:
        endpoint = client.title_detail_article
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
