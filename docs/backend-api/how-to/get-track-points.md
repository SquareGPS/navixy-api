---
title: Get track points for trips
description: About getting all points for trips
---

# How to get track points for trips

Sometimes necessary to get all points of a trip with more info about the device's moves.
How to get them?

Firstly you need to [get hash](./get-session-hash.md).

Once you get the hash, you need to [get your tracker_id](./get-tracker-list.md). The platform must know points for what device must be in reply.

Now you can get all points for the interesting period using [`/track/read` API call](../resources/tracking/track/index.md#read).  
Parameters that necessary for this call:

* `tracker_id` - we got them in [tracker/list](../resources/tracking/tracker/index.md#list) call. Use only one tracker_id per call. It should be an integer.
* `from` - a string containing start [date/time](../getting-started.md#data-types) in `yyyy-MM-dd HH:mm:ss` format (in user's timezone).
* `to` - a string containing end [date/time](../getting-started.md#data-types) in `yyyy-MM-dd HH:mm:ss` format (in user's timezone).

Optional parameters:

* `track_id` - we can get them using [track/list](../resources/tracking/track/index.md#list) API call.
  If specified, only points belonging to the specified track will be returned. If not, 
  any valid track points between `from` and `to` will be returned. 
  All requested track ids must be unique and not null.
* `include_gsm_lbs` – boolean parameter. It may contain true or false. 
  If false && track_id not specified, GSM LBS points will be filtered out. It is true by default.
* `point_limit` – integer. If it specified, the returned track would be simplified to contain
  this number of points. Min=2, Max=3000.
* `filter` – boolean. If true, the returned track will be filtered, applicable only for LBS tracks. 
  It is false by default.

The platform will reply:

```json5
{
    "success": true,
    "limit_exceeded": true, // boolean. true if requested time period exceeds limit specified in tracker's tariff
    "list": [
      {
        "lat": 53.445181, // latitude
        "lng": -2.276432, // longitude
        "alt": 10, // int. altitude in meters
        "satellites": 8, // number of satellites used in fix for this point
        "get_time": "2011-06-18 03:39:44", // GPS timestamp of the point, in user's timezone
        "address": "4B Albany Road, Manchester, Great Britain", // string. point address. "" if no addresss was recorded
        "heading": 298, // int. bearing in degrees (0..360)
        "speed": 70, // int. speed in km/h
        "precision": 100, // int. precision in meters, optional
        "gsm_lbs": true, // boolean. true if location is detected by GSM LBS, optional
        "parking": true, // boolean. true if point does not belongs to track, optional
      }, ...
    ]}
```
You can also [download](../resources/tracking/track/index.md#download) a KML file. 
You could use this file with map services. 
It is useful if you need to see all points on the map:

    {{ extra.api_example_url }}/track/download

All parameters are identical with track/read with the except of two new optional parameters:

* `format` – string. File format, "kml" or "kmz". Default is "kml".
* `split` – boolean. If true, split tracks by folders with start/end placemarks and track line. Default "false".
