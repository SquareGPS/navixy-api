---
title: BLE beacon data
description: Contains list of methods to get BLE beacon data.
---

# BLE beacon data

Methods for obtaining collected BLE beacon data.
BLE beacon data is data about radio tags (BLE beacons) visible to a tracker, e.g. iBeacon, Teltonika EYE Beacon\Sensor, Eddystone.


## BLE beacon data entry
```json
{
  "tracker_id": 10181654,
  "hardware_id": "7cf9501df3d6924e423cabcde4c924ff",
  "rssi": -101,
  "get_time": "2023-04-17 17:14:42",
  "latitude": 50.3487321,
  "longitude": 7.58238,
  "ext_data": {
    "voltage": 3.075,
    "temperature": 24.0
  }
}
```

* `tracker_id` - int. An ID of the tracker (aka "object_id").
* `hardware_id` - string. An ID of the beacon.
* `rssi` - int. RSSI stands for received signal strength indicator and represents the power of received signal on a device. According to it, you can understand how far away the beacon is from the tracker.
* `get_time` - [date/time](../../../getting-started/introduction.md#data-types). When this data received.
* `latitude` - float.  Latitude.
* `longitude` - float.  Longitude.
* `ext_data` - object. Additional beacon data.

## API actions

API path: `/beacon/data/read`.

### `read`

List of beacon data history between `from` date/time and `to` date/time sorted by **get_time** field.

#### Parameters

| name      | description                                                                                              | type                                                       |
|:----------|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| from      | Start date/time for searching.                                                                           | string [date/time](../../../getting-started/introduction.md#data-types) |
| to        | End date/time for searching. Must be after "from" date.                                                  | string [date/time](../../../getting-started/introduction.md#data-types) |
| trackers  | Optional. Default: null. List of trackers.                                                               | int array                                                  |
| beacons   | Optional. Default: null. List of beacons IDs. All IDs must not be empty and not more than 64 characters. | string array                                               |
 

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/beacon/data/read' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "from": "2023-04-17 17:00:00",
    "to": "2023-04-17 18:00:00",
    "beacons": ["ffffffffd86f4f75868d55aa831afa1f", "7cf9501df3d6924e423cabcde4c924ff"],
    "trackers": [10181654]
    }'
    ```

#### Response

```json
{
  "list": [
    {
      "tracker_id": 10181654,
      "hardware_id": "ffffffffd86f4f75868d55aa831afa1f",
      "rssi": -96,
      "get_time": "2023-04-17 17:14:20",
      "latitude": 50.3487301,
      "longitude": 7.58207,
      "ext_data": {
        "minor": "0055",
        "major": "3138"
      }
    },
    {
      "tracker_id": 10181654,
      "hardware_id": "7cf9501df3d6924e423cabcde4c924ff",
      "rssi": -101,
      "get_time": "2023-04-17 17:14:42",
      "latitude": 50.3487321,
      "longitude": 7.58238,
      "ext_data": {
        "voltage": 3.075,
        "temperature": 24.0
      }
    }
  ],
  "success": true
}
```

* `list` - list of zero or more `beacon_data_entry` objects which is described in [Beacon data entry](index.md#ble-beacon-data-entry).


API path: `/beacon/data/last_values`.

### `last values`

List of last BLE beacon data visible on the trackers.

#### Parameters

| name                    | description                                                                       | type              |
|:------------------------|:----------------------------------------------------------------------------------|:------------------|
| trackers                | Optional. Default: null. List of trackers.                                        | int array         |
| skip_older_than_seconds | Optional. Default: 3600. Skip entries older than the specified number of seconds. | int               |    




#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/beacon/data/last_values' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "trackers": [10181654],
    "skip_older_than_seconds": 3600
    }'
    ```

#### Response

```json
{
  "list": [
    {
      "tracker_id": 10181654,
      "hardware_id": "7cf9501df3d6924e423cabcde4c924ff",
      "rssi": -101,
      "get_time": "2023-04-17 17:14:42",
      "latitude": 50.3487321,
      "longitude": 7.58238,
      "ext_data": {
        "voltage": 3.075,
        "temperature": 24.0
      }
    }
  ],
  "success": true
}
```

* `list` - list of zero or more `beacon_data_entry` objects which is described in [Beacon data entry](index.md#ble-beacon-data-entry).
