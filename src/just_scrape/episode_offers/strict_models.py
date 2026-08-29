from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class PlanOffer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    retail_price: str = Field(..., alias='retailPrice')
    is_trial: bool = Field(..., alias='isTrial')
    duration_days: int = Field(..., alias='durationDays')
    retail_price_value: int | float = Field(..., alias='retailPriceValue')
    retail_price_converted: str = Field(..., alias='retailPriceConverted')
    children: list[None]
    field__typename: str = Field(..., alias='__typename')

class Package(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    package_id: int = Field(..., alias='packageId')
    clear_name: str = Field(..., alias='clearName')
    short_name: str = Field(..., alias='shortName')
    technical_name: str = Field(..., alias='technicalName')
    icon: str
    icon_wide: str = Field(..., alias='iconWide')
    mask_referrer: None = Field(..., alias='maskReferrer')
    plan_offers: list[PlanOffer] = Field(..., alias='planOffers')
    field__typename: str = Field(..., alias='__typename')

class Plan(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    retail_price: str = Field(..., alias='retailPrice')
    is_trial: bool = Field(..., alias='isTrial')
    duration_days: int = Field(..., alias='durationDays')
    retail_price_value: int | float = Field(..., alias='retailPriceValue')
    retail_price_converted: str = Field(..., alias='retailPriceConverted')
    children: list[None]
    field__typename: str = Field(..., alias='__typename')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    presentation_type: str = Field(..., alias='presentationType')
    monetization_type: str = Field(..., alias='monetizationType')
    new_element_count: int = Field(..., alias='newElementCount')
    retail_price: None = Field(..., alias='retailPrice')
    retail_price_value: None = Field(..., alias='retailPriceValue')
    user_local_currency: str = Field(..., alias='userLocalCurrency')
    retail_price_converted: None = Field(..., alias='retailPriceConverted')
    currency: str
    last_change_retail_price_value: None = Field(..., alias='lastChangeRetailPriceValue')
    type: str
    country: str
    package: Package
    plans: list[Plan]
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    stream_url: None = Field(..., alias='streamUrl')
    stream_url_external_player: None = Field(..., alias='streamUrlExternalPlayer')
    element_count: int = Field(..., alias='elementCount')
    available_to: None = Field(..., alias='availableTo')
    available_from_time: AwareDatetime | None = Field(..., alias='availableFromTime')
    available_to_time: None = Field(..., alias='availableToTime')
    subtitle_languages: list[str] = Field(..., alias='subtitleLanguages')
    video_technology: list[str] = Field(..., alias='videoTechnology')
    audio_technology: list[str] = Field(..., alias='audioTechnology')
    audio_languages: list[str] = Field(..., alias='audioLanguages')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    media_deal_id: None = Field(..., alias='mediaDealId')
    field__typename: str = Field(..., alias='__typename')

class Package1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    id: str
    icon_wide: str = Field(..., alias='iconWide')
    clear_name: str = Field(..., alias='clearName')
    package_id: int = Field(..., alias='packageId')
    short_name: str = Field(..., alias='shortName')
    field__typename: str = Field(..., alias='__typename')

class Node1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    clear_name: str = Field(..., alias='clearName')
    icon: str
    technical_name: str = Field(..., alias='technicalName')
    bundle_id: int = Field(..., alias='bundleId')
    short_name: str = Field(..., alias='shortName')
    packages: list[Package1]
    field__typename: str = Field(..., alias='__typename')

class Package2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    package_id: int = Field(..., alias='packageId')
    clear_name: str = Field(..., alias='clearName')
    short_name: str = Field(..., alias='shortName')
    technical_name: str = Field(..., alias='technicalName')
    icon: str
    icon_wide: str = Field(..., alias='iconWide')
    mask_referrer: None = Field(..., alias='maskReferrer')
    plan_offers: list[PlanOffer] = Field(..., alias='planOffers')
    field__typename: str = Field(..., alias='__typename')

class Offer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    presentation_type: str = Field(..., alias='presentationType')
    monetization_type: str = Field(..., alias='monetizationType')
    new_element_count: int = Field(..., alias='newElementCount')
    retail_price: None = Field(..., alias='retailPrice')
    retail_price_value: None = Field(..., alias='retailPriceValue')
    user_local_currency: str = Field(..., alias='userLocalCurrency')
    retail_price_converted: None = Field(..., alias='retailPriceConverted')
    currency: str
    last_change_retail_price_value: None = Field(..., alias='lastChangeRetailPriceValue')
    type: str
    country: str
    package: Package2
    plans: list[Plan]
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    stream_url: None = Field(..., alias='streamUrl')
    stream_url_external_player: None = Field(..., alias='streamUrlExternalPlayer')
    element_count: int = Field(..., alias='elementCount')
    available_to: None = Field(..., alias='availableTo')
    available_from_time: AwareDatetime = Field(..., alias='availableFromTime')
    available_to_time: None = Field(..., alias='availableToTime')
    subtitle_languages: list[str] = Field(..., alias='subtitleLanguages')
    video_technology: list[None] = Field(..., alias='videoTechnology')
    audio_technology: list[str] = Field(..., alias='audioTechnology')
    audio_languages: list[str] = Field(..., alias='audioLanguages')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    media_deal_id: None = Field(..., alias='mediaDealId')
    field__typename: str = Field(..., alias='__typename')

class Bundle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node: Node1
    promotion_url: str = Field(..., alias='promotionUrl')
    offer: Offer
    field__typename: str = Field(..., alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    field__typename: str = Field(..., alias='__typename')
    offer_count: int = Field(..., alias='offerCount')
    max_offer_updated_at: AwareDatetime | None = Field(..., alias='maxOfferUpdatedAt')
    total_packages: int = Field(..., alias='totalPackages')
    offers_history: list[None] = Field(..., alias='offersHistory')
    flatrate: list[FlatrateItem]
    dvd_bluray: list[None] = Field(..., alias='dvdBluray')
    buy: list[None]
    rent: list[None]
    free: list[None]
    linear: list[None]
    bundles: list[Bundle]

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node: Node

class EpisodeOffersModel(BaseModel):
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
