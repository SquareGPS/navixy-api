---
description: >-
  A guide on how to add data attributes created within Initiate Attribute nodes
  to navixy UI using API.
---

# Adding calculated attributes to Navixy UI

This scenario demonstrates how to create IoT Logic flows with calculated attributes and then make these custom attributes visible and usable in the Navixy platform UI. This approach allows developers to configure everything programmatically while providing end users with meaningful data visualization without any UI knowledge.

## Overview

This scenario combines two powerful Navixy capabilities:

1. **IoT Logic flow creation**: Building flows that process raw device data and create calculated attributes
2. **Sensor configuration via API**: Making calculated attributes visible in the Navixy UI by creating corresponding sensors

The key advantage is that developers can set up the entire data processing pipeline programmatically, while end users get immediate access to meaningful, processed data through the familiar Navixy interface.

## Prerequisites

Before proceeding with this scenario, ensure you have:

* **Devices configured and sending data**: Your IoT devices must be connected to the Navixy platform and actively transmitting data
* **Basic understanding of IoT Logic concepts**: Familiarity with flows, nodes, and the JEXL expression language
* **API access**: Valid session token for both IoT Logic API and main Navixy API
* **Device IDs**: Knowledge of the specific device IDs you want to use in your flow

### Step 1: Authentication

Before making API calls, you need to authenticate and obtain an API key. For detailed authentication instructions, see the [Authentication guide](../authentication.md).

Once authenticated, you'll have an API key for use in subsequent requests.

### Step 2: Create IoT Logic flow with calculated attributes

Create a flow that processes device data and calculates new attributes. This example demonstrates temperature and speed calculations:

{% code overflow="wrap" %}
```bash
curl -X POST "https://api.eu.navixy.com/v2/iot/logic/flow/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: NVX your_api_key" \
  -d '{
    "flow": {
      "title": "Vehicle Monitoring with Calculated Attributes",
      "enabled": true,
      "nodes": [
        {
          "id": 1,
          "type": "data_source",
          "enabled": true,
          "data": {
            "title": "Vehicle Fleet",
            "source_ids": [394892, 394893, 394894]
          },
          "view": {
            "position": {
              "x": 50,
              "y": 100
            }
          }
        },
        {
          "id": 2,
          "type": "initiate_attributes",
          "data": {
            "title": "Temperature and Speed Processing",
            "items": [
              {
                "name": "engine_temp_fahrenheit",
                "value": "value(\"engine_temp\")*1.8 + 32",
                "generation_time": "genTime(\"engine_temp\", 0, \"valid\")",
                "server_time": "now()"
              },
              {
                "name": "average_speed_kmh",
                "value": "(value(\"speed\", 0) + value(\"speed\", 1) + value(\"speed\", 2))/3",
                "generation_time": "genTime(\"speed\", 0, \"valid\")",
                "server_time": "now()"
              }
            ]
          },
          "view": {
            "position": {
              "x": 300,
              "y": 100
            }
          }
        },
        {
          "id": 3,
          "type": "output_endpoint",
          "enabled": true,
          "data": {
            "title": "Navixy Platform",
            "output_endpoint_type": "output_default"
          },
          "view": {
            "position": {
              "x": 550,
              "y": 100
            }
          }
        }
      ],
      "edges": [
        {
          "from": 1,
          "to": 2
        },
        {
          "from": 2,
          "to": 3
        }
      ]
    }
  }'
```
{% endcode %}

Response example:

```json
{
  "success": true,
  "id": 125
}
```

### Step 3: Create measurement sensors in Navixy UI

Now create sensors that correspond to your calculated attributes. These sensors will make the calculated data visible in the Navixy platform UI.

{% hint style="info" %}
**Important naming note**

In the API, these are called "**Metering sensors**", but in the Navixy UI, they appear as "**Measurement/IoT Logic sensors**". This is the same functionality with different terminology.
{% endhint %}

