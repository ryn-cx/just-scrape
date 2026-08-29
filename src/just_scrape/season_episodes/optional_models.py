from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    clear_name: str | None = Field(None, alias='clearName')
    package_id: int | None = Field(None, alias='packageId')
    field__typename: str | None = Field(None, alias='__typename')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    package: Package | None = None
    field__typename: str | None = Field(None, alias='__typename')

class BuyItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    package: Package | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    title: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    episode_number: int | None = Field(None, alias='episodeNumber')
    season_number: int | None = Field(None, alias='seasonNumber')
    is_released: bool | None = Field(None, alias='isReleased')
    runtime: int | None = None
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    unique_offer_count: int | None = Field(None, alias='uniqueOfferCount')
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[Any] | None = None
    free: list[Any] | None = None
    fast: list[Any] | None = None
    content: Content | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    field__typename: str | None = Field(None, alias='__typename')
    episodes: list[Episode] | None = None

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node: Node | None = None

class SeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: Data | None = None
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
