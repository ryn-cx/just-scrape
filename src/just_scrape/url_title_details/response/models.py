# ruff: noqa: COM812, TC003, D100, D101, D102
from __future__ import annotations

from datetime import date

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_serializer


class PlanOffer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float = Field(..., alias="retailPriceValue")
    children: list[None]
    field__typename: str = Field(..., alias="__typename")


class Package(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon: str
    icon_wide: str = Field(..., alias="iconWide")
    plan_offers: list[PlanOffer] = Field(..., alias="planOffers")
    field__typename: str = Field(..., alias="__typename")


class Plan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float = Field(..., alias="retailPriceValue")
    children: list[None]
    field__typename: str = Field(..., alias="__typename")


class Offer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    new_element_count: int = Field(..., alias="newElementCount")
    retail_price: None = Field(..., alias="retailPrice")
    retail_price_value: None = Field(..., alias="retailPriceValue")
    currency: str
    last_change_retail_price_value: None = Field(
        ..., alias="lastChangeRetailPriceValue"
    )
    type: str
    country: str
    package: Package
    plans: list[Plan]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: None = Field(..., alias="availableTo")
    subtitle_languages: list[str] = Field(..., alias="subtitleLanguages")
    video_technology: list[str] = Field(..., alias="videoTechnology")
    audio_technology: list[str] = Field(..., alias="audioTechnology")
    audio_languages: list[str] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")


class Package1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    icon: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon_wide: str = Field(..., alias="iconWide")
    has_rectangular_icon: bool = Field(..., alias="hasRectangularIcon")
    field__typename: str = Field(..., alias="__typename")


class WatchNowOffer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    package: Package1
    retail_price: None = Field(..., alias="retailPrice")
    retail_price_value: None = Field(..., alias="retailPriceValue")
    last_change_retail_price_value: None = Field(
        ..., alias="lastChangeRetailPriceValue"
    )
    currency: str
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    available_to: None = Field(..., alias="availableTo")
    date_created: date = Field(..., alias="dateCreated")
    new_element_count: int = Field(..., alias="newElementCount")


class Clip(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source_url: str = Field(..., alias="sourceUrl")
    external_id: str = Field(..., alias="externalId")
    provider: str
    name: str
    field__typename: str = Field(..., alias="__typename")


class DailymotionClip(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source_url: str = Field(..., alias="sourceUrl")
    external_id: str = Field(..., alias="externalId")
    provider: str
    name: str
    field__typename: str = Field(..., alias="__typename")


class FallBackClips(BaseModel):
    model_config = ConfigDict(extra="forbid")
    clips: list[Clip]
    videobuster_clips: list[None] = Field(..., alias="videobusterClips")
    dailymotion_clips: list[DailymotionClip] = Field(..., alias="dailymotionClips")
    field__typename: str = Field(..., alias="__typename")


class Backdrop(BaseModel):
    model_config = ConfigDict(extra="forbid")
    backdrop_url: str = Field(..., alias="backdropUrl")
    field__typename: str = Field(..., alias="__typename")


class FullBackdrop(BaseModel):
    model_config = ConfigDict(extra="forbid")
    backdrop_url: str = Field(..., alias="backdropUrl")
    field__typename: str = Field(..., alias="__typename")


class ExternalIds(BaseModel):
    model_config = ConfigDict(extra="forbid")
    imdb_id: str = Field(..., alias="imdbId")
    wikidata_id: str = Field(..., alias="wikidataId")
    field__typename: str = Field(..., alias="__typename")


class Scoring(BaseModel):
    model_config = ConfigDict(extra="forbid")
    imdb_score: float = Field(..., alias="imdbScore")
    imdb_votes: int = Field(..., alias="imdbVotes")
    tmdb_popularity: float = Field(..., alias="tmdbPopularity")
    tmdb_score: float = Field(..., alias="tmdbScore")
    jw_rating: float = Field(..., alias="jwRating")
    tomato_meter: int = Field(..., alias="tomatoMeter")
    certified_fresh: bool = Field(..., alias="certifiedFresh")
    field__typename: str = Field(..., alias="__typename")


class Genre(BaseModel):
    model_config = ConfigDict(extra="forbid")
    short_name: str = Field(..., alias="shortName")
    translation: str
    field__typename: str = Field(..., alias="__typename")


class Url(BaseModel):
    model_config = ConfigDict(extra="forbid")
    full_path: str = Field(..., alias="fullPath")
    field__typename: str = Field(..., alias="__typename")


class Content1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    short_name: str = Field(..., alias="shortName")
    name: str
    field__typename: str = Field(..., alias="__typename")
    url: Url


class Subgenre(BaseModel):
    model_config = ConfigDict(extra="forbid")
    content: Content1
    field__typename: str = Field(..., alias="__typename")


class Credit(BaseModel):
    model_config = ConfigDict(extra="forbid")
    role: str
    name: str
    character_name: str = Field(..., alias="characterName")
    person_id: int = Field(..., alias="personId")
    portrait_url: str | None = Field(..., alias="portraitUrl")
    profile_path: None = Field(..., alias="profilePath")
    field__typename: str = Field(..., alias="__typename")


class Interactions(BaseModel):
    model_config = ConfigDict(extra="forbid")
    dislikelist_additions: int = Field(..., alias="dislikelistAdditions")
    likelist_additions: int = Field(..., alias="likelistAdditions")
    votes_number: int = Field(..., alias="votesNumber")
    field__typename: str = Field(..., alias="__typename")


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    backdrops: list[Backdrop]
    full_backdrops: list[FullBackdrop] = Field(..., alias="fullBackdrops")
    clips: list[Clip]
    videobuster_clips: list[None] = Field(..., alias="videobusterClips")
    dailymotion_clips: list[DailymotionClip] = Field(..., alias="dailymotionClips")
    external_ids: ExternalIds = Field(..., alias="externalIds")
    full_path: str = Field(..., alias="fullPath")
    poster_url: str = Field(..., alias="posterUrl")
    full_poster_url: str = Field(..., alias="fullPosterUrl")
    runtime: int
    is_released: bool = Field(..., alias="isReleased")
    scoring: Scoring
    short_description: str = Field(..., alias="shortDescription")
    title: str
    original_release_year: int = Field(..., alias="originalReleaseYear")
    original_release_date: date = Field(..., alias="originalReleaseDate")
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")
    genres: list[Genre]
    subgenres: list[Subgenre]
    text_recommendations: None = Field(..., alias="textRecommendations")
    field__typename: str = Field(..., alias="__typename")
    original_title: str = Field(..., alias="originalTitle")
    age_certification: str = Field(..., alias="ageCertification")
    credits: list[Credit]
    interactions: Interactions
    production_countries: list[str] = Field(..., alias="productionCountries")
    tags: list[None]


class PopularityRank(BaseModel):
    model_config = ConfigDict(extra="forbid")
    rank: int
    trend: str
    trend_difference: int = Field(..., alias="trendDifference")
    field__typename: str = Field(..., alias="__typename")


class StreamingChartInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    rank: int
    trend: str
    trend_difference: int = Field(..., alias="trendDifference")
    updated_at: AwareDatetime = Field(..., alias="updatedAt")
    days_in_top10: int = Field(..., alias="daysInTop10")
    days_in_top100: int = Field(..., alias="daysInTop100")
    days_in_top1000: int = Field(..., alias="daysInTop1000")
    days_in_top3: int = Field(..., alias="daysInTop3")
    top_rank: int = Field(..., alias="topRank")
    field__typename: str = Field(..., alias="__typename")

    @field_serializer("updated_at")
    def serialize_updated_at(self, value: AwareDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S.%f").rstrip("0").rstrip(".") + "Z"


class Edge(BaseModel):
    model_config = ConfigDict(extra="forbid")
    streaming_chart_info: StreamingChartInfo = Field(..., alias="streamingChartInfo")
    field__typename: str = Field(..., alias="__typename")


class StreamingCharts(BaseModel):
    model_config = ConfigDict(extra="forbid")
    edges: list[Edge]
    field__typename: str = Field(..., alias="__typename")


class SimilarTitlesV2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    sponsored_ad: None = Field(..., alias="sponsoredAd")
    field__typename: str = Field(..., alias="__typename")


class Package2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon: str
    icon_wide: str = Field(..., alias="iconWide")
    plan_offers: list[PlanOffer] = Field(..., alias="planOffers")
    field__typename: str = Field(..., alias="__typename")


class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    new_element_count: int = Field(..., alias="newElementCount")
    retail_price: None = Field(..., alias="retailPrice")
    retail_price_value: None = Field(..., alias="retailPriceValue")
    currency: str
    last_change_retail_price_value: None = Field(
        ..., alias="lastChangeRetailPriceValue"
    )
    type: str
    country: str
    package: Package2
    plans: list[Plan]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: None = Field(..., alias="availableTo")
    subtitle_languages: list[str] = Field(..., alias="subtitleLanguages")
    video_technology: list[str] = Field(..., alias="videoTechnology")
    audio_technology: list[str] = Field(..., alias="audioTechnology")
    audio_languages: list[str] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")


class RankInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    rank: int
    trend: str
    trend_difference: int = Field(..., alias="trendDifference")
    updated_at: AwareDatetime = Field(..., alias="updatedAt")
    days_in_top10: int = Field(..., alias="daysInTop10")
    days_in_top100: int = Field(..., alias="daysInTop100")
    days_in_top1000: int = Field(..., alias="daysInTop1000")
    days_in_top3: int = Field(..., alias="daysInTop3")
    top_rank: int = Field(..., alias="topRank")
    field__typename: str = Field(..., alias="__typename")

    @field_serializer("updated_at")
    def serialize_updated_at(self, value: AwareDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S.%f").rstrip("0").rstrip(".") + "Z"


class Title(BaseModel):
    model_config = ConfigDict(extra="forbid")
    full_path: str = Field(..., alias="fullPath")
    jw_entity_id: str = Field(..., alias="jwEntityID")
    poster_url: str = Field(..., alias="posterUrl")
    title: str
    show_title: None = Field(..., alias="showTitle")
    season_number: None = Field(..., alias="seasonNumber")
    rank_info: RankInfo = Field(..., alias="rankInfo")
    field__typename: str = Field(..., alias="__typename")


class Genre1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    translation: str
    field__typename: str = Field(..., alias="__typename")


class Scoring1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    imdb_votes: int | float | None = Field(..., alias="imdbVotes")
    imdb_score: int | float | None = Field(..., alias="imdbScore")
    tomato_meter: int | None = Field(..., alias="tomatoMeter")
    certified_fresh: bool | None = Field(..., alias="certifiedFresh")
    jw_rating: float | None = Field(..., alias="jwRating")
    field__typename: str = Field(..., alias="__typename")


class Interactions1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    votes_number: int = Field(..., alias="votesNumber")
    field__typename: str = Field(..., alias="__typename")


class Content3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    poster_url: str | None = Field(..., alias="posterUrl")
    full_path: str = Field(..., alias="fullPath")
    genres: list[Genre1]
    backdrops: list[Backdrop]
    scoring: Scoring1
    interactions: Interactions1
    field__typename: str = Field(..., alias="__typename")


class SeenState(BaseModel):
    model_config = ConfigDict(extra="forbid")
    progress: int
    seen_episode_count: int = Field(..., alias="seenEpisodeCount")
    field__typename: str = Field(..., alias="__typename")


class Node1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    content: Content3
    watchlist_entry_v2: None = Field(..., alias="watchlistEntryV2")
    likelist_entry: None = Field(..., alias="likelistEntry")
    dislikelist_entry: None = Field(..., alias="dislikelistEntry")
    field__typename: str = Field(..., alias="__typename")
    seenlist_entry: None = Field(None, alias="seenlistEntry")
    seen_state: SeenState | None = Field(None, alias="seenState")


class Titles1Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    node: Node1
    field__typename: str = Field(..., alias="__typename")


class Content2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    titles: list[Title] | None = Field(None, alias="Titles")
    field__typename: str = Field(..., alias="__typename")
    titles_1: list[Titles1Item] | None = Field(None, alias="titles")


class Template(BaseModel):
    model_config = ConfigDict(extra="forbid")
    anchor: str
    content_type: str = Field(..., alias="contentType")
    technical_name: str = Field(..., alias="technicalName")
    field__typename: str = Field(..., alias="__typename")


class TitleModule(BaseModel):
    model_config = ConfigDict(extra="forbid")
    content: Content2
    fomo_score: int = Field(..., alias="fomoScore")
    template: Template
    field__typename: str = Field(..., alias="__typename")


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_type: str = Field(..., alias="objectType")
    object_id: int = Field(..., alias="objectId")
    field__typename: str = Field(..., alias="__typename")
    justwatch_tv_offers: list[None] = Field(..., alias="justwatchTVOffers")
    disney_offers_count: int = Field(..., alias="disneyOffersCount")
    star_offers_count: int = Field(..., alias="starOffersCount")
    unique_offer_count: int = Field(..., alias="uniqueOfferCount")
    offers: list[Offer]
    watch_now_offer: WatchNowOffer = Field(..., alias="watchNowOffer")
    available_to: list[None] = Field(..., alias="availableTo")
    fall_back_clips: FallBackClips = Field(..., alias="fallBackClips")
    content: Content
    recommended_by_count: int = Field(..., alias="recommendedByCount")
    watched_by_count: int = Field(..., alias="watchedByCount")
    popularity_rank: PopularityRank = Field(..., alias="popularityRank")
    streaming_charts: StreamingCharts = Field(..., alias="streamingCharts")
    likelist_entry: None = Field(..., alias="likelistEntry")
    dislikelist_entry: None = Field(..., alias="dislikelistEntry")
    watchlist_entry_v2: None = Field(..., alias="watchlistEntryV2")
    customlist_entries: list[None] = Field(..., alias="customlistEntries")
    similar_titles_v2: SimilarTitlesV2 = Field(..., alias="similarTitlesV2")
    permanent_audiences: list[str] = Field(..., alias="permanentAudiences")
    seenlist_entry: None = Field(..., alias="seenlistEntry")
    offer_count: int = Field(..., alias="offerCount")
    max_offer_updated_at: AwareDatetime = Field(..., alias="maxOfferUpdatedAt")
    offers_history: list[None] = Field(..., alias="offersHistory")
    flatrate: list[FlatrateItem]
    buy: list[None]
    rent: list[None]
    free: list[None]
    fast: list[None]
    bundles: list[None]
    promoted_bundles: list[None] = Field(..., alias="promotedBundles")
    promoted_offers: list[None] = Field(..., alias="promotedOffers")
    title_modules: list[TitleModule] = Field(..., alias="titleModules")

    @field_serializer("max_offer_updated_at")
    def serialize_max_offer_updated_at(self, value: AwareDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S.%f").rstrip("0").rstrip(".") + "Z"


class UrlV2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    meta_description: str = Field(..., alias="metaDescription")
    meta_keywords: str = Field(..., alias="metaKeywords")
    meta_robots: str = Field(..., alias="metaRobots")
    meta_title: str = Field(..., alias="metaTitle")
    heading1: str
    heading2: str
    html_content: str = Field(..., alias="htmlContent")
    node: Node
    field__typename: str = Field(..., alias="__typename")


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url_v2: UrlV2 = Field(..., alias="urlV2")


class Variables(BaseModel):
    model_config = ConfigDict(extra="forbid")
    platform: str
    exclude_text_recommendation_title: bool = Field(
        ..., alias="excludeTextRecommendationTitle"
    )
    first: int
    fallback_to_foreign_offers: bool = Field(..., alias="fallbackToForeignOffers")
    exclude_packages: list[str] = Field(..., alias="excludePackages")
    full_path: str = Field(..., alias="fullPath")
    language: str
    country: str
    episode_max_limit: int = Field(..., alias="episodeMaxLimit")


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    referer: str = Field(..., alias="Referer")
    origin: str = Field(..., alias="Origin")


class JustScrape(BaseModel):
    model_config = ConfigDict(extra="forbid")
    variables: Variables
    query: str
    operation_name: str = Field(..., alias="operationName")
    headers: Headers


class UrlTitleDetailsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
