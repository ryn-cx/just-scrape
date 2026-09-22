# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from just_scrape.exceptions import GraphQLError

if TYPE_CHECKING:
    from just_scrape import JustScrape

NODE_IDS = [
    pytest.param("tss486285", id="frieren beyond journeys end season 2"),
    # An id nothing is under is echoed back as a season with no episodes, which
    # is the same answer a real season with nothing listed gives.
    pytest.param("tss0000000", id="season that does not exist"),
]


# TODO: Validate
@pytest.mark.parametrize("node_id", NODE_IDS)
def test_download(client: JustScrape, node_id: str) -> None:
    season = client.season_episodes(node_id)
    assert season.id == node_id


# TODO: Validate
def test_download_all(client: JustScrape) -> None:
    endpoint = client.season_episodes
    node_id = "tss486285"
    pages = endpoint.load_pages(endpoint.download_all(node_id))
    merged = endpoint.load(endpoint.merge_pages(endpoint.download_all(node_id)))
    assert len(merged.episodes) == sum(len(page.episodes) for page in pages)


# TODO: Validate
def test_download_invalid(client: JustScrape) -> None:
    with pytest.raises(GraphQLError):
        client.season_episodes.download("0000000")
