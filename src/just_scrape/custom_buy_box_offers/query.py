# ruff: noqa: E501
# dateCreated was added.
QUERY = """query GetBuyBoxOffers($nodeId: ID!, $country: Country!, $language: Language!, $platform: Platform! = WEB, $fallbackToForeignOffers: Boolean = true, $excludePackages: [String!] = []) {
  node(id: $nodeId) {
    id
    ...BuyBoxOffers
    __typename
  }
}

fragment BuyBoxOffers on MovieOrShowOrSeasonOrEpisode {
  __typename
  offerCount(country: $country, platform: $platform)
  maxOfferUpdatedAt(country: $country, platform: $platform)
  offersHistory(
    country: $country
    platform: $platform
    filterV2: {monetizationTypes: [FLATRATE, FLATRATE_AND_BUY, RENT, FREE, ADS, BUY, FAST], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
  ) {
    ...OffersHistory
    __typename
  }
  flatrate: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [FLATRATE, FLATRATE_AND_BUY, CINEMA], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
  ) {
    ...TitleOffer
    __typename
  }
  buy: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [BUY], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
  ) {
    ...TitleOffer
    offerSeasons
    minRetailPrice(country: $country, platform: $platform, language: $language)
    __typename
  }
  rent: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [RENT], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
  ) {
    ...TitleOffer
    offerSeasons
    minRetailPrice(country: $country, platform: $platform, language: $language)
    __typename
  }
  free: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [FREE, ADS], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
  ) {
    ...TitleOffer
    __typename
  }
  fast: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [FAST], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
  ) {
    ...FastOffer
    __typename
  }
  bundles(country: $country, platform: WEB) {
    node {
      id
      clearName
      icon(profile: S100)
      technicalName
      bundleId
      packages(country: $country, platform: $platform) {
        icon
        id
        iconWide(profile: S160)
        clearName
        packageId
        __typename
      }
      __typename
    }
    promotionUrl
    offer {
      ...TitleOffer
      __typename
    }
    __typename
  }
  ... on MovieOrShowOrSeason {
    promotedBundles(country: $country, platform: WEB) {
      node {
        id
        clearName
        icon(profile: S100)
        technicalName
        bundleId
        packages(country: $country, platform: $platform) {
          icon
          id
          clearName
          packageId
          iconWide(profile: S160)
          __typename
        }
        __typename
      }
      promotionUrl
      offer {
        ...TitleOffer
        __typename
      }
      __typename
    }
    promotedOffers(
      country: $country
      platform: WEB
      filter: {bestOnly: true, preAffiliate: true}
    ) {
      ...TitleOffer
      minRetailPrice(country: $country, platform: $platform, language: $language)
      __typename
    }
    __typename
  }
}

fragment OffersHistory on OfferHistory {
  __typename
  id
  country
  dateRanges {
    end
    start
    __typename
  }
  package {
    icon
    id
    iconWide(profile: S160)
    clearName
    packageId
    monetizationTypes
    __typename
  }
}

fragment TitleOffer on Offer {
  id
  dateCreated
  presentationType
  monetizationType
  newElementCount
  retailPrice(language: $language)
  retailPriceValue
  currency
  lastChangeRetailPriceValue
  type
  country
  package {
    id
    packageId
    clearName
    shortName
    technicalName
    icon(profile: S100)
    iconWide(profile: S160)
    planOffers(country: $country, platform: WEB) {
      title
      retailPrice(language: $language)
      isTrial
      durationDays
      retailPriceValue
      children {
        title
        retailPrice(language: $language)
        isTrial
        durationDays
        retailPriceValue
        __typename
      }
      __typename
    }
    __typename
  }
  plans(platform: WEB) {
    title
    retailPrice(language: $language)
    isTrial
    durationDays
    retailPriceValue
    children {
      title
      retailPrice(language: $language)
      isTrial
      durationDays
      retailPriceValue
      __typename
    }
    __typename
  }
  standardWebURL
  preAffiliatedStandardWebURL
  streamUrl
  streamUrlExternalPlayer
  elementCount
  availableTo
  subtitleLanguages
  videoTechnology
  audioTechnology
  audioLanguages(language: $language)
  __typename
}

fragment FastOffer on Offer {
  ...TitleOffer
  availableTo
  availableFromTime
  availableToTime
  __typename
}
"""
