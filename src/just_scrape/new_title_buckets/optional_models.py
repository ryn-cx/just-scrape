from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from datetime import date as date_aliased

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_cursor: str | Any = Field(None, alias='startCursor', union_mode='left_to_right')
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')
    has_previous_page: bool | Any = Field(None, alias='hasPreviousPage', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Key(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    date: date_aliased | Any = Field(default=None, union_mode='left_to_right')
    package: Package | Any = Field(default=None, union_mode='left_to_right')

class PageInfo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_cursor: str | Any = Field(None, alias='startCursor', union_mode='left_to_right')
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')
    has_previous_page: bool | Any = Field(None, alias='hasPreviousPage', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')
    page_info: PageInfo1 | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: Key | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class NewTitleBucketsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
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
