from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package: Package | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class BuyItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package: Package | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    episode_number: int | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    is_released: bool | Any = Field(None, alias='isReleased', union_mode='left_to_right')
    runtime: int | Any = Field(default=None, union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    unique_offer_count: int | Any = Field(None, alias='uniqueOfferCount', union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    free: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    fast: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class SeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    episodes: list[Episode] | Any = Field(default=None, union_mode='left_to_right')
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
