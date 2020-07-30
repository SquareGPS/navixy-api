---
title: Track
description: Track
---

# Track

API path: `/track`.

## download()
Download track points as KML/KMZ file for the specified track ID, tracker and time period.

#### parameters
* **tracker_id** – **int**. ID of the tracker (aka "object_id"). Tracker must belong to authorized user and must not be blocked.
* **from** – **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone).
* **to** – **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). Specified date must be after "from" date.
* **track_ids** – **array of int**. (optional) If specified, only points belonging to the specified tracks will be returned. If not, any valid track points between "from" and "to" will be returned.
* **include_gsm_lbs** – **boolean**. (optional, default=true) If false && track_ids not specified, GSM LBS points will be filtered out.
* **point_limit** – **int**. (optional) If specified, the returned track will be simplified to contain this number of points. Min=2, Max=3000.
* **filter** – **boolean**. (optional) If specified, the returned track will be filtered, applicable only for LBS tracks now.
* **format** – **string**. file format, "kml" or "kmz", default is "kml".
* **split** – **boolean**. If true, split tracks by folders with start/end placemarks and track line. default "false".

#### return
_KML/KMZ file_ or _JSON response_ if requested time period exceeds limit specified in tracker's tariff:
```js
{ 
    "success": true, 
    "list": [], 
    "limit_exceeded": true 
}
```

#### errors
*   204 (Entity not found) – if there is no tracker with such ID belonging to authorized user.
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
*   211 (Requested time span is too big) – if interval between "from" and "to" is too big (maximum value is specified in API config.

## list()
Get a list of track descriptions for the specified tracker and time period.

#### parameters
* **tracker_id** – **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and must not be blocked.
* **from** – **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user’s timezone)
* **to** – **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user’s timezone). Specified date must be after “from” date.
* **filter** – **boolean**. (optional, default=true) If true, tracks which are too short (in terms of length and number of points) will be omitted from resulting list.
* **split** – **boolean**. (optional, default=true) If false, all tracks will be merged into single one.
* **include_gsm_lbs** – **boolean**. (optional, default=true) If false, GSM LBS tracks will be filtered out.
* **cluster_single_reports** – **boolean**. (optional, default=false) If true, single point reports will be clustered by its coordinates.
* **count_events** – **boolean**. (optional, default=false) If true, number of events occurred during each non-singlepoint track will be returned.

