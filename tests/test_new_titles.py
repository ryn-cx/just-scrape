# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

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
@pytest.mark.parametrize("release_date", DATES)
def test_download(client: JustScrape, release_date: str) -> None:
    new_titles = client.new_titles(
        date=date.fromisoformat(release_date),
        first=FIRST,
    )
    assert bool(new_titles.edges) == bool(new_titles.total_count)
