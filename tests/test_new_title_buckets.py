# TODO: Validate
from __future__ import annotations

import json
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape
from tests.utils import data_path, download_if_missing

if TYPE_CHECKING:
    from just_scrape.new_title_buckets import NewTitleBuckets

client = JustScrape(get_around_client=build_client_automatically())

# download() takes no id; the response is keyed on the default page type.
PAGE_TYPE = "NEW"


@pytest.fixture(scope="session")
def endpoint() -> NewTitleBuckets:
    return client.new_title_buckets


class TestNewTitleBuckets:
    def test_download(self, endpoint: NewTitleBuckets) -> None:
        download_if_missing(endpoint, PAGE_TYPE, endpoint.download)

    def test_extract_edges(self, endpoint: NewTitleBuckets) -> None:
        data = endpoint.parse(
            json.loads(data_path(endpoint, PAGE_TYPE).read_text()),
        )
        edges = endpoint.extract_edges(data)
        assert edges is not None
        # TODO: assert expected value (needs live data)

    # Live pagination test: walks the buckets back to a date over the network and
    # has no clean cached-file equivalent.
    def test_get_all_since_date(self, endpoint: NewTitleBuckets) -> None:
        today = datetime.now().astimezone().date()
        end_date = today - timedelta(days=5)

        all_buckets = endpoint.get_all_since_date(end_date)
        all_edges = endpoint.extract_edges(all_buckets)

        assert len(all_buckets) >= 1
        assert len(all_edges) >= 1

        if len(all_buckets) > 1:
            assert len(all_edges) > 3  # noqa: PLR2004
