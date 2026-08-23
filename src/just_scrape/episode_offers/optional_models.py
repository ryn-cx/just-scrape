from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class PlanOffer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    retail_price: str | None = Field(None, alias='retailPrice')
    is_trial: bool | None = Field(None, alias='isTrial')
    duration_days: int | None = Field(None, alias='durationDays')
    retail_price_value: int | float | None = Field(None, alias='retailPriceValue')
    retail_price_converted: str | None = Field(None, alias='retailPriceConverted')
    children: list[Any] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    package_id: int | None = Field(None, alias='packageId')
    clear_name: str | None = Field(None, alias='clearName')
    short_name: str | None = Field(None, alias='shortName')
    technical_name: str | None = Field(None, alias='technicalName')
    icon: str | None = None
    icon_wide: str | None = Field(None, alias='iconWide')
    mask_referrer: Any | None = Field(None, alias='maskReferrer')
    plan_offers: list[PlanOffer] | None = Field(None, alias='planOffers')
    field__typename: str | None = Field(None, alias='__typename')

class Plan(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    retail_price: str | None = Field(None, alias='retailPrice')
    is_trial: bool | None = Field(None, alias='isTrial')
    duration_days: int | None = Field(None, alias='durationDays')
    retail_price_value: int | float | None = Field(None, alias='retailPriceValue')
    retail_price_converted: str | None = Field(None, alias='retailPriceConverted')
    children: list[Any] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    presentation_type: str | None = Field(None, alias='presentationType')
    monetization_type: str | None = Field(None, alias='monetizationType')
    new_element_count: int | None = Field(None, alias='newElementCount')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    user_local_currency: str | None = Field(None, alias='userLocalCurrency')
    retail_price_converted: Any | None = Field(None, alias='retailPriceConverted')
    currency: str | None = None
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | None = None
    country: str | None = None
    package: Package | None = None
    plans: list[Plan] | None = None
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | None = Field(None, alias='elementCount')
    available_to: Any | None = Field(None, alias='availableTo')
    available_from_time: Any | AwareDatetime | None = Field(None, alias='availableFromTime')
    available_to_time: Any | None = Field(None, alias='availableToTime')
    subtitle_languages: list[str] | None = Field(None, alias='subtitleLanguages')
    video_technology: list[str] | None = Field(None, alias='videoTechnology')
    audio_technology: list[str] | None = Field(None, alias='audioTechnology')
    audio_languages: list[str] | None = Field(None, alias='audioLanguages')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    media_deal_id: Any | None = Field(None, alias='mediaDealId')
    field__typename: str | None = Field(None, alias='__typename')

class Package1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon: str | None = None
    id: str | None = None
    icon_wide: str | None = Field(None, alias='iconWide')
    clear_name: str | None = Field(None, alias='clearName')
    package_id: int | None = Field(None, alias='packageId')
    short_name: str | None = Field(None, alias='shortName')
    field__typename: str | None = Field(None, alias='__typename')

class Node1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    clear_name: str | None = Field(None, alias='clearName')
    icon: str | None = None
    technical_name: str | None = Field(None, alias='technicalName')
    bundle_id: int | None = Field(None, alias='bundleId')
    short_name: str | None = Field(None, alias='shortName')
    packages: list[Package1] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Package2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    package_id: int | None = Field(None, alias='packageId')
    clear_name: str | None = Field(None, alias='clearName')
    short_name: str | None = Field(None, alias='shortName')
    technical_name: str | None = Field(None, alias='technicalName')
    icon: str | None = None
    icon_wide: str | None = Field(None, alias='iconWide')
    mask_referrer: Any | None = Field(None, alias='maskReferrer')
    plan_offers: list[PlanOffer] | None = Field(None, alias='planOffers')
    field__typename: str | None = Field(None, alias='__typename')

class Offer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    presentation_type: str | None = Field(None, alias='presentationType')
    monetization_type: str | None = Field(None, alias='monetizationType')
    new_element_count: int | None = Field(None, alias='newElementCount')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    user_local_currency: str | None = Field(None, alias='userLocalCurrency')
    retail_price_converted: Any | None = Field(None, alias='retailPriceConverted')
    currency: str | None = None
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | None = None
    country: str | None = None
    package: Package2 | None = None
    plans: list[Plan] | None = None
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | None = Field(None, alias='elementCount')
    available_to: Any | None = Field(None, alias='availableTo')
    available_from_time: AwareDatetime | None = Field(None, alias='availableFromTime')
    available_to_time: Any | None = Field(None, alias='availableToTime')
    subtitle_languages: list[str] | None = Field(None, alias='subtitleLanguages')
    video_technology: list[Any] | None = Field(None, alias='videoTechnology')
    audio_technology: list[str] | None = Field(None, alias='audioTechnology')
    audio_languages: list[str] | None = Field(None, alias='audioLanguages')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    media_deal_id: Any | None = Field(None, alias='mediaDealId')
    field__typename: str | None = Field(None, alias='__typename')

class Bundle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    node: Node1 | None = None
    promotion_url: str | None = Field(None, alias='promotionUrl')
    offer: Offer | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    field__typename: str | None = Field(None, alias='__typename')
    offer_count: int | None = Field(None, alias='offerCount')
    max_offer_updated_at: Any | AwareDatetime | None = Field(None, alias='maxOfferUpdatedAt')
    total_packages: int | None = Field(None, alias='totalPackages')
    offers_history: list[Any] | None = Field(None, alias='offersHistory')
    flatrate: list[FlatrateItem] | None = None
    dvd_bluray: list[Any] | None = Field(None, alias='dvdBluray')
    buy: list[Any] | None = None
    rent: list[Any] | None = None
    free: list[Any] | None = None
    linear: list[Any] | None = None
    bundles: list[Bundle] | None = None

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    node: Node | None = None

class EpisodeOffersModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
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
