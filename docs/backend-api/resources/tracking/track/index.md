---
title: Track
description: Contains API calls to interact with tracks and for getting all track points.
---

# Track

This section includes API calls that allow you to interact with tracks and retrieve track points.

Learn more about the track API by following our [instructions](../../../how-to/get-track-points.md).

***

## API actions

API path: `/track`.

### download

This method allows you to download track points as a KML/KMZ file which can be used in other apps to show tracks.

#### parameters

| name            | description                                                                                                                                                                                                                                                                                                                                                                                   | type                                                      | format                  |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|:------------------------|
| tracker_id      | ID of the tracker (aka "object_id"). The tracker must be associated with the user whose hash is being used for the request, and not tariff-blocked.                                                                                                                                                                                                                                           | int                                                       | `123456`                |
| from            | The start date/time for your KML file's track points. The file begins with the next point after this time.                                                                                                                                                                                                                                                                                    | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 03:24:00"` |
| to              | An end date/time for your KML file's track points. The file concludes with the last point before this time. Ensure this date is later than the "from" date.                                                                                                                                                                                                                                   | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 06:24:00"` |
| track_ids       | Optional. If specified, the file will only contain points from selected tracks. If not, it includes all valid points between the "from" and "to" times.                                                                                                                                                                                                                                       | int array                                                 | `[123456, 234567]`      | 
| include_gsm_lbs | Optional. If set to `false` without specified track_ids, GSM LBS points will be excluded. Default is true.                                                                                                                                                                                                                                                                                    | boolean                                                   | `true`                  |
| simplify        | Optional. If set to `true`, tracks in the returned file will be simplified with fewer points, optimized for uploading to other apps. Default is `true`.                                                                                                                                                                                                                                       | boolean                                                   | `true`                  |
| point_limit     | Optional. If it is specified and `simplify=true`, the returned tracks in a file will be reduced to contain that specified number of points. The minimum value is 2, and the maximum is 3000. If it is not specified, the server's default settings for simplifying tracks will be applied. This is not a strict limit; the returned file can potentially contain more points than specified.  | int                                                       | `300`                   |
| filter          | Optional. If this is set to `true`, the returned tracks in a file will be filtered. This is currently only applicable to LBS tracks.                                                                                                                                                                                                                                                          | boolean                                                   | `true`                  |
| format          | File format can be "kml" or "kmz". Default is "kml".                                                                                                                                                                                                                                                                                                                                          | [enum](../../../getting-started.md#data-types)            | `"kml"`                 |
| split           | If set to `true`, tracks in the file will be split by stops into folders with start/end markers. Default is`false`.                                                                                                                                                                                                                                                                           | boolean                                                   | `false`                 |

#### example

Let's consider an example, where we're looking for a KML file for a tracker with ID 1683258 that doesn't break down by stops. 
The data should cover trips starting from 3:24 AM to 6:24 AM on November 19, 2023, according to the user's local time.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 1683258, "from": "2023-11-19 03:24:00", "to": "2023-11-19 06:24:00", "format": "kml", "split": false}'
    ```

#### response

In case the available storage period is not exceeded, you will get the file.

!!!+ example "KML file example with two points"

    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0">
      <Document>
        <name>track-John (Scania) 2023-11-19 03:24:00</name>
        <Placemark>
          <name>point #1</name>
          <visibility>1</visibility>
          <description>2023-11-19 03:24:03</description>
          <TimeStamp>
            <when>2023-11-19T03:24:03.000-06:00</when>
          </TimeStamp>
          <ExtendedData>
            <Data name="speed">
              <value>37</value>
            </Data>
            <Data name="heading">
              <value>27</value>
            </Data>
          </ExtendedData>
          <Point>
            <coordinates>-78.768105,43.1172216</coordinates>
          </Point>
        </Placemark>
        <Placemark>
          <name>point #2</name>
          <visibility>1</visibility>
          <description>2023-11-19 03:27:11</description>
          <TimeStamp>
            <when>2023-11-19T03:27:11.000-06:00</when>
          </TimeStamp>
          <ExtendedData>
            <Data name="speed">
              <value>57</value>
            </Data>
            <Data name="heading">
              <value>13</value>
            </Data>
          </ExtendedData>
          <Point>
            <coordinates>-78.7549233,43.1356483</coordinates>
          </Point>
        </Placemark>
      </Document>
    </kml>
    ```

For example, if the device's plan has maximum available storage period 3 months (default value) and we request data from 
6 months, the response will contain JSON with the next information: 

```json
{
  "list": [],
  "limit_exceeded": true,
  "success": true
}
```

#### errors

* 201 - Not found in database – the tracker ID in your request may not match any trackers linked to the user account with this 
session hash. Ensure the correct tracker_id and hash of an appropriate user are used.
* 208 - Device blocked – if a tracker exists under this user account but is currently inactive due to tariff plan 
restrictions or any other reason.
* 211 - Requested time span is too big – If the interval between the "from" and "to" dates is too large, it may exceed 
the maximum value defined in the API configuration.

***

### list

This method retrieves a list of tracks for a given tracker within a specified time period.

#### parameters

| name                   | description                                                                                                                                                                                                                                                                                                                                            | type                                                      | format                  |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|:------------------------|
| tracker_id             | ID of the tracker (aka "object_id"). The tracker must be associated with the user whose hash is being used for the request, and not tariff-blocked.                                                                                                                                                                                                    | int                                                       | `123456`                |
| from                   | The start date/time for trips. The response begins with the next trip point after this time.                                                                                                                                                                                                                                                           | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 03:24:00"` |
| to                     | An end date/time for trips. The response concludes with the last point before this time. Ensure this date is later than the "from" date.                                                                                                                                                                                                               | [date/time](../../../getting-started.md#datetime-formats) | `"2020-09-23 06:24:00"` |
| filter                 | Optional. Default is `true`. If set to `true`, any tracks that are deemed too short, based on their length and number of points, will be excluded from the final list.                                                                                                                                                                                 | boolean                                                   | `true`                  |
| split                  | Optional. Default is `true`. If set to `false`, all the tracks will be combined into one single track within the period.                                                                                                                                                                                                                               | boolean                                                   | `true`                  |
| include_gsm_lbs        | Optional. Default is `true`. If set to `false`, GSM LBS points will be excluded.                                                                                                                                                                                                                                                                       | boolean                                                   | `true`                  |
| cluster_single_reports | Optional. Default is `false`. If set to `true`, trips consisting of a single point will be grouped together based on their coordinates.                                                                                                                                                                                                                | boolean                                                   | `false`                 | 
| count_events           | Optional. Default is `false`. If set to `true`, the system will return the count of events that occurred during each track that isn't a single point.                                                                                                                                                                                                  | boolean                                                   | `false`                 |
| omit_addresses         | Optional. Default is `false`. If set to `true`, address parameters will be empty.                                                                                                                                                                                                                                                                      | boolean                                                   | `false`                 |
| with_points            | Optional. Default is `false`. If set to `true`, track point lists will be included.                                                                                                                                                                                                                                                                    | boolean                                                   | `false`                 |
| point_limit            | Optional. If specified, the returned data will be reduced to contain that specified number of points. The minimum value is 2, and the maximum is 3000. If it is not specified, the server's default settings for simplifying tracks will be applied. This is not a strict limit; the returned data can potentially contain more points than specified. | int                                                       | `300`                   |

#### example

For example, if we need to retrieve all trips for tracker 1683258 in November, without applying smart filter, including 
LBS points recorded, without clustering, separated by parkings, while also counting the number of events that occur during 
each trip, we only need to specify the "filter" and "count_events" from optional parameters. This is because the other optional 
settings will provide us with necessary info by default.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 1683258, "from": "2023-11-01 03:24:00", "to": "2023-11-30 06:24:00", "filter": false, "count_events": true}'
    ```

#### response

```json
{
    "success": true,
    "limit_exceeded": false,
    "list": [track_info]
}
```

* `limit_exceeded` - boolean. It will be `true` if the requested time period surpasses the limit set in the tracker's tariff. 
For instance, if the device's plan has a maximum storage period of three months (the default value), and we request trips 
for six months.
* `list` - an array of JSON objects containing track information. It consists of zero or more JSON objects. Zero objects 
indicates that there were no trips based on the track options or the device didn't supply any points to the platform.

where `track_info` is either `regular`, `single_report`, `merged` or `cluster`:

`regular` object:

```json
{
    "id": 123456,
    "start_date": "2023-11-23 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "max_speed": 62,
    "end_date": "2023-11-23 06:39:44",
    "end_address": "888 5th Ave, New York, NY 10021, USA",
    "length": 5.5,
    "points": 327,
    "avg_speed": 49,
    "event_count": 3,
    "norm_fuel_consumed": 1.07,
    "type": "regular",
    "gsm_lbs": false,
    "points_list": [point_info] 
}
```

* `id` - int. Track id.
* `start_date` - [date/time](../../../getting-started.md#data-types). Track start date, in user's timezone e.g. "2011-06-18 03:39:44".
* `start_address` - string. Track start address.
* `max_speed` - int. Maximum speed registered during track in km/h, e.g. 96.
* `end_date` - [date/time](../../../getting-started.md#data-types). Track end date, in user's timezone e.g. "2011-06-18 05:18:36".
* `end_address` - string. Track end address.
* `length` - float. Track length in kilometers, e.g. 85.5.
* `points` - int. Total number of points in a track, e.g. 724.
* `avg_speed` - int. Average speed in km/h, e.g. 70.
* `event_count` - int. It represents the number of events recorded during this track. This field will not be present if "count_events" is set to `false`.
* `norm_fuel_consumed` - float. It is representing the amount of fuel consumed during the track, measured
  in litres. This field will not be present if there's no [vehicle_object](../../fleet/vehicle/index.md#vehicle) linked to the
  tracker or if "normAvgFuelConsumption" is not defined for the linked vehicle object.
* `type` - [enum](../../../getting-started.md#data-types) with possible values: `regular`, `single_report`, `merged`, `cluster`. 
It's used to differentiate this regular track type from other types.
* `gsm_lbs` - optional boolean. GSM LBS point flag.
* `points_list` - array of JSON objects. A list of [point info](#point-info).

`single_report` object is returned when the device operates in "interval" mode or only one point per track is provided 
(for example, an M7 tracker operating in interval mode):

```json
{
    "id": 123456,
    "start_date": "2023-11-24 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "avg_speed": 34,
    "gsm_lbs": false,
    "type": "single_report",
    "precision": 10,
    "points_list": [point_info]
}
```

* `id` - int. Track id.
* `start_date` - [date/time](../../../getting-started.md#data-types). It represents the date and time when the tracker registered the point, adjusted to 
the user's timezone, for example, "2011-06-18 03:39:44".
* `start_address` - string. Point address.
* `avg_speed` - int. Average speed in km/h, e.g. 70.
* `gsm_lbs` - optional boolean. GSM LBS point flag.
* `type` - [enum](../../../getting-started.md#data-types): `regular`, `single_report`, `merged`, `cluster`.
  Used to distinguish this track type (`single_report`) from the others.
* `precision` - optional int. It signifies the precision of the location in meters. Its presence relies on the device model.
* `points_list` - array of JSON objects. A list of [point info](#point-info).

`merged` object. Only returned if "split" is set to `false`:

```json
{
    "start_date": "2023-11-24 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "max_speed": 62,
    "end_date": "2023-11-24 06:39:44",
    "end_address": "888 5th Ave, New York, NY 10021, USA",
    "length": 5.5,
    "points": 327,
    "avg_speed": 49,
    "event_count": 3,
    "norm_fuel_consumed": 1.07,
    "type": "merged",
    "gsm_lbs": false,
    "points_list": [point_info]
}
```

* `start_date` - [date/time](../../../getting-started.md#data-types). Track start date, in user's timezone e.g. "2011-06-18 03:39:44". It signifies the 
initial point identified as a track for a specified time period.
* `start_address` - string. Track start address.
* `max_speed` - int. Maximum speed registered during period in km/h, e.g. 96.
* `end_date` - [date/time](../../../getting-started.md#data-types). Track end date, in user's timezone e.g. "2011-06-18 05:18:36". It signifies the
last point identified as a track for a specified time period.
* `end_address` - string. Track end address.
* `length` - float. Track length during period in kilometers, e.g. 85.5.
* `points` - int. Total number of points in a track, e.g. 724.
* `avg_speed` - int. Average speed in km/h, e.g. 70.
* `event_count` - int. It represents the number of events recorded during this track. This field will not be present if "count_events" is set to `false`.
* `norm_fuel_consumed` - float. It is representing the amount of fuel consumed during the track, measured
  in litres. This field will not be present if there's no [vehicle_object](../../fleet/vehicle/index.md#vehicle) linked to the
  tracker or if "normAvgFuelConsumption" is not defined for the linked vehicle object.
* `type` - [enum](../../../getting-started.md#data-types): `regular`, `single_report`, `merged`, `cluster`. 
  Used to distinguish this track type (`merged`) from the others. 
* `gsm_lbs` - optional boolean. GSM LBS flag.
* `points_list` - array of JSON objects. A list of [point info](#point-info).

`cluster` object. Can be returned only if "split" is set to `true`:

```json
{
    "start_date": "2023-11-24 03:39:44",
    "start_address": "1255 6th Ave, New York, NY 10020, USA",
    "end_date": "2020-09-24 06:39:44",
    "precision": 500,
    "points": [{"lat": 34.178868, "lng": -118.599672}, {"lat": 31.738386, "lng": -106.453854}],
    "type": "cluster",
    "gsm_lbs": false
}
```

* `start_date` - [date/time](../../../getting-started.md#data-types). Track start date, in user's timezone e.g. "2011-06-18 03:39:44".
* `start_address` - string. Track start address.
* `end_date` - [date/time](../../../getting-started.md#data-types). Track end date, in user's timezone e.g. "2011-06-18 05:18:36".
* `precision` - optional int. It signifies the precision of the location in meters. Its presence relies on the device model.
* `points` - array of point objects in a cluster.
* `type` - [enum](../../../getting-started.md#data-types): `regular`, `single_report`, `merged`, `cluster`. 
  Used to distinguish this track type (`cluster`) from the others. 
* `gsm_lbs` - optional boolean. GSM LBS flag. If a cluster only contains GSM LBS points, then this value will be set to `true`.

#### errors

* 201 - Not found in database – the tracker ID in your request may not match any trackers linked to the user account with this
  session hash. Ensure the correct tracker_id and hash of an appropriate user are used.
* 208 - Device blocked – if a tracker exists under this user account but is currently inactive due to tariff plan
  restrictions or any other reason.
* 211 - Requested time span is too big – If the interval between the "from" and "to" dates is too large, it may exceed
  the maximum value defined in the API configuration.

***

### read

This method fetches all track points that a GPS tracker has recorded and sent to the platform within a specified time 
frame. The timestamp for each point corresponds to when the tracker recorded the point, adjusted to the user's time zone.

#### parameters

| name            | description                                                                                                                                                                                                                                                                                                                                                                      | type                                                      | format                |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|:----------------------|
| tracker_id      | ID of the tracker (aka "object_id"). The tracker must be associated with the user whose hash is being used for the request, and not tariff-blocked.                                                                                                                                                                                                                              | int                                                       | 123456                |
| from            | The start date/time for trips. The response begins with the next trip point after this time.                                                                                                                                                                                                                                                                                     | [date/time](../../../getting-started.md#datetime-formats) | "2020-09-23 03:24:00" |
| to              | An end date/time for trips. The response concludes with the last point before this time. Ensure this date is later than the "from" date.                                                                                                                                                                                                                                         | [date/time](../../../getting-started.md#datetime-formats) | "2020-09-23 06:24:00" |
| track_id        | Optional. If a specific track is identified, only points related to that track will be provided. If no track is specified, all valid track points recorded within the specified "from" and "to" timeframe will be returned.                                                                                                                                                      | int                                                       | 234567                |
| include_gsm_lbs | Optional. Default is `true`. If the value is `false` && a track_id is not provided, the GSM LBS points will be excluded from the results.                                                                                                                                                                                                                                        | boolean                                                   | true                  |
| simplify        | Optional. Default is `true`. If set to `true`, the returned data will be simplified, resulting in fewer points.                                                                                                                                                                                                                                                                  | boolean                                                   | `true`                |
| point_limit     | Optional. If it is specified and `simplify=true`, the returned data will be reduced to contain that specified number of points. The minimum value is 2, and the maximum is 3000. If it is not specified, the server's default settings for simplifying tracks will be applied. This is not a strict limit; the returned data can potentially contain more points than specified. | int                                                       | `300`                 |
| filter          | Optional. If this is set to `true`, the returned tracks will be filtered. This is currently only applicable to LBS tracks. If set to `false`, the response will include parking points.                                                                                                                                                                                          | boolean                                                   | false                 |

#### example

For instance, if we need to obtain track points for tracker 1683258 that fall within November 1, and are solely part of 
track ID 923150, without applying a smart filter, LBS points and simplifier. Since these optional parameters by default 
are `true`, we should list them in our request.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 1683258, "track_id": 923150, "from": "2023-11-01 00:00:00", "to": "2023-11-01 23:59:59", "filter": false, "simplify": false, "include_gsm_lbs": false}'
    ```

#### response

```json
{
    "success": true,
    "limit_exceeded": true,
    "list": [point_info]
}
```

* `limit_exceeded` - boolean. It will be `true` if the requested time period surpasses the limit set in the tracker's tariff.
  For instance, if the device's plan has a maximum storage period of three months (the default value), and we request trips
  for six months.
* `list` - array of JSON objects. A list of [point info](#point-info).

#### point info

```json
{
    "lat": 43.0375133,
    "lng": -79.226505,
    "alt": 0,
    "satellites": 10,
    "mileage": 43.93,
    "get_time": "2023-11-01 04:38:39",
    "address": "Kottmeier Road, Thorold, Golden Horseshoe, Ontario, Canada, L3B 5N6",
    "heading": 280,
    "speed": 53,
    "precision": 100,
    "gsm_lbs": false,
    "parking": false,
    "buffered": true
}
```

* `lat` - float. Represents latitude.
* `lng` - float. Represents longitude.
* `alt` - int. Indicates the altitude in meters.
* `satellites` - int. Shows the number of GPS satellites used to determine this point.
* `mileage` - float. Represents mileage.
* `get_time` - [date/time](../../../getting-started.md#data-types). This is the GPS timestamp of the point, adjusted to the user's timezone.
* `address` - string. Represents the location's address. Will be "" if no address recorded. If no address has been recorded, it will appear as "". An address is recorded when it marks the beginning or end of a trip, or when an event occurs.
* `heading` - int. A value that represents the direction in degrees, with a range of 0 to 360. 0 corresponds to North.
* `speed` - int. A value representing speed in kilometers per hour.
* `precision` - optional int. A value indicating precision in meters. Its presence relies on the device model.
* `gsm_lbs` - optional boolean. It returns `true` if the location was detected by GSM LBS.
* `parking` - optional boolean. It will return true if the point does not correspond to a trip. [Parking detection](https://www.navixy.com/docs/user/web-interface-docs/devices-doc/parking-detection/) feature on the platform influences the categorization of points as either trip or parking states.
* `buffered` - optional boolean. It will return `true` if the point was initially saved in the device's memory and then sent to the server later. This parameter may vary based on the tracker model.

#### errors

* 201 - Not found in database – the tracker ID in your request may not match any trackers linked to the user account with this
  session hash. Ensure the correct tracker_id and hash of an appropriate user are used.
* 208 - Device blocked – if a tracker exists under this user account but is currently inactive due to tariff plan
  restrictions or any other reason.
* 211 - Requested time span is too big – If the interval between the "from" and "to" dates is too large, it may exceed
  the maximum value defined in the API configuration.

***

### visit/list

This method fetches IDs of zones and places that contain at least one track point.

#### parameters

| name           | description                                                                                                                                         | type                                                | format                |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|:----------------------|
| tracker_id     | ID of the tracker (aka "object_id"). The tracker must be associated with the user whose hash is being used for the request, and not tariff-blocked. | int                                                 | 123456                |
| from           | Start date/time for searching.                                                                                                                      | [date/time](../../../getting-started.md#data-types) | "2024-01-10 00:00:00" |
| to             | End date/time for searching. Must be after `from` date.                                                                                             | [date/time](../../../getting-started.md#data-types) | "2024-01-20 00:00:00" | 
| include_zones  | Optional. Default is `true`. If the value is `false`, zones IDs will be excluded.                                                                   | boolean                                             | true                  |
| include_places | Optional. Default is `true`. If the value is `false`, places IDs will be excluded.                                                                  | boolean                                             | true                  |

#### example

For instance, if we need to obtain IDs of zones and places that contain at least one track point related to tracker 1683258 in January.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/visit/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 1683258, "from": "2024-01-01 00:00:00", "to": "2024-01-31 00:00:00"}'
    ```

#### response

```json
{
  "success": true,
  "value": {
    "zones": [
      54865,
      35284
    ],
    "places": [
      18404
    ]
  }
}
```

* `zones` - int array. List of zones IDs.
* `places` - int array. List of places IDs.

#### errors

* 204 - Entity not found – the tracker ID in your request may not match any trackers linked to the user account with this
  session hash. Ensure the correct tracker_id and hash of an appropriate user are used.
