---
title: Get track points for trips
description: How to get all points of trips
---

# How to get track points for trips

Sometimes necessary to get all points of a trip with more info about the device's moves.
How to get them?

Firstly you need to [obtain hash of an API key](./get-api-key.md).

Once you get the hash, you need to [get your tracker_id](./get-tracker-list.md). The platform must know points for what device must be in reply.

Now you can get all points for the interesting period using [`/track/read` API call](../resources/tracking/track/index.md#read).  
Parameters that necessary for this call:

* `tracker_id` - we got them in [tracker/list](../resources/tracking/tracker/index.md#list) call. Use only one tracker_id per call. It should be an integer.
* `from` - a string containing start [date/time](../getting-started.md#datetime-formats).
* `to` - a string containing end [date/time](../getting-started.md#datetime-formats).

Full parameters description see at [`/track/read` API call](../resources/tracking/track/index.md#read). 

The platform will reply:

```json
{
    "success": true,
    "limit_exceeded": true,
    "list": [
        {
            "lat": 53.445181,
            "lng": -2.276432,
            "alt": 10,
            "satellites": 8,
            "get_time": "2011-06-18 03:39:44",
            "address": "4B Albany Road, Manchester, Great Britain",
            "heading": 298,
            "speed": 70,
            "precision": 100,
            "gsm_lbs": true,
            "parking": true
        }
    ]
}
```

* `limit_exceeded` - boolean. `true` if the requested time period exceeds limit specified in a tracker's tariff.
* `lat` - float.  Latitude.
* `lng` - float.  Longitude.
* `alt` - int. Altitude in meters. 
* `satellites` - int. Number of satellites used in fix for this point.
* `get_time` - date/time. GPS timestamp of the point, in user's timezone.
* `address` - string. Point address. Will be "" if no address recorded.
* `heading` - int. Bearing in degrees (0..360).
* `speed` - int. Speed in km/h.
* `precision` - optional int. Precision in meters.
* `gsm_lbs` - optional boolean. `true` if location detected by GSM LBS.
* `parking` - optional boolean. `true` if point does not belong to track.

You can also [download](../resources/tracking/track/index.md#download) a KML file. 
You could use this file with map services. 
It is useful if you need to see all points on the map:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "from": "2020-09-23 03:24:00", "to": "2020-09-23 06:24:00", "format": "kml", "split": false}'
    ```


All parameters are the same with track/read plus two new optional parameters:

* `format` – string. File format, "kml" or "kmz". Default is "kml".
* `split` – boolean. If `true`, split tracks by folders with start/end placemarks and track line. Default `false`.
