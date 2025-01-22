# Retrieving Sensor and Counter Data

This guide provides comprehensive instructions on retrieving and manipulating sensor data and counter information using the Navixy API. It includes detailed steps on working with various sensors, generating reports, and setting up rules based on sensor data.

## Sensor types

In the Navixy software, the concept of a sensor represents an abstraction used to monitor and collect data from various IoT sensing devices. This abstraction seamlessly integrates both the software and hardware perspectives. From a hardware standpoint, a sensor can range from a simple thermometer that measures temperature to a sophisticated dash cam that analyzes in-vehicle video footage. In the software, these sensors are treated as data sources that provide valuable information for monitoring and analysis.

Navixy supports both **Physical sensors** and **Virtual sensors**. Physical sensors include measurement sensors (e.g., temperature, voltage), discrete sensors (e.g., ignition on/off, door open/closed), and counters (e.g., odometer, engine hours). Virtual sensors, on the other hand, help to further transform and interpret the values from physical sensors, enabling advanced data processing and custom metrics creation.

## Physical sensors

Within the category of Physical sensors, Navixy differentiates three categories of sensors:
   
1. **Measurement sensors**: These sensors measure and report continuous data points such as temperature, voltage, or fuel level. For example, a coolant temperature sensor that monitors the engine coolant temperature.

2. **Discrete sensors**: These sensors detect and report binary states such as on/off or open/close. For instance, an ignition sensor that indicates whether the vehicle ignition is on or off, or a door sensor that shows if a door is open or closed.
   
3. **Counters**: These sensors track cumulative data over time, such as distance traveled or operating hours. Examples include an odometer that measures the total distance a vehicle has traveled, or an engine hours counter that logs the total operating time of an engine.

