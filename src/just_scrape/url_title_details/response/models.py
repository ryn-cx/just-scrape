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
    retail_price_value: int | float = Field(..., alias="retailPriceValue")
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
    retail_price_value: int | float = Field(..., alias="retailPriceValue")
    children: list[None]
    field__typename: str = Field(..., alias="__typename")


class Offer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    new_element_count: int = Field(..., alias="newElementCount")
    retail_price: str | None = Field(..., alias="retailPrice")
    retail_price_value: float | None = Field(..., alias="retailPriceValue")
    currency: str
    last_change_retail_price_value: float | None = Field(
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
    available_to: date | None = Field(..., alias="availableTo")
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


class Package2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    short_name: str = Field(..., alias="shortName")
    field__typename: str = Field(..., alias="__typename")


class AvailableToItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    available_count_down: int = Field(..., alias="availableCountDown")
    available_to_date: date = Field(..., alias="availableToDate")
    package: Package2
    field__typename: str = Field(..., alias="__typename")


class Clip(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source_url: str = Field(..., alias="sourceUrl")
    external_id: str = Field(..., alias="externalId")
    provider: str
    name: str
    field__typename: str = Field(..., alias="__typename")


class VideobusterClip(BaseModel):
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
    videobuster_clips: list[VideobusterClip] = Field(..., alias="videobusterClips")
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
    wikidata_id: str | None = Field(..., alias="wikidataId")
    field__typename: str = Field(..., alias="__typename")


class Scoring(BaseModel):
    model_config = ConfigDict(extra="forbid")
    imdb_score: float = Field(..., alias="imdbScore")
    imdb_votes: int = Field(..., alias="imdbVotes")
    tmdb_popularity: float = Field(..., alias="tmdbPopularity")
    tmdb_score: float = Field(..., alias="tmdbScore")
    jw_rating: float = Field(..., alias="jwRating")
    tomato_meter: int = Field(..., alias="tomatoMeter")
    certified_fresh: bool | None = Field(..., alias="certifiedFresh")
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
    url: Url | None


class Subgenre(BaseModel):
    model_config = ConfigDict(extra="forbid")
    content: Content1
    field__typename: str = Field(..., alias="__typename")


class WatchedOn(BaseModel):
    model_config = ConfigDict(extra="forbid")
    clear_name: str = Field(..., alias="clearName")
    id: str
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    package_id: int = Field(..., alias="packageId")
    selected: bool
    monetization_types: list[str] = Field(..., alias="monetizationTypes")
    icon: str
    addon_parent: None = Field(..., alias="addonParent")
    field__typename: str = Field(..., alias="__typename")


class Profile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    display_name: str = Field(..., alias="displayName")
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    location: str
    country: str
    bio: str
    avatar_url: str = Field(..., alias="avatarUrl")
    is_complete: bool = Field(..., alias="isComplete")
    external_urls: None = Field(..., alias="externalUrls")
    owned_by_user: bool = Field(..., alias="ownedByUser")
    profile_url: str = Field(..., alias="profileUrl")
    profile_type: str = Field(..., alias="profileType")
    content_person_id: None = Field(..., alias="contentPersonId")
    text_recommendations_count: int = Field(..., alias="textRecommendationsCount")


class TextRecommendation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    headline: str
    body: str
    body_html: str = Field(..., alias="bodyHTML")
    original_headline: None = Field(..., alias="originalHeadline")
    original_body: None = Field(..., alias="originalBody")
    original_body_html: None = Field(..., alias="originalBodyHTML")
    watch_if: list[None] = Field(..., alias="watchIf")
    skip_if: list[None] = Field(..., alias="skipIf")
    custom_profile_type: None = Field(..., alias="customProfileType")
    tags: list[None]
    watched_at: date = Field(..., alias="watchedAt")
    watched_on: WatchedOn = Field(..., alias="watchedOn")
    like_count: int = Field(..., alias="likeCount")
    liked_by_user: bool = Field(..., alias="likedByUser")
    owned_by_user: bool = Field(..., alias="ownedByUser")
    profile: Profile
    updated_at: date = Field(..., alias="updatedAt")
    video: None


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


class Tag(BaseModel):
    model_config = ConfigDict(extra="forbid")
    technical_name: str = Field(..., alias="technicalName")
    translated_name: str = Field(..., alias="translatedName")
    field__typename: str = Field(..., alias="__typename")


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    backdrops: list[Backdrop]
    full_backdrops: list[FullBackdrop] = Field(..., alias="fullBackdrops")
    clips: list[Clip]
    videobuster_clips: list[VideobusterClip] = Field(..., alias="videobusterClips")
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
    text_recommendations: list[TextRecommendation] | None = Field(
        ..., alias="textRecommendations"
    )
    field__typename: str = Field(..., alias="__typename")
    original_title: str = Field(..., alias="originalTitle")
    age_certification: str = Field(..., alias="ageCertification")
    credits: list[Credit]
    interactions: Interactions
    production_countries: list[str] = Field(..., alias="productionCountries")
    tags: list[Tag]


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
        if not value:
            return None
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


class Package3(BaseModel):
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
    package: Package3
    plans: list[Plan]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: date | None = Field(..., alias="availableTo")
    subtitle_languages: list[str] = Field(..., alias="subtitleLanguages")
    video_technology: list[str] = Field(..., alias="videoTechnology")
    audio_technology: list[str] = Field(..., alias="audioTechnology")
    audio_languages: list[str] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")


class Package4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon: str
    icon_wide: str = Field(..., alias="iconWide")
    plan_offers: list[None] = Field(..., alias="planOffers")
    field__typename: str = Field(..., alias="__typename")


class BuyItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    new_element_count: int = Field(..., alias="newElementCount")
    retail_price: str = Field(..., alias="retailPrice")
    retail_price_value: float = Field(..., alias="retailPriceValue")
    currency: str
    last_change_retail_price_value: float | None = Field(
        ..., alias="lastChangeRetailPriceValue"
    )
    type: str
    country: str
    package: Package4
    plans: list[None]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: None = Field(..., alias="availableTo")
    subtitle_languages: list[None] = Field(..., alias="subtitleLanguages")
    video_technology: list[None] = Field(..., alias="videoTechnology")
    audio_technology: list[None] = Field(..., alias="audioTechnology")
    audio_languages: list[str] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")
    offer_seasons: list[str] = Field(..., alias="offerSeasons")
    min_retail_price: str | None = Field(..., alias="minRetailPrice")


class FastItem(BaseModel):
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
    package: Package4
    plans: list[None]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: None = Field(..., alias="availableTo")
    subtitle_languages: list[None] = Field(..., alias="subtitleLanguages")
    video_technology: list[None] = Field(..., alias="videoTechnology")
    audio_technology: list[None] = Field(..., alias="audioTechnology")
    audio_languages: list[None] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")
    available_from_time: AwareDatetime = Field(..., alias="availableFromTime")
    available_to_time: None = Field(..., alias="availableToTime")

    @field_serializer("available_from_time")
    def serialize_available_from_time(self, value: AwareDatetime) -> str:
        if not value:
            return None
        return value.strftime("%Y-%m-%dT%H:%M:%S.%f").rstrip("0").rstrip(".") + "Z"

    @field_serializer("available_to_time")
    def serialize_available_to_time(self, value: AwareDatetime) -> str:
        if not value:
            return None
        return value.strftime("%Y-%m-%dT%H:%M:%S.%f").rstrip("0").rstrip(".") + "Z"


class PlanOffer2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float = Field(..., alias="retailPriceValue")
    children: list[None]
    field__typename: str = Field(..., alias="__typename")


class Package6(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon: str
    icon_wide: str = Field(..., alias="iconWide")
    plan_offers: list[PlanOffer2] = Field(..., alias="planOffers")
    field__typename: str = Field(..., alias="__typename")


class Plan2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float = Field(..., alias="retailPriceValue")
    children: list[None]
    field__typename: str = Field(..., alias="__typename")


class PromotedOffer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    new_element_count: int = Field(..., alias="newElementCount")
    retail_price: str | None = Field(..., alias="retailPrice")
    retail_price_value: float | None = Field(..., alias="retailPriceValue")
    currency: str
    last_change_retail_price_value: float | None = Field(
        ..., alias="lastChangeRetailPriceValue"
    )
    type: str
    country: str
    package: Package6
    plans: list[Plan2]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: None = Field(..., alias="availableTo")
    subtitle_languages: list[None] = Field(..., alias="subtitleLanguages")
    video_technology: list[None] = Field(..., alias="videoTechnology")
    audio_technology: list[None] = Field(..., alias="audioTechnology")
    audio_languages: list[None] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")
    min_retail_price: None = Field(..., alias="minRetailPrice")


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
        if not value:
            return None
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
    season_number: int | None = Field(None, alias="seasonNumber")


class SeenState(BaseModel):
    model_config = ConfigDict(extra="forbid")
    progress: int
    seen_episode_count: int = Field(..., alias="seenEpisodeCount")
    field__typename: str = Field(..., alias="__typename")


class Content4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    field__typename: str = Field(..., alias="__typename")


class Show(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    field__typename: str = Field(..., alias="__typename")
    content: Content4


class Node1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    content: Content3
    watchlist_entry_v2: None = Field(None, alias="watchlistEntryV2")
    likelist_entry: None = Field(None, alias="likelistEntry")
    dislikelist_entry: None = Field(None, alias="dislikelistEntry")
    field__typename: str = Field(..., alias="__typename")
    seenlist_entry: None = Field(None, alias="seenlistEntry")
    seen_state: SeenState | None = Field(None, alias="seenState")
    show: Show | None = None


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


class TitleModules(BaseModel):
    model_config = ConfigDict(extra="forbid")
    content: Content2
    fomo_score: int = Field(..., alias="fomoScore")
    template: Template
    field__typename: str = Field(..., alias="__typename")


class Package7(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    short_name: str = Field(..., alias="shortName")
    field__typename: str = Field(..., alias="__typename")


class AvailableToItem1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    available_to_date: date = Field(..., alias="availableToDate")
    available_count_down: int = Field(..., alias="availableCountDown")
    package: Package7
    field__typename: str = Field(..., alias="__typename")


class Package8(BaseModel):
    model_config = ConfigDict(extra="forbid")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    field__typename: str = Field(..., alias="__typename")


class Offer1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    package: Package8
    monetization_type: str = Field(..., alias="monetizationType")
    retail_price: str | None = Field(..., alias="retailPrice")
    retail_price_value: int | float | None = Field(..., alias="retailPriceValue")
    field__typename: str = Field(..., alias="__typename")


class Content5(BaseModel):
    model_config = ConfigDict(extra="forbid")
    poster_url: str = Field(..., alias="posterUrl")
    season_number: int = Field(..., alias="seasonNumber")
    full_path: str = Field(..., alias="fullPath")
    title: str
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")
    is_released: bool = Field(..., alias="isReleased")
    original_release_year: int = Field(..., alias="originalReleaseYear")
    field__typename: str = Field(..., alias="__typename")


class Content6(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    field__typename: str = Field(..., alias="__typename")


class Show1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    watchlist_entry_v2: None = Field(..., alias="watchlistEntryV2")
    content: Content6


class FallBackClips1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    clips: list[Clip]
    videobuster_clips: list[VideobusterClip] = Field(..., alias="videobusterClips")
    dailymotion_clips: list[DailymotionClip] = Field(..., alias="dailymotionClips")
    field__typename: str = Field(..., alias="__typename")


class Season(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    total_episode_count: int = Field(..., alias="totalEpisodeCount")
    available_to: list[AvailableToItem1] = Field(..., alias="availableTo")
    offers: list[Offer1]
    content: Content5
    show: Show1
    fall_back_clips: FallBackClips1 = Field(..., alias="fallBackClips")
    field__typename: str = Field(..., alias="__typename")


class Package9(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    clear_name: str = Field(..., alias="clearName")
    package_id: int = Field(..., alias="packageId")
    field__typename: str = Field(..., alias="__typename")


class FlatrateItem1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package9
    field__typename: str = Field(..., alias="__typename")


class BuyItem1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package9
    field__typename: str = Field(..., alias="__typename")


class Content7(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    title: str
    short_description: str = Field(..., alias="shortDescription")
    episode_number: int = Field(..., alias="episodeNumber")
    season_number: int = Field(..., alias="seasonNumber")
    is_released: bool = Field(..., alias="isReleased")
    runtime: int
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")


class RecentEpisode(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    seenlist_entry: None = Field(..., alias="seenlistEntry")
    unique_offer_count: int = Field(..., alias="uniqueOfferCount")
    flatrate: list[FlatrateItem1]
    buy: list[BuyItem1]
    rent: list[None]
    free: list[None]
    fast: list[None]
    content: Content7
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
    available_to: list[AvailableToItem] = Field(..., alias="availableTo")
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
    seenlist_entry: None = Field(None, alias="seenlistEntry")
    offer_count: int = Field(..., alias="offerCount")
    max_offer_updated_at: AwareDatetime = Field(..., alias="maxOfferUpdatedAt")
    offers_history: list[None] = Field(..., alias="offersHistory")
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[None]
    free: list[None]
    fast: list[FastItem]
    bundles: list[None]
    promoted_bundles: list[None] = Field(..., alias="promotedBundles")
    promoted_offers: list[PromotedOffer] = Field(..., alias="promotedOffers")
    title_modules: list[TitleModules | None] = Field(..., alias="titleModules")
    total_season_count: int | None = Field(None, alias="totalSeasonCount")
    seen_state: SeenState | None = Field(None, alias="seenState")
    tv_show_tracking_entry: None = Field(None, alias="tvShowTrackingEntry")
    seasons: list[Season] | None = None
    recent_episodes: list[RecentEpisode] | None = Field(None, alias="recentEpisodes")

    @field_serializer("max_offer_updated_at")
    def serialize_max_offer_updated_at(self, value: AwareDatetime) -> str:
        if not value:
            return None
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
    operation_name: str = Field(..., alias="operationName")
    headers: Headers
    timestamp: AwareDatetime


class UrlTitleDetailsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
