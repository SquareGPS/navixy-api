---
title: Raw data request - date and time
description: Describes how date-time format works for data warehouse requests. 
---

# Raw data request - date and time

When requesting raw data, you must specify the exact period of time for which you need the data, only in this case the 
platform is able to correctly process your request and return you the necessary information.

As in the Backend API, here you can specify date and time either in the usual `YYYYY-MM-DD HH:mm:ss` form with or without 
time zone, or in accordance with ISO 8601.

The difference is that ISO 8601 is the default format for Data Warehouse API requests.

!!! warning "The platform allows you to request raw data for any period not exceeding 30 days back from the current date. Raw data for earlier periods will not be requested."

## ISO 8601

!!! note "[ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) is an international standard of representing date and time-related data in unambiguous form, both human- and machine-readable. However, some programs, including Microsoft Excel, may not be able to read such timestamps, therefore it is optional."

Using this date/time standard when requesting raw data, you can specify the exact time for which you need the data, as 
well as the time zone - not only as in the user account or UTC+0, but any other time zone of your choice, if required.

According to ISO 8601, the date and time are represented starting with year, followed by month, day, hour, minutes, 
seconds, milliseconds and time zone offset.

Date and time format:

```
[yyyy]-[mm]-[dd]T[hh]:[mm]:[ss]±[offset]
```

Time zone offset can be specified using any of the following formats:

* `+-HH:mm` - for example, -06:00 or +05:30. 
* `+-HHmm` - for example, -0500 or +0100.
* `+-HH` - for example, -03 or +07.
* `Z` - no offset (UTC+0).

Timestamp examples:

Let's assume that the client account is set to UTC+4 (Dubai) time, and the time we need is 10:20 AM, the date is 
December 2, 2023. Then we can specify the timestamp in one of the following ways:

* `2023-12-02T10:20:00+04:00`
* `2023-12-02T10:20:00+04`
* `2023-12-02T06:20:00Z` (converted to UTC+0)

Another example. The client account is set to UTC-6 (Mexico) time, and the time we need is 10:55 PM, the date is 
December 11, 2023. Then we can specify the timestamp in one of the following ways:

* `2023-12-11T23:55:00-06:00`
* `2023-12-11T23:55:00-06`
* `2023-12-12T04:55:00Z` (converted to UTC+0, mind the date)

### API request example:

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
    -H 'accept: text/csv' \
    -H 'Content-Type: application/json' \
    -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "10033823",
    "from": "2023-12-12T09:00:00Z",
    "to": "2023-12-12T09:25:00Z",
    "columns": ["lat","lng","discrete_inputs.1","inputs.board_voltage"]}'
    ```

!!! note "The output for a raw data request will always contain a `msg_time` column that contains time stamps according to user account time zone. If you need to obtain `msg_time` in any other time zone, please refer to **Time zone** section below."

## Regular date and time

Another valid option to specify date and time is the usual `YYYYY-MM-DD HH:mm:ss` format.

Since this is not the default format, you need to specify the parameter `iso_datetime=false` in the API request.

### API request example:

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
    -H 'accept: text/csv' \
    -H 'Content-Type: application/json' \
    -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "iso_datetime": false,
    "tracker_id": "10033823",
    "from": "2023-12-12 14:00:00",
    "to": "2023-12-12 14:25:00",
    "columns": ["lat","lng","discrete_inputs.1","inputs.board_voltage"]}'
    ```

In this case, the retrieved data will be **in the time zone of the user account**.

## Time zone

There may be situations when you need to obtain data in some specific time zone different from user account. This can be
useful when the customer's time zone differs from yours due to geographical reasons.

In this case you need to supplement your request with the `time_zone` parameter and specify the required zone ID. You can 
request all the possible zone IDs using [timezone/list](../../backend-api/resources/commons/timezone.md) request from 
Backend API.

### API request example:

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
    -H 'accept: text/csv' \
    -H 'Content-Type: application/json' \
    -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "iso_datetime": false,
    "time_zone": "Europe/London",
    "tracker_id": "10033823",
    "from": "2023-12-12 14:00:00",
    "to": "2023-12-12 14:25:00",
    "columns": ["lat","lng","discrete_inputs.1","inputs.board_voltage"]}'
    ```

## Time period

When requesting raw data, you have an option of specifying the request period in two ways: by specifying the date and 
time "from" and "to" or by specifying an interval. Both methods are equally valid, but you should use only the one of 
your choice.

### "from" and "to"

A common way to indicate the period of data request is to specify two timestamps of start and end. This is done using 
the `from` and `to` parameters. The values are specified either according to ISO 8601 or in a regular 
`YYYYY-MM-DD HH:mm:ss` form - as described above.

Examples: 

```
"from": "2023-11-30T17:00:00-06:00",
"to": "2023-11-30T18:00:00-06:00",
```

or

```
"from": "2023-11-30 17:00:00",
"to": "2023-11-30 18:00:00",
```

!!! note "Note that the `to` date and time must be after the `from`, otherwise the query will result in an `Invalid parameters` error."

### Interval

An alternative method of indicating the request period is an interval. Here you specify the start or end date and time 
of the period appended by duration of the period. 

!!! note "When specifying the `interval` parameter, then `from` and `to` parameters must not be specified. These are mutually exclusive ways of specifying the data request period."

The interval can be specified in different forms:

* Starting from a specific date and time. 
* Ending with a specific date and time 
* Indicated by start and end timestamps, without a period.

Possible `inerval` parameter formats:

```
[start date and time]/P[dd]T[hh]H[mm]M[ss]S
```

or 

```
P[dd]T[hh]H[mm]M[ss]S/[end date and time]
```

or

```
[start date and time]/[end date and time]
```

The date and time can be specified either according to ISO 8601 or in a regular form.

`PT` in interval value stands for “Period and Time” and indicates the period after the specified time stamp. 
For example, `PT1H30M15S` means 1 hour 30 minutes 15 seconds.

If you need to request data for several days, you can specify the amount of days between `P` and `T`. 
For example, `P2DT3H45M10S` means 2 days 3 hours 45 minutes 10 seconds.

Examples:

* `"interval": "2023-11-30T17:00:00-0600/PT1H30M10S"` - data will be requested from 17:00:00 to 18:30:10, November 30 (UTC-6).
* `"interval": "2023-11-30 17:00:00/P2DT2H45M10S"` - data will be requested from November 30, 17:00:00 to December 2, 19:45:10 (according to user account time zone).
* `"interval": "P2DT2H45M10S/2023-11-30 17:00:00"` - data will be requested from November 28, 14:14:50 to November 30, 17:00:00 (according to user account time zone).

!!! note "All of the above methods of specifying the date and time are equally correct. Therefore, you can choose any of them that you find more convenient or that better matches the format used in your integrations."
