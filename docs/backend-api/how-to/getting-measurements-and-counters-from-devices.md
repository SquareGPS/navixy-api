---
title: Get sensors and counters data
description: This resource will describe - how to get information from tracker sensors and counters.
---

# How to get information from sensors and counters of tracker

Devices can be used not only to track GPS location. They can provide information about mileage, engine hours, measured
from sensors like fuel level and temperature. All API calls to interact with devices can be found in tracking/tracker branch.

<hr>

## Counters

Odometer allows to control a vehicle’s mileage in real-time. The mileage readings can be based on the data received from 
a GPS tracking device or CAN bus.

Engine hours is a tool that allows owners of vehicles and special machinery to monitor engine running time and schedule 
maintenance works based on this data.

### Counter creation

To get information from counters they should be created. To create a counter use the call [value/set](../resources/tracking/tracker/counter.md#valueset).

For example, we need to create odometer and engine hours counters. In this case we should use the next commands:

Odometer:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 311852, "type": "odometer", "value": 98342.1}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/counter/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=311852&type=odometer&value=98342.1
    ```

Engine hours:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 311852, "type": "engine_hours", "value": 2368.2}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/counter/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=311852&type=engine_hours&value=2368.2
    ```

The platform will notify you about success in reply.

<hr>

### Getting values from counter

Now we can get information from these counters when we need with the [get_counters](../resources/tracking/tracker/counter.md#get_counters) API call.
With it the last update time and values of all counters in one call will be received. 
If necessary to get information from only specific counter type and one device then [value/get](../resources/tracking/tracker/counter.md#valueget) 
call will be suitable.
The same information can be obtained for the list of devices . In this case use [value/list](../resources/tracking/tracker/counter.md#valuelist) call.

<hr>

### Counter values for a history period

Sometimes necessary to get data for the specific period. For example, it may be necessary for insurances or governments.
In this case should be used [data/list](../resources/tracking/tracker/counter.md#datalist) call. It will return JSON with
the next information:
???+ example "Response"

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

<hr>

## Sensors

The platform has two sub-types of sensors:

* [metering sensors](../resources/tracking/tracker/sensor/index.md#metering-sensor) - Discrete sensors responsible for 
  inputs states on the platform.
* [discrete sensors](../resources/tracking/tracker/sensor/index.md#metering-sensor) -  Measurement sensors will show 
  information from variable types of sensors.

The list of all supported sensors can be found [here](../resources/tracking/tracker/sensor/input_name.md#response)

### Sensor creation

The ability to connect sensors, as well as their number may vary depending on the device model. Some sensors automatically
creates by the platform. The list of these sensors depends on device model and information received from them. Some sensors
should be created manually.

Full sensor creation has several steps:

1. Data sending from the sensor should be configured on the device's side, and it should be received by the platform. How 
  to know - which one is received by the platform? The best way is connecting to [AirConsole](../../panel-api/resources/tracker.md#consoleconnect). 
2. We know - which sensor sends data and can choose one to [create](../resources/tracking/tracker/sensor/index.md#create)
3. If this is an analog sensor, or it is a sensor that sends data in uncalibrated values (for example, fuel sensor that
   sends percents instead of liters) - it should be [calibrated](../resources/tracking/tracker/sensor/calibration_data.md).
   
<hr>

### Getting values from sensors

All sensors can be found in different widgets. Discrete widgets in the inputs' widget. Measurement sensors can be found 
in the sensors readings, OBD & CAN and Fuel level widgets. For every widget we have its own API call to get data:

* To get input states use [get_inputs](../resources/tracking/tracker/index.md#get_inputs) request.
* To get data from CAN and OBD sensors  [get_diagnostics](../resources/tracking/tracker/index.md#get_diagnostics) API action.
* Data from the fuel sensors can be obtained using [get_fuel](../resources/tracking/tracker/index.md#get_fuel) call.
* Readings from metering not CAN, OBD and fuel sensors mey be received with [get_readings](../resources/tracking/tracker/index.md#get_readings) call.

<hr>

### Getting values from all sensors and states

Also, you are able to get the data from all sensors of the device and its states. Use [tracker/readings](../resources/tracking/tracker/readings.md)
request. It will reply with the next information:

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
            "field": "movement_state",
            "value": "parked",
            "update_time": "2021-06-01 15:23:03"
        },
        {
            "field": "actual_track",
            "value": 34112,
            "update_time": "2021-06-01 12:58:03"
        },
        {
            "field": "output_status",
            "value": 3,
            "update_time": "2021-06-01 15:23:03"
        },
        {
            "field": "tcp_status",
            "value": 2,
            "update_time": "2021-06-01 15:23:05"
        }
    ]
}
```

* input status and output status fields will show you binary information in decimal form. For example, output_status 
  field shows 3 - it is 11 in binary. The example device has two outputs. That's why 11 means output 1 = On and output 2 = ON.
