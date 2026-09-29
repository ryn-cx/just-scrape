from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class PlanOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    retail_price: str | Any = Field(None, alias='retailPrice', union_mode='left_to_right')
    is_trial: bool | Any = Field(None, alias='isTrial', union_mode='left_to_right')
    duration_days: int | Any = Field(None, alias='durationDays', union_mode='left_to_right')
    retail_price_value: int | float | Any = Field(None, alias='retailPriceValue', union_mode='left_to_right')
    retail_price_converted: str | Any = Field(None, alias='retailPriceConverted', union_mode='left_to_right')
    children: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    icon_wide: str | Any = Field(None, alias='iconWide', union_mode='left_to_right')
    mask_referrer: Any | None = Field(None, alias='maskReferrer')
    plan_offers: list[PlanOffer] | Any = Field(None, alias='planOffers', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Plan(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    retail_price: str | Any = Field(None, alias='retailPrice', union_mode='left_to_right')
    is_trial: bool | Any = Field(None, alias='isTrial', union_mode='left_to_right')
    duration_days: int | Any = Field(None, alias='durationDays', union_mode='left_to_right')
    retail_price_value: int | float | Any = Field(None, alias='retailPriceValue', union_mode='left_to_right')
    retail_price_converted: str | Any = Field(None, alias='retailPriceConverted', union_mode='left_to_right')
    children: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    presentation_type: str | Any = Field(None, alias='presentationType', union_mode='left_to_right')
    monetization_type: str | Any = Field(None, alias='monetizationType', union_mode='left_to_right')
    new_element_count: int | Any = Field(None, alias='newElementCount', union_mode='left_to_right')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    user_local_currency: str | Any = Field(None, alias='userLocalCurrency', union_mode='left_to_right')
    retail_price_converted: Any | None = Field(None, alias='retailPriceConverted')
    currency: str | Any = Field(default=None, union_mode='left_to_right')
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    package: Package | Any = Field(default=None, union_mode='left_to_right')
    plans: list[Plan] | Any = Field(default=None, union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | Any = Field(None, alias='elementCount', union_mode='left_to_right')
    available_to: Any | None = Field(None, alias='availableTo')
    available_from_time: AwareDatetime | Any = Field(None, alias='availableFromTime', union_mode='left_to_right')
    available_to_time: Any | None = Field(None, alias='availableToTime')
    subtitle_languages: list[str] | Any = Field(None, alias='subtitleLanguages', union_mode='left_to_right')
    video_technology: list[str] | Any = Field(None, alias='videoTechnology', union_mode='left_to_right')
    audio_technology: list[str] | Any = Field(None, alias='audioTechnology', union_mode='left_to_right')
    audio_languages: list[str] | Any = Field(None, alias='audioLanguages', union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(None, alias='updatedAt', union_mode='left_to_right')
    media_deal_id: Any | None = Field(None, alias='mediaDealId')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    icon_wide: str | Any = Field(None, alias='iconWide', union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    bundle_id: int | Any = Field(None, alias='bundleId', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    packages: list[Package1] | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    clear_name: str | Any = Field(None, alias='clearName', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    technical_name: str | Any = Field(None, alias='technicalName', union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    icon_wide: str | Any = Field(None, alias='iconWide', union_mode='left_to_right')
    mask_referrer: Any | None = Field(None, alias='maskReferrer')
    plan_offers: list[PlanOffer] | Any = Field(None, alias='planOffers', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Offer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    presentation_type: str | Any = Field(None, alias='presentationType', union_mode='left_to_right')
    monetization_type: str | Any = Field(None, alias='monetizationType', union_mode='left_to_right')
    new_element_count: int | Any = Field(None, alias='newElementCount', union_mode='left_to_right')
    retail_price: Any | None = Field(None, alias='retailPrice')
    retail_price_value: Any | None = Field(None, alias='retailPriceValue')
    user_local_currency: str | Any = Field(None, alias='userLocalCurrency', union_mode='left_to_right')
    retail_price_converted: Any | None = Field(None, alias='retailPriceConverted')
    currency: str | Any = Field(default=None, union_mode='left_to_right')
    last_change_retail_price_value: Any | None = Field(None, alias='lastChangeRetailPriceValue')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    package: Package2 | Any = Field(default=None, union_mode='left_to_right')
    plans: list[Plan] | Any = Field(default=None, union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    stream_url: Any | None = Field(None, alias='streamUrl')
    stream_url_external_player: Any | None = Field(None, alias='streamUrlExternalPlayer')
    element_count: int | Any = Field(None, alias='elementCount', union_mode='left_to_right')
    available_to: Any | None = Field(None, alias='availableTo')
    available_from_time: AwareDatetime | Any = Field(None, alias='availableFromTime', union_mode='left_to_right')
    available_to_time: Any | None = Field(None, alias='availableToTime')
    subtitle_languages: list[str] | Any = Field(None, alias='subtitleLanguages', union_mode='left_to_right')
    video_technology: list[Any] | Any = Field(None, alias='videoTechnology', union_mode='left_to_right')
    audio_technology: list[str] | Any = Field(None, alias='audioTechnology', union_mode='left_to_right')
    audio_languages: list[str] | Any = Field(None, alias='audioLanguages', union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(None, alias='updatedAt', union_mode='left_to_right')
    media_deal_id: Any | None = Field(None, alias='mediaDealId')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Bundle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node: Node | Any = Field(default=None, union_mode='left_to_right')
    promotion_url: str | Any = Field(None, alias='promotionUrl', union_mode='left_to_right')
    offer: Offer | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class EpisodeOffersModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    offer_count: int | Any = Field(None, alias='offerCount', union_mode='left_to_right')
    max_offer_updated_at: AwareDatetime | Any = Field(None, alias='maxOfferUpdatedAt', union_mode='left_to_right')
    total_packages: int | Any = Field(None, alias='totalPackages', union_mode='left_to_right')
    offers_history: list[Any] | Any = Field(None, alias='offersHistory', union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    dvd_bluray: list[Any] | Any = Field(None, alias='dvdBluray', union_mode='left_to_right')
    buy: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    free: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    linear: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    bundles: list[Bundle] | Any = Field(default=None, union_mode='left_to_right')
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
