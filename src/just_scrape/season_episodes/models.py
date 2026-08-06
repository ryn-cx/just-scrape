from pydantic import ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from typing import Any

class Package(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    clear_name: str = Field(..., alias='clearName')
    package_id: int = Field(..., alias='packageId')
    field__typename: str = Field(..., alias='__typename')

class FlatrateItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    package: Package
    field__typename: str = Field(..., alias='__typename')

class BuyItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    package: Package
    field__typename: str = Field(..., alias='__typename')

class FastItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    package: Package
    field__typename: str = Field(..., alias='__typename')

class Content(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field__typename: str = Field(..., alias='__typename')
    title: str
    short_description: str = Field(..., alias='shortDescription')
    episode_number: int = Field(..., alias='episodeNumber')
    season_number: int = Field(..., alias='seasonNumber')
    is_released: bool = Field(..., alias='isReleased')
    runtime: int
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')

class Episode(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    seenlist_entry: None = Field(..., alias='seenlistEntry')
    unique_offer_count: int = Field(..., alias='uniqueOfferCount')
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[None]
    free: list[None]
    fast: list[FastItem]
    content: Content
    field__typename: str = Field(..., alias='__typename')

class Node(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    field__typename: str = Field(..., alias='__typename')
    episodes: list[Episode]

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    node: Node

class SeasonEpisodesResponse(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data
