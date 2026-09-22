from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from datetime import date as date_aliased

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_cursor: str | None = Field(None, alias='startCursor')
    end_cursor: str | None = Field(None, alias='endCursor')
    has_previous_page: bool | None = Field(None, alias='hasPreviousPage')
    has_next_page: bool | None = Field(None, alias='hasNextPage')
    field__typename: str | None = Field(None, alias='__typename')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    package_id: int | None = Field(None, alias='packageId')
    short_name: str | None = Field(None, alias='shortName')
    icon: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Key(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    date: date_aliased | None = None
    package: Package | None = None

class PageInfo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_cursor: str | None = Field(None, alias='startCursor')
    end_cursor: str | None = Field(None, alias='endCursor')
    has_next_page: bool | None = Field(None, alias='hasNextPage')
    has_previous_page: bool | None = Field(None, alias='hasPreviousPage')
    field__typename: str | None = Field(None, alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_count: int | None = Field(None, alias='totalCount')
    page_info: PageInfo1 | None = Field(None, alias='pageInfo')
    field__typename: str | None = Field(None, alias='__typename')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: Key | None = None
    node: Node | None = None
    field__typename: str | None = Field(None, alias='__typename')

class NewTitleBucketsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_info: PageInfo | None = Field(None, alias='pageInfo')
    edges: list[Edge] | None = None
    field__typename: str | None = Field(None, alias='__typename')
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