For a comprehensive list of supported sensors, refer to the [input_name documentation](../../resources/tracking/tracker/sensor/input_name.md#response).

### Managing physical sensors

There are two primary methods for creating physical sensors on the Navixy platform: automatic sensor creation and manual sensor creation.

#### Automatic sensor creation

Some sensors are automatically created by the platform when a new device is activated. The list of such sensors depends on the model capabilities. These automatically created sensors provide immediate and valuable data without requiring additional setup, enabling a seamless and efficient monitoring experience for IoT and telematics applications.

**Example:** When an OBDII tracker is activated, the platform can automatically create a variety of sensors depending on the device's model and capabilities. These sensors can include:
- Ignition sensor
- Fuel level sensor
- Coolant temperature sensor
- Engine RPM sensor
- etc.

#### Manual sensor creation

For sensors that require manual creation, follow these steps:

1. **Configure Data Sending:** Ensure that the sensor is configured to send data from the device side.
2. **Verify Data Reception:** Use [AirConsole](../../../../panel-api/resources/tracker.md#consoleconnect) to verify that the platform is receiving the data correctly.
3. **Calibrate the Sensor:** If necessary, [calibrate the sensor](../../resources/tracking/tracker/sensor/calibration_data.md) (for analog sensors or those sending uncalibrated values) to ensure accurate data readings.

By using these methods, you can effectively manage both automatically and manually created physical sensors, ensuring comprehensive and reliable data collection for your IoT and telematics applications.

### Retrieving physical sensor data

#### Current sensor values

To retrieve current sensor values, use the following API calls:

- Input states: [get_inputs](../../resources/tracking/tracker/index.md#get_inputs)
- CAN and OBD sensor data: [get_diagnostics](../../resources/tracking/tracker/index.md#get_diagnostics)
- Fuel sensor data: [get_fuel](../../resources/tracking/tracker/index.md#get_fuel)
- Other metering sensor readings: [get_readings](../../resources/tracking/tracker/index.md#get_readings)

#### Comprehensive sensor data

To retrieve data from all sensors, states, and counters of a device, use the [tracker/readings](../../resources/tracking/tracker/readings.md) API call.

Example response:

```json
{
    "success": true,
    "inputs": [
        {
            "label": "Board voltage",
            "units": "V",
            "name": "board_voltage",
            "type": "power",
            "value": 26.13,
            "units_type": "custom",
            "converted_units_type": null,
            "converted_value": null,
            "update_time": "2021-06-01 15:23:03"
        },
        {
            "label": "Analog sensor #1",
            "units": "",
            "name": "analog_1",
            "type": "fuel",
            "min_value": 0.0,
            "max_value": 450.0,
            "value": 269.82,
            "units_type": "litre",
            "converted_units_type": null,
            "converted_value": null,
            "update_time": "2021-06-01 15:23:03"
        }
    ],
    "states": [
        {
            "field": "battery_level",
            "value": 4.01,
            "update_time": "2021-06-01 15:23:03"
        },
        {
            "field": "input_status",
            "value": 0,
            "update_time": "2021-06-01 15:23:03"
        },
        {
            "field": "output_status",
            "value": 3,
            "update_time": "2021-06-01 15:23:03"
        }
    ]
}
```

Note: The `input_status` and `output_status` fields provide binary information in decimal form. For example, an `output_status` of 3 (binary 11) indicates that both output 1 and output 2 are ON.

#### Batch retrieval for multiple devices

To optimize requests for multiple devices, use the [tracker/readings/batch_list](../../resources/tracking/tracker/readings.md#batchlist) API call.

#### Historical sensor data

To retrieve historical data from measurement sensors (up to 30 days), use the [tracker/sensor/data/read](../../resources/tracking/tracker/sensor/index.md#dataread) API call. Specify the sensor ID, which can be obtained using the [sensor/list](../../resources/tracking/tracker/sensor/index.md#list) request.

### Using counters

Counters are tools for monitoring specific metrics, such as odometer (mileage) and engine hours.

#### Counter creation

To create a counter, use the [value/set](../../resources/tracking/tracker/counter.md#valueset) API call.

Example for creating an odometer counter:

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/counter/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 311852, "type": "odometer", "value": 98342.1}'
```

Example for creating an engine hours counter:

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/counter/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 311852, "type": "engine_hours", "value": 2368.2}'
```

#### Retrieving counter values

- Get all counter values: [get_counters](../../resources/tracking/tracker/counter.md#get_counters)
- Get specific counter type for one device: [value/get](../../resources/tracking/tracker/counter.md#valueget)
- Get counter values for multiple devices: [value/list](../../resources/tracking/tracker/counter.md#valuelist)

#### Historical counter data

To retrieve counter values with timestamps for a specific period, use the [data/list](../../resources/tracking/tracker/counter.md#dataread) API call.

Example response:

```json
{
  "success": true,
  "list": [
    {
      "value": 581321.0,
      "update_time": "2021-05-30 12:16:01"
    },
    {
      "value": 581322.0,
      "update_time": "2021-05-30 12:36:01"
    },
    {
      "value": 581323.0,
      "update_time": "2021-05-30 12:56:01"
    },
    {
      "value": 581324.0,
      "update_time": "2021-05-30 13:16:01"
    },
    {
      "value": 581325.0,
      "update_time": "2021-05-30 13:36:01"
    }
  ]
}
```

#### Aggregated counter data

To retrieve counted values for a specific period:
- Mileage: [stats/mileage](../../resources/tracking/tracker/stats/stats_mileage.md)
- Engine hours: [stats/engine_hours](../../resources/tracking/tracker/stats/stats_engine_hours.md)

## Virtual sensors

Virtual sensors provide an additional server-side layer where users can process input values to produce derived output values. They can be configured to analyze and manipulate data from other sensors, creating custom metrics or alerts. 

By interpreting and translating raw data from physical sensors, virtual sensors make information more comprehensible and actionable. They are particularly useful for monitoring ignition states, translating complex sensor values, and working with predefined sets of values.

**Virtual sensor object structure:**

```json
{
  "type": "virtual",
  "id": 1700049,
  "sensor_type": "virtual_ignition",
  "name": "Virtual Ignition",
  "input_name": "board_voltage",
  "parameters": {
    "calc_method": "in_range",
    "range_from": 13.4,
    "value_titles": [{
        "value": "0",
        "title": "Off"
    }, {
        "value": "1",
        "title": "On"
    }]
  }
}
```

Key parameters:

| Field          | Type   | Description                                                                                          |
|----------------|--------|------------------------------------------------------------------------------------------------------|
| `type`         | string | Must be set as `virtual` for virtual sensors.                                                        |
| `id`           | int    | The sensor's ID.                                                                                     |
| `sensor_type`  | enum   | Must be "virtual_ignition" for virtual ignition sensor or "state" for others.                        |
| `name`         | string | Name of the sensor. May contain up to 100 characters.                                                |
| `input_name`   | string | Source input field (identifier). Indicates which sensor provides the information to the platform.    |
| `parameters`   | object | Additional parameters for the sensor.                                                                |
| `calc_method`  | enum   | Method of sensor value calculation. Must be one of: `in_range`, `identity`, `bit_index`.             |
| `range_from`   | double | Lower boundary of the range (used with "in_range" calculation method).                               |
| `range_to`     | double | Upper boundary of the range (used with "in_range" calculation method).                               |
| `bit_index`    | int    | Bit index in the input field source value (used with "bit_index" calculation method). Range: [1..N]. |
| `value_titles` | array  | Mapping for assigning special titles to sensor values.                                               |
| `value`        | string | Raw sensor value from the device. Max size: 64 characters.                                           |
| `title`        | string | Custom title for the sensor value. Max size: 64 characters.                                          |

**Notes:**
- Only one virtual sensor of the type `virtual_ignition` is allowed per GPS device.
- For the `in_range` calculation method, at least one of `range_from` or `range_to` must be specified.
- The `bit_index` field is required for the `bit_index` calculation method, and all values within "value_titles" must be unique.


### Use cases for virtual sensors

#### Monitoring parameter boundaries (`in_range`)

One of the common uses for Virtual sensor functionality is monitoring and maintaining critical parameters within specified boundaries. This sensor type is particularly useful for:

- Virtual ignition monitoring
- Temperature control
- Humidity regulation
- Fuel level management

**Operational principle:**
A virtual sensor with the `in_range`  type operates by evaluating whether the sensor value falls within predefined boundaries. Based on this evaluation, it outputs either *A value* for normal operation or *B value* to signal a potential issue.

| Condition                                    | Output  | Description                                                                                              |
|----------------------------------------------|---------|----------------------------------------------------------------------------------------------------------|
| Sensor value falls within defined boundaries | Value A | Indicates that the sensor is operating within the expected range, signaling safe or optimal levels.      |
| Sensor value is outside defined boundaries   | Value B | Signals that the sensor has detected a value outside the predefined range, alerting to potential issues. |

##### Example 1. Virtual ignition (evaluated on the server side)

A particular case of a sensor the type `in_range`  is the virtual ignition implementation calculated on the server side. This is useful for GPS tracking devices lacking a dedicated ignition input or with all physical inputs occupied. A virtual ignition sensor can be configured to detect the ignition state by monitoring significant increases in the vehicle's onboard voltage during engine startup.

**Implementation details:**
- Typical threshold for vehicles with 12V on-board electrical system : 13.2V
- When board voltage exceeds threshold: Engine operational
- When board voltage falls below threshold: Engine off

##### Example 2. Sensor value normalization

The 'Value in Range' approach can be applied to normalize various sensor readings, transforming raw data into more comprehensible and user-friendly formats. For instance, temperature data from an uncalibrated analog sensor can be translated into a more meaningful temperature scale that users can easily understand.

Let's consider an example where we have a raw temperature sensor output that needs to be normalized. The raw output from the sensor might be uncalibrated and not in a human-readable format. By configuring a virtual sensor, we can translate these raw values into comprehensible temperature readings.

- **Raw sensor output**: 1020 = -10°C, 1900 = 0°C
- **Virtual sensor configuration**:

    * `type`: `virtual`
    * `sensor_type`: `state`
    * `name`: `Normalized Temperature Sensor`
    * `input_name`: `raw_temp_sensor`
    * `parameters`: `{ ... }` (additional parameters if needed)
    * `calc_method`: `in_range`
    * `range_from`: 1020
    * `range_to`: 1900
    * `value_titles`: 
      ```json
      {
        "1020": "-10°C",
        "1900": "0°C"
      }
      ```

**Configuration**:

```json
{
  "type": "virtual",
  "id": 456,
  "sensor_type": "state",
  "name": "Normalized Temperature Sensor",
  "input_name": "raw_temp_sensor",
  "calc_method": "in_range",
  "range_from": 1020,
  "range_to": 1900,
  "value_titles": {
    "1020": "-10°C",
    "1900": "0°C"
  }
}
```

#### Mapping nominal sensor values (`identity`)

Virtual sensors in Navixy also allow for custom definitions of received values, making them ideal for scenarios where predefined sets of nominal values (or strings) are used. You can map nominal input values into predefined output values using the `identity` type of virtual sensor.

**Applications:**

| Type                    | Description                                       | Examples                                                  |
|-------------------------|---------------------------------------------------|-----------------------------------------------------------|
| **Binary States**       | Easily handle simple on/off or true/false states. | Ignition on/off, door open/closed                         |
| **Multi-State Systems** | Manage states that have more than two conditions. | Security system armed/disarmed, window open/closed/locked |
| **Enumerated States**   | Work with a predefined set of named states.       | Device states like state1/state2/state3 or key1/key2/key3 |

This flexibility guarantees that you can accurately capture and interpret the operational status of connected equipment, providing clear insights and actionable data for IoT and telematics applications.

**Operational principle:**
1. Received value 1 = Defined value A
2. Received value 2 = Defined value B
3. Received value 3 = Defined value C, etc.

**Note:** For historical data on these sensors, utilize the state field value alert with the "Report on All Events" feature.

##### Example 1. PTO drive engagement sensor

Consider a truck equipped with a Power Take-Off (PTO) drive engagement sensor outputting the following values:

| Raw Value | Meaning                        |
|-----------|--------------------------------|
| 0         | No PTO drive engaged           |
| 1         | At least one PTO drive engaged |
| 2         | Error                          |
| 3         | Not available                  |

A virtual sensor can translate these raw values into meaningful status information.

##### Example 2. Hardware driver / asset identificators readings

Certain telematics devices can identify drivers, equipment, or trailers using:
- iButtons
- RFID keys
- Bluetooth sensors

The platform identifies the nearest entity to the device, and a Virtual Sensor can display the corresponding names.

**Implementation:**
1. Each unit (driver/equipment/trailer) is assigned a unique tag.
2. The tag serves as a hardware key recognizable by the platform.
3. When a unit connects to the device, its key is transmitted to the platform.
4. The virtual sensor displays the associated name or identifier.

This method ensures clear identification of the unit currently interacting with the telematics device.

##### Example 3. Hardware event codes reading

The Navixy platform can process and display the most recent event code received from a device. This feature is particularly useful for systems with predefined event codes.

**Example:** For a dash camera, you can access and display Driver Monitoring System (DMS) events through a virtual sensor. By mapping event codes with descriptions, you can log important events in a meaningful, user-friendly format.

| Event Code | Description                   |
|------------|-------------------------------|
| DMS_001    | Driver fatigue detected       |
| DMS_002    | Driver distraction detected   |
| DMS_003    | Smoking detected              |
| DMS_004    | Phone usage detected          |

#### Decoding binary data (`bit_index`)

Virtual sensors in Navixy also allow decoding complex data packets from IoT devices in binary format, where multiple parameters are consolidated into a single value. For this purpose, you should use the `bit_index` sensor type.

**Operational principle:**
The virtual sensor interprets specific bits within the transmitted value, allowing for the extraction of individual parameters. This method is particularly useful for telematics applications where data efficiency and clarity are critical.

**Example:**
Given a transmitted value of 011 (interpreted in little-endian format):

| Bit           | Value | Meaning                                          |
|---------------|-------|--------------------------------------------------|
| 1 (rightmost) | 1     | Driver's seat belt: 0 = fastened, 1 = unfastened |
| 2             | 1     | Driver's door: 0 = closed, 1 = open              |
| 3             | 0     | Hood: 0 = closed, 1 = open                       |

To utilize this data effectively, create a separate virtual sensor for each parameter you wish to monitor. By decoding the specific bits, you can track various states and conditions of a vehicle in a precise and efficient manner, making your telematics solution more robust and insightful.

### Managing virtual sensors 

#### Creating a virtual sensor

To create a virtual sensor, use the [tracker/sensor/create](../../resources/tracking/tracker/sensor/index.md#create) API call. This allows you to define and configure virtual sensors based on specific input parameters. Virtual sensors can be used to monitor various conditions and provide meaningful insights.

Example for creating a virtual ignition sensor:

```shell
curl -X POST 'https://api.navixy.com/v2/tracker/sensor/create' \
-H 'Content-Type: application/json' \
-d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor": {"type": "virtual", "sensor_type": "virtual_ignition", "name": "Virtual Ignition", "input_name": "board_voltage", "parameters": {"calc_method": "in_range", "range_from": 13.4, "value_titles": [{"value": "0", "title": "Off"}, {"value": "1", "title": "On"}]}}}'
```

This example demonstrates how to create a virtual ignition sensor that monitors the board voltage to determine the ignition state. The sensor will output "Off" when the voltage is below 13.4V and "On" when it is above.

#### Updating a virtual sensor

To update an existing virtual sensor, use the [tracker/sensor/update](../../resources/tracking/tracker/sensor/index.md#update) API call. This is useful for modifying the parameters or configuration of an already created sensor to reflect new thresholds or settings.

Example for updating a virtual ignition sensor:

```shell
curl -X POST 'https://api.navixy.com/v2/tracker/sensor/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor": {"type": "virtual", "sensor_id": 965837, "sensor_type": "virtual_ignition", "name": "Virtual Ignition", "input_name": "board_voltage", "parameters": {"calc_method": "in_range", "range_from": 13.7, "value_titles": [{"value": "0", "title": "Off"}, {"value": "1", "title": "On"}]}}}'
```

This example shows how to update a virtual ignition sensor, changing the voltage threshold from 13.4V to 13.7V. The sensor will now use the updated threshold to determine the ignition state, ensuring that the monitoring criteria are current and accurate.
### Retrieving virtual sensor data

1. **Historical data**
   Use the [tracker/sensor/data/read](../../resources/tracking/tracker/sensor/index.md#dataread) API call.

   Example:
   ```shell
   curl -X POST 'https://api.navixy.com/v2/tracker/sensor/data/read' \
       -H 'Content-Type: application/json' \
       -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor_id": 965837, "from": "2023-07-24 00:00:00", "to": "2023-07-24 23:59:00", "raw_data": false}'
   ```

2. **Current values**
   Use the [tracker/readings/batch_list](../../resources/tracking/tracker/readings.md#batchlist) API call for multiple devices.

   Example:
   ```shell
   curl -X POST '{{ extra.api_example_url }}/tracker/readings/batch_list' \
       -H 'Content-Type: application/json' \
       -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": [10181215,10038816]}'
   ```

## Reports

Various reports can be generated to analyze sensor and counter data:

1. **Equipment working time report**
    * Plugin ID: 12
    * Shows operational times of units linked to discrete or virtual inputs.

    Example:
    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Equipment working time", "trackers": [642546], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs":true,"plugin_id":12,"show_seconds":false,"min_working_period_duration":60,"show_idle_percent":true,"filter":false,"sensors":[{"tracker_id":642546,"sensor_id":1931610}]}}'
    ```

2. **Engine hours report**
    * Plugin ID: 7
    * Shows working duration for ignition-based sensors.

    Example:
    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Engine hours report", "trackers": [642546], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs":true,"plugin_id":7,"show_seconds":false,"show_detailed":true,"include_summary_sheet":true,"include_summary_sheet_only":false,"filter":true}}'
    ```

3. **Measuring sensors report**
    * Plugin ID: 9
    * Displays data from measurement sensors or virtual sensors with source value calculation method.

    Example:
    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Measuring sensors report", "trackers": [1685505], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs": true, "plugin_id": 9, "details_interval_minutes": 5, "graph_type": "time", "smoothing": true, "show_address": false, "filter": true, "sensors": [{"tracker_id": 1685505, "sensor_id": 613753}]}}'
    ```

4. **Vehicle readings report**
    * Plugin ID: 22
    * Shows data from vehicle instruments via CAN/OBD or virtual sensors.

    Example:
    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
     -H 'Content-Type: application/json' \
     -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Vehicle readings report", "trackers": [642546], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs": true, "plugin_id": 22, "details_interval_minutes": 5, "graph_type": "time", "smoothing": true, "show_address": false, "filter": true, "sensors": [{"tracker_id": 1685505, "sensor_id": 613753}]}}'
    ```   