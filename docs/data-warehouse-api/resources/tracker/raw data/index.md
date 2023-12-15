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
| from       | From date/time. Starting from what moment logs messages should be retrieved. The time is specified along with time zone according to ISO8601.                                     | date/time    | "2023-08-24T08:04:36.306Z"                                                        |
| to         | To date/time. Till which moment messages should be retrieved into log. Specified date must be after "from" date. The time is specified along with time zone according to ISO8601. | date/time    | "2023-08-24T08:04:36.306Z"                                                        |
| columns    | List of CSV columns to retrieve                                                                                                                                                   | string array | `["flags.location_valid","lat","lng","discrete_inputs.1","inputs.board_voltage"]` |

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

#### example

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
    -H 'accept: text/csv' \
    -H 'Content-Type: application/json' \
    -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "123456",
    "from": "2023-11-29T08:31:00.000Z",
    "to": "2023-11-29T08:32:00.000Z",
    "columns": ["lat","lng","speed","inputs.lls_level_1","inputs.hw_mileage"]}'
    ```

#### response

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

#### errors

* 201 – Not found in the database – tracker ID does not exist.
* 204 – Entity not found – there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked – tracker exists but was blocked due to tariff restrictions or some other reason.



