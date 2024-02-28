---
title: Raw data
description: Contains API calls to retrieve trackers raw data.
---

# Raw data

Tracking devices vary significantly in terms of form factor, connectivity, and use cases, but their most substantial 
divergence lies in the data they monitor and report. Even when dealing with various device types, the datasets can differ 
significantly; however, the platform processes all data and stores it in the database in some manner.

This API requests allows you to get and download parsed raw data from the platform for the various period of time, but 
not more than last 30 days. This API request returns data for all inputs and state fields which the tracker transmitted.

!!! note "Parsed raw data - Data obtained immediately after decoding (parsing) incoming data packets, taking into account the protocol and specifics of the device model from which the packets were received."

## API actions

API base path: `/tracker/raw_data/`

### get_inputs

Returns available metering inputs and state fields of a device.

Before requesting raw data, it is crucial to comprehend the device's data capabilities and the specific names of the data 
input and state fields it possesses.

It's important to note that this API request does not provide actual device data. Rather, it serves as a supplementary 
request aimed at gaining insights into the fields, which data that can be obtained subsequently.

#### parameters

| name       | description                                                                                                                                         | type | format |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). The tracker must be associated with the user whose hash is being used for the request, and not tariff-blocked. | int  | 123456 |

#### example

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/get_inputs' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "6dc7d304dec4434f4c4202ec42817f83","tracker_id": 123456}'
    ```

#### response

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

* `discrete_inputs` - int. A number of discrete inputs.
* `discrete_outputs` - int. A number of discrete outputs.
* `inputs` - string array. A list of available metering inputs.
* `states` - string array. A list of available state fields.

If there is more than one input of the same type, they are indexed (1, 2, 3...). In this case, only input with the maximum 
index is returned.

For example:

* If LLS Levels from 1 to 4 are available, `lls_level_4` is returned , and it is assumed that LLS levels 1 through 3 also exist. 
* If AVL IOs from 1 to 100000 are available for a device, `avl_io_100000` is returned, and AVL IOs with smaller indexes also exist.

#### errors

* 201 – Not found in the database – tracker ID does not exist. 
* 204 – Entity not found – there is no tracker with such ID belonging to authorized user. 
* 208 – Device blocked – tracker exists but was blocked due to tariff restrictions or some other reason.

### read

Retrieves parsed raw data - values received from tracking devices and decoded by the platform.

!!! note "The names and values of the inputs and state fields returned by this request align with the names visible in [Air Console](https://docs.navixy.com/admin-panel/air-console) when connecting to a device. You can find them in the right column, where the incoming data is decoded."

#### parameters

| name       | description                                                                                                                                                                       | type         | format                                                                            |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:----------------------------------------------------------------------------------|
| tracker_id | ID of the tracker (aka "object_id"). The tracker must be associated with the user whose hash is being used for the request, and not tariff-blocked.                               | int          | 123456                                                                            |
| from       | From date/time. Starting from what moment logs messages should be retrieved. It relates to the message time - when the packet was registered by a tracker. The time is specified along with time zone according to ISO8601.                                     | date/time    | "2023-08-24T08:04:36Z"                                                            |
| to         | To date/time. Till which moment messages should be retrieved into log. It relates to the message time - when the packet was registered by a tracker. Specified date must be after "from" date. The time is specified along with time zone according to ISO8601. | date/time    | "2023-08-24T08:04:36Z"                                                            |
| columns    | List of CSV columns to retrieve                                                                                                                                                   | string array | `["flags.location_valid","lat","lng","discrete_inputs.1","inputs.board_voltage"]` |
| server_time_filter | Optional interval for additional filtering message by server time. If it is used - messages will be returned not only be messaage time - when the packet was registered by a tracker, they will be filtered by server time - when the message sent to the server.                                                                                                                                              | string/object | `"2024-02-03T10:26:26+0500/2024-02-03T10:27:18+0500"` / `{"from": "2024-02-03T10:26:26+0500", "to": "2024-02-03T10:27:18+0500"}` / `{"interval":"2024-02-03T10:26:26+0500/PT1H"}` |

!!! note "Instead of using from/to parameters it is possible to set interval parameter - ISO8601 formatted interval, for example 2023-08-24T08:04:36.306Z/PT24H."

The response is provided in a CSV format file, with columns that are predefined in the `columns` parameter of the API request.
Here are the specifications for the table output:

* Rows are enclosed in double quotes. A double quote inside a string is output as two double quotes in a row. There are no other rules for escaping characters.
* Date and date-time are enclosed in double quotes.
* Numbers are output without quotes.
* Values are separated by a comma character `,` .
* Rows are separated using the Unix line feed (LF).
* `NULL` is represented as `\N`.
* Requested column can be a simple or complex.

**Simple** columns:

* `msg_time` - time of message sent by device. Always returned in CSV output and does not need to be requested separately. Indicated according to user account time zone.
* `server_time` - time of message processing by the server.
* `gps_fix_type` - enum. One of `UNKNOWN`, `NO_FIX`, `HAS_FIX`, `LAST_KNOWN_POSITION`.
* `lat` - float. Latitude.
* `lng` - float. Longitude.
* `speed` - decimal. Speed, km/h.
* `alt` - int. Altitude, meters.
* `satellites` - int. Satellites count (`-1` = unknown).
* `heading` - int. Heading degrees.
* `precision` - int. Location precision, meters.
* `hdop` - float. Horizontal dilution of precision  (`-1` = unknown).
* `pdop` - float. Position dilution of precision (`-1` = unknown).
* `event_id` - int. Event ID.
* `mn_name` - string. Mobile network name.
* `mn_roaming` - int. Roaming status (`0` = no roaming, `1` = roaming, `-1` = unknown).
* `mn_code` - int. Mobile network operator code.
* `mn_csq` - int. Mobile network signal strength, CSQ, values from 0 to 31 (`99` = unknown).
* `mn_type` - enum. Mobile network type, one of `UNKNOWN`, `GSM`, `CDMA`, `WCDMA`, `LTE`, `NR`.

**Complex** columns:

* `flags` - bitmap of flags:
    * bit 0 `location_valid`: `0` = location invalid, `1` = location valid.
    * bit 1 `lbs`:  `0` = GPS, `1` = LBS.
    * bit 2 `soft_lbs`:  `0` = device LBS, `1` = software LBS.
* `discrete_inputs` - map of discrete inputs states, inputs enumerated from 1.
* `discrete_outputs` - map of discrete outputs states, outputs enumerated from 1.
* `inputs` - map of metering inputs values. Inputs list depends on device.
* `states` - map of various states. States list depends on device.

To retrieve internal value from complex column, you need to use period symbol. For example: `flags.location_valid`,
`inputs.board_voltage`. Unknown internal values will be returned as `NULL`.

The list of available internal values for a particular device is obtained using `get_inputs` method described above.

If you specify complex column without specifying internal value, then all internal values will be returned as JSON map
(except flags that will be returned as integer).

You can append complex columns with an asterisk symbol:

* `inputs.*`
* `states.*`
* `discrete_inputs.*`
* `discrete_outputs.*`

In this case, the platform will search for all available columns in the specified data range and then request them from the database. In the resulting CSV output, instead of the column with an asterisk will be all the existing columns in alphabetical order. If there are no columns, they will not be shown in the response.

#### example for standard searching by message time only

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
    -H 'accept: text/csv' \
    -H 'Content-Type: application/json' \
    -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "123456",
    "from": "2023-11-30T07:13:00.000Z",
    "to": "2023-11-30T07:15:00.000Z",
    "columns": ["lat","lng","speed","inputs.ble_lls_level_1","inputs.hw_mileage","discrete_inputs.*"]}'
    ```

