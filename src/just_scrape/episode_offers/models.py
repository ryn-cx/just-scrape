"""EpisodeOffersModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import EpisodeOffersModel as OptionalModel
from .strict_models import EpisodeOffersModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Bundle,
        EpisodeOffersModel,
        FlatrateItem,
        Node,
        Offer,
        Package,
        Package1,
        Package2,
        Plan,
        PlanOffer,
    )
else:
    from .optional_models import (
        Bundle,
        EpisodeOffersModel,
        FlatrateItem,
        Node,
        Offer,
        Package,
        Package1,
        Package2,
        Plan,
        PlanOffer,
    )

__all__ = [
    "Bundle",
    "EpisodeOffersModel",
    "FlatrateItem",
    "Node",
    "Offer",
    "Package",
    "Package1",
    "Package2",
    "Plan",
    "PlanOffer",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> EpisodeOffersModel:
    """Read a downloaded file into EpisodeOffersModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
