# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import NewTitleBucketsModel as OptionalModel
from .strict_models import NewTitleBucketsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Edge,
        Key,
        NewTitleBucketsModel,
        Node,
        Package,
        PageInfo,
        PageInfo1,
    )
else:
    from .optional_models import (
        Edge,
        Key,
        NewTitleBucketsModel,
        Node,
        Package,
        PageInfo,
        PageInfo1,
    )

__all__ = [
    "Edge",
    "Key",
    "NewTitleBucketsModel",
    "Node",
    "Package",
    "PageInfo",
    "PageInfo1",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> NewTitleBucketsModel:
    """Read a downloaded file into NewTitleBucketsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
