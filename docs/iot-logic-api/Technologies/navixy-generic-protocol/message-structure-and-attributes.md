---
description: >-
  Complete reference for NGP message attributes: location, events, cell towers,
  Wi-Fi, sensors, I/O, and custom fields.
---

# Message structure and attributes

NGP messages are JSON objects transmitted one per request. Each message must contain two **mandatory** attributes: `device_id` and `message_time`. For transport connection parameters and body encoding requirements, see [Transport layer](transport-layer.md).

{% hint style="warning" %}
`message_time` must not be earlier than the timestamp of the most recently received message for this device. Messages with an out-of-order timestamp will be discarded by the platform.
{% endhint %}

{% hint style="info" %}
Fields with no availability tag work in all versions. Fields with restricted availability are marked:

- `1.2+` — requires `"version": "1.2"` in the message
- `on demand` — requires a separate arrangement with Navixy; not available for standard integrations
{% endhint %}

### Minimum valid message

```json
{
    "message_time": "2026-02-05T06:00:11Z",
    "device_id": "1112312212"
}
```

### Minimum message to be stored by the platform

The platform requires a valid location with at least 3 satellites before saving a data point. The `device_id` must already be registered on the platform.

```json
{
    "message_time": "2026-02-05T06:00:11Z",
    "device_id": "1112312212",
    "location": {
        "latitude": 34.15929687705282,
        "longitude": -118.4614133834839,
        "satellites": 3
    }
}
```

## Attributes

