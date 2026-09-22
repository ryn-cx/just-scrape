from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from datetime import date

class PlanOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    retail_price: str | None = Field(None, alias='retailPrice')
    is_trial: bool | None = Field(None, alias='isTrial')
    duration_days: int | None = Field(None, alias='durationDays')
    retail_price_value: float | None = Field(None, alias='retailPriceValue')
    children: list[Any] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    package_id: int | None = Field(None, alias='packageId')
    clear_name: str | None = Field(None, alias='clearName')
    short_name: str | None = Field(None, alias='shortName')
    technical_name: str | None = Field(None, alias='technicalName')
    icon: str | None = None
    icon_wide: str | None = Field(None, alias='iconWide')
    plan_offers: list[PlanOffer] | None = Field(None, alias='planOffers')
    field__typename: str | None = Field(None, alias='__typename')

class Plan(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    retail_price: str | None = Field(None, alias='retailPrice')
    is_trial: bool | None = Field(None, alias='isTrial')
    duration_days: int | None = Field(None, alias='durationDays')
    retail_price_value: float | None = Field(None, alias='retailPriceValue')
    children: list[Any] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Offer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    presentation_type: str | None = Field(None, alias='presentationType')
    monetization_type: str | None = Field(None, alias='monetizationType')
    new_element_count: int | None = Field(None, alias='newElementCount')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    currency: str | None = None
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | None = None
    country: str | None = None
    package: Package | None = None
    plans: list[Plan] | None = None
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | None = Field(None, alias='elementCount')
    available_to: Any | None = Field(None, alias='availableTo')
    subtitle_languages: list[Any] | None = Field(None, alias='subtitleLanguages')
    video_technology: list[str] | None = Field(None, alias='videoTechnology')
    audio_technology: list[str] | None = Field(None, alias='audioTechnology')
    audio_languages: list[Any] | None = Field(None, alias='audioLanguages')
    field__typename: str | None = Field(None, alias='__typename')

class Package1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    icon: str | None = None
    package_id: int | None = Field(None, alias='packageId')
    clear_name: str | None = Field(None, alias='clearName')
    short_name: str | None = Field(None, alias='shortName')
    technical_name: str | None = Field(None, alias='technicalName')
    icon_wide: str | None = Field(None, alias='iconWide')
    has_rectangular_icon: bool | None = Field(None, alias='hasRectangularIcon')
    field__typename: str | None = Field(None, alias='__typename')

class WatchNowOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    package: Package1 | None = None
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    currency: str | None = None
    presentation_type: str | None = Field(None, alias='presentationType')
    monetization_type: str | None = Field(None, alias='monetizationType')
    available_to: Any | None = Field(None, alias='availableTo')
    date_created: date | None = Field(None, alias='dateCreated')
    new_element_count: int | None = Field(None, alias='newElementCount')

class Clip(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source_url: str | None = Field(None, alias='sourceUrl')
    external_id: str | None = Field(None, alias='externalId')
    provider: str | None = None
    name: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class DailymotionClip(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source_url: str | None = Field(None, alias='sourceUrl')
    external_id: str | None = Field(None, alias='externalId')
    provider: str | None = None
    name: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class FallBackClips(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    clips: list[Clip] | None = None
    videobuster_clips: list[Any] | None = Field(None, alias='videobusterClips')
    dailymotion_clips: list[DailymotionClip] | None = Field(None, alias='dailymotionClips')
    field__typename: str | None = Field(None, alias='__typename')

class Backdrop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrop_url: str | None = Field(None, alias='backdropUrl')
    field__typename: str | None = Field(None, alias='__typename')

class FullBackdrop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrop_url: str | None = Field(None, alias='backdropUrl')
    field__typename: str | None = Field(None, alias='__typename')

class ExternalIds(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_id: str | None = Field(None, alias='imdbId')
    wikidata_id: str | None = Field(None, alias='wikidataId')
    field__typename: str | None = Field(None, alias='__typename')

class Scoring(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_score: float | None = Field(None, alias='imdbScore')
    imdb_votes: int | None = Field(None, alias='imdbVotes')
    tmdb_popularity: float | None = Field(None, alias='tmdbPopularity')
    tmdb_score: float | None = Field(None, alias='tmdbScore')
    jw_rating: float | None = Field(None, alias='jwRating')
    tomato_meter: int | None = Field(None, alias='tomatoMeter')
    certified_fresh: bool | None = Field(None, alias='certifiedFresh')
    field__typename: str | None = Field(None, alias='__typename')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    short_name: str | None = Field(None, alias='shortName')
    translation: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Url(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    full_path: str | None = Field(None, alias='fullPath')
    field__typename: str | None = Field(None, alias='__typename')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    short_name: str | None = Field(None, alias='shortName')
    name: str | None = None
    field__typename: str | None = Field(None, alias='__typename')
    url: Url | None = None

class Subgenre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content1 | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    role: str | None = None
    name: str | None = None
    character_name: str | None = Field(None, alias='characterName')
    person_id: int | None = Field(None, alias='personId')
    portrait_url: str | None = Field(None, alias='portraitUrl')
    profile_path: Any | None = Field(None, alias='profilePath')
    field__typename: str | None = Field(None, alias='__typename')

class Interactions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dislikelist_additions: int | None = Field(None, alias='dislikelistAdditions')
    likelist_additions: int | None = Field(None, alias='likelistAdditions')
    votes_number: int | None = Field(None, alias='votesNumber')
    field__typename: str | None = Field(None, alias='__typename')

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    technical_name: str | None = Field(None, alias='technicalName')
    translated_name: str | None = Field(None, alias='translatedName')
    field__typename: str | None = Field(None, alias='__typename')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrops: list[Backdrop] | None = None
    full_backdrops: list[FullBackdrop] | None = Field(None, alias='fullBackdrops')
    clips: list[Clip] | None = None
    videobuster_clips: list[Any] | None = Field(None, alias='videobusterClips')
    dailymotion_clips: list[DailymotionClip] | None = Field(None, alias='dailymotionClips')
    external_ids: ExternalIds | None = Field(None, alias='externalIds')
    full_path: str | None = Field(None, alias='fullPath')
    poster_url: str | None = Field(None, alias='posterUrl')
    full_poster_url: str | None = Field(None, alias='fullPosterUrl')
    runtime: int | None = None
    is_released: bool | None = Field(None, alias='isReleased')
    scoring: Scoring | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    title: str | None = None
    original_release_year: int | None = Field(None, alias='originalReleaseYear')
    original_release_date: date | None = Field(None, alias='originalReleaseDate')
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')
    genres: list[Genre] | None = None
    subgenres: list[Subgenre] | None = None
    text_recommendations: Any | None = Field(None, alias='textRecommendations')
    field__typename: str | None = Field(None, alias='__typename')
    original_title: str | None = Field(None, alias='originalTitle')
    age_certification: str | None = Field(None, alias='ageCertification')
    credits: list[Credit] | None = None
    interactions: Interactions | None = None
    production_countries: list[str] | None = Field(None, alias='productionCountries')
    tags: list[Tag] | None = None

class PopularityRank(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rank: int | None = None
    trend: str | None = None
    trend_difference: int | None = Field(None, alias='trendDifference')
    field__typename: str | None = Field(None, alias='__typename')

class StreamingChartInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rank: int | None = None
    trend: str | None = None
    trend_difference: int | None = Field(None, alias='trendDifference')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    days_in_top10: int | None = Field(None, alias='daysInTop10')
    days_in_top100: int | None = Field(None, alias='daysInTop100')
    days_in_top1000: int | None = Field(None, alias='daysInTop1000')
    days_in_top3: int | None = Field(None, alias='daysInTop3')
    top_rank: int | None = Field(None, alias='topRank')
    field__typename: str | None = Field(None, alias='__typename')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    streaming_chart_info: StreamingChartInfo | None = Field(None, alias='streamingChartInfo')
    field__typename: str | None = Field(None, alias='__typename')

class StreamingCharts(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    edges: Any | list[Edge] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class SimilarTitlesV2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sponsored_ad: Any | None = Field(None, alias='sponsoredAd')
    field__typename: str | None = Field(None, alias='__typename')

class DateRange(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end: AwareDatetime | None = None
    start: AwareDatetime | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Package2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    id: str | None = None
    icon_wide: str | None = Field(None, alias='iconWide')
    clear_name: str | None = Field(None, alias='clearName')
    package_id: int | None = Field(None, alias='packageId')
    monetization_types: list[str] | None = Field(None, alias='monetizationTypes')
    field__typename: str | None = Field(None, alias='__typename')

class OffersHistoryItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    country: str | None = None
    date_ranges: list[DateRange] | None = Field(None, alias='dateRanges')
    package: Package2 | None = None

class Package3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    package_id: int | None = Field(None, alias='packageId')
    clear_name: str | None = Field(None, alias='clearName')
    short_name: str | None = Field(None, alias='shortName')
    technical_name: str | None = Field(None, alias='technicalName')
    icon: str | None = None
    icon_wide: str | None = Field(None, alias='iconWide')
    plan_offers: list[PlanOffer] | None = Field(None, alias='planOffers')
    field__typename: str | None = Field(None, alias='__typename')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    presentation_type: str | None = Field(None, alias='presentationType')
    monetization_type: str | None = Field(None, alias='monetizationType')
    new_element_count: int | None = Field(None, alias='newElementCount')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    currency: str | None = None
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | None = None
    country: str | None = None
    package: Package3 | None = None
    plans: list[Plan] | None = None
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | None = Field(None, alias='elementCount')
    available_to: Any | None = Field(None, alias='availableTo')
    subtitle_languages: list[Any] | None = Field(None, alias='subtitleLanguages')
    video_technology: list[str] | None = Field(None, alias='videoTechnology')
    audio_technology: list[str] | None = Field(None, alias='audioTechnology')
    audio_languages: list[Any] | None = Field(None, alias='audioLanguages')
    field__typename: str | None = Field(None, alias='__typename')

class RankInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rank: int | None = None
    trend: str | None = None
    trend_difference: int | None = Field(None, alias='trendDifference')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    days_in_top10: int | None = Field(None, alias='daysInTop10')
    days_in_top100: int | None = Field(None, alias='daysInTop100')
    days_in_top1000: int | None = Field(None, alias='daysInTop1000')
    days_in_top3: int | None = Field(None, alias='daysInTop3')
    top_rank: int | None = Field(None, alias='topRank')
    field__typename: str | None = Field(None, alias='__typename')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    full_path: str | None = Field(None, alias='fullPath')
    jw_entity_id: str | None = Field(None, alias='jwEntityID')
    poster_url: str | None = Field(None, alias='posterUrl')
    title: str | None = None
    show_title: Any | None = Field(None, alias='showTitle')
    season_number: Any | None = Field(None, alias='seasonNumber')
    rank_info: RankInfo | None = Field(None, alias='rankInfo')
    field__typename: str | None = Field(None, alias='__typename')

class Genre1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    translation: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Scoring1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_votes: int | float | None = Field(None, alias='imdbVotes')
    imdb_score: int | float | None = Field(None, alias='imdbScore')
    tomato_meter: int | None = Field(None, alias='tomatoMeter')
    certified_fresh: bool | None = Field(None, alias='certifiedFresh')
    jw_rating: float | None = Field(None, alias='jwRating')
    field__typename: str | None = Field(None, alias='__typename')

class Interactions1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    votes_number: int | None = Field(None, alias='votesNumber')
    field__typename: str | None = Field(None, alias='__typename')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    poster_url: str | None = Field(None, alias='posterUrl')
    full_path: str | None = Field(None, alias='fullPath')
    genres: list[Genre1] | None = None
    backdrops: list[Backdrop] | None = None
    scoring: Scoring1 | None = None
    interactions: Interactions1 | None = None
    field__typename: str | None = Field(None, alias='__typename')
    season_number: int | None = Field(None, alias='seasonNumber')

class SeenState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    progress: int | None = None
    seen_episode_count: int | None = Field(None, alias='seenEpisodeCount')
    field__typename: str | None = Field(None, alias='__typename')

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Show(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    field__typename: str | None = Field(None, alias='__typename')
    content: Content4 | None = None

class Node1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    content: Content3 | None = None
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    field__typename: str | None = Field(None, alias='__typename')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    seen_state: SeenState | None = Field(None, alias='seenState')
    show: Show | None = None

class Titles1Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node: Node1 | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    titles: list[Title] | None = Field(None, alias='Titles')
    field__typename: str | None = Field(None, alias='__typename')
    titles_1: list[Titles1Item] | None = Field(None, alias='titles')

class Template(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    anchor: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    technical_name: str | None = Field(None, alias='technicalName')
    field__typename: str | None = Field(None, alias='__typename')

class TitleModules(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content2 | None = None
    fomo_score: int | None = Field(None, alias='fomoScore')
    template: Template | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_url: str | None = Field(None, alias='posterUrl')
    season_number: int | None = Field(None, alias='seasonNumber')
    full_path: str | None = Field(None, alias='fullPath')
    title: str | None = None
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')
    is_released: bool | None = Field(None, alias='isReleased')
    original_release_year: int | None = Field(None, alias='originalReleaseYear')
    field__typename: str | None = Field(None, alias='__typename')

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Show1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    content: Content6 | None = None

class FallBackClips1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    clips: list[Clip] | None = None
    videobuster_clips: list[Any] | None = Field(None, alias='videobusterClips')
    dailymotion_clips: list[DailymotionClip] | None = Field(None, alias='dailymotionClips')
    field__typename: str | None = Field(None, alias='__typename')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    total_episode_count: int | None = Field(None, alias='totalEpisodeCount')
    available_to: list[Any] | None = Field(None, alias='availableTo')
    offers: list[Any] | None = None
    content: Content5 | None = None
    show: Show1 | None = None
    fall_back_clips: FallBackClips1 | None = Field(None, alias='fallBackClips')
    field__typename: str | None = Field(None, alias='__typename')

class Content7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    title: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    episode_number: int | None = Field(None, alias='episodeNumber')
    season_number: int | None = Field(None, alias='seasonNumber')
    is_released: bool | None = Field(None, alias='isReleased')
    runtime: int | None = None
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')

class RecentEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    unique_offer_count: int | None = Field(None, alias='uniqueOfferCount')
    flatrate: list[Any] | None = None
    buy: list[Any] | None = None
    rent: list[Any] | None = None
    free: list[Any] | None = None
    fast: list[Any] | None = None
    content: Content7 | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    object_type: str | None = Field(None, alias='objectType')
    object_id: int | None = Field(None, alias='objectId')
    field__typename: str | None = Field(None, alias='__typename')
    justwatch_tv_offers: list[Any] | None = Field(None, alias='justwatchTVOffers')
    disney_offers_count: int | None = Field(None, alias='disneyOffersCount')
    star_offers_count: int | None = Field(None, alias='starOffersCount')
    unique_offer_count: int | None = Field(None, alias='uniqueOfferCount')
    offers: list[Offer] | None = None
    watch_now_offer: Any | WatchNowOffer | None = Field(None, alias='watchNowOffer')
    available_to: list[Any] | None = Field(None, alias='availableTo')
    fall_back_clips: FallBackClips | None = Field(None, alias='fallBackClips')
    content: Content | None = None
    recommended_by_count: int | None = Field(None, alias='recommendedByCount')
    watched_by_count: int | None = Field(None, alias='watchedByCount')
    popularity_rank: PopularityRank | None = Field(None, alias='popularityRank')
    streaming_charts: StreamingCharts | None = Field(None, alias='streamingCharts')
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    customlist_entries: list[Any] | None = Field(None, alias='customlistEntries')
    similar_titles_v2: SimilarTitlesV2 | None = Field(None, alias='similarTitlesV2')
    permanent_audiences: list[str] | None = Field(None, alias='permanentAudiences')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    offer_count: int | None = Field(None, alias='offerCount')
    max_offer_updated_at: Any | AwareDatetime | None = Field(None, alias='maxOfferUpdatedAt')
    offers_history: list[OffersHistoryItem] | None = Field(None, alias='offersHistory')
    flatrate: list[FlatrateItem] | None = None
    buy: list[Any] | None = None
    rent: list[Any] | None = None
    free: list[Any] | None = None
    fast: list[Any] | None = None
    bundles: list[Any] | None = None
    promoted_bundles: list[Any] | None = Field(None, alias='promotedBundles')
    promoted_offers: list[Any] | None = Field(None, alias='promotedOffers')
    title_modules: list[Any | TitleModules] | None = Field(None, alias='titleModules')
    total_season_count: int | None = Field(None, alias='totalSeasonCount')
    seen_state: SeenState | None = Field(None, alias='seenState')
    tv_show_tracking_entry: Any | None = Field(None, alias='tvShowTrackingEntry')
    seasons: list[Season] | None = None
    recent_episodes: list[RecentEpisode] | None = Field(None, alias='recentEpisodes')

class UrlTitleDetailsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    meta_description: str | None = Field(None, alias='metaDescription')
    meta_keywords: str | None = Field(None, alias='metaKeywords')
    meta_robots: str | None = Field(None, alias='metaRobots')
    meta_title: str | None = Field(None, alias='metaTitle')
    heading1: str | None = None
    heading2: str | None = None
    html_content: str | None = Field(None, alias='htmlContent')
    node: Node | None = None
    field__typename: str | None = Field(None, alias='__typename')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
