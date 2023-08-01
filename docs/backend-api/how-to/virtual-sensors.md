---
title: Virtual sensors usage
description: How to use virtual sensors and get information from them
---

# Virtual sensors usage

In the world of IoT and telematics, understanding and interpreting data is crucial. This is where virtual sensors come 
into play. These powerful tools help users comprehend data from various device sensors in a more meaningful way, often 
translating it into text form for easier understanding. In this article, we'll delve into what virtual sensors are, how 
they work, and how to configure them.

***

## What are virtual sensors

Virtual sensors interpret and translate raw data from the physical sensors of a device, making it comprehensible and actionable. For example, they can get data from state fields or even from a certain bit in a particular field.

One of the standout features of virtual sensors is their ability to monitor ignition, even on devices where no ignition input is provided or that input is already occupied by other needs. This allows users to read ignition from any desired source, be it motion, RPM, or voltage.

The information from virtual sensors can be viewed in several ways:

* Current readings in widgets. 
* Historical readings in reports. 
* Alerts when certain values are received in rules.

The virtual sensor object consists of the following parameters:

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

* `type` - string. This should be set as `virtual` for virtual sensors.
* `id` - int. This is the sensor's ID.
* `sensor_type` - enum. Must be "virtual_ignition" for virtual ignition sensor or "state" for others.
* `name` - string. Your name of a sensor. May contain up to 100 characters.
* `input_name` - string. A source input field (identifier). It indicates from which sensor the information is received by the platform.
* `parameters` - an object with additional parameters.
* `calc_method` - enum. This defines the method of sensor value calculation. It must be one of the following: `in_range`, `identity`, `bit_index`.
* `range_from` -  double. Lower boundary of the range and is only used with the "in_range" calculation method.
* `range_to` - double. Upper boundary of the range and is only used with the "in_range" calculation method.
* `bit_index` - int, [1..N]. A bit index in the input field source value and is only used with the "bit_index" calculation method.
* `value_titles` - a mapping for assigning special titles for sensor values, if required.
* `value` - string. Sensor value - raw value that comes from a device. Max size 64 chars.
* `title` - string. Your title for the sensor value. Max size 64 chars.


!!! note "There can only be one virtual sensor of type `virtual_ignition` for each tracker. 
For the "in_range" calculation method, one or both fields "range_from" and "range_to" must be specified.
The "bit_index" field is mandatory for the "bit_index" calculation method. 
All values within "value_titles" must be unique."

1## Where virtual sensors types are useful

***

### Value in range

A 'Value in Range' sensor is an effective tool for maintaining essential parameters, such as virtual ignition, 
temperature, humidity, and fuel level, within a specified range. It functions on a simple principle:

* if a sensor value falls within defined boundaries, it equates to 1 (your A value).
* if it's outside these boundaries, it corresponds to 0 (your B value).

#### To get virtual ignition

If your device is without an ignition input or all physical inputs are used on it, a virtual ignition can be utilized to
detect the ignition state. This process works by detecting a significant increase in the car's onboard voltage when the 
engine is turned on. This change in voltage can then be used as a signal to determine whether the engine is running or 
not. Typically, if the board voltage exceeds 13.2 V, it's a clear indication that the engine is operational.

***

#### To get sensor values into understandable format

This example parallels the one we just discussed about setting up a virtual ignition, but in this case, instead of 
monitoring a vehicle's ignition, we're keeping tabs on temperature.

Let's say you have an analog sensor that gathers temperature data. For instance, it might output 1020 for -10°C, 
and 1900 for 0°C. It's important to note that the information from these analog sensors comes uncalibrated, which 
means you'll need to specify it in this raw form when setting up your virtual sensor.

So, by following this method, you can translate complex sensor values into a simplified, more understandable format.

***

### Source value

With virtual sensors, you have the flexibility to assign your own definitions to any values received. This feature is 
particularly handy when dealing with predefined sets of values or strings, allowing you to work with static 
values without the need to specify different ranges. Plus, it's adaptable to any data you require.

For instance:

* 0/1
* true/false
* on/off
* open/close
* armed/disarmed
* state 1/state 2/state 3
* key 1/key 2/key 3, etc.

The mode operates in the following way:

* When value 1 is received, that's designated as your value A.
* When value 2 arrives, that becomes your value B.
* When value 3 is transmitted, that's identified as your value C, and so forth.

The best way to get historical readings on this calculation method sensors is to use it with state field value alert 
with report on all events.

Let's clarify this functionality with a practical example.

#### When you need to define every sensor value to understand the readings

Certain sensors might supply different numerical values to a platform. For example, let's say we have a truck equipped 
with a PTO drive engagement sensor that only outputs the following values:

* 0 - No PTO drive is engaged
* 1 - At least one PTO drive is engaged
* 2 - Error
* 3 - Not available

With virtual sensor you can get useful information instead of codes like 0, 1 or others.

***

#### Hardware key readings for drivers, equipment and trailers

