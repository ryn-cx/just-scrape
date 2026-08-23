# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import ArticleNotFoundError
from just_scrape.title_detail_article.models import TitleDetailArticleModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from just_scrape import JustScrape

FULL_PATHS = [
    pytest.param("/us/movie/the-thursday-murder-club", id="movie with no articles"),
]


# TODO: Validate
class TitleDetailArticleTest(RecordedEndpoint):
    MODEL = TitleDetailArticleModel


# TODO: Validate
@pytest.mark.parametrize("full_path", FULL_PATHS)
def test_download(client: JustScrape, full_path: str) -> None:
    TitleDetailArticleTest.download_test(
        full_path,
        lambda: client.title_detail_article.download(full_path),
    )


# TODO: Validate
@pytest.mark.parametrize("full_path", FULL_PATHS)
def test_parse(client: JustScrape, full_path: str) -> None:
    data = client.title_detail_article.load(
        TitleDetailArticleTest.recorded_content(full_path),
    )
    assert data.data.url_v2.node.id


# TODO: Validate
@pytest.mark.parametrize(
    "full_path",
    [pytest.param("/us/movie/invalid-movie", id="path no title sits at")],
)
def test_download_invalid(client: JustScrape, full_path: str) -> None:
    TitleDetailArticleTest.error_test(
        full_path,
        lambda: client.title_detail_article.download(full_path),
        ArticleNotFoundError,
    )
