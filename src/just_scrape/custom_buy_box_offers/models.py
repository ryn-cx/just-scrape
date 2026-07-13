# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from datetime import date

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class Child(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: None = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: None = Field(..., alias="retailPriceValue")
    field__typename: str = Field(..., alias="__typename")


class PlanOffer(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str | None = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float | None = Field(..., alias="retailPriceValue")
    children: list[Child]
    field__typename: str = Field(..., alias="__typename")


class Package(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon: str
    icon_wide: str = Field(..., alias="iconWide")
    plan_offers: list[PlanOffer] = Field(..., alias="planOffers")
    field__typename: str = Field(..., alias="__typename")


class Plan(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str | None = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float | None = Field(..., alias="retailPriceValue")
    children: list[Child]
    field__typename: str = Field(..., alias="__typename")


class FlatrateItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    date_created: date = Field(..., alias="dateCreated")
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    new_element_count: int = Field(..., alias="newElementCount")
    retail_price: None = Field(..., alias="retailPrice")
    retail_price_value: None = Field(..., alias="retailPriceValue")
    currency: str
    last_change_retail_price_value: None = Field(
        ...,
        alias="lastChangeRetailPriceValue",
    )
    type: str
    country: str
    package: Package
    plans: list[Plan]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ...,
        alias="preAffiliatedStandardWebURL",
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: None = Field(..., alias="availableTo")
    subtitle_languages: list[None] = Field(..., alias="subtitleLanguages")
    video_technology: list[str] = Field(..., alias="videoTechnology")
    audio_technology: list[str] = Field(..., alias="audioTechnology")
    audio_languages: list[None] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")


class Package1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    id: str
    icon_wide: str = Field(..., alias="iconWide")
    clear_name: str = Field(..., alias="clearName")
    package_id: int = Field(..., alias="packageId")
    field__typename: str = Field(..., alias="__typename")


class Node1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    clear_name: str = Field(..., alias="clearName")
    icon: str
    technical_name: str = Field(..., alias="technicalName")
    bundle_id: int = Field(..., alias="bundleId")
    packages: list[Package1]
    field__typename: str = Field(..., alias="__typename")


class PlanOffer1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str | None = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float | None = Field(..., alias="retailPriceValue")
    children: list[Child]
    field__typename: str = Field(..., alias="__typename")


class Package2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon: str
    icon_wide: str = Field(..., alias="iconWide")
    plan_offers: list[PlanOffer1] = Field(..., alias="planOffers")
    field__typename: str = Field(..., alias="__typename")


class Plan1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    retail_price: str | None = Field(..., alias="retailPrice")
    is_trial: bool = Field(..., alias="isTrial")
    duration_days: int = Field(..., alias="durationDays")
    retail_price_value: float | None = Field(..., alias="retailPriceValue")
    children: list[Child]
    field__typename: str = Field(..., alias="__typename")


class Offer(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    date_created: date = Field(..., alias="dateCreated")
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    new_element_count: int = Field(..., alias="newElementCount")
    retail_price: None = Field(..., alias="retailPrice")
    retail_price_value: None = Field(..., alias="retailPriceValue")
    currency: str
    last_change_retail_price_value: None = Field(
        ...,
        alias="lastChangeRetailPriceValue",
    )
    type: str
    country: str
    package: Package2
    plans: list[Plan1]
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ...,
        alias="preAffiliatedStandardWebURL",
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    element_count: int = Field(..., alias="elementCount")
    available_to: None = Field(..., alias="availableTo")
    subtitle_languages: list[None] = Field(..., alias="subtitleLanguages")
    video_technology: list[str] = Field(..., alias="videoTechnology")
    audio_technology: list[str] = Field(..., alias="audioTechnology")
    audio_languages: list[None] = Field(..., alias="audioLanguages")
    field__typename: str = Field(..., alias="__typename")


class Bundle(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    node: Node1
    promotion_url: str = Field(..., alias="promotionUrl")
    offer: Offer
    field__typename: str = Field(..., alias="__typename")


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    field__typename: str = Field(..., alias="__typename")
    offer_count: int = Field(..., alias="offerCount")
    max_offer_updated_at: AwareDatetime | None = Field(..., alias="maxOfferUpdatedAt")
    offers_history: list[None] = Field(..., alias="offersHistory")
    flatrate: list[FlatrateItem]
    buy: list[None]
    rent: list[None]
    free: list[None]
    fast: list[None]
    bundles: list[Bundle]


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    node: Node


class Variables(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    platform: str
    fallback_to_foreign_offers: bool = Field(..., alias="fallbackToForeignOffers")
    exclude_packages: list[str] = Field(..., alias="excludePackages")
    node_id: str = Field(..., alias="nodeId")
    country: str
    language: str


class Headers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    referer: str = Field(..., alias="Referer")
    origin: str = Field(..., alias="Origin")


class JustScrape(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    variables: Variables
    operation_name: str = Field(..., alias="operationName")
    headers: Headers
    timestamp: AwareDatetime


class CustomBuyBoxOffersResponse(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape | None = None