Certain devices have the ability to recognize drivers and their iButtons, RFID keys, or equipment linked via Bluetooth 
sensors. The platform can identify the closest equipment or driver to the device, and a Virtual Sensor can display these 
names.

The simplest method of identification is through the use of tags. Each unit that's connected to heavy equipment has its 
own sensor with an attached tag. This tag serves as a hardware key that's recognizable by the platform. When the unit is 
connected to the machine, this key is transmitted to the platform.

Just like the way we named values for PTO, the associated name of this key can be displayed in an easily understandable 
format. This ensures that you always know which unit is communicating with your machine.

***

#### Event code readings

Navixy platform has the capability to provide you with the most recent event code received from your device. In this 
scenario, you can select the event code input and define the appropriate event codes to be displayed in widgets. For 
instance, if you're using a Jimi JC400, you can access Driver Monitoring System (DMS) events.

***

### Bit index

Certain devices might transmit complex data in their packets, sometimes consolidating several parameters into a single 
value. The Virtual Sensors feature gives you the ability to interact with segments of telematics values, helping you 
decode the data sent by the GPS hardware.

For instance, let's say a value of 011 is transmitted. We must first interpret this information in little endian 
(from he right to the left) according to the protocol:

* 1 - Indicates the status of the driver's seat belt: 0 signifies it's fastened, 1 means it's unfastened. (Bit 1)
* 1 - Displays the status of the driver's door: 0 means it's closed, 1 indicates it's open. (Bit 2)
* 0 - Represents the condition of the hood: 0 means it's closed, 1 indicates it's open. (Bit 3)

Each position in the parameter reflects the status of different vehicle systems. To configure and display these, you'll 
need to create a separate sensor for each parameter.

***

## Create