The table below lists all pre-defined attributes, organized by category. In addition to these, the protocol allows custom attributes. See [Custom attributes](message-structure-and-attributes.md#custom-attributes).

{% hint style="warning" %}
The platform validates all incoming messages. Messages with invalid JSON or out-of-range field values are silently discarded.
{% endhint %}

<table><thead><tr><th width="158">Attribute</th><th width="111">Type</th><th width="105">Object</th><th width="110">Required</th><th>Description</th><th>Availability</th></tr></thead><tbody><tr><td><strong>Basic attributes</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>message_time</td><td>Timestamp</td><td>Root</td><td>Yes</td><td>Date and time the message was sent by the device (ISO 8601 UTC).</td><td></td></tr><tr><td>device_id</td><td>String</td><td>Root</td><td>Yes</td><td>Unique device identifier. Maximum 64 characters.</td><td></td></tr><tr><td>version</td><td>String</td><td>Root</td><td>No</td><td>NGP version of this message. Defaults to <code>1.0</code> if omitted.</td><td></td></tr><tr><td><strong>Location</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>location</td><td>Object</td><td>Root</td><td>No</td><td>Device position. May be determined by GNSS (satellite), LBS (cell towers), or a third-party positioning service.</td><td></td></tr><tr><td>└─ latitude</td><td>Float</td><td>location</td><td>No</td><td>Latitude in decimal degrees (−90.0 to 90.0).</td><td></td></tr><tr><td>└─ longitude</td><td>Float</td><td>location</td><td>No</td><td>Longitude in decimal degrees (−180.0 to 180.0).</td><td></td></tr><tr><td>└─ altitude</td><td>Float</td><td>location</td><td>No</td><td>Altitude above sea level in meters (−1000 to 10000).</td><td></td></tr><tr><td>└─ gnss_time</td><td>Timestamp</td><td>location</td><td>No</td><td>Time when the position fix was acquired by the device.</td><td></td></tr><tr><td>└─ fix_type</td><td>String</td><td>location</td><td>No</td><td>Position fix type. Possible values: <code>HAS_FIX</code> (default), <code>NO_FIX</code>, <code>LAST_KNOWN_POSITION</code>, <code>FIX_2D</code>, <code>FIX_3D</code>.</td><td></td></tr><tr><td>└─ satellites</td><td>Integer</td><td>location</td><td>No</td><td>Number of GNSS satellites used for the fix (0–64).</td><td></td></tr><tr><td>└─ hdop</td><td>Float</td><td>location</td><td>No</td><td>Horizontal dilution of precision. Lower is more accurate.</td><td></td></tr><tr><td>└─ vdop</td><td>Float</td><td>location</td><td>No</td><td>Vertical dilution of precision. Lower is more accurate.</td><td></td></tr><tr><td>└─ pdop</td><td>Float</td><td>location</td><td>No</td><td>3D position dilution of precision, combining horizontal and vertical.</td><td></td></tr><tr><td>└─ speed</td><td>Float</td><td>location</td><td>No</td><td>Device speed in km/h (positive values only).</td><td></td></tr><tr><td>└─ heading</td><td>Integer</td><td>location</td><td>No</td><td>Direction of movement in degrees, clockwise from north (1–360).</td><td></td></tr><tr><td>└─ source_type</td><td>String</td><td>location</td><td>No</td><td>Positioning source. Possible values: <code>GNSS</code> (satellite), <code>LBS</code> (cell tower-based), <code>ATLAS</code> (third-party positioning service). Defaults to <code>GNSS</code> when omitted.</td><td><code>1.2+</code></td></tr><tr><td>└─ precision</td><td>Integer</td><td>location</td><td>No</td><td>Location accuracy in meters. Recommended for LBS and ATLAS positions.</td><td><code>1.2+</code></td></tr><tr><td><strong>Event information</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>event_id</td><td>Integer</td><td>Root</td><td>No</td><td>Platform event identifier. See <a href="predefined-event-identifiers.md">Predefined event identifiers</a> for standard values. Custom events start at 10,000.</td><td></td></tr><tr><td><strong>Mobile cells</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>mobile_cells</td><td>Array [Object]</td><td>Root</td><td>No</td><td>List of visible cell towers. Used to provide data for network-based positioning (LBS) when GNSS is unavailable.</td><td></td></tr><tr><td>└─ mcc</td><td>Integer</td><td>mobile_cells</td><td>Yes</td><td>Mobile Country Code. Identifies the country of the mobile network.</td><td></td></tr><tr><td>└─ mnc</td><td>Integer</td><td>mobile_cells</td><td>Yes</td><td>Mobile Network Code. Identifies the mobile operator within the country.</td><td></td></tr><tr><td>└─ lac</td><td>Integer</td><td>mobile_cells</td><td>Yes</td><td>Location Area Code. Identifies the area within the mobile network.</td><td></td></tr><tr><td>└─ cell_id</td><td>Integer</td><td>mobile_cells</td><td>Yes</td><td>Unique identifier of the cell tower.</td><td></td></tr><tr><td>└─ rssi</td><td>Integer</td><td>mobile_cells</td><td>No</td><td>Signal strength from the cell tower in dBm (negative values).</td><td></td></tr><tr><td>└─ type</td><td>String</td><td>mobile_cells</td><td>No</td><td>Radio access technology. Possible values: <code>GSM</code> (default), <code>CDMA</code>, <code>WCDMA</code>, <code>LTE</code>, <code>NR</code>.</td><td></td></tr><tr><td><strong>Wi-Fi points</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>wifi_points</td><td>Array [Object]</td><td>Root</td><td>No</td><td>List of visible Wi-Fi access points. Used alongside <code>mobile_cells</code> to improve network-based positioning accuracy.</td><td></td></tr><tr><td>└─ mac</td><td>String</td><td>wifi_points</td><td>Yes</td><td>MAC address of the access point. Colon-delimited bytes, e.g. <code>12:33:FF:45:04:33</code>.</td><td></td></tr><tr><td>└─ rssi</td><td>Integer</td><td>wifi_points</td><td>Yes</td><td>Signal strength in dBm (negative values).</td><td></td></tr><tr><td>└─ age</td><td>Integer</td><td>wifi_points</td><td>No</td><td>Milliseconds since this access point was last detected.</td><td></td></tr><tr><td>└─ channel</td><td>Integer</td><td>wifi_points</td><td>No</td><td>Radio channel number used by the access point.</td><td></td></tr><tr><td><strong>Device motion and status</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>is_moving</td><td>Boolean</td><td>Root</td><td>No</td><td><code>true</code> if the device is currently moving, <code>false</code> if stationary.</td><td></td></tr><tr><td>hardware_mileage</td><td>Float</td><td>Root</td><td>No</td><td>Cumulative mileage counted by the device hardware, in kilometers.</td><td></td></tr><tr><td>battery_voltage</td><td>Float</td><td>Root</td><td>No</td><td>Built-in battery voltage in volts.</td><td></td></tr><tr><td>battery_level</td><td>Integer</td><td>Root</td><td>No</td><td>Built-in battery charge level as a percentage (0–100).</td><td></td></tr><tr><td>board_voltage</td><td>Float</td><td>Root</td><td>No</td><td>External power supply voltage in volts.</td><td></td></tr><tr><td><strong>Input/Output status</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>input_status</td><td>Integer</td><td>Root</td><td>No</td><td>State of discrete inputs as a bitmask. Bit 0 = input 1, bit 1 = input 2, and so on. A set bit means the input is active.</td><td></td></tr><tr><td>output_status</td><td>Integer</td><td>Root</td><td>No</td><td>State of outputs as a bitmask. Bit 0 = output 1, bit 1 = output 2, and so on. A set bit means the output is active.</td><td></td></tr><tr><td><strong>Sensor data</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>analog_n</td><td>Float</td><td>Root</td><td>No</td><td>Analog input voltage in volts. <code>n</code> is the sensor index from 1 to 16, e.g. <code>analog_1</code>, <code>analog_2</code>.</td><td></td></tr><tr><td>temperature_internal</td><td>Float</td><td>Root</td><td>No</td><td>Temperature from the built-in hardware sensor, in degrees Celsius.</td><td></td></tr><tr><td>temperature_n</td><td>Float</td><td>Root</td><td>No</td><td>External temperature sensor reading in degrees Celsius. <code>n</code> is the sensor index from 1 to 16, e.g. <code>temperature_1</code>, <code>temperature_2</code>.</td><td></td></tr><tr><td>humidity_internal</td><td>Float</td><td>Root</td><td>No</td><td>Relative humidity from the built-in hardware sensor, as a percentage.</td><td></td></tr><tr><td>humidity_n</td><td>Float</td><td>Root</td><td>No</td><td>External relative humidity sensor reading as a percentage. <code>n</code> is the sensor index from 1 to 16, e.g. <code>humidity_1</code>.</td><td></td></tr><tr><td>fuel_level_n</td><td>Float</td><td>Root</td><td>No</td><td>Fuel level from a fuel sensor, in liters or as a percentage. <code>n</code> is the sensor index from 1 to 16, e.g. <code>fuel_level_1</code>.</td><td></td></tr><tr><td>fuel_temperature_n</td><td>Float</td><td>Root</td><td>No</td><td>Fuel temperature from a fuel sensor, in degrees Celsius. <code>n</code> is the sensor index from 1 to 16, e.g. <code>fuel_temperature_1</code>.</td><td></td></tr><tr><td>impulse_counter_n</td><td>Integer</td><td>Root</td><td>No</td><td>Impulse counter reading. <code>n</code> is the counter index from 1 to 16, e.g. <code>impulse_counter_1</code>.</td><td></td></tr><tr><td><strong>Identification data</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>hardware_key</td><td>String</td><td>Root</td><td>No</td><td>Driver or asset identifier, typically read via RFID, iButton, or similar method.</td><td></td></tr><tr><td>vin</td><td>String</td><td>Root</td><td>No</td><td>Vehicle Identification Number (VIN).</td><td></td></tr><tr><td><strong>Custom data</strong></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>custom_*</td><td>Mixed</td><td>Root</td><td>No</td><td>Any additional device-specific attribute. See <a href="message-structure-and-attributes.md#custom-attributes">Custom attributes</a>.</td><td></td></tr><tr><td>custom_attributes</td><td>Array [Object]</td><td>Root</td><td>No</td><td>Structured custom attribute array with metadata. Requires <code>"version": "1.1a"</code> and a separate arrangement with Navixy.</td><td><code>on demand</code></td></tr><tr><td>└─ type</td><td>String</td><td>custom_attributes</td><td>Yes</td><td>Attribute name.</td><td><code>on demand</code></td></tr><tr><td>└─ id</td><td>Integer</td><td>custom_attributes</td><td>No</td><td>Attribute order number.</td><td><code>on demand</code></td></tr><tr><td>└─ value</td><td>Mixed</td><td>custom_attributes</td><td>Yes</td><td>Attribute value. Any JSON type.</td><td><code>on demand</code></td></tr><tr><td>└─ units</td><td>String</td><td>custom_attributes</td><td>No</td><td>Unit of measurement, e.g. <code>rpm</code>, <code>percent</code>.</td><td><code>on demand</code></td></tr></tbody></table>

## Location source and accuracy

`source_type` identifies where the position coordinates came from. When omitted, the platform treats the location as GNSS by default. Declaring the source explicitly lets the platform apply the correct processing logic — for example, skipping satellite-count validation for LBS positions.

`precision` reports the estimated accuracy of the resolved coordinates in meters. It is optional but recommended for LBS and ATLAS positions, where accuracy can vary significantly. The platform can use this value to determine whether the accuracy is sufficient for a given use case.

Both fields require `"version": "1.2"` in the message.

{% code title="Example: LBS-based position report" %}
```json
{
    "message_time": "2024-09-02T10:05:12Z",
    "device_id": "857378374927457",
    "version": "1.2",
    "location": {
        "latitude": 56.352100,
        "longitude": 60.128900,
        "source_type": "LBS",
        "precision": 800
    },
    "event_id": 402,
    "mobile_cells": [
        {
            "mcc": 250,
            "mnc": 0,
            "lac": 32445,
            "cell_id": 343455,
            "rssi": -78,
            "type": "LTE"
        }
    ]
}
```
{% endcode %}

The `precision` value of `800` indicates the resolved coordinates are accurate within approximately 800 meters.

## Message example

A complete telemetry message from a GPS device with GNSS positioning:

```json
{
    "message_time": "2024-09-02T10:03:43Z",
    "device_id": "857378374927457",
    "version": "1.2",
    "location": {
        "gnss_time": "2024-09-02T10:03:41Z",
        "fix_type": "HAS_FIX",
        "latitude": 56.348579,
        "longitude": 60.12344,
        "altitude": 271,
        "satellites": 8,
        "hdop": 0.41,
        "pdop": 2.0,
        "speed": 43,
        "heading": 77,
        "source_type": "GNSS"
    },
    "event_id": 406,
    "mobile_cells": [
        {
            "mcc": 250,
            "mnc": 0,
            "lac": 32445,
            "cell_id": 343455,
            "rssi": -54,
            "type": "LTE"
        }
    ],
    "wifi_points": [
        {
            "mac": "12:33:FF:45:04:33",
            "rssi": -54,
            "age": 4002,
            "channel": 11
        }
    ],
    "is_moving": true,
    "hardware_mileage": 7382.3,
    "battery_voltage": 4.12,
    "battery_level": 93,
    "board_voltage": 13.9,
    "input_status": 1,
    "output_status": 0,
    "hardware_key": "12FFABC54234",
    "temperature_internal": 12.3,
    "temperature_2": -13.7,
    "custom_fuel": 86
}
```

## Custom attributes

The protocol allows you to extend messages with device-specific or application-specific data that has no pre-defined attribute. Custom attributes are added directly to the root of the message object.

Any field name not listed in the attributes table above is treated as a custom attribute and passed through to the platform unchanged. Common use cases include hardware-specific telemetry fields such as `avl_io_1`, `flex_id`, or `engine_rpm`. This format requires no version declaration and covers most integration needs.

```json
{
    "message_time": "2024-09-02T12:23:45Z",
    "device_id": "857378374927457",
    "version": "1.0",
    "location": {
        "latitude": 34.15929687705282,
        "longitude": -118.4614133834839
    },
    "custom_fuel": 86
}
```

### Structured custom attributes

For integrations that need typed metadata alongside sensor values, NGP supports an alternative format: the `custom_attributes` array. Each entry carries a `type` (attribute name), `value`, and optional `id` (ordering) and `units` fields. This is useful when units of measurement, attribute ordering, or typed metadata are required by the receiving system.

For most integrations, the simple `custom_*` format above is sufficient and preferable. Use `custom_attributes` only when the structured metadata is a specific requirement of your integration.

Both formats can coexist in the same message. `custom_attributes` requires `"version": "1.1a"` and a separate arrangement with Navixy — it is not available for standard integrations.

{% code title="Example: simple and structured custom attributes in the same message" %}
```json
{
    "message_time": "2024-09-02T12:23:45Z",
    "device_id": "857378374927457",
    "version": "1.1a",
    "location": {
        "latitude": 34.15929687705282,
        "longitude": -118.4614133834839
    },
    "custom_fuel": 86,
    "custom_attributes": [
        {
            "type": "engine_rpm",
            "id": 1,
            "value": 2100,
            "units": "rpm"
        },
        {
            "type": "vehicle_load",
            "id": 2,
            "value": 75,
            "units": "percent"
        }
    ]
}
```
{% endcode %}

Continue reading to learn about [Predefined event identifiers](predefined-event-identifiers.md) in Navixy Generic Protocol.
