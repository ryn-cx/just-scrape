# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import TitleNotFoundError

if TYPE_CHECKING:
    from just_scrape import JustScrape

FULL_PATHS = [
    pytest.param("/us/movie/the-thursday-murder-club", id="movie"),
    pytest.param("/us/tv-show/darker-than-black", id="tv show with seasons"),
]


# TODO: Validate
@pytest.mark.parametrize("full_path", FULL_PATHS)
def test_download(client: JustScrape, full_path: str) -> None:
    title = client.url_title_details(full_path)
    assert title.node.content.full_path == full_path


# TODO: Validate
def test_download_invalid(client: JustScrape) -> None:
    with pytest.raises(TitleNotFoundError):
        client.url_title_details.download("/us/tv-show/invalid-url")
