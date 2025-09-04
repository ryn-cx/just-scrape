# ruff: noqa: E501
QUERY = """query GetSeasonEpisodes($nodeId: ID!, $country: Country!, $language: Language!, $platform: Platform! = WEB, $limit: Int, $offset: Int) {
  node(id: $nodeId) {
    id
    __typename
    ... on Season {
      episodes(limit: $limit, offset: $offset) {
        ...Episode
        __typename
      }
      __typename
    }
  }
}

fragment Episode on Episode {
  id
  objectId
  objectType
  seenlistEntry {
    createdAt
    __typename
  }
  uniqueOfferCount: offerCount(
    country: $country
    platform: $platform
    filter: {bestOnly: true}
  )
  flatrate: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [FLATRATE_AND_BUY, FLATRATE, ADS, CINEMA, FREE], bestOnly: true, preAffiliate: true}
  ) {
    id
    package {
      id
      clearName
      packageId
      __typename
    }
    __typename
  }
  buy: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [BUY], bestOnly: true, preAffiliate: true}
  ) {
    id
    package {
      id
      clearName
      packageId
      __typename
    }
    __typename
  }
  rent: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [RENT], bestOnly: true, preAffiliate: true}
  ) {
    id
    package {
      id
      clearName
      packageId
      __typename
    }
    __typename
  }
  free: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [ADS, FREE], bestOnly: true, preAffiliate: true}
  ) {
    id
    package {
      id
      clearName
      packageId
      __typename
    }
    __typename
  }
  fast: offers(
    country: $country
    platform: $platform
    filter: {monetizationTypes: [FAST], bestOnly: true, preAffiliate: true}
  ) {
    id
    package {
      id
      clearName
      packageId
      __typename
    }
    __typename
  }
  content(country: $country, language: $language) {
    __typename
    title
    shortDescription
    episodeNumber
    seasonNumber
    isReleased
    runtime
    upcomingReleases {
      releaseCountDown(country: $country)
      releaseDate
      releaseType
      label
      package {
        id
        packageId
        shortName
        clearName
        monetizationTypes
        icon(profile: S100)
        iconWide(profile: S160)
        hasRectangularIcon(country: $country, platform: WEB)
        planOffers(country: $country, platform: $platform) {
          retailPrice(language: $language)
          durationDays
          presentationType
          isTrial
          retailPriceValue
          currency
          __typename
        }
        __typename
      }
      __typename
    }
  }
  __typename
}
"""
