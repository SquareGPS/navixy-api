---
title: Track
description: Contains API calls to interact with tracks and for getting all track points.
---

# Track

Contains API calls to interact with tracks and for getting tracks' points.

***

## API actions

API path: `/track`.

### download

Downloads track points as KML/KMZ file for the specified track ID, tracker and time period.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | `123456` |
| from | From date/time. | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 03:24:00"` |
| to | To date/time. Specified date must be after "from" date. | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 06:24:00"` |
| track_ids | Optional. If specified, only points belonging to the specified tracks will be returned. If not, any valid track points between "from" and "to" will be returned. | int array | `[123456, 234567]` | 
| include_gsm_lbs | Optional. If `false` && track_ids not specified, GSM LBS points will be filtered out. Default=`true`. | boolean | `true` |
| simplify | Optional. If `true` the returned track will be simplified. Default=`true`. | boolean | `true` |
| point_limit | Optional. If specified and `simplify=true`, the returned track will be simplified to contain this number of points. Min=2, Max=3000. If not specified, the server settings to decimates track will be used. It is not a hard limit, returned track may contain more points.| int | `300` |
| filter | Optional. If specified, the returned track will be filtered, applicable only for LBS tracks now. | boolean | `true` |
| format | File format, "kml" or "kmz", default is "kml". | [enum](../../../getting-started.md#data-types) | `"kml"` |
| split | If `true`, split tracks by folders with start/end placemarks and track line. Default=`false`. | boolean | `false` |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/download' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "from": "2020-09-23 03:24:00", "to": "2020-09-23 06:24:00", "format": "kml", "split": false}'
    ```

#### response

KML/KMZ file or JSON response if requested time period exceeds limit specified in a tracker's tariff:

```json
{ 
    "success": true, 
    "list": [], 
    "limit_exceeded": true 
}
```

#### errors

* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 211 - Requested time span is too big – if interval between "from" and "to" is too big (maximum value specified 
in API config).

***

### list

Gets a list of track descriptions for the specified tracker and time period.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | `123456` |
| from | From date/time. | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 03:24:00"` |
| to | To date/time. Specified date must be after "from" date. | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 06:24:00"` |
| filter | Optional, default=`true`. If `true`, tracks which are too short (in terms of length and number of points) will be omitted from resulting list. | boolean | `true` |
| split | Optional, default=`true`. If `false`, all tracks will be merged into single one.| boolean | `true` |
| include_gsm_lbs | Optional, default=`true`. If `false`, GSM LBS tracks will be filtered out. | boolean | `true` |
| cluster_single_reports | Optional, default=`false`. If `true`, single point reports will be clustered by its coordinates. | boolean | `false` | 
| count_events | Optional, default=`false`. If `true`, number of events occurred during each non-single point track will be returned. | `true` |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "from": "2020-09-23 03:24:00", "to": "2020-09-23 06:24:00"}'
    ```

#### response

```json
{
    "success": true,
    "limit_exceeded": false,
    "list": [<track_info>]
}
```

* `limit_exceeded` - boolean. `true` if the requested time period exceeds limit specified in a tracker's tariff.
* `list` - array of JSON objects. List of zero or more JSON objects.

where <track_info> is either <regular>, <single_report>, <merged> or <cluster>:

`regular` object:

```json
{
    "id": 123456,
    "start_date": "2020-09-23 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "max_speed": 62,
    "end_date": "2020-09-23 06:39:44",
    "end_address": "888 5th Ave, New York, NY 10021, USA",
    "length": 5.5,
    "points": 327,
    "avg_speed": 49,
    "event_count": 3,
    "norm_fuel_consumed": 1.07,
    "type": "regular",
    "gsm_lbs": false
}
```

* `id` - int. Track id.
* `start_date` - [date/time](../../../getting-started.md#data-types). Track start date, in user's timezone e.g. "2011-06-18 03:39:44".
* `start_address` - string. Track start address.
* `max_speed` - int. Maximum speed in km/h, e.g. 96.
* `end_date` - [date/time](../../../getting-started.md#data-types). Track end date, in user's timezone e.g. "2011-06-18 05:18:36".
* `end_address` - string. Track end address.
* `length` - float. Track length in kilometers, e.g. 85.5.
* `points` - int. Total number of points in a track, e.g. 724.
* `avg_speed` - int. Average speed in km/h, e.g. 70.
* `event_count` - int. Number of events on this track. Field will be omitted if "count_events" is `false`.
* `norm_fuel_consumed` - float. A consumed fuel on track, litres. Field will be omitted if no vehicle bound to tracker 
or no normAvgFuelConsumption defined in a vehicle.
* `type` - [enum](../../../getting-started.md#data-types): `regular`, `single_report`, `merged`, `cluster`. 
  Used to distinguish this track type (`regular`) from the others. 
* `gsm_lbs` - optional boolean. GSM LBS point flag.

`single_report` object. Returned if device was creating reports in "interval" mode (e.g. M7 tracker in interval mode):

```json
{
    "id": 123456,
    "start_date": "2020-09-24 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "avg_speed": 34,
    "gsm_lbs": false,
    "type": "single_report",
    "precision": 10
}
```

* `id` - int. Track id.
* `start_date` - [date/time](../../../getting-started.md#data-types). Point creation date, in user's timezone e.g. "2011-06-18 03:39:44".
* `start_address` - string. Point address.
* `avg_speed` - int. Average speed in km/h, e.g. 70.
* `gsm_lbs` - optional boolean. GSM LBS point flag.
* `type` - [enum](../../../getting-started.md#data-types): `regular`, `single_report`, `merged`, `cluster`.
  Used to distinguish this track type (`single_report`) from the others.
* `precision` - optional int. Location precision, meters.


`merged` object. Only returned if "split" is set to `false`:

```json
{
    "start_date": "2020-09-24 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "max_speed": 62,
    "end_date": "2020-09-24 06:39:44",
    "end_address": "888 5th Ave, New York, NY 10021, USA",
    "length": 5.5,
    "points": 327,
    "avg_speed": 49,
    "event_count": 3,
    "norm_fuel_consumed": 1.07,
    "type": "merged",
    "gsm_lbs": false
}
```

* `start_date` - [date/time](../../../getting-started.md#data-types). Track start date, in user's timezone e.g. "2011-06-18 03:39:44".
* `start_address` - string. Track start address.
* `max_speed` - int. Maximum speed in km/h, e.g. 96.
* `end_date` - [date/time](../../../getting-started.md#data-types). Track end date, in user's timezone e.g. "2011-06-18 05:18:36".
* `end_address` - string. Track end address.
* `length` - float. Track length in kilometers, e.g. 85.5.
* `points` - int. Total number of points in a track, e.g. 724.
* `avg_speed` - int. Average speed in km/h, e.g. 70.
* `event_count` - int. Number of events on this track. Field will be omitted if "count_events" is `false`.
* `norm_fuel_consumed` - float. A consumed fuel on track, litres. Field will be omitted if no vehicle bound to tracker 
or no normAvgFuelConsumption defined in a vehicle.
* `type` - [enum](../../../getting-started.md#data-types): `regular`, `single_report`, `merged`, `cluster`. 
  Used to distinguish this track type (`merged`) from the others. 
* `gsm_lbs` - optional boolean. GSM LBS flag.

`cluster` object. Only returned if "split" is set to `true`:

```json
{
    "start_date": "2020-09-24 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "end_date": "2020-09-24 06:39:44",
    "precision": 500,
    "points": [{"lat": 56.829274,"lng": 60.597125}, {"lat": 56.829279,"lng": 60.597123}],
    "type": "cluster",
    "gsm_lbs": false
}
```

* `start_date` - [date/time](../../../getting-started.md#data-types). Track start date, in user's timezone e.g. "2011-06-18 03:39:44".
* `start_address` - string. Track start address.
* `end_date` - [date/time](../../../getting-started.md#data-types). Track end date, in user's timezone e.g. "2011-06-18 05:18:36".
* `precision` - optional int. Location precision, meters.
* `points` - array of points in a cluster.
* `type` - [enum](../../../getting-started.md#data-types): `regular`, `single_report`, `merged`, `cluster`. 
  Used to distinguish this track type (`cluster`) from the others. 
* `gsm_lbs` - optional boolean. GSM LBS flag, true if cluster contains only GSM LBS points.

#### errors

* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 211 - Requested time span is too big – if interval between "from" and "to" is too big (maximum value specified in 
API config).

***

### read

Gets track points for the specified track ID, tracker and time period.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| from | From date/time. | [date/time](../../../getting-started.md#datetime-formats) | "2020-09-23 03:24:00" |
| to | To date/time. Specified date must be after "from" date. | [date/time](../../../getting-started.md#datetime-formats) | "2020-09-23 06:24:00" |
| track_id | Optional. If specified, only points belonging to the specified track will be returned. If not, any valid track points between "from" and "to" will be returned. | int | 234567 |
| include_gsm_lbs | Optional, default=`true`. If `false` && track_id not specified, GSM LBS points will be filtered out. | boolean | true |
| simplify | Optional. If `true` the returned track will be simplified. Default=`true`. | boolean | `true` |
| point_limit | Optional. If specified and `simplify=true`, the returned track will be simplified to contain this number of points. Min=2, Max=3000. If not specified, the server settings to decimates track will be used. It is not a hard limit, returned track may contain more points.| int | `300` |
| filter | Optional. If specified, the returned track will be filtered, applicable only for LBS tracks now. If `false` a response will contain parking points. | boolean | false |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "from": "2020-09-23 03:24:00", "to": "2020-09-23 06:24:00"}'
    ```

#### response

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
            "parking": true,
            "buffered": true
        }
    ]
}
```

* `limit_exceeded` - boolean. `true` if requested time period exceeds limit specified in a tracker's tariff.
* `lat` - float.  Latitude.
* `lng` - float.  Longitude.
* `alt` - int. Altitude in meters. 
* `satellites` - int. Number of satellites used in fix for this point.
* `get_time` - [date/time](../../../getting-started.md#data-types). GPS timestamp of the point, in user's timezone.
* `address` - string. Point address. Will be "" if no address recorded.
* `heading` - int. Bearing in degrees (0..360).
* `speed` - int. Speed in km/h.
* `precision` - optional int. Precision in meters.
* `gsm_lbs` - optional boolean. `true` if location detected by GSM LBS.
* `parking` - optional boolean. `true` if point does not belong to track.
* `buffered` - optional boolean. `true` if point was saved in device memory and transferred to server later.

#### errors

* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 211 - Requested time span is too big – if interval between "from" and "to" is too big (maximum value specified in 
API config).