For complete details on sensor configuration options and all available API calls, see the [Sensor API resource documentation](https://app.gitbook.com/s/6dtcPLayxXVB2qaaiuIL/user-api/backend-api/resources/tracking/tracker/sensor/index).

#### Create engine temperature sensor

```bash
curl -X POST "https://api.eu.navixy.com/v2/tracker/sensor/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: NVX your_api_key" \
  -d '{
    "tracker_id": 394892,
    "sensor": {
      "type": "metering",
      "sensor_type": "temperature",
      "name": "Engine Temperature (°F)",
      "input_name": "engine_temp_fahrenheit",
      "divider": 1.0,
      "accuracy": 0.1,
      "units": "°F",
      "units_type": "fahrenheit"
    }
  }'
```

#### Create average speed sensor

```bash
curl -X POST "https://api.eu.navixy.com/v2/tracker/sensor/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: NVX your_api_key" \
  -d '{
    "tracker_id": 394892,
    "sensor": {
      "type": "metering",
      "sensor_type": "speed",
      "name": "Average Speed (km/h)",
      "input_name": "average_speed_kmh",
      "divider": 1.0,
      "accuracy": 0.1,
      "units": "km/h",
      "units_type": "speed"
    }
  }'
```

### Step 4: Repeat for all devices

You can createe one sensor at a time. Repeat the sensor creation process for each device in your flow:

```bash
# For device 394893
curl -X POST "https://api.eu.navixy.com/v2/tracker/sensor/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: NVX your_api_key" \
  -d '{
    "tracker_id": 394893,
    "sensor": {
      "type": "metering",
      "sensor_type": "temperature",
      "name": "Engine Temperature (°F)",
      "input_name": "engine_temp_fahrenheit",
      "divider": 1.0,
      "accuracy": 0.1,
      "units": "°F",
      "units_type": "fahrenheit"
    }
  }'

# And similarly for device 394894...
```

### Step 5: Verification and monitoring

#### Verify flow status

Check that your flow is running correctly:

```bash
curl -X POST "https://api.eu.navixy.com/v2/iot/logic/flow/read" \
  -H "Content-Type: application/json" \
  -H "Authorization: NVX your_api_key" \
  -d '{
    "flow_id": 125
  }'
```

#### Check sensor configuration

Verify that sensors were created correctly:

{% code overflow="wrap" %}
```bash
curl -X POST 'https://api.eu.navixy.com/v2/tracker/sensor/list' \
    -H 'Content-Type: application/json' \
    -H "Authorization: NVX your_api_key" \
    -d '{"tracker_id": 123456}'
```
{% endcode %}

{% hint style="success" %}
**Congratulations!**

You have successfully created an IoT Logic flow with calculated attributes and made them visible in the Navixy UI. This setup demonstrates how developers can build sophisticated data processing pipelines entirely through APIs while providing end users with meaningful, processed data visualization.

Your flow now:

* Processes raw device data in real-time using custom calculations
* Creates new attributes (temperature in Fahrenheit, average speed) that are more useful for business operations
* Makes calculated data available in Navixy UI widgets, reports, and dashboards without any manual UI configuration

This approach scales efficiently for large deployments where multiple devices need consistent data processing and visualization configurations. See [Steps explained](adding-calculated-attributes-to-navixy-ui.md#steps-explained) fordetailed breakdown.
{% endhint %}

### Steps explained

This scenario creates a complete data processing pipeline that transforms raw device data into meaningful UI elements:

#### IoT Logic flow processing

1. **Data Source node**: Collects raw telemetry data from your specified devices (engine temperature in Celsius, speed readings)
2. **Initiate Attributes node**: Applies JEXL expressions to transform raw data:
   * `engine_temp_fahrenheit`: Converts Celsius temperature to Fahrenheit using the formula `(°C × 1.8) + 32`
   * `average_speed_kmh`: Calculates a 3-point rolling average from recent speed readings to smooth out variations
3. **Output Endpoint node**: Sends all data (original + calculated attributes) to the Navixy platform in real-time

#### Sensor integration

4. **Metering sensor creation**: Creates sensors in Navixy that map to the calculated attributes by matching `input_name` with attribute names
5. **UI availability**: The sensors automatically appear in various Navixy interface components where users can view and analyze the processed data

#### End result

* **Raw data** (engine\_temp: 80°C, speed variations) becomes **meaningful information** (Engine Temperature: 176°F, Average Speed: 65 km/h)
* **Developers** configure everything programmatically without touching the UI
* **End users** get processed, business-relevant data in familiar Navixy widgets and reports
* **Real-time processing** ensures data is always current as devices send updates

## UI Visualization

Once configured, users will see the calculated attributes in several Navixy UI locations:

* **Obgect Widget**: Real-time display of current calculated values
* **Reports Section**: Historical data analysis using calculated attributes
* **Measurement Sensors Reports**: Dedicated reports for sensor data over time

For detailed information about how these calculated attributes appear in the Navixy UI, refer to the [Displaying new calculated attributes on the Navixy platform guide](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/initiate-attribute-node/displaying-new-calculated-attributes-on-the-navixy-platform).

## Troubleshooting

#### Common Issues

1. **Calculated attributes not appearing**: Ensure the `input_name` in sensor configuration exactly matches the calculated attribute name from your flow
2. **Sensor data not updating**: Verify that your flow is enabled and devices are actively sending the required source data
3. **Incorrect calculations**: Check JEXL expressions for syntax errors and verify source attribute names

#### Verification Steps

1. Confirm flow is processing data using the [IoT Logic monitoring tools](../Websocket-access-for-DSA.md)
2. Check [sensor readings via API](https://app.gitbook.com/s/6dtcPLayxXVB2qaaiuIL/user-api/backend-api/resources/tracking/tracker/sensor/index#data-read) to ensure data is flowing correctly
3. Verify UI display shows expected calculated values
