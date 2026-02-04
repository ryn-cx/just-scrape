from just_scrape import JustScrape
from just_scrape.buy_box_offers import BUY_BOX_OFFERS_CUSTOMIZATIONS
from just_scrape.custom_buy_box_offers import CUSTOM_BUY_BOX_OFFERS_CUSTOMIZATIONS
from just_scrape.custom_season_episodes import (
    CUSTOM_SEASON_EPISODES_CUSTOMIZATIONS,
)
from just_scrape.url_title_details import URL_TITLE_DETAILS_CUSTOMIZATIONS

if __name__ == "__main__":
    client = JustScrape()
    endpoints = [
        "new_title_buckets",
        "new_titles",
        "season_episodes",
        "title_detail_article",
        "buy_box_offers",
        "url_title_details",
    ]

    # Make all of the normal request and response models then overwrite them with the
    # customized ones.
    for endpoint in endpoints:
        for request_or_response in ["request", "response"]:
            client.rebuild_models(f"{endpoint}/{request_or_response}")

    client.rebuild_models(
        "custom_season_episodes/response",
        CUSTOM_SEASON_EPISODES_CUSTOMIZATIONS,
    )

    client.rebuild_models(
        "url_title_details/response",
        URL_TITLE_DETAILS_CUSTOMIZATIONS,
    )

    client.rebuild_models(
        "buy_box_offers/response",
        BUY_BOX_OFFERS_CUSTOMIZATIONS,
    )

    client.rebuild_models(
        "custom_buy_box_offers/response",
        CUSTOM_BUY_BOX_OFFERS_CUSTOMIZATIONS,
    )
