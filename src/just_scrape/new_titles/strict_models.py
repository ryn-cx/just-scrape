from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from datetime import date

class Package(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    icon: str
    package_id: int = Field(..., alias='packageId')
    clear_name: str = Field(..., alias='clearName')
    short_name: str = Field(..., alias='shortName')
    technical_name: str = Field(..., alias='technicalName')
    icon_wide: str = Field(..., alias='iconWide')
    has_rectangular_icon: bool = Field(..., alias='hasRectangularIcon')
    field__typename: str = Field(..., alias='__typename')

class NewOffer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    id: str
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    stream_url: None = Field(..., alias='streamUrl')
    stream_url_external_player: None = Field(..., alias='streamUrlExternalPlayer')
    package: Package
    retail_price: str | None = Field(..., alias='retailPrice')
    retail_price_value: float | None = Field(..., alias='retailPriceValue')
    last_change_retail_price_value: float | None = Field(..., alias='lastChangeRetailPriceValue')
    currency: str
    presentation_type: str = Field(..., alias='presentationType')
    monetization_type: str = Field(..., alias='monetizationType')
    available_to: date | None = Field(..., alias='availableTo')
    date_created: date = Field(..., alias='dateCreated')
    new_element_count: int = Field(..., alias='newElementCount')
    last_change_retail_price: str | None = Field(..., alias='lastChangeRetailPrice')
    last_change_percent: int | float = Field(..., alias='lastChangePercent')

class Scoring(BaseModel):
    model_config = ConfigDict(defer_build=True)
    imdb_votes: int = Field(..., alias='imdbVotes')
    imdb_score: int | float = Field(..., alias='imdbScore')
    tmdb_popularity: float = Field(..., alias='tmdbPopularity')
    tmdb_score: float = Field(..., alias='tmdbScore')
    tomato_meter: int | None = Field(..., alias='tomatoMeter')
    certified_fresh: bool | None = Field(..., alias='certifiedFresh')
    field__typename: str = Field(..., alias='__typename')

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    translation: str
    field__typename: str = Field(..., alias='__typename')

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    short_description: str = Field(..., alias='shortDescription')
    full_path: str = Field(..., alias='fullPath')
    scoring: Scoring
    poster_url: str = Field(..., alias='posterUrl')
    runtime: int
    genres: list[Genre]
    is_released: bool = Field(..., alias='isReleased')
    field__typename: str = Field(..., alias='__typename')
    season_number: int | None = Field(None, alias='seasonNumber')

class Scoring1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    imdb_votes: int = Field(..., alias='imdbVotes')
    imdb_score: float = Field(..., alias='imdbScore')
    tmdb_popularity: float = Field(..., alias='tmdbPopularity')
    tmdb_score: float = Field(..., alias='tmdbScore')
    field__typename: str = Field(..., alias='__typename')

class Content1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    short_description: str = Field(..., alias='shortDescription')
    full_path: str = Field(..., alias='fullPath')
    scoring: Scoring1
    poster_url: str = Field(..., alias='posterUrl')
    runtime: int
    genres: list[Genre]
    field__typename: str = Field(..., alias='__typename')

class SeenState(BaseModel):
    model_config = ConfigDict(defer_build=True)
    progress: int
    field__typename: str = Field(..., alias='__typename')

class Show(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    content: Content1
    likelist_entry: None = Field(..., alias='likelistEntry')
    dislikelist_entry: None = Field(..., alias='dislikelistEntry')
    watchlist_entry_v2: None = Field(..., alias='watchlistEntryV2')
    seen_state: SeenState = Field(..., alias='seenState')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    content: Content
    likelist_entry: None = Field(..., alias='likelistEntry')
    dislikelist_entry: None = Field(..., alias='dislikelistEntry')
    seenlist_entry: None = Field(None, alias='seenlistEntry')
    watchlist_entry_v2: None = Field(None, alias='watchlistEntryV2')
    show: Show | None = None

class Edge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cursor: str
    new_offer: NewOffer = Field(..., alias='newOffer')
    node: Node
    field__typename: str = Field(..., alias='__typename')

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_cursor: str = Field(..., alias='endCursor')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    has_next_page: bool = Field(..., alias='hasNextPage')
    field__typename: str = Field(..., alias='__typename')

class NewTitlesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total_count: int = Field(..., alias='totalCount')
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')
    field__typename: str = Field(..., alias='__typename')
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
