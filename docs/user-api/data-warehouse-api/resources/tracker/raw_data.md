---
title: Raw IoT Data
description: Contains API calls to retrieve trackers raw data.
---
# Raw IoT Data

The Navixy Raw IoT Data API allows you to retrieve all the data sent by your devices in a raw format up to 6 months depending on your plan.

!!! note "Parsed raw data — Data obtained immediately after decoding (parsing) incoming data packets, considering the protocol and specifics of the device model from which the packets were received."

On this page, you'll learn about API methods that give you access to parsed raw data, perfect for detailed analysis.

You can access various types of data that your devices send, such as:

* GPS and GSM information,
* Sensor readings,
* Status of inputs and outputs,
* Other attributes.

The Navixy Raw IoT Data API provides the following key methods:

- **`get_inputs`**: To retrieve a list of available attributes from a device to understand which ones can be requested in a file.
- **`read`**: To get a CSV file with decoded data values sent by tracking devices.

## API Actions

API base path: `/tracker/raw_data/`

### get_inputs

This API request returns the available attributes of a device. Before you dive into requesting raw data,
it's crucial to understand the device's data capabilities and the specific names of its attributes.

Keep in mind that this request doesn't provide actual device data. Instead, it acts as a supplementary request to give 
you insights into the fields, so you know what data you can obtain subsequently.

You can get information about one device per request.

#### Request parameters

| name       | type    | description                                                                         | format | required |
|:-----------|:--------|:------------------------------------------------------------------------------------|:-------|:---------|
| tracker_id | integer | An ID of a tracker for which you want to retrieve the list of available attributes. | 123456 | yes      |

#### Request example

For example, we have a tracker with ID 123456, and we don't know which attributes are available to request in the raw data 
file. We will add its ID to this API request.

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

#### Response example

