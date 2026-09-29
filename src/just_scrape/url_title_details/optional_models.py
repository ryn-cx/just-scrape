from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from datetime import date

class PlanOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    retail_price: str | Any = Field(None, alias='retailPrice', union_mode='left_to_right')
    is_trial: bool | Any = Field(None, alias='isTrial', union_mode='left_to_right')
    duration_days: int | Any = Field(None, alias='durationDays', union_mode='left_to_right')
    retail_price_value: float | Any = Field(None, alias='retailPriceValue', union_mode='left_to_right')
    children: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    icon_wide: str | Any = Field(None, alias='iconWide', union_mode='left_to_right')
    plan_offers: list[PlanOffer] | Any = Field(None, alias='planOffers', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Plan(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    retail_price: str | Any = Field(None, alias='retailPrice', union_mode='left_to_right')
    is_trial: bool | Any = Field(None, alias='isTrial', union_mode='left_to_right')
    duration_days: int | Any = Field(None, alias='durationDays', union_mode='left_to_right')
    retail_price_value: float | Any = Field(None, alias='retailPriceValue', union_mode='left_to_right')
    children: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Offer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    presentation_type: str | Any = Field(None, alias='presentationType', union_mode='left_to_right')
    monetization_type: str | Any = Field(None, alias='monetizationType', union_mode='left_to_right')
    new_element_count: int | Any = Field(None, alias='newElementCount', union_mode='left_to_right')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    currency: str | Any = Field(default=None, union_mode='left_to_right')
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    package: Package | Any = Field(default=None, union_mode='left_to_right')
    plans: list[Plan] | Any = Field(default=None, union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | Any = Field(None, alias='elementCount', union_mode='left_to_right')
    available_to: Any | None = Field(None, alias='availableTo')
    subtitle_languages: list[Any] | Any = Field(None, alias='subtitleLanguages', union_mode='left_to_right')
    video_technology: list[str] | Any = Field(None, alias='videoTechnology', union_mode='left_to_right')
    audio_technology: list[str] | Any = Field(None, alias='audioTechnology', union_mode='left_to_right')
    audio_languages: list[Any] | Any = Field(None, alias='audioLanguages', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    icon_wide: str | Any = Field(None, alias='iconWide', union_mode='left_to_right')
    has_rectangular_icon: bool | Any = Field(None, alias='hasRectangularIcon', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class WatchNowOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    package: Package1 | Any = Field(default=None, union_mode='left_to_right')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    currency: str | Any = Field(default=None, union_mode='left_to_right')
    presentation_type: str | Any = Field(None, alias='presentationType', union_mode='left_to_right')
    monetization_type: str | Any = Field(None, alias='monetizationType', union_mode='left_to_right')
    available_to: Any | None = Field(None, alias='availableTo')
    date_created: date | Any = Field(None, alias='dateCreated', union_mode='left_to_right')
    new_element_count: int | Any = Field(None, alias='newElementCount', union_mode='left_to_right')

class Clip(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source_url: str | Any = Field(None, alias='sourceUrl', union_mode='left_to_right')
    external_id: str | Any = Field(None, alias='externalId', union_mode='left_to_right')
    provider: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class DailymotionClip(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source_url: str | Any = Field(None, alias='sourceUrl', union_mode='left_to_right')
    external_id: str | Any = Field(None, alias='externalId', union_mode='left_to_right')
    provider: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class FallBackClips(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    clips: list[Clip] | Any = Field(default=None, union_mode='left_to_right')
    videobuster_clips: list[Any] | Any = Field(None, alias='videobusterClips', union_mode='left_to_right')
    dailymotion_clips: list[DailymotionClip] | Any = Field(None, alias='dailymotionClips', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Backdrop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrop_url: str | Any = Field(None, alias='backdropUrl', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class FullBackdrop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrop_url: str | Any = Field(None, alias='backdropUrl', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class ExternalIds(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_id: str | Any = Field(None, alias='imdbId', union_mode='left_to_right')
    wikidata_id: str | Any = Field(None, alias='wikidataId', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Scoring(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_score: float | Any = Field(None, alias='imdbScore', union_mode='left_to_right')
    imdb_votes: int | Any = Field(None, alias='imdbVotes', union_mode='left_to_right')
    tmdb_popularity: float | Any = Field(None, alias='tmdbPopularity', union_mode='left_to_right')
    tmdb_score: float | Any = Field(None, alias='tmdbScore', union_mode='left_to_right')
    jw_rating: float | Any = Field(None, alias='jwRating', union_mode='left_to_right')
    tomato_meter: int | Any = Field(None, alias='tomatoMeter', union_mode='left_to_right')
    certified_fresh: bool | Any = Field(None, alias='certifiedFresh', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    translation: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Url(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    url: Url | Any = Field(default=None, union_mode='left_to_right')

class Subgenre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content1 | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    role: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    character_name: str | Any = Field(None, alias='characterName', union_mode='left_to_right')
    person_id: int | Any = Field(None, alias='personId', union_mode='left_to_right')
    portrait_url: str | Any = Field(None, alias='portraitUrl', union_mode='left_to_right')
    profile_path: Any | None = Field(None, alias='profilePath')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Interactions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dislikelist_additions: int | Any = Field(None, alias='dislikelistAdditions', union_mode='left_to_right')
    likelist_additions: int | Any = Field(None, alias='likelistAdditions', union_mode='left_to_right')
    votes_number: int | Any = Field(None, alias='votesNumber', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    translated_name: str | Any = Field(None, alias='translatedName', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrops: list[Backdrop] | Any = Field(default=None, union_mode='left_to_right')
    full_backdrops: list[FullBackdrop] | Any = Field(None, alias='fullBackdrops', union_mode='left_to_right')
    clips: list[Clip] | Any = Field(default=None, union_mode='left_to_right')
    videobuster_clips: list[Any] | Any = Field(None, alias='videobusterClips', union_mode='left_to_right')
    dailymotion_clips: list[DailymotionClip] | Any = Field(None, alias='dailymotionClips', union_mode='left_to_right')
    external_ids: ExternalIds | Any = Field(None, alias='externalIds', union_mode='left_to_right')
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    full_poster_url: str | Any = Field(None, alias='fullPosterUrl', union_mode='left_to_right')
    runtime: int | Any = Field(default=None, union_mode='left_to_right')
    is_released: bool | Any = Field(None, alias='isReleased', union_mode='left_to_right')
    scoring: Scoring | Any = Field(default=None, union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    original_release_year: int | Any = Field(None, alias='originalReleaseYear', union_mode='left_to_right')
    original_release_date: date | Any = Field(None, alias='originalReleaseDate', union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')
    subgenres: list[Subgenre] | Any = Field(default=None, union_mode='left_to_right')
    text_recommendations: Any | None = Field(None, alias='textRecommendations')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    original_title: str | Any = Field(None, alias='originalTitle', union_mode='left_to_right')
    age_certification: str | Any = Field(None, alias='ageCertification', union_mode='left_to_right')
    credits: list[Credit] | Any = Field(default=None, union_mode='left_to_right')
    interactions: Interactions | Any = Field(default=None, union_mode='left_to_right')
    production_countries: list[str] | Any = Field(None, alias='productionCountries', union_mode='left_to_right')
    tags: list[Tag] | Any = Field(default=None, union_mode='left_to_right')

class PopularityRank(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rank: int | Any = Field(default=None, union_mode='left_to_right')
    trend: str | Any = Field(default=None, union_mode='left_to_right')
    trend_difference: int | Any = Field(None, alias='trendDifference', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class StreamingChartInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rank: int | Any = Field(default=None, union_mode='left_to_right')
    trend: str | Any = Field(default=None, union_mode='left_to_right')
    trend_difference: int | Any = Field(None, alias='trendDifference', union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(None, alias='updatedAt', union_mode='left_to_right')
    days_in_top10: int | Any = Field(None, alias='daysInTop10', union_mode='left_to_right')
    days_in_top100: int | Any = Field(None, alias='daysInTop100', union_mode='left_to_right')
    days_in_top1000: int | Any = Field(None, alias='daysInTop1000', union_mode='left_to_right')
    days_in_top3: int | Any = Field(None, alias='daysInTop3', union_mode='left_to_right')
    top_rank: int | Any = Field(None, alias='topRank', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    streaming_chart_info: StreamingChartInfo | Any = Field(None, alias='streamingChartInfo', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class StreamingCharts(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class SimilarTitlesV2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sponsored_ad: Any | None = Field(None, alias='sponsoredAd')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class DateRange(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    start: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    icon_wide: str | Any = Field(None, alias='iconWide', union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    monetization_types: list[str] | Any = Field(None, alias='monetizationTypes', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class OffersHistoryItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    date_ranges: list[DateRange] | Any = Field(None, alias='dateRanges', union_mode='left_to_right')
    package: Package2 | Any = Field(default=None, union_mode='left_to_right')

class Package3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    icon_wide: str | Any = Field(None, alias='iconWide', union_mode='left_to_right')
    plan_offers: list[PlanOffer] | Any = Field(None, alias='planOffers', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    presentation_type: str | Any = Field(None, alias='presentationType', union_mode='left_to_right')
    monetization_type: str | Any = Field(None, alias='monetizationType', union_mode='left_to_right')
    new_element_count: int | Any = Field(None, alias='newElementCount', union_mode='left_to_right')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    currency: str | Any = Field(default=None, union_mode='left_to_right')
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    package: Package3 | Any = Field(default=None, union_mode='left_to_right')
    plans: list[Plan] | Any = Field(default=None, union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | Any = Field(None, alias='elementCount', union_mode='left_to_right')
    available_to: Any | None = Field(None, alias='availableTo')
    subtitle_languages: list[Any] | Any = Field(None, alias='subtitleLanguages', union_mode='left_to_right')
    video_technology: list[str] | Any = Field(None, alias='videoTechnology', union_mode='left_to_right')
    audio_technology: list[str] | Any = Field(None, alias='audioTechnology', union_mode='left_to_right')
    audio_languages: list[Any] | Any = Field(None, alias='audioLanguages', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class RankInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rank: int | Any = Field(default=None, union_mode='left_to_right')
    trend: str | Any = Field(default=None, union_mode='left_to_right')
    trend_difference: int | Any = Field(None, alias='trendDifference', union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(None, alias='updatedAt', union_mode='left_to_right')
    days_in_top10: int | Any = Field(None, alias='daysInTop10', union_mode='left_to_right')
    days_in_top100: int | Any = Field(None, alias='daysInTop100', union_mode='left_to_right')
    days_in_top1000: int | Any = Field(None, alias='daysInTop1000', union_mode='left_to_right')
    days_in_top3: int | Any = Field(None, alias='daysInTop3', union_mode='left_to_right')
    top_rank: int | Any = Field(None, alias='topRank', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    jw_entity_id: str | Any = Field(None, alias='jwEntityID', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    show_title: Any | None = Field(None, alias='showTitle')
    season_number: Any | None = Field(None, alias='seasonNumber')
    rank_info: RankInfo | Any = Field(None, alias='rankInfo', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Genre1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    translation: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Scoring1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_votes: int | float | Any = Field(None, alias='imdbVotes', union_mode='left_to_right')
    imdb_score: int | float | Any = Field(None, alias='imdbScore', union_mode='left_to_right')
    tomato_meter: int | Any = Field(None, alias='tomatoMeter', union_mode='left_to_right')
    certified_fresh: bool | Any = Field(None, alias='certifiedFresh', union_mode='left_to_right')
    jw_rating: float | Any = Field(None, alias='jwRating', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Interactions1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    votes_number: int | Any = Field(None, alias='votesNumber', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    genres: list[Genre1] | Any = Field(default=None, union_mode='left_to_right')
    backdrops: list[Backdrop] | Any = Field(default=None, union_mode='left_to_right')
    scoring: Scoring1 | Any = Field(default=None, union_mode='left_to_right')
    interactions: Interactions1 | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')

class SeenState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    progress: int | Any = Field(default=None, union_mode='left_to_right')
    seen_episode_count: int | Any = Field(None, alias='seenEpisodeCount', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Show(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    content: Content4 | Any = Field(default=None, union_mode='left_to_right')

class Node1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    content: Content3 | Any = Field(default=None, union_mode='left_to_right')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    seen_state: SeenState | Any = Field(None, alias='seenState', union_mode='left_to_right')
    show: Show | Any = Field(default=None, union_mode='left_to_right')

class Titles1Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node: Node1 | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    titles: list[Title] | Any = Field(None, alias='Titles', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    titles_1: list[Titles1Item] | Any = Field(None, alias='titles', union_mode='left_to_right')

class Template(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    anchor: str | Any = Field(default=None, union_mode='left_to_right')
    content_type: str | Any = Field(None, alias='contentType', union_mode='left_to_right')
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class TitleModules(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content2 | Any = Field(default=None, union_mode='left_to_right')
    fomo_score: int | Any = Field(None, alias='fomoScore', union_mode='left_to_right')
    template: Template | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')
    is_released: bool | Any = Field(None, alias='isReleased', union_mode='left_to_right')
    original_release_year: int | Any = Field(None, alias='originalReleaseYear', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Show1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    content: Content6 | Any = Field(default=None, union_mode='left_to_right')

class FallBackClips1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    clips: list[Clip] | Any = Field(default=None, union_mode='left_to_right')
    videobuster_clips: list[Any] | Any = Field(None, alias='videobusterClips', union_mode='left_to_right')
    dailymotion_clips: list[DailymotionClip] | Any = Field(None, alias='dailymotionClips', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    total_episode_count: int | Any = Field(None, alias='totalEpisodeCount', union_mode='left_to_right')
    available_to: list[Any] | Any = Field(None, alias='availableTo', union_mode='left_to_right')
    offers: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    content: Content5 | Any = Field(default=None, union_mode='left_to_right')
    show: Show1 | Any = Field(default=None, union_mode='left_to_right')
    fall_back_clips: FallBackClips1 | Any = Field(None, alias='fallBackClips', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    episode_number: int | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    is_released: bool | Any = Field(None, alias='isReleased', union_mode='left_to_right')
    runtime: int | Any = Field(default=None, union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')

class RecentEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    unique_offer_count: int | Any = Field(None, alias='uniqueOfferCount', union_mode='left_to_right')
    flatrate: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    free: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    fast: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    content: Content7 | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    justwatch_tv_offers: list[Any] | Any = Field(None, alias='justwatchTVOffers', union_mode='left_to_right')
    disney_offers_count: int | Any = Field(None, alias='disneyOffersCount', union_mode='left_to_right')
    star_offers_count: int | Any = Field(None, alias='starOffersCount', union_mode='left_to_right')
    unique_offer_count: int | Any = Field(None, alias='uniqueOfferCount', union_mode='left_to_right')
    offers: list[Offer] | Any = Field(default=None, union_mode='left_to_right')
    watch_now_offer: WatchNowOffer | Any = Field(None, alias='watchNowOffer', union_mode='left_to_right')
    available_to: list[Any] | Any = Field(None, alias='availableTo', union_mode='left_to_right')
    fall_back_clips: FallBackClips | Any = Field(None, alias='fallBackClips', union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    recommended_by_count: int | Any = Field(None, alias='recommendedByCount', union_mode='left_to_right')
    watched_by_count: int | Any = Field(None, alias='watchedByCount', union_mode='left_to_right')
    popularity_rank: PopularityRank | Any = Field(None, alias='popularityRank', union_mode='left_to_right')
    streaming_charts: StreamingCharts | Any = Field(None, alias='streamingCharts', union_mode='left_to_right')
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    customlist_entries: list[Any] | Any = Field(None, alias='customlistEntries', union_mode='left_to_right')
    similar_titles_v2: SimilarTitlesV2 | Any = Field(None, alias='similarTitlesV2', union_mode='left_to_right')
    permanent_audiences: list[str] | Any = Field(None, alias='permanentAudiences', union_mode='left_to_right')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    offer_count: int | Any = Field(None, alias='offerCount', union_mode='left_to_right')
    max_offer_updated_at: AwareDatetime | Any = Field(None, alias='maxOfferUpdatedAt', union_mode='left_to_right')
    offers_history: list[OffersHistoryItem] | Any = Field(None, alias='offersHistory', union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    free: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    fast: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    bundles: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    promoted_bundles: list[Any] | Any = Field(None, alias='promotedBundles', union_mode='left_to_right')
    promoted_offers: list[Any] | Any = Field(None, alias='promotedOffers', union_mode='left_to_right')
    title_modules: list[TitleModules] | Any = Field(None, alias='titleModules', union_mode='left_to_right')
    total_season_count: int | Any = Field(None, alias='totalSeasonCount', union_mode='left_to_right')
    seen_state: SeenState | Any = Field(None, alias='seenState', union_mode='left_to_right')
    tv_show_tracking_entry: Any | None = Field(None, alias='tvShowTrackingEntry')
    seasons: list[Season] | Any = Field(default=None, union_mode='left_to_right')
    recent_episodes: list[RecentEpisode] | Any = Field(None, alias='recentEpisodes', union_mode='left_to_right')

class UrlTitleDetailsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    meta_description: str | Any = Field(None, alias='metaDescription', union_mode='left_to_right')
    meta_keywords: str | Any = Field(None, alias='metaKeywords', union_mode='left_to_right')
    meta_robots: str | Any = Field(None, alias='metaRobots', union_mode='left_to_right')
    meta_title: str | Any = Field(None, alias='metaTitle', union_mode='left_to_right')
    heading1: str | Any = Field(default=None, union_mode='left_to_right')
    heading2: str | Any = Field(default=None, union_mode='left_to_right')
    html_content: str | Any = Field(None, alias='htmlContent', union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
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
