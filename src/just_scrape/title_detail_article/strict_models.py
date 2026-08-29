from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from typing import Any
from pydantic import BaseModel, Field

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    articles: list[None]
    field__typename: str = Field(..., alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    content: Content
    field__typename: str = Field(..., alias='__typename')

class UrlV2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    node: Node
    field__typename: str = Field(..., alias='__typename')

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url_v2: UrlV2 = Field(..., alias='urlV2')

class TitleDetailArticleModel(BaseModel):
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
