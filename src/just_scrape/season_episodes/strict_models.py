from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from typing import Any

class Package(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    clear_name: str = Field(..., alias='clearName')
    package_id: int = Field(..., alias='packageId')
    field__typename: str = Field(..., alias='__typename')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    package: Package
    field__typename: str = Field(..., alias='__typename')

class BuyItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    package: Package
    field__typename: str = Field(..., alias='__typename')

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    title: str
    short_description: str = Field(..., alias='shortDescription')
    episode_number: int = Field(..., alias='episodeNumber')
    season_number: int = Field(..., alias='seasonNumber')
    is_released: bool = Field(..., alias='isReleased')
    runtime: int
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    seenlist_entry: None = Field(..., alias='seenlistEntry')
    unique_offer_count: int = Field(..., alias='uniqueOfferCount')
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[None]
    free: list[None]
    fast: list[None]
    content: Content
    field__typename: str = Field(..., alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    field__typename: str = Field(..., alias='__typename')
    episodes: list[Episode]

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node: Node

class SeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
