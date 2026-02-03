from just_scrape import JustScrape
from just_scrape.custom_season_episodes import (
    CUSTOM_SEASON_EPISODES_CUSTOMIZATIONS,
)
from just_scrape.url_title_details import URL_TITLE_DETAILS_CUSTOMIZATIONS

if __name__ == "__main__":
    client = JustScrape()
    # No requests file because it uses season_episodes/request
    client.rebuild_models(
        "custom_season_episodes/response",
        CUSTOM_SEASON_EPISODES_CUSTOMIZATIONS,
    )

    client.rebuild_models(
        "url_title_details/response",
        URL_TITLE_DETAILS_CUSTOMIZATIONS,
    )
    client.rebuild_models("url_title_details/request")

    for input_type in ["request", "response"]:
        client.rebuild_models(f"new_title_buckets/{input_type}")
        client.rebuild_models(f"new_titles/{input_type}")
        client.rebuild_models(f"season_episodes/{input_type}")
        client.rebuild_models(f"title_detail_article/{input_type}")
        client.rebuild_models(f"buy_box_offers/{input_type}")
