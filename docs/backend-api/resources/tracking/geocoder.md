---
title: Geocoder
description: API calls to search address and location using geocoder
---

# Geocoder

API path: `/geocoder`.

API calls to search address and location using geocoder.

## Geocoder types

* google.
* yandex.
* progorod.
* osm.
* locationiq.

### search_address

Performs a forward geocoding. Returns a list of locations matching the given address. Items in the list sorted by relevance.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| q | Address (or place) or coordinates to geocode. | string/location | "750 Avenue E,San Francisco,CA 94130,USA./60.0, 61.0" |
| lang | Language in which results should be. | [enum](../../../getting-started.md#data-types) | "en" |
| geocoder | Optional. Geocoder type that will be preferably used for searching. | [enum](../../../getting-started.md#data-types) | "google" |
| bounds | Optional. JSON object. The bounding box, specified by coordinates of northwest and southeast corners. Geocoder will preferably return results from within these bounds. That is the parameter influences the priority of results, so if more relevant results exist outside of bounds, they may be included.| bounds_object | `{"nw":{"lat":60.0,"lng":61.0},"se":{"lat":55.0,"lng":60.0}}` |
| lang | Optional. ISO 639 [language code](../../getting-started.md#data-types). | [enum](../../../getting-started.md#data-types) | "en_US" |
| with_details | Optional. If `true` then the response will contain details. | boolean | `true` |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/geocoder/search_address' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "q": "750 Avenue E,San Francisco,CA 94130,USA", "lang": "en", "geocoder": "google"}'
    ```

#### response

```json
{
    "success": true,
    "locations": [{
            "lat": 56.26697,
            "lng": 19.55436,
            "address": "750 Avenue E,San Francisco",
            "details": {
              "country": "USA",
              "province": "CA",
              "locality": "San Francisco",
              "street": "Avenue E",
              "house": "750",
              "postcode": "94130",
              "bounds": {
                "nw":{
                  "lat": 62.23621,
                  "lng": 58.56997
                },
                "se":{
                  "lat": 31.98753,
                  "lng": 42.23694
                }
              }
            }
    }]
}
```

* `lat` - double. Latitude.
* `lng` - double. Longitude.
* `address` - string. Address.
* `details` - details object.
    * `country` - optional string.
    * `province` - optional string.
    * `locality` - optional string.
    * `street` - optional string.
    * `house` - optional string.
    * `postcode` - optional string.
    * `bounds` - optional object, the bounding box which can fully contain the returned result.
        * `nw` - North West corner.
        * `se` - South East corner.


### search_location

Search address by location using geocoder.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| location | Location coordinates (see: [data types description section](../../getting-started.md#data-types) section). | location | `{"lat": , "lng": }` |
| geocoder | Optional. Geocoder type that will be preferably used for searching. | [enum](../../../getting-started.md#data-types) | "google" |
| lang | Optional. ISO 639 [language code](../../getting-started.md#data-types). | [enum](../../../getting-started.md#data-types) | "en_US" |
| with_details | Optional. If `true` then the response will contain details. | boolean | `true` |
| goal | Helps to choose the target geocoder. Now supported `ui`, `ui_user_action`. Use `ui_user_action` for requests initiated by user, otherwise `ui`. | [enum](../../../getting-started.md#data-types) | "ui" | 

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/geocoder/search_location' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "location": "{"lat": 56.827001, "lng": 60.594296}}'
    ```

#### response

```json
{
    "success": true,
    "value": "750 Avenue E,San Francisco,CA 94130,USA",
    "details": {
      "country": "USA",
      "province": "CA",
      "locality": "San Francisco",
      "street": "Avenue E",
      "house": "750",
      "postcode": "94130",
      "bounds": {
        "nw":{
          "lat": 62.23621,
          "lng": 58.56997
        },
        "se":{
          "lat": 31.98753,
          "lng": 42.23694
        }
      }
    }
}
```

* `value` - string. Address.
* `details` - optional details object.
    * `country` - optional string.
    * `province` - optional string.
    * `locality` - optional string.
    * `street` - optional string.
    * `house` - optional string.
    * `postcode` - optional string.
    * `bounds` - optional object, the bounding box which can fully contain the returned result.
        * `nw` - North West corner.
        * `se` - South East corner.