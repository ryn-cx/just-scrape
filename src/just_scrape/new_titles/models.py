# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import NewTitlesModel as OptionalModel
from .strict_models import NewTitlesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Content,
        Content1,
        Edge,
        Genre,
        NewOffer,
        NewTitlesModel,
        Node,
        Package,
        PageInfo,
        Scoring,
        Scoring1,
        SeenState,
        Show,
    )
else:
    from .optional_models import (
        Content,
        Content1,
        Edge,
        Genre,
        NewOffer,
        NewTitlesModel,
        Node,
        Package,
        PageInfo,
        Scoring,
        Scoring1,
        SeenState,
        Show,
    )

__all__ = [
    "Content",
    "Content1",
    "Edge",
    "Genre",
    "NewOffer",
    "NewTitlesModel",
    "Node",
    "Package",
    "PageInfo",
    "Scoring",
    "Scoring1",
    "SeenState",
    "Show",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> NewTitlesModel:
    """Read a downloaded file into NewTitlesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
