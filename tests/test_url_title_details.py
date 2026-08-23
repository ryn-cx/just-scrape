# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import TitleNotFoundError
from just_scrape.url_title_details.models import UrlTitleDetailsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from just_scrape import JustScrape

FULL_PATHS = [
    pytest.param("/us/movie/the-thursday-murder-club", id="movie"),
    pytest.param("/us/tv-show/darker-than-black", id="tv show with seasons"),
]


# TODO: Validate
class UrlTitleDetailsTest(RecordedEndpoint):
    MODEL = UrlTitleDetailsModel


# TODO: Validate
@pytest.mark.parametrize("full_path", FULL_PATHS)
def test_download(client: JustScrape, full_path: str) -> None:
    UrlTitleDetailsTest.download_test(
        full_path,
        lambda: client.url_title_details.download(full_path),
    )


# TODO: Validate
@pytest.mark.parametrize("full_path", FULL_PATHS)
def test_parse(client: JustScrape, full_path: str) -> None:
    data = client.url_title_details.load(
        UrlTitleDetailsTest.recorded_content(full_path),
    )
    assert data.data.url_v2.node.content.full_path == full_path


# TODO: Validate
@pytest.mark.parametrize(
    "full_path",
    [pytest.param("/us/tv-show/invalid-url", id="path no title sits at")],
)
def test_download_invalid(client: JustScrape, full_path: str) -> None:
    UrlTitleDetailsTest.error_test(
        full_path,
        lambda: client.url_title_details.download(full_path),
        TitleNotFoundError,
    )