You can create such sensor with [tracker/sensor/create](../resources/tracking/tracker/sensor/index.md#create) request. 
For example, we need to track the virtual ignition on a device by the board voltage. In this case, we should use call:

=== "cURL"

    ```shell
    curl -X POST 'https://api.navixy.com/v2/tracker/sensor/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor": {"type": "virtual", "sensor_type": "virtual_ignition", "name": "Virtual Ignition", "input_name": "board_voltage", "parameters": {"calc_method": "in_range", "range_from": 13.4, "value_titles": [{"value": "0", "title": "Off"}, {"value": "1", "title": "On"}]}}}'
    ```

!!! note "Don’t use sensor_id parameter in the sensor object since there is no sensor with any ID before it is created."

The platform will notify you about the result with the assigned ID to this newly created sensor.

***

## Reconfigure

In case you want to change something in the virtual sensor settings, you can 
use [tracker/sensor/update](../resources/tracking/tracker/sensor/index.md#update) API call. For instance, 
we should change the range from which the virtual ignition must be calculated.

=== "cURL"

    ```shell
    curl -X POST 'https://api.navixy.com/v2/tracker/sensor/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor": {"type": "virtual", "sensor_id": 965837, "sensor_type": "virtual_ignition", "name": "Virtual Ignition", "input_name": "board_voltage", "parameters": {"calc_method": "in_range", "range_from": 13.7, "value_titles": [{"value": "0", "title": "Off"}, {"value": "1", "title": "On"}]}}}'
    ```

***

## Get values per period

When you want to show sensor readings or probably generate your own report it will be useful to get information in form 
value - time. 
In this case, the API call [tracker/sensor/data/read](../resources/tracking/tracker/sensor/index.md#dataread) will help.

=== "cURL"

    ```shell
    curl -X POST 'https://api.navixy.com/v2/tracker/sensor/data/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor_id": 965837, "from": "2023-07-24 00:00:00", "to": "2023-07-24 23:59:00", "raw_data": false}'
    ```

!!! note "Use raw_data: true in case, you need to get the raw sensor values per period."

***

## Get the current values

It is possible to read all current values from all virtual and measurement sensors and counters from multiple devices at once
with [tracker/readings/batch_list](../resources/tracking/tracker/readings.md#batchlist) API call. It will provide you with
all current information per one call so your app may request a lot of other requests without getting the limit 50 calls per second.

=== "cURL"

    ```shell
        curl -X POST '{{ extra.api_example_url }}/tracker/readings/batch_list' \
            -H 'Content-Type: application/json' \
            -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": [10181215,10038816]}'
    ```

***

## Get readings with reports

It is possible to get information about sensor readings within reports. Let's describe every report type and provide some
examples.

### Equipment working time report

The equipment working time report reveals the operational times of any unit linked to discrete or virtual inputs with a 
calculation method value in the range or bit index. It allows you to learn about the operating time of the equipment 
both while moving and stationary, obtain daily activity data, and pinpoint when and where the equipment was activated.

Report may be generated with [plugin 12](../resources/commons/plugin/report_plugins.md#equipment-working-time). Use the next example for reference:

=== "cURL"

    ```shell
        curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
            -H 'Content-Type: application/json' \
            -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Equipment working time", "trackers": [642546], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {{"hide_empty_tabs":true,"plugin_id":12,"show_seconds":false,"min_working_period_duration":60,"show_idle_percent":true,"filter":false,"sensors":[{"tracker_id":642546,"sensor_id":1931610}]}}'
    ```

***

### Engine hours report

The engine hours report provides the working duration for ignition-based sensors. It offers valuable insights into the 
operation time of your ignition-based equipment, whether it's on the move or idle. The report also delivers daily 
activity data, enabling you to identify precisely when and where the ignition was on.

Generate report using [plugin 7](../resources/commons/plugin/report_plugins.md#engine-hours-report). The next example shows correct API request for that:

=== "cURL"

    ```shell
        curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
            -H 'Content-Type: application/json' \
            -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Engine hours report", "trackers": [642546], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs":true,"plugin_id":7,"show_seconds":false,"show_detailed":true,"include_summary_sheet":true,"include_summary_sheet_only":false,"filter":true}}'
    ```

***

### Measuring sensors report

The measuring sensors report displays data from any configured measurement sensors or virtual sensors with a calculation 
method source value for a selected period. It enables you to view both graphical and statistical information from your 
device's sensors.

This report can be generated with [plugin 9](../resources/commons/plugin/report_plugins.md#measuring-sensors-report). For instance:

=== "cURL"

    ```shell
        curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
            -H 'Content-Type: application/json' \
            -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Measuring sensors report", "trackers": [1685505], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs":true,"plugin_id":9,"details_interval_minutes":5,"graph_type":"time","smoothing":true,"show_address":false,"filter":true,"sensors":[{"tracker_id":1685505,"sensor_id":613753}]}}'
    ```

***

### Vehicle readings report

The vehicle readings report showcases data gathered from your vehicle's instruments via the CAN/OBD or virtual sensors 
for any chosen time frame. This includes information such as mileage, engine RPMs, speed, fuel consumption, coolant 
temperature, and more.

Report is available with [plugin 22](../resources/commons/plugin/report_plugins.md#vehicle-sensors-report):

=== "cURL"

    ```shell
        curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
            -H 'Content-Type: application/json' \
            -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Vehicle readings report", "trackers": [642546], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs":true,"plugin_id":22,"details_interval_minutes":30,"graph_type":"time","smoothing":false,"sensors":[{"tracker_id":642546,"sensor_id":1866139}]}}'
    ```

***

### Report on all events

Reports on all events is handy for obtaining information about specific states received by the sensor with the aid of 
rules.

Generate this report type with [plugin 11](../resources/commons/plugin/report_plugins.md#report-on-all-events).

=== "cURL"

    ```shell
        curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
            -H 'Content-Type: application/json' \
            -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Event report", "trackers": [642546], "from": "2023-07-27 00:00:00", "to": "2023-07-27 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs":true,"plugin_id":11,"show_seconds":false,"group_by_type":false,"event_types":["state_field_control","sensor_inrange","sensor_outrange"]}}'
    ```

For obtaining information from reports, follow to our [instructions](./how-to-obtain-information-from-report.md).

***

## Rules for virtual sensors

Since we have the possibility to generate events report, let's describe rules. There are a couple of rules you can 
implement to receive alerts based on virtual sensor values:

### Parameter in range

Parameter in range rule is associated with the use of measurement sensors. Its function is to generate a notification 
whenever the sensor data received by the platform falls within or outside a specified range.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {{"name": "Parameter in range","description": "Rule for getting alert on specific range","alerts": {"sms_phones": [],"emails": [],"phones": [],"push_enabled": true },"extended_params": {"sensor_id": 1991090,"threshold": 0,"min": 2,"max": 3 },"primary_text": "Sensor value out range","secondary_text": "Sensor value in range","suspended": false,"trackers": [642546],"type": "sensor_range","param": null,"zone_ids": [],"schedule": [{"type": "weekly","from": {"weekday": 1,"time": "00:00:00"},"to": {"weekday": 7,"time": "23:59:59"}}]}}'
    ```

***

### State field value 

State field value is used to monitor any virtual sensor states that you define in the state column when configuring the 
virtual sensor. As soon as that state is received, you'll be notified.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"name": "State field value","description": "Rule for getting specific states","alerts": {"sms_phones": [],"emails": [],"phones": [],"push_enabled": true },"extended_params": {"state_field_index": null,"state_field_max_index": null,"virtual_sensor_id": 2136502,"trigger_value": "1","allow_repeat": false,"repeat_delay_seconds": null,"state_field_index_max": null },"primary_text": "Eye sensor: movement detected","secondary_text": "","suspended": false,"trackers": [642546],"type": "state_field_control","param": null,"zone_ids": [],"schedule": [{"type": "weekly","from": {"weekday": 1,"time": "00:00:00"},"to": {"weekday": 7,"time": "23:59:59"}}]}}'
    ```

To obtain notifications on these rules refer to [the instruction](./how-to-work-with-notifications.md).

