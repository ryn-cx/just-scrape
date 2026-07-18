# TODO: Validate
from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from just_scrape import JustScrape
    from just_scrape.new_title_buckets import NewTitleBuckets

# download() takes no id; the response is keyed on the default page type.
PAGE_TYPE = "NEW"


@pytest.fixture(scope="session")
def endpoint(client: JustScrape) -> NewTitleBuckets:
    return client.new_title_buckets


class TestNewTitleBuckets:
    def test_download(self, endpoint: NewTitleBuckets) -> None:
        download_and_save(endpoint, PAGE_TYPE, endpoint.download)

    def test_extract_edges(self, endpoint: NewTitleBuckets) -> None:
        data = parse_json(endpoint, PAGE_TYPE)
        edges = endpoint.extract_edges(data)
        assert edges is not None
        # TODO: assert expected value (needs live data)

    # Live pagination test: walks the buckets back to a date over the network and
    # has no clean cached-file equivalent.
    def test_download_and_parse_since_date(self, endpoint: NewTitleBuckets) -> None:
        today = datetime.now().astimezone().date()
        end_date = today - timedelta(days=5)

        all_buckets = endpoint.download_and_parse_since_date(end_date)
        all_edges = endpoint.extract_edges(all_buckets)

        assert len(all_buckets) >= 1
        assert len(all_edges) >= 1

        if len(all_buckets) > 1:
            assert len(all_edges) > 3  # noqa: PLR2004


@pytest.mark.parametrize("country", [None, "CA"])
def test_log_id(endpoint: NewTitleBuckets, country: str | None) -> None:
    expected = f"NewTitleBuckets page_type={PAGE_TYPE!r}"
    if country is not None:
        expected += f" country={country!r}"
    assert endpoint.get_log_id(country=country or "US") == expected
