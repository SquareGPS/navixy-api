---
title: Requesting raw data
description: How to request raw tracker data from Navixy Raw IoT Data API and typical use cases.
---
# Requesting Raw IoT Data

Navixy Raw IoT Data API allows telematics solution providers and developers of location-based solutions to access comprehensive, unprocessed data from tracking devices. This enables accurate information retrieval and a deeper understanding of collected data, facilitating issue resolution and integration into other systems for extensive analysis and business use.

## Typical Use Case

For efficient fuel management, especially in fleet management or cargo transportation, integrating your ERP system with the Navixy platform is essential. This integration allows you to seamlessly request raw fuel data from specific devices, enhancing your fuel monitoring and expense tracking capabilities.

Imagine that you need to retrieve the following data:

* Fuel Level
* Device Location
* Mileage (Odometer)
* Speed
* Date and Time
* Any other data valuable to your business

Please note that you will not receive human-readable information about fuel drains and refills, excessive consumption, idling, and other analytics—those are available through [backend-API methods](../../backend-api/getting-started/introduction.md). Raw data requests provide unprocessed data received directly from the device, decoded by the Navixy platform, offering instantaneous data readings for a specific period. This data is suitable for further processing and analysis on your end.

## Requesting Inputs List

Tracking devices from different manufacturers have different specifics of work and send data in various forms. In addition, sensors can be of different types: digital and analog, wired and wireless, built-in and external. Also, there can be several sensors monitoring the same type of readings: for example, two fuel sensors in two tanks, internal and external temperature sensors, etc.