#### response

```
"msg_time","lat","lng","speed","inputs.ble_lls_level_1","inputs.hw_mileage","discrete_inputs.1","discrete_inputs.2"
"2023-11-30T13:13:14+0600",54.22809,69.5264283,28,2871,24296.444,0,1
"2023-11-30T13:13:25+0600",54.228095,69.5278333,32,2871,24296.536,0,1
"2023-11-30T13:13:36+0600",54.227765,69.5293916,39,2871,24296.644,0,1
"2023-11-30T13:13:46+0600",54.22744,69.5310083,39,2871,24296.756,0,1
"2023-11-30T13:13:55+0600",54.227205,69.5323383,29,2871,24296.847,0,1
"2023-11-30T13:13:56+0600",54.2271866,69.5324516,27,\N,\N,\N,\N
"2023-11-30T13:14:00+0600",54.2270866,69.5328033,22,2871,24296.881,0,1
"2023-11-30T13:14:01+0600",54.2270433,69.53286,23,2871,24296.887,0,1
"2023-11-30T13:14:02+0600",54.2269866,69.5328883,22,2871,24296.893,0,1
"2023-11-30T13:14:04+0600",54.2268766,69.5328683,22,2871,24296.906,0,1
"2023-11-30T13:14:05+0600",54.2268266,69.5328266,23,2871,24296.912,0,1
"2023-11-30T13:14:13+0600",54.2263733,69.5321966,33,2871,24296.977,0,1
"2023-11-30T13:14:18+0600",54.2259866,69.5318949,34,2871,24297.014,0,1
"2023-11-30T13:14:22+0600",54.2256266,69.5318,33,2871,24297.065,0,1
"2023-11-30T13:14:25+0600",54.22534,69.5318866,35,2871,24297.097,0,1
"2023-11-30T13:14:31+0600",54.224835,69.532085,33,2871,24297.155,0,1
"2023-11-30T13:14:42+0600",54.2238583,69.5320866,38,2871,24297.264,0,1
"2023-11-30T13:14:52+0600",54.2229033,69.5321616,36,2871,24297.36,0,1
"2023-11-30T13:15:00+0600",54.222275,69.5320816,36,2871,24297.44,0,1
```

