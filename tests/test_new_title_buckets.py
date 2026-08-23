# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.new_title_buckets.models import NewTitleBucketsModel
from tests.utils import RecordedEndpoint

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
class NewTitleBucketsTest(RecordedEndpoint):
    MODEL = NewTitleBucketsModel
    # A bucket holds whatever turned up on the day it was recorded, so its date,
    # its service and its count are different every time it is downloaded.
    SAME_TYPE = (
        "Key.date",
        "Package.id",
        "Package.package_id",
        "Package.short_name",
        "Package.icon",
        "Node.total_count",
        "PageInfo.start_cursor",
        "PageInfo.end_cursor",
        "PageInfo1.start_cursor",
        "PageInfo1.end_cursor",
    )


# TODO: Validate
@pytest.mark.parametrize("object_type", OBJECT_TYPES)
def test_download(client: JustScrape, object_type: str) -> None:
    NewTitleBucketsTest.download_test(
        object_type,
        lambda: client.new_title_buckets.download(
            filter_object_types=[object_type],
            first=FIRST,
        ),
    )


# TODO: Validate
@pytest.mark.parametrize("object_type", OBJECT_TYPES)
def test_parse(client: JustScrape, object_type: str) -> None:
    data = client.new_title_buckets.load(
        NewTitleBucketsTest.recorded_content(object_type),
    )
    assert data.data.new_title_buckets.edges
