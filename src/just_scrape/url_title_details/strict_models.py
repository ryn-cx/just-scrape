from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any
from datetime import date

class PlanOffer(BaseModel):
    title: str
    retail_price: str = Field(..., alias='retailPrice')
    is_trial: bool = Field(..., alias='isTrial')
    duration_days: int = Field(..., alias='durationDays')
    retail_price_value: float = Field(..., alias='retailPriceValue')
    children: list[None]
    field__typename: str = Field(..., alias='__typename')

class Package(BaseModel):
    id: str
    package_id: int = Field(..., alias='packageId')
    clear_name: str = Field(..., alias='clearName')
    short_name: str = Field(..., alias='shortName')
    technical_name: str = Field(..., alias='technicalName')
    icon: str
    icon_wide: str = Field(..., alias='iconWide')
    plan_offers: list[PlanOffer] = Field(..., alias='planOffers')
    field__typename: str = Field(..., alias='__typename')

class Plan(BaseModel):
    title: str
    retail_price: str = Field(..., alias='retailPrice')
    is_trial: bool = Field(..., alias='isTrial')
    duration_days: int = Field(..., alias='durationDays')
    retail_price_value: float = Field(..., alias='retailPriceValue')
    children: list[None]
    field__typename: str = Field(..., alias='__typename')

class Offer(BaseModel):
    id: str
    presentation_type: str = Field(..., alias='presentationType')
    monetization_type: str = Field(..., alias='monetizationType')
    new_element_count: int = Field(..., alias='newElementCount')
    retail_price: None = Field(..., alias='retailPrice')
    retail_price_value: None = Field(..., alias='retailPriceValue')
    currency: str
    last_change_retail_price_value: None = Field(..., alias='lastChangeRetailPriceValue')
    type: str
    country: str
    package: Package
    plans: list[Plan]
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    stream_url: None = Field(..., alias='streamUrl')
    stream_url_external_player: None = Field(..., alias='streamUrlExternalPlayer')
    element_count: int = Field(..., alias='elementCount')
    available_to: None = Field(..., alias='availableTo')
    subtitle_languages: list[None] = Field(..., alias='subtitleLanguages')
    video_technology: list[str] = Field(..., alias='videoTechnology')
    audio_technology: list[str] = Field(..., alias='audioTechnology')
    audio_languages: list[None] = Field(..., alias='audioLanguages')
    field__typename: str = Field(..., alias='__typename')

class Package1(BaseModel):
    id: str
    icon: str
    package_id: int = Field(..., alias='packageId')
    clear_name: str = Field(..., alias='clearName')
    short_name: str = Field(..., alias='shortName')
    technical_name: str = Field(..., alias='technicalName')
    icon_wide: str = Field(..., alias='iconWide')
    has_rectangular_icon: bool = Field(..., alias='hasRectangularIcon')
    field__typename: str = Field(..., alias='__typename')

