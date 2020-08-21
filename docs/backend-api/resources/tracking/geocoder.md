---
title: Geocoder
description: Search address and location using geocoder
---

# Geocoder

API path: `/geocoder`.

### Geocoder types:

Geocoder types:

*   google
*   yandex
*   progorod
*   osm
*   locationiq

### search_address

Performs a forward geocoding. Returns a list of locations matching the given address. Items in the list are sorted by relevance.

#### parameters

|name|description|type|format|
|--- |--- |--- |--- |
| q | address (or place) or coordinates to geocode | string/location | 750 Avenue E,San Francisco,CA 94130,USA./60.0, 61.0 |
| lang | language in which results should be | string (enum) | en |
| geocoder | optional, geocoder type that will be preferably used for searching | string (enum) | google |
| bounds | optional. JSON object. The bounding box, specified by coordinates of northwest and southeast corners. Geocoder will preferably return results from within these bounds. That is the parameter influences the priority of results, so if more relevant results exist outside of bounds, they may be included.| bounds_object | `{"nw":{"lat":60.0,"lng":61.0},"se":{"lat":55.0,"lng":60.0}}` |
| lang | optional. ISO 639 [language code](../../getting-started.md#data-types) | locale | en_US |
| with_details | optional. If true then the response will contain details | boolean | true/false |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/geocoder/search_address' \
  -H 'Content-Type: application/json' \ 
  -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "q": "750 Avenue E,San Francisco,CA 94130,USA", "lang": "en", "geocoder": "google"}' 
```

#### response

```json5
{
    "success": true,
    "locations": [
        {
            "lat": <lat>,        // double
            "lng": <lng>,        // double
            "address": <address>, // string
            "details": <details_object> // optional
        },
        ...
    ]
}
```

where **details_object** is:

```json5
{
    "country": <string>, // optional
    "province": <string>, // optional
    "locality": <string>, // optional
    "street": <string>, // optional
    "house": <string>, // optional
    "postcode": <string>, // optional
    "bounds": <bounds_object> //optional, the bounding box which can fully contain the returned result
}
```

**bounds_object** is:

```json5
{
  "nw":{ //northwest corner
    "lat":<double>,
    "lng":<double>
  },
  "se":{ //southeast corner
    "lat":<double>,
    "lng":<double>
  }
}
```

### search_location

Search address by location using geocoder

#### parameters

|name|description|type|format|
|--- |--- |--- |--- |
| location | location coordinates (see: [data types description section](../../getting-started.md#data-types) section) | location | `{"lat": , "lng": }` |
| geocoder | optional, geocoder type that will be preferably used for searching | string (enum) | google |
| lang | optional. ISO 639 [language code](../../getting-started.md#data-types) | locale | en_US |
| with_details | optional. If true then the response will contain details | boolean | true/false |
| goal | Helps to choose the target geocoder. Now supported `ui`, `ui_user_action`. Use `ui_user_action` for requests initiated by user, otherwise `ui` | string (enum) | ui | 

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/geocoder/search_location' \
  -H 'Content-Type: application/json' \ 
  -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "location": "{"lat": 56.827001, "lng": 60.594296}"}' 
```
#### response

```json5
{
    "success": true,
    "value": <address>, // string
    "details": <details_object> // optional
}
```
 