```json
{
    "discrete_inputs": 2,
    "discrete_outputs": 1,
    "inputs": [
        "analog_1",
        "avl_io_100000",
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

#### Response description

| name             | type         | description                                                                                     | format            |
|:-----------------|:-------------|:------------------------------------------------------------------------------------------------|:------------------|
| discrete_inputs  | int          | A number of discrete inputs.                                                                    | 8                 |
| discrete_outputs | int          | A number of discrete outputs.                                                                   | 8                 |
| inputs           | string array | A list of available metering inputs with indexes. How to read these indexes is described below. | `["lls_level_4"]` |
| states           | string array | A list of available status attributes.                                                          | `["event_code]`   |

If there is more than one input of the same type, they are indexed (1, 2, 3...). In this case, only the input with the 
maximum index will be returned.

For example:

* If LLS Levels from 1 to 4 are available, `lls_level_4` is returned, and it is assumed that LLS levels 1 through 3 also exist.
* If AVL IOs from 1 to 100000 are available for a device, `avl_io_100000` is returned, then AVL IOs with smaller indexes also exist.

Additionally, you can get a description of all inputs from response using the 
[input_name](../../../backend-api/resources/tracking/tracker/sensor/input_name.md#list) endpoint.

#### Possible errors

* **201: Not found in the database.** The tracker ID in your request may not match any trackers linked to the authorized 
user account. Ensure the correct tracker_id and API key of an appropriate user are used. The tracker number and user ID 
for which you request information will be included in the error description.
* **208: Device blocked.** This error occurs if the tracker with the specified tracker_ID exists but has been blocked due to 
its tariff plan. For example, it may have been blocked because the user does not have enough money to cover the plan's charge.

### read

Retrieves parsed raw data—values received from tracking devices by the platform. Each attribute in the exported file will 
be placed in a separate column.

!!! note "The names and values of the inputs and status attributes returned by this request align with the names visible in [Air Console](https://docs.navixy.com/admin-panel/air-console) when connecting to a device. You can find them in the right column, where the incoming data is decoded."

#### Request parameters

| name               | type          | description                                                                                                                                                                                                                                                                                                            | format                                                                                                                                                                            | required |
|:-------------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| tracker_id         | int           | An ID of a tracker for which you want to retrieve the file with the parsed raw data.                                                                                                                                                                                                                                   | 123456                                                                                                                                                                            | yes      |
| from               | date/time     | The start date/time for the file, indicating from what moment the parsed raw data should be retrieved. This relates to the message time—when the packet was registered by a tracker. It can be up to 6 months from current moment depending on your plan. The time is specified along with the time zone according to ISO 8601. | "2023-08-24T08:04:36Z"                                                                                                                                                            | yes      |
| to                 | date/time     | The end date/time, indicating up to which moment messages should be retrieved into the file. This relates to the message time—when the packet was registered by a tracker. The specified date must be after the "from" date. The time is specified along with the time zone according to ISO 8601.                     | "2023-08-24T08:04:36Z"                                                                                                                                                            | yes      |
| columns            | string array  | List of attributes to retrieve in CSV/Parquet file. You can obtain it with [get_inputs](raw_data.md#get_inputs) request.                                                                                                                                                                                             | `["flags.location_valid","lat","lng","discrete_inputs.1","inputs.board_voltage"]`                                                                                                 | yes      |
| server_time_filter | string/object | An interval for additional filtering of messages by server time. If used, messages will be returned not only based on the message time (when the packet was registered by a tracker), but also filtered by the server time (when the message was received by the server).                                              | `"2024-02-03T10:26:26+0500/2024-02-03T10:27:18+0500"` / `{"from": "2024-02-03T10:26:26+0500", "to": "2024-02-03T10:27:18+0500"}` / `{"interval":"2024-02-03T10:26:26+0500/PT1H"}` | no       |
| format             | string        | This is used when you need to request data in `parquet` format. If the format parameter is not provided, the default format used will be CSV.                                                                                                                                                                          | `"parquet"`                                                                                                                                                                       | no       |

!!! note "Instead of using the `from`/`to` parameters, you can set the `interval` parameter — an ISO 8601 formatted interval, for example, `2023-08-24T08:04:36.306Z/PT24H`."

The response could be provided in a CSV or [Parquet](https://parquet.apache.org/docs/overview/) format file, with columns 
predefined in the `columns` parameter of the API request. 

Here are the specifications for the table output in the CSV format:

* Rows are enclosed in double quotes. A double quote inside a string is output as two double quotes in a row. There are no other rules for escaping characters.
* Date and date-time values are enclosed in double quotes.
* Numbers are output without quotes.
* Values are separated by a comma character `,`.
* Rows are separated using the Unix line feed (LF).
* `NULL` is represented as `\N`.
* Requested column can be a simple or complex.

##### Simple columns

Simple columns are columns that contain straightforward and general information applicable to most models, such as time, 
GPS, and GSM data. For example: `columns: ["server_time", "gps_fix_type", "lat", "lng", "speed"]`.

In the table below, you will find a list of all simple columns along with descriptions of what these columns mean and 
what they may return in the file.

| name         | type      | description                                                                                                                                                                                                                                                                                                                                                                                                            | format in file               |
|:-------------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|
| msg_time     | date/time | The time of a message sent by a tracking device. This is always included in the CSV output and does not need to be requested separately within the `columns` request parameter. Indicated according to the chosen time zone.                                                                                                                                                                                           | `"2024-12-10T13:13:14+0600"` |
| server_time  | date/time | The time when a message was received by the server. Indicated according to the chosen time zone.                                                                                                                                                                                                                                                                                                                       | `"2023-12-10T13:13:14+0600"` |
| gps_fix_type | enum      | In response it will provide you with the next: <br/>`UNKNOWN` - If a device can't provide such information or hasn't determined the GPS fix type for this packet.<br/>`NO_FIX` - GPS tracker marked location as not valid.<br/>`HAS_FIX` - GPS tracker marked location as valid.<br/>`LAST_KNOWN_POSITION` - In case the tracker provides current input and other states within the last known location.               | `HAS_FIX`                    |
| lat          | float     | Represents latitude.                                                                                                                                                                                                                                                                                                                                                                                                   | 45.123456                    |
| lng          | float     | Represents longitude.                                                                                                                                                                                                                                                                                                                                                                                                  | -75.123456                   |
| speed        | decimal   | A value representing speed in kilometers per hour.                                                                                                                                                                                                                                                                                                                                                                     | 60.45                        |
| alt          | int       | Indicates the altitude in meters.                                                                                                                                                                                                                                                                                                                                                                                      | 200                          |
| satellites   | int       | Shows the number of GPS satellites used to determine this point. `-1` = unknown.                                                                                                                                                                                                                                                                                                                                       | 14                           |
| heading      | int       | A value that represents the direction in degrees, with a range of 0 to 360. 0 corresponds to North.                                                                                                                                                                                                                                                                                                                    | 90                           |
| precision    | int       | A value indicating precision in meters. Its presence relies on the device model.                                                                                                                                                                                                                                                                                                                                       | 10                           |
| hdop         | float     | Horizontal dilution of precision. `-1` = unknown.                                                                                                                                                                                                                                                                                                                                                                      | `-1`                         |
| pdop         | float     | Position dilution of precision. `-1` = unknown.                                                                                                                                                                                                                                                                                                                                                                        | `-1`                         |
| event_id     | int       | Platform related event ID. You can find the full list of event IDs [here](https://docs.navixy.com/expert-center/understanding-the-raw-data-file#ColumnsinCSVFile-Simplecolumns).                                                                                                                                                                                                                                       | 2                            |
| mn_name      | string    | Mobile network name. Determined by the tracking device.                                                                                                                                                                                                                                                                                                                                                                | `"Network Name"`             |
| mn_roaming   | int       | Roaming status. Is determined by the device:<br/>`0` - No roaming.<br/>`1` - This point was generated by a device in roaming.<br/>`-1` - If the device can't provide such data or couldn't do it for this particular message.                                                                                                                                                                                          | 1                            |
| mn_code      | int       | Mobile network operator code. Determined by the tracking device.                                                                                                                                                                                                                                                                                                                                                       | 12345                        |
| mn_csq       | int       | Mobile network signal strength, CSQ, values from `0` to `31`. Determined by the tracking device. If the device can't provide such data or couldn't do it for this particular message, it will be `99` (unknown).                                                                                                                                                                                                       | 31                           |
| mn_type      | enum      | Mobile network type. Is determined by the tracking device. One of:<br/>`UNKNOWN` - If the device can't provide such data or couldn't do it for this particular message.<br/>`GSM` - If the device determined GSM type.<br/>`CDMA` - If the device determined CDMA type.<br/>`WCDMA` - If the device determined WCDMA type.<br/>`LTE` - If the device determined LTE type.<br/>`NR` - If the device determined NR type. | `LTE`                        |

In Parquet files, all `enum` parameters (such as `gps_fix_type`, `mn_type`, etc.) are transmitted as numbers starting 
from `0`.

Examples:

* gps_fix_type - `UNKNOWN` = 0, `NO_FIX` = 1, `HAS_FIX` = 2, `LAST_KNOWN_POSITION` = 3.
* mn_type - `UNKNOWN` = 0, `GSM` = 1, `CDMA` = 2, `WCDMA` = 3, `LTE` = 4, `NR` = 5.

##### Complex columns

Complex columns are columns that represent various attributes of trackers, such as sensor data and states. We store them 
as different boxes, each with a common name. To access specific information, you first need to specify which box the data 
is from and then use a period to indicate the exact attribute name or input/output number. For example:
`"columns: ["flags.location_valid", "inputs.board_voltage", "discrete_inputs.1", "discrete_outputs.2"]`.

Unknown internal values will be returned as `NULL` in the file. The list of available internal values for a particular 
device should be obtained using the [get_inputs](#getinputs) method described above.

The type and format for different inputs may vary, so we will provide you with the complex column name (without internal values)
and its description in the table below.

| name               | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flags              | Three flags representing location validity and LBS. You can request only necessary: <br>- `flags.location_valid`: Indicates the validity status of the location. It is 0 if the location is invalid, and 1 if the location is valid.<br> - `flags.lbs`: Indicates the LBS status of the point. If 0, the point is received by GPS; if 1, the point is received by LBS.<br>- `flags.soft_lbs`: Indicates the source of the LBS point. If 0, the point is determined by device LBS; if 1, by the platform's LBS. |
| discrete_inputs    | Discrete inputs states, inputs enumerated from 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| discrete_outputs   | Discrete outputs states, outputs enumerated from 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| inputs             | Metering inputs values. Inputs list depends on the device.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| states             | Various states. States list depends on the device.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

If you specify a complex column without specifying an internal value, then all internal values will be returned as a JSON 
map (except for flags, which will be returned as an integer).

You can append complex columns with an asterisk symbol:

* `inputs.*`
* `states.*`
* `discrete_inputs.*`
* `discrete_outputs.*`

In this case, the platform will search for all available columns within the specified data range and then request them from
the database. In the resulting CSV/Parquet output, instead of the column with an asterisk, all existing columns will be shown in 
alphabetical order. Columns that are unavailable for the device model will not be included in the resulting file.

#### Example for standard searching by message time only in CSV

Suppose we need to request the following information about device 123456 for the period from October 10 to October 11, 2024: 
data on latitude and longitude, speed, fuel level from wireless fuel level sensor 1, calculated mileage, and the status 
of all discrete inputs. We do not need the message reception time by the server for our analysis. 
To get a csv file our request header must contain `accept: text/csv` and would look like this:

=== "cURL for CSV"

```shell
curl -X 'POST' \
  'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
  -H 'accept: text/csv' \
  -H 'Content-Type: application/json' \
  -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "123456",
    "from": "2024-10-10T00:00:00.000Z",
    "to": "2024-10-11T00:00:00.000Z",
    "columns": [
      "lat",
      "lng",
      "speed",
      "inputs.ble_lls_level_1",
      "inputs.hw_mileage",
      "discrete_inputs.*"
    ]
  }'
```

#### Response example for case 1 in CSV

```
"msg_time","lat","lng","speed","inputs.ble_lls_level_1","inputs.hw_mileage","discrete_inputs.1","discrete_inputs.2"
"2024-10-10T13:13:14+0600",54.22809,69.5264283,28,2871,24296.444,0,1
"2024-10-10T13:13:25+0600",54.228095,69.5278333,32,2871,24296.536,0,1
"2024-10-10T13:13:36+0600",54.227765,69.5293916,39,2871,24296.644,0,1
"2024-10-10T13:13:46+0600",54.22744,69.5310083,39,2871,24296.756,0,1
```

#### Parquet file format request example

For getting a Parquet file with the same parameters add the `format: "parquet"` to the request body.

In the next example, we will slightly adjust the body of the request, so you can further test the downloaded Parquet file (navixy_data.parquet).
The following code block is a Bash script used for downloading a Parquet file using a Linux distribution and its terminal.

=== "cURL for Parquet"

```shell
#!/bin/bash

curl -X 'POST' \
'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
-H 'accept: application/octet-stream' \
-H 'Content-Type: application/json' \
-d '{
  "hash": "feed000000000000000000000000cafe",
  "tracker_id": "3036057",
  "from": "2024-09-10T02:00:00Z",
  "to": "2024-09-10T06:00:00Z",
  "columns": [
	"lat",
	"lng",
	"speed",
	"inputs.can_fuel_litres"
  ],
  "format": "parquet"
}' \
--output navixy_data.parquet
```

1. Switch to the root user or use the ```sudo``` prefix before the terminal commands

2. Create an .sh file using nano - ```nano curl.sh```

3. Paste the cURL example above into the file

4. Write the file (CTRL+O -> Enter) and exit ```nano``` (CTRL+X)

5. Add the Execution rights to the file using the ```chmod +x curl.sh``` command

6. Run the script ```./curl.sh```


<video controls style="width: 100%; height: auto;">
  <source src="../assets/videos/1_parquet_curl_linux.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

#### Example for searching by server time additionally

This API is designed to accommodate scenarios where you retrieve information from trackers to your applications within 
specified time intervals. Occasionally, trackers may experience connectivity issues. During such occurrences, these 
trackers automatically store information in their memory buffers. Upon re-establishing a connection, devices promptly 
transmit their stored information to the platform.

For instance:

A tracker was connected from 10:00 to 10:30. It then loses GSM signal, storing information in its buffer from 10:30 to 12:00. 
At 12:00, it reconnects and begins sending packets from the buffer. These packets are timestamped with message times starting 
from 10:30, 10:31, and so forth. However, the server time reflects 12:00, 12:01, and so on. If your program requests data 
from 10:00 to 11:00 at 11:00 without utilizing the `server_time_filter` parameter, it will receive messages only 
from 10:00 to 10:30. The program might not be aware that it needs to re-request this data once all data from the buffer 
has been uploaded.

To address such situations, there is optional filtering using the `server_time_filter` parameter. This ensures that your 
program will get all buffered information. This approach helps prevent potential data gaps and enhances the reliability 
of your application.

=== "cURL"

```shell
curl -X 'POST' \
  'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
  -H 'accept: text/csv' \
  -H 'Content-Type: application/json' \
  -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "123456",
    "from": "2024-10-10T07:00:00.000Z",
    "to": "2024-10-103T07:23:59.000Z",
    "server_time_filter": {
      "from": "2024-10-10T10:30:00.000Z",
      "to": "2024-10-10T12:30:00.000Z"
    },
    "columns": [
      "lat",
      "lng",
      "speed",
      "inputs.ble_lls_level_1",
      "inputs.hw_mileage",
      "discrete_inputs.*"
    ]
  }'
```


#### Response example for case 2

```
"msg_time","server_time","lat","lng","speed","inputs.ble_lls_level_1","inputs.hw_mileage","discrete_inputs.1","discrete_inputs.2"
"2024-10-10T07:13:14+0600","2024-10-10T10:41:20+0600",54.22809,69.5264283,28,2871,24296.444,0,1
"2024-10-10T07:13:25+0600","2024-10-10T10:41:21+0600",54.228095,69.5278333,32,2871,24296.536,0,1
"2024-10-10T07:13:36+0600","2024-10-10T10:41:22+0600",54.227765,69.5293916,39,2871,24296.644,0,1
"2024-10-10T07:13:46+0600","2024-10-10T10:41:24+0600",54.22744,69.5310083,39,2871,24296.756,0,1
```

#### Possible errors

* **201: Not found in the database.** The tracker ID in your request may not match any trackers linked to the authorized
  user account. Ensure the correct tracker_id and API key of an appropriate user are used.
* **208: Device blocked.** This error occurs if the tracker with the specified tracker_ID exists but has been blocked due to
  its tariff plan. For example, it may have been blocked because the user does not have enough money to cover the plan's charge.
