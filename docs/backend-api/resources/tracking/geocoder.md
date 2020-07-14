---
title: /geocoder
description: /geocoder
---

# geocoder/ actions:

Geocoders:

*   google
*   yandex
*   progorod
*   osm
*   locationiq

**details_object** is:
```javascript
{
    "country": <string>, // optional
    "province": <string>, // optional
    "locality": <string>, // optional
    "street": <string>, // optional
    "house": <string>, // optional
    "postcode": <string> // optional
}
```

## search_address(…)

Performs a forward geocoding. Returns a list of locations matching the given address. Items in the list are sorted by relevance.

#### parameters:

*   q – address (or place) or coordinates (comma separated decimal degrees e.g. _60.0,-61.0_) to geocode
*   lang – language in which results should be. E.g. “en”
*   geocoder – geocoder type
*   bounds – optional, JSON object. The bounding box, specified by coordinates of northwest and southeast corners. Geocoder will preferably return results from within these bounds. That is the parameter influences the priority of results, so if more relevant results exist outside of bounds, they may be included.
*   lang – optional, string, ISO 639 language code
*   with_details – optional, boolean. If true then the response will contain details


    bounds={"nw":{"lat":60.0,"lng":61.0},"se":{"lat":55.0,"lng":60.0}}

#### return:

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

---
## search_location(…)

#### parameters:

*   location – not null, **location** (see: [data types description section](../../getting-started.md#data-types) section)
*   geocoder – optional, string (enum). Now supported `google`, `osm`, `yandex`, `locationiq` geocoders.
*   lang – optional, string, ISO 639 language code
*   with_details – optional, boolean. If true then the response will contain details
*   goal - optional, string (enum). Now supported `ui`, `ui_user_action`. Helps to choose the target geocoder. 
Use `ui_user_action` for requests initiated by user, otherwise `ui`.

Search address by location.
User language wil be used If `lang` is omitted.

#### return:

    {
        "success": true,
        "value": <address>, // string
        "details": <details_object> // optional
    }