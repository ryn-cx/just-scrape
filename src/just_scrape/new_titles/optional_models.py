from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any
from datetime import date

class Package(BaseModel):
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

class NewOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    package: Package | Any = Field(default=None, union_mode='left_to_right')
    retail_price: str | Any = Field(None, alias='retailPrice', union_mode='left_to_right')
    retail_price_value: float | Any = Field(None, alias='retailPriceValue', union_mode='left_to_right')
    last_change_retail_price_value: float | Any = Field(None, alias='lastChangeRetailPriceValue', union_mode='left_to_right')
    currency: str | Any = Field(default=None, union_mode='left_to_right')
    presentation_type: str | Any = Field(None, alias='presentationType', union_mode='left_to_right')
    monetization_type: str | Any = Field(None, alias='monetizationType', union_mode='left_to_right')
    available_to: date | Any = Field(None, alias='availableTo', union_mode='left_to_right')
    date_created: date | Any = Field(None, alias='dateCreated', union_mode='left_to_right')
    new_element_count: int | Any = Field(None, alias='newElementCount', union_mode='left_to_right')
    last_change_retail_price: str | Any = Field(None, alias='lastChangeRetailPrice', union_mode='left_to_right')
    last_change_percent: int | float | Any = Field(None, alias='lastChangePercent', union_mode='left_to_right')

class Scoring(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_votes: int | Any = Field(None, alias='imdbVotes', union_mode='left_to_right')
    imdb_score: int | float | Any = Field(None, alias='imdbScore', union_mode='left_to_right')
    tmdb_popularity: float | Any = Field(None, alias='tmdbPopularity', union_mode='left_to_right')
    tmdb_score: int | float | Any = Field(None, alias='tmdbScore', union_mode='left_to_right')
    tomato_meter: int | Any = Field(None, alias='tomatoMeter', union_mode='left_to_right')
    certified_fresh: bool | Any = Field(None, alias='certifiedFresh', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    translation: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    scoring: Scoring | Any = Field(default=None, union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    runtime: int | Any = Field(default=None, union_mode='left_to_right')
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')
    is_released: bool | Any = Field(None, alias='isReleased', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')

class Scoring1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_votes: int | Any = Field(None, alias='imdbVotes', union_mode='left_to_right')
    imdb_score: int | float | Any = Field(None, alias='imdbScore', union_mode='left_to_right')
    tmdb_popularity: float | Any = Field(None, alias='tmdbPopularity', union_mode='left_to_right')
    tmdb_score: int | float | Any = Field(None, alias='tmdbScore', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    scoring: Scoring1 | Any = Field(default=None, union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    runtime: int | Any = Field(default=None, union_mode='left_to_right')
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class SeenState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    progress: int | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Show(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    content: Content1 | Any = Field(default=None, union_mode='left_to_right')
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    seen_state: SeenState | Any = Field(None, alias='seenState', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    show: Show | Any = Field(default=None, union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    new_offer: NewOffer | Any = Field(None, alias='newOffer', union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')
    has_previous_page: bool | Any = Field(None, alias='hasPreviousPage', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class NewTitlesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
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
