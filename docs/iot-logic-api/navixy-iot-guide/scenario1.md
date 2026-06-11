---
description: Create an IoT Logic flow with an embedded MQTT output node in a single API request. Includes the full request body, curl example, and response structure.
---

# Sending device data to an external system

Let's create a flow that sends your device data to an external system through MQTT. Rather than creating multiple endpoints separately, we can accomplish this in one single request.

{% hint style="info" %}
Need HTTP POST instead of MQTT? Use the [Webhook node](../technical-details/nodes.md#webhook-node-webhook).
{% endhint %}

## Creating a complete flow with integrated MQTT node

The simplest approach is to define both your data sources and MQTT output endpoint directly in your flow creation request. To do it, send a request to the following endpoint:

{% openapi-operation spec="iot-logic" path="/iot/logic/flow/create" method="post" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-operation %}

### Request example

```bash
curl -X POST "https://api.{region}.navixy.com/v2/iot/logic/flow/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: NVX your_token_here" \
  -d '{
  "flow": {
    "title": "Fleet data to external system",
    "enabled": true,
    "nodes": [
      {
        "id": 1,
        "type": "data_source",
        "enabled": true,
        "data": {
          "title": "Fleet vehicles",            // Title must be in the data object
          "sources": [12345, 12346, 12347]      // Your actual vehicle IDs
        },
        "view": {
          "position": { "x": 50, "y": 50 }
        }
      },
      {
        "id": 2,
        "type": "output_endpoint",
        "enabled": true,
        "data": {
          "title": "External MQTT System",       // Title must be located in the data object
          "output_endpoint_type": "output_mqtt_client",  // Defines this as an MQTT output
          "output_endpoint_id": 45678,           // Required ID (can be any unique number)
          "properties": {
            "protocol": "Navixy Generic Protocol (NGP)", // Navixy Generic Protocol
            "domain": "mqtt.mycompany.com",      // Your MQTT broker address
            "port": 1883,                        // Standard MQTT port
            "client_id": "navixy-integration",   // Identifier for this client
            "qos": 1,                            // Quality of Service level
            "topics": ["fleet/vehicles/data"],   // Topics to publish to
            "version": "5.0",                    // MQTT protocol version
            "use_ssl": true,                     // Secure connection
            "mqtt_auth": true,                   // Authentication required
            "user_name": "mqtt_username",        // Your MQTT credentials
            "user_password": "mqtt_password"
          }
        },
        "view": {
          "position": { "x": 250, "y": 50 }
        }
      }
    ],
    "edges": [
      {
        "from": 1,  // Connect the data source node (id: 1)
        "to": 2     // to the MQTT output node (id: 2)
      }
    ]
  }
}'
```

The response will include the flow ID:

```json
{
  "success": true,
  "id": 1234
}
```

{% hint style="success" %}
**Congratulations!**

You've now set up a flow that creates a complete end-to-end data pipeline in a single API call. This flow:

* Connects to multiple vehicles in your fleet through a data source endpoint
* Sends the device data to your external MQTT system
* Uses your custom MQTT broker settings for secure data transfer
{% endhint %}