class WatchNowOffer(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    id: str
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    stream_url: None = Field(..., alias='streamUrl')
    stream_url_external_player: None = Field(..., alias='streamUrlExternalPlayer')
    package: Package1
    retail_price: None = Field(..., alias='retailPrice')
    retail_price_value: None = Field(..., alias='retailPriceValue')
    last_change_retail_price_value: None = Field(..., alias='lastChangeRetailPriceValue')
    currency: str
    presentation_type: str = Field(..., alias='presentationType')
    monetization_type: str = Field(..., alias='monetizationType')
    available_to: None = Field(..., alias='availableTo')
    date_created: date = Field(..., alias='dateCreated')
    new_element_count: int = Field(..., alias='newElementCount')

class Clip(BaseModel):
    source_url: str = Field(..., alias='sourceUrl')
    external_id: str = Field(..., alias='externalId')
    provider: str
    name: str
    field__typename: str = Field(..., alias='__typename')

class DailymotionClip(BaseModel):
    source_url: str = Field(..., alias='sourceUrl')
    external_id: str = Field(..., alias='externalId')
    provider: str
    name: str
    field__typename: str = Field(..., alias='__typename')

class FallBackClips(BaseModel):
    clips: list[Clip]
    videobuster_clips: list[None] = Field(..., alias='videobusterClips')
    dailymotion_clips: list[DailymotionClip] = Field(..., alias='dailymotionClips')
    field__typename: str = Field(..., alias='__typename')

class Backdrop(BaseModel):
    backdrop_url: str = Field(..., alias='backdropUrl')
    field__typename: str = Field(..., alias='__typename')

class FullBackdrop(BaseModel):
    backdrop_url: str = Field(..., alias='backdropUrl')
    field__typename: str = Field(..., alias='__typename')

class ExternalIds(BaseModel):
    imdb_id: str = Field(..., alias='imdbId')
    wikidata_id: str | None = Field(..., alias='wikidataId')
    field__typename: str = Field(..., alias='__typename')

class Scoring(BaseModel):
    imdb_score: float = Field(..., alias='imdbScore')
    imdb_votes: int = Field(..., alias='imdbVotes')
    tmdb_popularity: float = Field(..., alias='tmdbPopularity')
    tmdb_score: float = Field(..., alias='tmdbScore')
    jw_rating: float = Field(..., alias='jwRating')
    tomato_meter: int | None = Field(..., alias='tomatoMeter')
    certified_fresh: bool | None = Field(..., alias='certifiedFresh')
    field__typename: str = Field(..., alias='__typename')

class Genre(BaseModel):
    short_name: str = Field(..., alias='shortName')
    translation: str
    field__typename: str = Field(..., alias='__typename')

class Url(BaseModel):
    full_path: str = Field(..., alias='fullPath')
    field__typename: str = Field(..., alias='__typename')

class Content1(BaseModel):
    short_name: str = Field(..., alias='shortName')
    name: str
    field__typename: str = Field(..., alias='__typename')
    url: Url

class Subgenre(BaseModel):
    content: Content1
    field__typename: str = Field(..., alias='__typename')

class Credit(BaseModel):
    role: str
    name: str
    character_name: str = Field(..., alias='characterName')
    person_id: int = Field(..., alias='personId')
    portrait_url: str | None = Field(..., alias='portraitUrl')
    profile_path: None = Field(..., alias='profilePath')
    field__typename: str = Field(..., alias='__typename')

class Interactions(BaseModel):
    dislikelist_additions: int = Field(..., alias='dislikelistAdditions')
    likelist_additions: int = Field(..., alias='likelistAdditions')
    votes_number: int = Field(..., alias='votesNumber')
    field__typename: str = Field(..., alias='__typename')

class Tag(BaseModel):
    technical_name: str = Field(..., alias='technicalName')
    translated_name: str = Field(..., alias='translatedName')
    field__typename: str = Field(..., alias='__typename')

class Content(BaseModel):
    backdrops: list[Backdrop]
    full_backdrops: list[FullBackdrop] = Field(..., alias='fullBackdrops')
    clips: list[Clip]
    videobuster_clips: list[None] = Field(..., alias='videobusterClips')
    dailymotion_clips: list[DailymotionClip] = Field(..., alias='dailymotionClips')
    external_ids: ExternalIds = Field(..., alias='externalIds')
    full_path: str = Field(..., alias='fullPath')
    poster_url: str = Field(..., alias='posterUrl')
    full_poster_url: str = Field(..., alias='fullPosterUrl')
    runtime: int
    is_released: bool = Field(..., alias='isReleased')
    scoring: Scoring
    short_description: str = Field(..., alias='shortDescription')
    title: str
    original_release_year: int = Field(..., alias='originalReleaseYear')
    original_release_date: date = Field(..., alias='originalReleaseDate')
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    genres: list[Genre]
    subgenres: list[Subgenre]
    text_recommendations: None = Field(..., alias='textRecommendations')
    field__typename: str = Field(..., alias='__typename')
    original_title: str = Field(..., alias='originalTitle')
    age_certification: str = Field(..., alias='ageCertification')
    credits: list[Credit]
    interactions: Interactions
    production_countries: list[str] = Field(..., alias='productionCountries')
    tags: list[Tag]

class PopularityRank(BaseModel):
    rank: int
    trend: str
    trend_difference: int = Field(..., alias='trendDifference')
    field__typename: str = Field(..., alias='__typename')

class StreamingChartInfo(BaseModel):
    rank: int
    trend: str
    trend_difference: int = Field(..., alias='trendDifference')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    days_in_top10: int = Field(..., alias='daysInTop10')
    days_in_top100: int = Field(..., alias='daysInTop100')
    days_in_top1000: int = Field(..., alias='daysInTop1000')
    days_in_top3: int = Field(..., alias='daysInTop3')
    top_rank: int = Field(..., alias='topRank')
    field__typename: str = Field(..., alias='__typename')

class Edge(BaseModel):
    streaming_chart_info: StreamingChartInfo = Field(..., alias='streamingChartInfo')
    field__typename: str = Field(..., alias='__typename')

class StreamingCharts(BaseModel):
    edges: list[Edge] | None
    field__typename: str = Field(..., alias='__typename')

class SimilarTitlesV2(BaseModel):
    sponsored_ad: None = Field(..., alias='sponsoredAd')
    field__typename: str = Field(..., alias='__typename')

class DateRange(BaseModel):
    end: AwareDatetime
    start: AwareDatetime
    field__typename: str = Field(..., alias='__typename')

class Package2(BaseModel):
    icon: str
    id: str
    icon_wide: str = Field(..., alias='iconWide')
    clear_name: str = Field(..., alias='clearName')
    package_id: int = Field(..., alias='packageId')
    monetization_types: list[str] = Field(..., alias='monetizationTypes')
    field__typename: str = Field(..., alias='__typename')

class OffersHistoryItem(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    id: str
    country: str
    date_ranges: list[DateRange] = Field(..., alias='dateRanges')
    package: Package2

class Package3(BaseModel):
    id: str
    package_id: int = Field(..., alias='packageId')
    clear_name: str = Field(..., alias='clearName')
    short_name: str = Field(..., alias='shortName')
    technical_name: str = Field(..., alias='technicalName')
    icon: str
    icon_wide: str = Field(..., alias='iconWide')
    plan_offers: list[PlanOffer] = Field(..., alias='planOffers')
    field__typename: str = Field(..., alias='__typename')

class FlatrateItem(BaseModel):
    id: str
    presentation_type: str = Field(..., alias='presentationType')
    monetization_type: str = Field(..., alias='monetizationType')
    new_element_count: int = Field(..., alias='newElementCount')
    retail_price: None = Field(..., alias='retailPrice')
    retail_price_value: None = Field(..., alias='retailPriceValue')
    currency: str
    last_change_retail_price_value: None = Field(..., alias='lastChangeRetailPriceValue')
    type: str
    country: str
    package: Package3
    plans: list[Plan]
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    stream_url: None = Field(..., alias='streamUrl')
    stream_url_external_player: None = Field(..., alias='streamUrlExternalPlayer')
    element_count: int = Field(..., alias='elementCount')
    available_to: None = Field(..., alias='availableTo')
    subtitle_languages: list[None] = Field(..., alias='subtitleLanguages')
    video_technology: list[str] = Field(..., alias='videoTechnology')
    audio_technology: list[str] = Field(..., alias='audioTechnology')
    audio_languages: list[None] = Field(..., alias='audioLanguages')
    field__typename: str = Field(..., alias='__typename')

class RankInfo(BaseModel):
    rank: int
    trend: str
    trend_difference: int = Field(..., alias='trendDifference')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    days_in_top10: int = Field(..., alias='daysInTop10')
    days_in_top100: int = Field(..., alias='daysInTop100')
    days_in_top1000: int = Field(..., alias='daysInTop1000')
    days_in_top3: int = Field(..., alias='daysInTop3')
    top_rank: int = Field(..., alias='topRank')
    field__typename: str = Field(..., alias='__typename')

class Title(BaseModel):
    full_path: str = Field(..., alias='fullPath')
    jw_entity_id: str = Field(..., alias='jwEntityID')
    poster_url: str = Field(..., alias='posterUrl')
    title: str
    show_title: None = Field(..., alias='showTitle')
    season_number: None = Field(..., alias='seasonNumber')
    rank_info: RankInfo = Field(..., alias='rankInfo')
    field__typename: str = Field(..., alias='__typename')

class Genre1(BaseModel):
    translation: str
    field__typename: str = Field(..., alias='__typename')

class Scoring1(BaseModel):
    imdb_votes: int | float | None = Field(..., alias='imdbVotes')
    imdb_score: int | float | None = Field(..., alias='imdbScore')
    tomato_meter: int | None = Field(..., alias='tomatoMeter')
    certified_fresh: bool | None = Field(..., alias='certifiedFresh')
    jw_rating: float | None = Field(..., alias='jwRating')
    field__typename: str = Field(..., alias='__typename')

class Interactions1(BaseModel):
    votes_number: int = Field(..., alias='votesNumber')
    field__typename: str = Field(..., alias='__typename')

class Content3(BaseModel):
    title: str
    poster_url: str | None = Field(..., alias='posterUrl')
    full_path: str = Field(..., alias='fullPath')
    genres: list[Genre1]
    backdrops: list[Backdrop]
    scoring: Scoring1
    interactions: Interactions1
    field__typename: str = Field(..., alias='__typename')
    season_number: int | None = Field(None, alias='seasonNumber')

class SeenState(BaseModel):
    progress: int
    seen_episode_count: int = Field(..., alias='seenEpisodeCount')
    field__typename: str = Field(..., alias='__typename')

class Content4(BaseModel):
    title: str
    field__typename: str = Field(..., alias='__typename')

class Show(BaseModel):
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    field__typename: str = Field(..., alias='__typename')
    content: Content4

class Node1(BaseModel):
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    content: Content3
    watchlist_entry_v2: None = Field(None, alias='watchlistEntryV2')
    likelist_entry: None = Field(None, alias='likelistEntry')
    dislikelist_entry: None = Field(None, alias='dislikelistEntry')
    field__typename: str = Field(..., alias='__typename')
    seenlist_entry: None = Field(None, alias='seenlistEntry')
    seen_state: SeenState | None = Field(None, alias='seenState')
    show: Show | None = None

class Titles1Item(BaseModel):
    node: Node1
    field__typename: str = Field(..., alias='__typename')

class Content2(BaseModel):
    titles: list[Title] | None = Field(None, alias='Titles')
    field__typename: str = Field(..., alias='__typename')
    titles_1: list[Titles1Item] | None = Field(None, alias='titles')

class Template(BaseModel):
    anchor: str
    content_type: str = Field(..., alias='contentType')
    technical_name: str = Field(..., alias='technicalName')
    field__typename: str = Field(..., alias='__typename')

class TitleModules(BaseModel):
    content: Content2
    fomo_score: int = Field(..., alias='fomoScore')
    template: Template
    field__typename: str = Field(..., alias='__typename')

class Content5(BaseModel):
    poster_url: str = Field(..., alias='posterUrl')
    season_number: int = Field(..., alias='seasonNumber')
    full_path: str = Field(..., alias='fullPath')
    title: str
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    is_released: bool = Field(..., alias='isReleased')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    field__typename: str = Field(..., alias='__typename')

class Content6(BaseModel):
    title: str
    field__typename: str = Field(..., alias='__typename')

class Show1(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    watchlist_entry_v2: None = Field(..., alias='watchlistEntryV2')
    content: Content6

class FallBackClips1(BaseModel):
    clips: list[Clip]
    videobuster_clips: list[None] = Field(..., alias='videobusterClips')
    dailymotion_clips: list[DailymotionClip] = Field(..., alias='dailymotionClips')
    field__typename: str = Field(..., alias='__typename')

class Season(BaseModel):
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    total_episode_count: int = Field(..., alias='totalEpisodeCount')
    available_to: list[None] = Field(..., alias='availableTo')
    offers: list[None]
    content: Content5
    show: Show1
    fall_back_clips: FallBackClips1 = Field(..., alias='fallBackClips')
    field__typename: str = Field(..., alias='__typename')

class Content7(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    title: str
    short_description: str = Field(..., alias='shortDescription')
    episode_number: int = Field(..., alias='episodeNumber')
    season_number: int = Field(..., alias='seasonNumber')
    is_released: bool = Field(..., alias='isReleased')
    runtime: int
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')

class RecentEpisode(BaseModel):
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    seenlist_entry: None = Field(..., alias='seenlistEntry')
    unique_offer_count: int = Field(..., alias='uniqueOfferCount')
    flatrate: list[None]
    buy: list[None]
    rent: list[None]
    free: list[None]
    fast: list[None]
    content: Content7
    field__typename: str = Field(..., alias='__typename')

class Node(BaseModel):
    id: str
    object_type: str = Field(..., alias='objectType')
    object_id: int = Field(..., alias='objectId')
    field__typename: str = Field(..., alias='__typename')
    justwatch_tv_offers: list[None] = Field(..., alias='justwatchTVOffers')
    disney_offers_count: int = Field(..., alias='disneyOffersCount')
    star_offers_count: int = Field(..., alias='starOffersCount')
    unique_offer_count: int = Field(..., alias='uniqueOfferCount')
    offers: list[Offer]
    watch_now_offer: WatchNowOffer | None = Field(..., alias='watchNowOffer')
    available_to: list[None] = Field(..., alias='availableTo')
    fall_back_clips: FallBackClips = Field(..., alias='fallBackClips')
    content: Content
    recommended_by_count: int = Field(..., alias='recommendedByCount')
    watched_by_count: int = Field(..., alias='watchedByCount')
    popularity_rank: PopularityRank = Field(..., alias='popularityRank')
    streaming_charts: StreamingCharts = Field(..., alias='streamingCharts')
    likelist_entry: None = Field(..., alias='likelistEntry')
    dislikelist_entry: None = Field(..., alias='dislikelistEntry')
    watchlist_entry_v2: None = Field(..., alias='watchlistEntryV2')
    customlist_entries: list[None] = Field(..., alias='customlistEntries')
    similar_titles_v2: SimilarTitlesV2 = Field(..., alias='similarTitlesV2')
    permanent_audiences: list[str] = Field(..., alias='permanentAudiences')
    seenlist_entry: None = Field(None, alias='seenlistEntry')
    offer_count: int = Field(..., alias='offerCount')
    max_offer_updated_at: AwareDatetime | None = Field(..., alias='maxOfferUpdatedAt')
    offers_history: list[OffersHistoryItem] = Field(..., alias='offersHistory')
    flatrate: list[FlatrateItem]
    buy: list[None]
    rent: list[None]
    free: list[None]
    fast: list[None]
    bundles: list[None]
    promoted_bundles: list[None] = Field(..., alias='promotedBundles')
    promoted_offers: list[None] = Field(..., alias='promotedOffers')
    title_modules: list[TitleModules | None] = Field(..., alias='titleModules')
    total_season_count: int | None = Field(None, alias='totalSeasonCount')
    seen_state: SeenState | None = Field(None, alias='seenState')
    tv_show_tracking_entry: None = Field(None, alias='tvShowTrackingEntry')
    seasons: list[Season] | None = None
    recent_episodes: list[RecentEpisode] | None = Field(None, alias='recentEpisodes')

class UrlV2(BaseModel):
    id: str
    meta_description: str = Field(..., alias='metaDescription')
    meta_keywords: str = Field(..., alias='metaKeywords')
    meta_robots: str = Field(..., alias='metaRobots')
    meta_title: str = Field(..., alias='metaTitle')
    heading1: str
    heading2: str
    html_content: str = Field(..., alias='htmlContent')
    node: Node
    field__typename: str = Field(..., alias='__typename')

class Data(BaseModel):
    url_v2: UrlV2 = Field(..., alias='urlV2')

class UrlTitleDetailsModel(BaseModel):
    data: Data
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
