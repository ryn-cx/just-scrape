# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

from just_scrape.new_titles.models import NewTitlesModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from just_scrape import JustScrape

FIRST = 3
"""A short page, so what a page holds stays small enough to read."""

DATES = [
    pytest.param("2026-08-01", id="date titles turned up on"),
    # A date nothing turned up on is answered with an empty page.
    pytest.param("2050-01-01", id="date nothing turned up on"),
]


# TODO: Validate
class NewTitlesTest(RecordedEndpoint):
    MODEL = NewTitlesModel


# TODO: Validate
@pytest.mark.parametrize("release_date", DATES)
def test_download(client: JustScrape, release_date: str) -> None:
    NewTitlesTest.download_test(
        release_date,
        lambda: client.new_titles.download(
            date=date.fromisoformat(release_date),
            first=FIRST,
        ),
    )


# TODO: Validate
@pytest.mark.parametrize("release_date", DATES)
def test_parse(client: JustScrape, release_date: str) -> None:
    data = client.new_titles.load(NewTitlesTest.recorded_content(release_date))
    new_titles = data.data.new_titles
    assert bool(new_titles.edges) == bool(new_titles.total_count)