#### return
```js
{
    "success": true,
    "limit_exceeded": <true if requested time period exceeds limit specified in tracker's tariff>, //boolean
    "list": [ <track_info>, ... ] //list of zero or more JSON objects
}
```
where <track_info> is either <regular>, <single_report>, <merged> or <cluster>:
```js
<regular> =
{
    "id": <track id>, //int
    "start_date": <track start date, in user's timezone e.g. "2011-06-18 03:39:44">,  //string
    "start_address": <track start address>, //string
    "max_speed": <maximum speed in km/h, e.g. 96>, //int
    "end_date": <track end date, in user's timezone e.g. "2011-06-18 05:18:36">,  //string
    "end_address": <track end address>, //string
    "length": <track length in kilometers, e.g. 85.5>, //float
    "points": <total number of points in track, e.g. 724>,  //int
    "avg_speed": <average speed in km/h, e.g. 70>,  //int
    "event_count": 3, //number of events on this track. Field is omitted if "count_events" is "false"
    "norm_fuel_consumed": 11.07, //consumed fuel on track, litres. Field is omitted if no vehicle binded to tracker or no normAvgFuelConsumption defined in vehicle
    "type": "regular",  //used to distinguish this track type from the others,
    "gsm_lbs": <GSM LBS point flag, optional>  //boolean
}

<single_report> = //returned if device was creating reports in "interval" mode (e.g. M7 tracker in interval mode)
{
    "id": <track id>, //int
    "type": "single_report", //used to distinguish this track type from the others
    "start_date": <point creation date in user's timezone e.g. "2011-06-16 15:35:01">,
    "start_address": <point address>, //string
    "avg_speed": <point speed in km/h, e.g. 34>,  //int
    "gsm_lbs": <GSM LBS point flag, optional>,  //boolean
    "precision": <location precision, meters, optional>  //int
}

<merged> =   //only returned if "split" is set to "false"
{
    "start_date": <track start date, in user's timezone e.g. "2011-06-18 03:39:44">,  //string
    "start_address": <track start address>, //string
    "max_speed": <maximum speed in km/h, e.g. 96>, //int
    "end_date": <track end date, in user's timezone e.g. "2011-06-18 05:18:36">,  //string
    "end_address": <track end address>, //string
    "length": <track length in kilometers, e.g. 85.5>, //float
    "points": <total number of points in track, e.g. 724>,  //int
    "avg_speed": <average speed in km/h, e.g. 70>,  //int
    "event_count": 3, //number of events on this track. Field is omitted if "count_events" is "false"
    "norm_fuel_consumed": 11.07, //consumed fuel on track, litres. Field is omitted if no vehicle binded to tracker or no normAvgFuelConsumption defined in vehicle
    "type": "merged",  //used to distinguish this track type from the others,
    "gsm_lbs": <GSM LBS point flag, optional>  //boolean
}

<cluster> =   //only returned if "split" is set to "true"
{
    "start_date": <track start date, in user's timezone e.g. "2011-06-18 03:39:44">,  //string
    "start_address": <track start address>, //string
    "end_date": <track end date, in user's timezone e.g. "2011-06-18 05:18:36">,  //string
    "precision": <radius in meters, e.g. 500>, //int
    "points": [<array of points in cluster, {"lat": 56.829279,"lng": 60.597123}>],  //array of points
    "type": "cluster",  //used to distinguish this track type from the others,
    "gsm_lbs": <GSM LBS flag, true if cluster contains only GSM LBS points>  //boolean
}
```

#### errors
*   204 (Entity not found) – if there is no tracker with such ID belonging to authorized user.
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
*   211 (Requested time span is too big) – if interval between "from" and "to" is too big (maximum value is specified in API config.

## read()
Get track points for the specified track ID, tracker and time period.

#### parameters
* **tracker_id** – **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and must not be blocked.
* **from** – **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user’s timezone).
* **to** – **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user’s timezone). Specified date must be after “from” date.
* **track_id** – **int**. (optional) If specified, only points belonging to the specified track will be returned. If not, any valid track points between “from” and “to” will be returned.
* **include_gsm_lbs** – **boolean**. (optional, default=true) If false && track_id not specified, GSM LBS points will be filtered out.
* **point_limit** – **int**. (optional) If specified, the returned track will be simplified to contain this number of points. Min=2, Max=3000
* **filter** – **boolean**. (optional) If specified, the returned track will be filtered, applicable only for LBS tracks now.

#### return
```js
{
    "success": true,
    "limit_exceeded": true,   // boolean. true if requested time period exceeds limit specified in tracker's tariff
    "list": [
        {
            "lat": 53.445181, // latitude
            "lng": -2.276432, // longitude
            "alt": 10,        // int. altitude in meters
            "satellites": 8,  // number of satellites used in fix for this point
            "get_time": "2011-06-18 03:39:44",  // GPS timestamp of the point, in user's timezone
            "address": "4B Albany Road, Manchester, Great Britain", // string. point address. "" if no addresss was recorded
            "heading": 298,   // int. bearing in degrees (0..360)
            "speed": 70,      // int. speed in km/h
            "precision": 100, // int. precision in meters, optional
            "gsm_lbs": true,  // boolean. true if location is detected by GSM LBS, optional
            "parking": true,  // boolean. true if point does not belongs to track, optional
        }, ...
    ]
}
```

#### errors
*   204 (Entity not found) – if there is no tracker with such ID belonging to authorized user.
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
*   211 (Requested time span is too big) – if interval between “from” and “to” is too big (maximum value is specified in API config).
