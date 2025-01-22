# Getting Track Points

In many scenarios, it becomes essential to retrieve all location points of a track to gain comprehensive insights into the movements of an object equipped with a GPS tracker. This guide will demonstrate how to accomplish this using the Navixy API.

## Prerequisites

### Obtain API Key Hash
First, you need to [obtain the hash of an API key](../../getting-started/authentication.md).

### Get Tracker ID
Next, [retrieve your tracker_id](get-tracker-list.md). This ID is essential as the platform needs to know which device's points to return.

## Retrieve Track Points

With the API key hash and tracker ID in hand, you can now get all points for a specified period using the [`/track/read`](../../resources/tracking/track/index.md#read) API method.

### Required Parameters
* `tracker_id` - Obtained from the [`tracker/list`](../../resources/tracking/tracker/index.md#list) call. Only one tracker_id per call. It should be an integer.
* `from` - A string containing the start [`date/time`](../../getting-started/introduction.md#datetime-formats).
* `to` - A string containing the end [`date/time`](../../getting-started/introduction.md#datetime-formats).

For a full description of the parameters, see the [`/track/read`](../../resources/tracking/track/index.md#read)API method.

### Example Response
The platform will respond with the following data:

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

### Response Fields
* `limit_exceeded` - boolean. `true` if the requested time period exceeds the limit specified in the tracker's tariff.
* `lat` - float. Latitude.
* `lng` - float. Longitude.
* `alt` - int. Altitude in meters.
* `satellites` - int. Number of satellites used for this point.
* `get_time` - date/time. GPS timestamp of the point, in the user's timezone.
* `address` - string. Point address. Will be "" if no address is recorded.
* `heading` - int. Bearing in degrees (0..360).
* `speed` - int. Speed in km/h.
* `precision` - optional int. Precision in meters.
* `gsm_lbs` - optional boolean. `true` if the location is detected by GSM LBS.
* `parking` - optional boolean. `true` if the point does not belong to the track.

## Download Track Points as KML File

You can also [download](../../resources/tracking/track/index.md#download) a KML file. This file can be used with map services to visualize all points on a map.

### Example Request

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/track/download' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "from": "2020-09-23 03:24:00", "to": "2020-09-23 06:24:00", "format": "kml", "split": false}'
```

### Additional Parameters
All parameters are the same as in `track/read` plus two new optional parameters:

* `format` – string. File format, either "kml" or "kmz". Default is "kml".
* `split` – boolean. If `true`, splits tracks by folders with start/end placemarks and track line. Default is `false`.

By following these steps, you can effectively retrieve and utilize track points for detailed analysis of device movements.