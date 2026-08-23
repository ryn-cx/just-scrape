# TODO: Validate
"""GraphQL query."""

# ruff: noqa: E501
QUERY = """query GetBuyBoxOffers($isLinearTvExperiment: Boolean = false, $nodeId: ID!, $country: Country!, $language: Language!, $platform: Platform! = WEB, $fallbackToForeignOffers: Boolean = true, $excludePackages: [String!] = []) {
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
  totalPackages(
    country: $country
    platform: $platform
    fallbackToForeignOffers: $fallbackToForeignOffers
  )
  offersHistory(
    country: $country
    platform: $platform
    filterV2: {monetizationTypes: [FLATRATE, FLATRATE_AND_BUY, RENT, FREE, ADS, BUY, FAST, LINEAR_FLATRATE, LINEAR_FREE], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
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
  dvdBluray: offers(
    country: $country
    platform: $platform
    filter: {presentationTypes: [DVD, BLURAY, BLURAY_4K], preAffiliate: true, excludePackages: $excludePackages}
  ) {
    ...TitleOffer
    offerSeasons
    minRetailPrice(country: $country, platform: $platform, language: $language)
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
  linear: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [FAST, LINEAR_FREE, LINEAR_FLATRATE], bestOnly: true, preAffiliate: true, fallbackToForeignOffers: $fallbackToForeignOffers, excludePackages: $excludePackages}
  ) {
    ...TitleOffer
    offerEpisodes @include(if: $isLinearTvExperiment) {
      offer {
        id
        availableFromTime
        availableToTime
        __typename
      }
      episode {
        id
        content(country: $country, language: $language) {
          title
          seasonNumber
          episodeNumber
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
  bundles(country: $country, platform: WEB) {
    node {
      id
      clearName
      icon(profile: S100)
      technicalName
      bundleId
      shortName
      packages(country: $country, platform: $platform) {
        icon
        id
        iconWide(profile: S160)
        clearName
        packageId
        shortName
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
        shortName
        packages(country: $country, platform: $platform) {
          icon
          id
          clearName
          packageId
          iconWide(profile: S160)
          shortName
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
      offerSeasons
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
  presentationType
  monetizationType
  newElementCount
  retailPrice(language: $language)
  retailPriceValue
  userLocalCurrency
  retailPriceConverted(language: $language)
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
    maskReferrer(country: $country, platform: WEB)
    planOffers(country: $country, platform: WEB) {
      title
      retailPrice(language: $language)
      isTrial
      durationDays
      retailPriceValue
      retailPriceConverted(language: $language)
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
    retailPriceConverted(language: $language)
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
  availableFromTime
  availableToTime
  subtitleLanguages
  videoTechnology
  audioTechnology
  audioLanguages(language: $language)
  updatedAt
  mediaDealId
  __typename
}
"""
