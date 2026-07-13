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
    from just_scrape.new_titles import NewTitles

client = JustScrape(get_around_client=build_client_automatically())

# download() takes no id; the response is keyed on the default page type.
PAGE_TYPE = "NEW"
PACKAGES = ["net"]


@pytest.fixture(scope="session")
def endpoint() -> NewTitles:
    return client.new_titles


class TestNewTitles:
    def test_download(self, endpoint: NewTitles) -> None:
        download_if_missing(
            endpoint,
            PAGE_TYPE,
            lambda: endpoint.download(
                filter_packages=PACKAGES,
                available_to_packages=PACKAGES,
            ),
        )

    def test_extract_edges(self, endpoint: NewTitles) -> None:
        data = endpoint.parse(
            json.loads(data_path(endpoint, PAGE_TYPE).read_text()),
        )
        edges = endpoint.extract_edges(data)
        assert edges is not None
        # TODO: assert expected value (needs live data)

    # Live pagination test: walks back through recent dates over the network
    # until one has more than a single page, with no clean cached-file
    # equivalent.
    def test_get_all_for_date(self, endpoint: NewTitles) -> None:
        # This test needs more than 10 entries in the response for it to show it
        # is working correctly. Amazon usually has 10 entries, but sometimes it
        # doesn't, so this test walks back through the last week until one is
        # found with more than 10 entries.

        # Always start 1 day behind the current day because the current day may
        # have incomplete data and is less likely to have 10+ entries.
        for i in range(1, 10):
            new_titles = endpoint.get_all_for_date(
                filter_packages=["amp"],
                available_to_packages=["amp"],
                date=datetime.now().astimezone().date() - timedelta(days=i),
            )
            expected_episodes = new_titles[0].data.new_titles.total_count
            all_edges = endpoint.extract_edges(new_titles)
            assert len(all_edges) == expected_episodes

            if expected_episodes > 10:  # noqa: PLR2004
                break

    # Live pagination test: walks a date range over the network and has no clean
    # cached-file equivalent.
    def test_get_all_since_date(self, endpoint: NewTitles) -> None:
        today = datetime.now().astimezone().date()
        new_titles = endpoint.get_all_since_date(
            today - timedelta(days=1),
            filter_packages=["amp"],
            available_to_packages=["amp"],
            end_date=today - timedelta(days=2),
        )
        assert len(new_titles) == 2  # noqa: PLR2004
        assert new_titles[0] != new_titles[1]

        expected_edges = 0
        for responses in new_titles:
            expected_edges += responses[0].data.new_titles.total_count

        assert len(endpoint.extract_edges(new_titles)) == expected_edges