#### example for searching by server time additionally

This API is designed to accommodate scenarios where you retrieve information from trackers to your applications within specified time intervals. Occasionally, trackers may experience connectivity issues. During such occurrences, these trackers automatically store information in their memory buffers. Upon re-establishing a connection, devices promptly transmit their stored information to the platform.

For instance:

A tracker was connected from 10:00 to 10:30. It then loses GSM signal, storing information in its buffer from 10:30 to 12:00. At 12:00, it reconnects and begins sending packets from the buffer. These packets are timestamped with message times starting from 10:30, 10:31, and so forth. However, the server time reflects 12:00, 12:01, and so on.
If your program requests data from 10:00 to 11:00 at 11:00 without utilizing the `server_time_filter` parameter, it will receive messages only from 10:00 to 10:30. The program might not be aware that it needs to re-request this data once all data from the buffer has been uploaded. 

To address such situations, there is an optional filtering using the `server_time_filter` parameter. This ensures that your program will get all buffered information. This approach helps prevent potential data gaps and enhances the reliability of your application.

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
    -H 'accept: text/csv' \
    -H 'Content-Type: application/json' \
    -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "123456",
    "from": "2024-02-03T07:00:00.000Z",
    "to": "2024-02-03T07:23:59.000Z",
    "server_time_filter": {"from": "2024-02-03T10:30:000Z", "to": "2024-02-03T12:30:000Z"}
    "columns": ["lat","lng","speed","inputs.ble_lls_level_1","inputs.hw_mileage","discrete_inputs.*"]}'
    ```

#### errors

* 201 – Not found in the database – tracker ID does not exist.
* 204 – Entity not found – there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked – tracker exists but was blocked due to tariff restrictions or some other reason.



