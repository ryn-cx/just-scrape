from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any
from datetime import date

class Package(BaseModel):
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

class NewOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    package: Package | None = None
    retail_price: str | None = Field(None, alias='retailPrice')
    retail_price_value: float | None = Field(None, alias='retailPriceValue')
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    currency: str | None = None
    presentation_type: str | None = Field(None, alias='presentationType')
    monetization_type: str | None = Field(None, alias='monetizationType')
    available_to: Any | date | None = Field(None, alias='availableTo')
    date_created: date | None = Field(None, alias='dateCreated')
    new_element_count: int | None = Field(None, alias='newElementCount')
    last_change_retail_price: Any | None = Field(None, alias='lastChangeRetailPrice')
    last_change_percent: int | None = Field(None, alias='lastChangePercent')

class Scoring(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_votes: int | None = Field(None, alias='imdbVotes')
    imdb_score: int | float | None = Field(None, alias='imdbScore')
    tmdb_popularity: float | None = Field(None, alias='tmdbPopularity')
    tmdb_score: float | None = Field(None, alias='tmdbScore')
    tomato_meter: int | None = Field(None, alias='tomatoMeter')
    certified_fresh: Any | None = Field(None, alias='certifiedFresh')
    field__typename: str | None = Field(None, alias='__typename')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    translation: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    full_path: str | None = Field(None, alias='fullPath')
    scoring: Scoring | None = None
    poster_url: str | None = Field(None, alias='posterUrl')
    runtime: int | None = None
    genres: list[Genre] | None = None
    is_released: bool | None = Field(None, alias='isReleased')
    field__typename: str | None = Field(None, alias='__typename')
    season_number: int | None = Field(None, alias='seasonNumber')

class Scoring1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_votes: int | None = Field(None, alias='imdbVotes')
    imdb_score: float | None = Field(None, alias='imdbScore')
    tmdb_popularity: float | None = Field(None, alias='tmdbPopularity')
    tmdb_score: float | None = Field(None, alias='tmdbScore')
    field__typename: str | None = Field(None, alias='__typename')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    short_description: str | None = Field(None, alias='shortDescription')
    full_path: str | None = Field(None, alias='fullPath')
    scoring: Scoring1 | None = None
    poster_url: str | None = Field(None, alias='posterUrl')
    runtime: int | None = None
    genres: list[Genre] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class SeenState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    progress: int | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Show(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    content: Content1 | None = None
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    seen_state: SeenState | None = Field(None, alias='seenState')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    content: Content | None = None
    likelist_entry: Any | None = Field(None, alias='likelistEntry')
    dislikelist_entry: Any | None = Field(None, alias='dislikelistEntry')
    seenlist_entry: Any | None = Field(None, alias='seenlistEntry')
    watchlist_entry_v2: Any | None = Field(None, alias='watchlistEntryV2')
    show: Show | None = None

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cursor: str | None = None
    new_offer: NewOffer | None = Field(None, alias='newOffer')
    node: Node | None = None
    field__typename: str | None = Field(None, alias='__typename')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_cursor: str | None = Field(None, alias='endCursor')
    has_previous_page: bool | None = Field(None, alias='hasPreviousPage')
    has_next_page: bool | None = Field(None, alias='hasNextPage')
    field__typename: str | None = Field(None, alias='__typename')

class NewTitles(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_count: int | None = Field(None, alias='totalCount')
    edges: list[Edge] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
    field__typename: str | None = Field(None, alias='__typename')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    new_titles: NewTitles | None = Field(None, alias='newTitles')

class NewTitlesModel(BaseModel):
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
