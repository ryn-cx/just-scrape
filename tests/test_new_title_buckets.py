# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from just_scrape import JustScrape

FIRST = 3
"""A short page, so what a page holds stays small enough to read."""

OBJECT_TYPES = [
    # The object type is filtered on because the API pages wrongly when it is
    # not, which is a server side bug the site itself has.
    pytest.param("MOVIE", id="movies"),
]


# TODO: Validate
@pytest.mark.parametrize("object_type", OBJECT_TYPES)
def test_download(client: JustScrape, object_type: str) -> None:
    buckets = client.new_title_buckets(
        filter_object_types=[object_type],
        first=FIRST,
    )
    assert buckets.edges
