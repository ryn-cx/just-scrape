# ruff: noqa: TC003, D100, D101, D102
from __future__ import annotations

from datetime import date

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_serializer


class Package(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    clear_name: str = Field(..., alias="clearName")
    package_id: int = Field(..., alias="packageId")
    field__typename: str = Field(..., alias="__typename")


class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package
    field__typename: str = Field(..., alias="__typename")


class BuyItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package
    field__typename: str = Field(..., alias="__typename")


class FreeItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package
    field__typename: str = Field(..., alias="__typename")


class Package3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    short_name: str = Field(..., alias="shortName")
    clear_name: str = Field(..., alias="clearName")
    monetization_types: list[str] = Field(..., alias="monetizationTypes")
    icon: str
    icon_wide: str = Field(..., alias="iconWide")
    has_rectangular_icon: bool = Field(..., alias="hasRectangularIcon")
    plan_offers: list[None] = Field(..., alias="planOffers")
    field__typename: str = Field(..., alias="__typename")


class UpcomingRelease(BaseModel):
    model_config = ConfigDict(extra="forbid")
    release_count_down: int = Field(..., alias="releaseCountDown")
    release_date: date = Field(..., alias="releaseDate")
    release_type: str = Field(..., alias="releaseType")
    label: str
    package: Package3
    field__typename: str = Field(..., alias="__typename")


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    title: str
    short_description: str = Field(..., alias="shortDescription")
    episode_number: int = Field(..., alias="episodeNumber")
    season_number: int = Field(..., alias="seasonNumber")
    is_released: bool = Field(..., alias="isReleased")
    runtime: int
    original_release_date: date = Field(..., alias="originalReleaseDate")
    upcoming_releases: list[UpcomingRelease] = Field(..., alias="upcomingReleases")


class Episode(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    seenlist_entry: None = Field(..., alias="seenlistEntry")
    unique_offer_count: int = Field(..., alias="uniqueOfferCount")
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[None]
    free: list[FreeItem]
    fast: list[None]
    content: Content
    field__typename: str = Field(..., alias="__typename")
    max_offer_updated_at: AwareDatetime = Field(..., alias="maxOfferUpdatedAt")

    @field_serializer("max_offer_updated_at")
    def serialize_max_offer_updated_at(self, value: AwareDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S.%f").rstrip("0").rstrip(".") + "Z"


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    field__typename: str = Field(..., alias="__typename")
    episodes: list[Episode]


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    node: Node


class Variables(BaseModel):
    model_config = ConfigDict(extra="forbid")
    platform: str
    country: str
    language: str
    limit: int
    node_id: str = Field(..., alias="nodeId")
    offset: int


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


class CustomSeasonEpisodesResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
