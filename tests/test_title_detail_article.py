# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import ArticleNotFoundError

if TYPE_CHECKING:
    from just_scrape import JustScrape

FULL_PATHS = [
    pytest.param("/us/movie/the-thursday-murder-club", id="movie with no articles"),
]


# TODO: Validate
@pytest.mark.parametrize("full_path", FULL_PATHS)
def test_download(client: JustScrape, full_path: str) -> None:
    article = client.title_detail_article(full_path)
    assert article.node.id


# TODO: Validate
def test_download_invalid(client: JustScrape) -> None:
    with pytest.raises(ArticleNotFoundError):
        client.title_detail_article.download("/us/movie/invalid-movie")
