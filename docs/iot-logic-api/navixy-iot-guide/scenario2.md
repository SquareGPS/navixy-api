# Managing your flows and endpoints

After you create one or multiple flows, you can proceed with managing thm. This guide demonstrates how to view, read details, and update existing IoT Logic flows using the Navixy IoT Logic API. You'll learn how to list all your flows, examine specific flow configurations including nodes and connections, and modify flows by adding new data processing rules. The examples show practical scenarios like managing fleet vehicle data flows, adding calculated attributes for business metrics, and connecting to MQTT endpoints for external system integration.

## Prerequisites

For this example, let's presume that we have already:

1. Created an MQTT output endpoint with ID 45678 using `/iot/logic/flow/endpoint/create`
2. Created a flow with ID 1234 using `/iot/logic/flow/create` with the following components:
   * A data source node (ID: 1) that captures data from devices 12345, 12346, and 12347
   * An attribute calculation node (ID: 2) for basic metrics
   * An output endpoint node (ID: 3) that sends data to the MQTT endpoint

## Viewing your flows

The flow list endpoint provides a quick overview of all IoT Logic flows in your account. This is useful for getting flow IDs and titles before performing detailed operations. Each flow in the response includes its unique identifier and descriptive title, allowing you to identify which flows you want to examine or modify further.

{% openapi-operation spec="iot-logic" path="/iot/logic/flow/list" method="get" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-operation %}

To see all your existing flows, send the request:

```bash
curl -X GET "https://api.eu.navixy.com/v2/iot/logic/flow/list" \
  -H "Authorization: NVX your_session_token_here" \
  -H "Content-Type: application/json"
```

You will receive `id` and `title` parameters in the response:

```json
{
  "success": true,
  "list": [
    {
      "id": 1234,
      "title": "Fleet Data to External System"
    }
  ]
}
```

## Viewing flow details

The flow read endpoint retrieves complete configuration details for a specific flow, including all nodes, their properties, and the connections between them. This detailed view shows you the entire data processing pipeline - from data sources through transformation nodes to output endpoints. Use this when you need to understand the current flow structure before making modifications or troubleshooting data processing issues.

{% openapi-operation spec="iot-logic" path="/iot/logic/flow/read" method="get" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-operation %}

To see the details of a specific flow, copy the `id` value of the needed flow from [GET /iot/logic/flow/list](scenario2.md#viewing-your-flows) response. Add it in the respective field of this request:

```bash
curl -X POST "https://api.eu.navixy.com/v2/iot/logic/flow/read" \
  -H "Authorization: NVX your_session_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "flow_id": 1234
  }'
```

You will receive the complete structure of the flow in the response:

```json
{
  "success": true,
  "value": {
    "id": 1234,
    "title": "Fleet Data to External System",
    "description": null,
    "enabled": true,
    "default_flow": false,
    "nodes": [
      {
        "id": 1,
        "type": "data_source",
        "view": {
          "position": { "x": 50, "y": 50 }
        },
        "data": {
          "title": "Fleet Vehicles",
          "source_ids": [12345, 12346, 12347]
        }
      },
      {
        "id": 2,
        "type": "initiate_attributes",
        "view": {
          "position": { "x": 200, "y": 50 }
        },
        "data": {
          "title": "Calculate Business Metrics",
          "items": [
            {
              "name": "fuel_efficiency",
              "value": "value(\"distance_traveled\") / value(\"fuel_consumed\")",
              "generation_time": "genTime(\"distance_traveled\", 0, \"valid\")",
              "server_time": "now()"
            },
            {
              "name": "idle_time_percent",
              "value": "(value(\"idle_time\") / (value(\"idle_time\") + value(\"moving_time\"))) * 100",
              "generation_time": "genTime(\"idle_time\", 0, \"valid\")",
              "server_time": "now()"
            },
            {
              "name": "vehicle_status",
              "value": "value(\"speed\") gt 0 ? \"moving\" : \"stopped\"",
              "generation_time": "genTime(\"speed\", 0, \"valid\")",
              "server_time": "now()"
            }
          ]
        }
      },
      {
        "id": 3,
        "type": "output_endpoint",
        "view": {
          "position": { "x": 350, "y": 50 }
        },
        "data": {
          "title": "Send to External System",
          "output_endpoint_type": "output_mqtt_client",
          "output_endpoint_id": 45678
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
}
```

## Updating a flow

The flow update endpoint allows you to modify existing flows by changing node configurations, adding new processing rules, or adjusting connections. When updating a flow, you must provide the complete flow structure, including all nodes and edges, even if you're only modifying one element. This ensures data consistency and prevents accidental deletion of existing components. In this example, we're adding a new calculated attribute to convert engine temperature from Fahrenheit to Celsius while preserving all existing functionality.

{% openapi-operation spec="iot-logic" path="/iot/logic/flow/update" method="post" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-operation %}

Copy the flow obgect structure from [POST /iot/logic/flow/read](scenario2.md#viewing-flow-details) response and add the new attribute to the Initiate Atribute node (`id": 2`). Then paste the resulting object in the body of this request:

```bash
curl -X POST "https://api.eu.navixy.com/v2/iot/logic/flow/update" \
  -H "Authorization: NVX your_session_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "flow": {
      "id": 1234,
      "title": "Fleet Data to External System",
      "description": null,
      "enabled": true,
      "default_flow": false,
      "nodes": [
        {
          "id": 1,
          "type": "data_source",
          "view": {
            "position": { "x": 50, "y": 50 }
          },
          "data": {
            "title": "Fleet Vehicles",
            "source_ids": [12345, 12346, 12347]
          }
        },
        {
          "id": 2,
          "type": "initiate_attributes",
          "view": {
            "position": { "x": 200, "y": 50 }
          },
          "data": {
            "title": "Calculate Business Metrics",
            "items": [
              {
                "name": "fuel_efficiency",
                "value": "value(\"distance_traveled\") / value(\"fuel_consumed\")",
                "generation_time": "genTime(\"distance_traveled\", 0, \"valid\")",
                "server_time": "now()"
              },
              {
                "name": "idle_time_percent",
                "value": "(value(\"idle_time\") / (value(\"idle_time\") + value(\"moving_time\"))) * 100",
                "generation_time": "genTime(\"idle_time\", 0, \"valid\")",
                "server_time": "now()"
              },
              {
                "name": "engine_temp_celsius",
                "value": "(value(\"engine_temp_f\") - 32) * 5/9",
                "generation_time": "genTime(\"engine_temp_f\", 0, \"valid\")",
                "server_time": "now()"
              }
            ]
          }
        },
        {
          "id": 3,
          "type": "output_endpoint",
          "view": {
            "position": { "x": 350, "y": 50 }
          },
          "data": {
            "title": "Send to External System",
            "output_endpoint_type": "output_mqtt_client",
            "output_endpoint_id": 45678
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

You will receive this request status in response:

```json
{
  "success": true
}
```

{% hint style="success" %}
**Congratulations!**

You've now successfully enhanced your data flow by:

* Adding an engine temperature conversion calculation (Fahrenheit to Celsius)
* Maintaining your existing business metrics calculations
* Updating your flow while preserving the connection to your fleet vehicles and MQTT endpoint
{% endhint %}