Before requesting raw data, we need to understand what data the device can report to the platform and what the data inputs are named. To do this, we need to use the [`raw_data/get_inputs`](../resources/tracker/raw_data.md#getinputs) request.

Example for a device with ID 123456:

=== "cURL"

```shell
curl -X 'POST' \
'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/get_inputs' \
-H 'Content-Type: application/json' \
-d '{
  "hash": "6dc7d304dec4434f4c4202ec42817f83",
  "tracker_id": 123456
}'
```

The platform will notify us about success, and we will see the following JSON object in response:

```json
{
  "discrete_inputs": 2,
  "discrete_outputs": 1,
  "inputs": [
    "analog_1",
    "battery_voltage",
    "board_voltage",
    "ext_temp_sensor_4",
    "freq_1",
    "hw_mileage",
    "impulse_counter_1",
    "lls_level_4",
    "lls_temperature_4"
  ],
  "states": [
    "hardware_key"
  ],
  "success": true
}
```

Among the obtained inputs, we see the one of interest to us - `lls_level_4`. This is a fuel level input, and the index 4 indicates the value is a range of LLS levels from `1` to `4`. This means the device can send fuel data on a maximum of four inputs: from `lls_level_1` to `lls_level_4`.

We also see the `hw_mileage`, which will allow us to get the value of the hardware odometer.

!!! note "The presence of some inputs in the received response does not mean that data is certainly available on these inputs. It means that data may come on them, but whether it is actually available or not depends on the configuration of a particular device."

## Requesting Raw Data Readings

Now we know the names of the inputs where the fuel data comes from, and we can use them in the API query. However, we also need other parameters for more accurate analysis. This data is not related to sensors, so the above query does not return it. They come in simple columns and are listed on the appropriate documentation page.

We will use the following columns:

* `lat`
* `lng`
* `speed`

In addition, we will use names for inputs according to the information obtained earlier:

* `inputs.lls_level_1`
* `inputs.hw_mileage`

!!! note "We specify `inputs.lls_level_1` because we know that our device only sends data on this input. If we didn't know the input number, we could have specified all four possible inputs, and then the inputs without data would just get zero values."

The API request [`raw_data/read`](../resources/tracker/raw_data.md#read) for reading the required raw data in our case should look like this:

=== "cURL"

```shell
curl -X 'POST' \
'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
-H 'accept: text/csv' \
-H 'Content-Type: application/json' \
-d '{
  "hash": "6dc7d304dec4434f4c4202ec42817f83",
  "tracker_id": "123456",
  "from": "2023-11-29T08:31:00Z",
  "to": "2023-11-29T08:32:00Z",
  "columns": [
    "lat",
    "lng",
    "speed",
    "inputs.lls_level_1",
    "inputs.hw_mileage"
  ]
}'
```

The response is returned in a CSV table format:

```
"msg_time","lat","lng","speed","inputs.lls_level_1","inputs.hw_mileage"
"2023-11-29T08:31:10Z",54.2312716,69.5261833,0,3307,24250.798
"2023-11-29T08:31:12Z",54.1811183,69.5331349,24,3274,24257.16
"2023-11-29T08:31:27Z",54.1802066,69.5333599,21,\N,\N
"2023-11-29T08:31:27Z",54.1802066,69.5333599,21,3274,24257.262
"2023-11-29T08:31:30Z",54.180055,69.533395,20,3274,24257.279
"2023-11-29T08:31:31Z",54.180005,69.5334083,20,3274,24257.285
"2023-11-29T08:31:33Z",54.179915,69.5334266,17,3274,24257.295
"2023-11-29T08:31:34Z",54.1798766,69.533435,15,3274,24257.299
"2023-11-29T08:31:36Z",54.1798116,69.5334433,12,3274,24257.306
"2023-11-29T08:31:37Z",54.179785,69.5334416,10,3274,24257.309
"2023-11-29T08:31:39Z",54.1797366,69.533425,9,3274,24257.315
"2023-11-29T08:31:40Z",54.1797183,69.5334083,8,3274,24257.315
"2023-11-29T08:31:42Z",54.1796883,69.5333449,10,3274,24257.322
"2023-11-29T08:31:43Z",54.17968,69.5333016,12,3274,24257.325
"2023-11-29T08:31:45Z",54.1796816,69.53318,15,3274,24257.333
"2023-11-29T08:31:47Z",54.1796816,69.533025,20,3274,24257.343
```

In the above example, we see the output for one minute of tracking. When querying raw data over a long period of time, the response can reach significant sizes — this must be considered.

!!! note "In one of the lines, we see `\N` instead of fuel level and mileage values. This means that no such information was received in this data packet. The `\N` symbol represents `NULL`."

The above example is one of the simplest, but it clearly demonstrates the process of using an API request to read raw data. You can query a lot of data at once and over large periods of time, depending on your objectives.

## Specifying Time Frame

When requesting raw data, you must specify the exact period for which you need the data to ensure the platform can accurately process your request and return the necessary information.

Similar to the [Backend API](../../backend-api/getting-started/introduction.md), you can specify the date and time in either the standard `YYYY-MM-DD HH:mm:ss` format with or without a time zone or in ISO 8601 format. 

The default format for Raw IoT Data API requests is ISO 8601.

The platform allows you to request raw data for any period within the [time frame limits](../getting-started.md#time-frame-limits).

All methods for specifying the date and time provided below are equally valid. Choose the one that is most convenient or best matches the format used in your integrations.

### ISO 8601

[ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) is an international standard for representing date and time-related data in an unambiguous form that is both human- and machine-readable. However, some programs, including Microsoft Excel, may not be able to read such timestamps, so its use is optional.

Using this date/time standard when requesting raw data, you can specify the exact time for which you need the data, as well as the time zone - not only as in the user account or UTC+0, but any other time zone of your choice, if required.

According to ISO 8601, the date and time are represented starting with the year, followed by month, day, hour, minutes, seconds, milliseconds, and time zone offset.

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

Let's assume that the client account is set to UTC+4 (Dubai) time, and the time we need is 10:20 AM, the date is December 2, 2023. Then we can specify the timestamp in one of the following ways:

* `2023-12-02T10:20:00+04:00`
* `2023-12-02T10:20:00+04`
* `2023-12-02T06:20:00Z` (converted to UTC+0)

Another example. The client account is set to UTC-6 (Mexico) time, and the time we need is 10:55 PM, the date is December 11, 2023. Then we can specify the timestamp in one of the following ways:

* `2023-12-11T23:55:00-06:00`
* `2023-12-11T23:55:00-06`
* `2023-12-12T04:55:00Z` (converted to UTC+0, mind the date)

**API request example:**

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
  "columns": ["lat","lng","discrete_inputs.1","inputs.board_voltage"]
}'
```

The output for a raw data request will always contain a `msg_time` column that contains timestamps according to the user account time zone. If you need to obtain `msg_time` in any other time zone, please refer to the [Time zone](#time-zone) section below.

### Regular Date and Time

Another valid option to specify date and time is the usual `YYYY-MM-DD HH:mm:ss` format. Since this is not the default format, you need to specify the parameter `iso_datetime=false` in the API request.

**API request example:**

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
  "columns": ["lat","lng","discrete_inputs.1","inputs.board_voltage"]
}'
```

In this case, the retrieved data will be in the time zone of the user account.

### Time Zone

There may be situations when you need to obtain data in a specific time zone different from the user account. This can be useful when the customer's time zone differs from yours due to geographical reasons.

In this case, you need to supplement your request with the `time_zone` parameter and specify the required zone ID. You can request all the possible zone IDs using the [`timezone/list`](../../backend-api/resources/commons/timezone.md) request from the Backend API.

**API request example:**

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
  "columns": ["lat","lng","discrete_inputs.1","inputs.board_voltage"]
}'
```

### Time Period

When requesting raw data, you have an option of specifying the request period in two ways: by specifying the date and time "from" and "to" or by specifying an interval. Both methods are equally valid, but you should use only one of your choice.

### From ... To

A common way to indicate the period of data request is to specify two timestamps of start and end. This is done using the `from` and `to` parameters. The values are specified either according to ISO 8601 or in a regular `YYYY-MM-DD HH:mm:ss` form - as described above.

**Examples:** 

```json
"from": "2023-11-30T17:00:00-06:00",
"to": "2023-11-30T18:00:00-06:00",
```

or

```json
"from": "2023-11-30 17:00:00",
"to": "2023-11-30 18:00:00",
```

!!! note "The `to` date and time must be after the `from`, otherwise the query will result in an `Invalid parameters` error."

### Interval

An alternative method of indicating the request period is an interval. Here you specify the start or end date and time of the period appended by the duration of the period.

!!! note "When specifying the `interval` parameter, the `from` and `to` parameters must not be specified. These are mutually exclusive ways of specifying the data request period."

The interval can be specified in different forms:

* Starting from a specific date and time.
* Ending with a specific date and time.
* Indicated by start and end timestamps, without a period.

Possible `interval` parameter formats:

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

`PT` in interval value stands for “Period and Time” and indicates the period after the specified timestamp. For example, `PT1H30M15S` means 1 hour 30 minutes 15 seconds.

If you need to request data for several days, you can specify the number of days between `P` and `T`. For example, `P2DT3H45M10S` means 2 days 3 hours 45 minutes 10 seconds.

**Examples:**

* `"interval": "2023-11-30T17:00:00-0600/PT1H30M10S"` - data will be requested from 17:00:00 to 18:30:10, November 30 (UTC-6).
* `"interval": "2023-11-30 17:00:00/P2DT2H45M10S"` - data will be requested from November 30, 17:00:00 to December 2, 19:45:10 (according to user account time zone).
* `"interval": "P2DT2H45M10S/2023-11-30 17:00:00"` - data will be requested from November 28, 14:14:50 to November 30, 17:00:00 (according to user account time zone).


