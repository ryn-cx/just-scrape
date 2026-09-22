from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from datetime import date as date_aliased

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_cursor: str = Field(..., alias='startCursor')
    end_cursor: str = Field(..., alias='endCursor')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    has_next_page: bool = Field(..., alias='hasNextPage')
    field__typename: str = Field(..., alias='__typename')

class Package(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    package_id: int = Field(..., alias='packageId')
    short_name: str = Field(..., alias='shortName')
    icon: str
    field__typename: str = Field(..., alias='__typename')

class Key(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    date: date_aliased
    package: Package

class PageInfo1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_cursor: str = Field(..., alias='startCursor')
    end_cursor: str = Field(..., alias='endCursor')
    has_next_page: bool = Field(..., alias='hasNextPage')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    field__typename: str = Field(..., alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total_count: int = Field(..., alias='totalCount')
    page_info: PageInfo1 = Field(..., alias='pageInfo')
    field__typename: str = Field(..., alias='__typename')

class Edge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    key: Key
    node: Node
    field__typename: str = Field(..., alias='__typename')

class NewTitleBucketsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_info: PageInfo = Field(..., alias='pageInfo')
    edges: list[Edge]
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
