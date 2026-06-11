---
description: "Build IoT Logic flows with six node types: data source, attribute, logic, webhook, action, and output endpoint. Schema and property reference for each."
---

# Nodes

## Data Source node (`data_source`)

This node specifies which devices will send data to your flow. It's the entry point of all data flows.

{% openapi-schemas spec="iot-logic" schemas="NodeDataSource" grouped="true" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-schemas %}

#### Data source node structure

```json
{
  "id": 1,
  "type": "data_source",
  "data": {
    "title": "Your Title Here",
    "source_ids": [12345, 67890]
  },
  "view": {
    "position": { "x": 50, "y": 50 }
  }
}
```

#### Key properties

| Property          | Type    | Required | Description                              |
| ----------------- | ------- | -------- | ---------------------------------------- |
| `id`              | integer | Yes      | Unique identifier within the flow        |
| `type`            | string  | Yes      | Must be `"data_source"`                  |
| `data.title`      | string  | Yes      | Human-readable name for the node         |
| `data.source_ids` | array   | Yes      | Array of device IDs to collect data from |

### Usage notes

* The `data_source` node type is required in every flow
* Multiple devices can be specified in the `source_ids` array
* Each device is identified by its numeric ID in the Navixy system
* A flow can have multiple data source nodes for different device groups

## Initiate Attribute node (`initiate_attributes`)

This node transforms raw data into meaningful information. It allows for creating new attributes or modifying existing ones through expressions.

{% openapi-schemas spec="iot-logic" schemas="NodeInitiateAttributes" grouped="true" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-schemas %}

#### Initiate Attribute node structure

```json
{
  "id": 2,
  "type": "initiate_attributes",
  "data": {
    "title": "Your Title Here",
    "items": [
      {
        "name": "attribute_name",
        "value": "expression"
      }
    ]
  },
  "view": {
    "position": { "x": 150, "y": 50 }
  }
}
```

#### Key properties

| Property             | Type    | Required | Description                         |
| -------------------- | ------- | -------- | ----------------------------------- |
| `id`                 | integer | Yes      | Unique identifier within the flow   |
| `type`               | string  | Yes      | Must be `"initiate_attributes"data` |
| `data.title`         | string  | Yes      | Human-readable name for the node    |
| `data.items`         | array   | Yes      | Array of attribute definitions      |
| `data.items[].name`  | string  | Yes      | The attribute identifier            |
| `data.items[].value` | string  | Yes      | Mathematical or logical expression  |

### Expression language

For calculations IoT Logic API uses [Navixy IoT Logic Expression Language](../technologies/navixy-iot-logic-expression-language/).\
Here's a quick reference:

| Feature                | Operators/Examples                  | Description                    |
| ---------------------- | ----------------------------------- | ------------------------------ |
| Mathematical operators | `+`, `-`, `*`, `/`, `%`             | Basic arithmetic operations    |
| Functions              | `now()`, `sqrt()`, `pow()`, `abs()` | Built-in functions             |
| Attribute references   | `speed`, `fuel_level`, `analog_1`   | Reference to device attributes |

{% hint style="info" %}
To find more examples of formulas, see [Calculation examples](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/initiate-attribute-node/calculation-examples) in our User docs.
{% endhint %}

**Expression examples**

| Scenario               | Expression                                                | Description                       |
| ---------------------- | --------------------------------------------------------- | --------------------------------- |
| Temperature conversion | `(temperature_f - 32) * 5/9`                              | Convert Fahrenheit to Celsius     |
| Distance calculation   | `sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))`                 | Calculate distance between points |
| Time-based condition   | `hour(time) >= 22 \|\| hour(time) <= 6 ? 'night' : 'day'` | Determine day/night status        |

### Core functions

**`value(parameter, index, validation_flag)`**

* `parameter` (string): Device parameter or calculated attribute name
* `index` (integer, 0-12, optional): Historical depth (0 = newest). Default: 0
* `validation_flag` (string, optional): `"valid"` excludes nulls, "all" includes nulls. Default: `"all"`

#### Historical data access (`index` )

IoT Logic maintains up to 12 historical values per parameter:

* Index 0: Current value
* Index 1-11: Previous values
* Index 12: Oldest available value

{% hint style="info" %}
Short syntax is also supported for attribute names in formulas. When referencing only the latest value of an attribute, you can omit the full `value()` function syntax and quotation marks. For example, the temperature conversion formula can be written as `temperature*1.8 + 32` instead of `value('temperature', 0, 'all')*1.8 + 32`.
{% endhint %}

### Usage notes

* Multiple attributes can be defined within a single node
* Expressions execute in real-time as device data arrives
* Historical values are stored in memory for high-performance access
* Use validation flags strategically: "valid" for accurate calculations, "all" when null values are meaningful
* Calculated attributes become available in Data Stream Analyzer and can create custom sensors in Navixy Tracking module when connected to Default Output Endpoint

## IF/THEN Logic node (`logic`) <a href="#logic-node-logic" id="logic-node-logic"></a>

This node creates conditional branching points that route incoming data down different paths based on logical expressions. It evaluates conditions against real-time data and creates boolean attributes for monitoring and decision-making.

{% openapi-schemas spec="iot-logic" schemas="NodeLogic" grouped="true" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-schemas %}

#### Logic node structure

```json
{
  "id": 2,
  "type": "logic",
  "data": {
    "title": "Temperature Alert Check",
    "name": "high_temperature_alert",
    "condition": "value('temperature', 0, 'valid') > 75"
  },
  "view": {
    "position": { "x": 150, "y": 50 }
  }
}
```

#### Key properties

<table><thead><tr><th width="158.9090576171875">Property</th><th width="103.3636474609375">Type</th><th width="108.5455322265625">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>integer</td><td>Yes</td><td>Unique identifier within the flow</td></tr><tr><td><code>type</code></td><td>string</td><td>Yes</td><td>Must be "logic"</td></tr><tr><td><code>data.title</code></td><td>string</td><td>Yes</td><td>Human-readable name for the node</td></tr><tr><td><code>data.name</code></td><td>string</td><td>Yes</td><td>Name for the boolean attribute created by this node</td></tr><tr><td><code>data.condition</code></td><td>string</td><td>Yes</td><td>Logical expression using Navixy IoT Logic Expression Language</td></tr></tbody></table>

#### Output connections

The Logic node supports two output connection types:

**THEN connection (`then_edge`)**

* Activates when the expression evaluates to `true`
* At least one THEN connection is required

**ELSE connection (`else_edge`)**

* Activates when the expression evaluates to `false`, `null`, or encounters errors
* Optional connection

#### Common topology patterns

When you need to both trigger a side effect and forward data to Navixy on the same branch, connect the Logic node to both the terminal node and the Output Endpoint node using separate `then_edge` connections.

This applies to any terminal node type (e.g. Action, Webhook) since neither can have outgoing connections downstream. Both `then` edges fire in parallel when the condition is true. A single Output Endpoint node can receive connections from multiple upstream nodes, including from both `then` and `else` branches simultaneously.

{% tabs %}
{% tab title="Action + Output" %}
Use this pattern when you need to send a GPRS command to a device and still forward telemetry data to output on the same branch.

```
[Logic node]
├─ then_edge → [Action node] ← sends command to device
├─ then_edge → [Output Endpoint] ← forwards data
└─ else_edge → [Output Endpoint] ← forwards data
```
{% endtab %}

{% tab title="Webhook + Output" %}
Use this pattern when you need to send an HTTP POST to an external system and still forward telemetry data to output on the same branch.

```
[Logic node]
├─ then_edge → [Webhook node] ← sends HTTP POST to external system
├─ then_edge → [Output Endpoint] ← forwards data
└─ else_edge → [Output Endpoint] ← forwards data
```
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
Do not attempt to chain Action → Output Endpoint or Webhook → Output Endpoint. Both Action and Webhook nodes are terminal and cannot have outgoing connections, this will produce a validation error on the Data Source node: "Flow path or one of its branches doesn't terminate with an output endpoint".
{% endhint %}

### Expression language

For logical conditions IoT Logic API uses [Navixy IoT Logic Expression Language](../technologies/navixy-iot-logic-expression-language/).

Here's a quick reference:

| Operator category    | Operators                         | Description                       |
| -------------------- | --------------------------------- | --------------------------------- |
| Comparison operators | `==`, `!=`, `<`, `<=`, `>`, `>=`  | Basic comparison operations       |
| Logical operators    | `&&`, `\|\|`, `!`                 | Logical operations (and, or, not) |
| Pattern matching     | `=~`, `!~`                        | Pattern matching operations       |
| String operators     | `=^`, `!^`, `=$`, `!$`            | String comparison operations      |
| Attribute references | `speed`, `fuel_level`, `analog_1` | Reference to device attributes    |

#### Expression examples

| Expression                                                                   | Description                               |
| ---------------------------------------------------------------------------- | ----------------------------------------- |
| `value('temperature', 0, 'valid') > 75`                                      | Temperature monitoring                    |
| `value('speed', 0, 'valid') > 60 && value('current_hour', 0, 'valid') >= 18` | Complex conditions with logical operators |
| `value('lock_state', 0, 'valid') =~ ['locked', 'unlocked']`                  | Pattern matching with arrays              |

### Usage notes

* The Logic node creates a boolean attribute using the `data.name` value
* This attribute appears in Data Stream Analyzer and can be referenced by subsequent nodes
* When expressions cannot be evaluated, the result is treated as `false` and data flows through the ELSE path
* Multiple Logic nodes can be chained together for complex decision trees

## Webhook node (`webhook`)

This node sends HTTP POST requests with IoT data to external endpoints, enabling real-time integration with any third-party system or API that accepts HTTP requests.

{% openapi-schemas spec="iot-logic" schemas="NodeWebhook" grouped="true" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-schemas %}

**Webhook node structure:**

```json
{
  "id": 5,
  "type": "webhook",
  "data": {
    "title": "External API Integration",
    "url": "https://api.example.com/iot/data",
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      },
      {
        "key": "Authorization",
        "value": "Bearer token123"
      }
    ],
    "body": "{\"device_id\": $\"device_id\", \"temperature\": $\"temperature\", \"location\": {\"lat\": $\"latitude\", \"lng\": $\"longitude\"}, \"timestamp\": $\"message_time\"}"
  },
  "view": {
    "position": { "x": 550, "y": 100 }
  }
}
```

#### Key properties

| Property       | Type    | Required | Description                                                                |
| -------------- | ------- | -------- | -------------------------------------------------------------------------- |
| `id`           | integer | Yes      | Unique identifier within the flow                                          |
| `type`         | string  | Yes      | Must be "webhook"                                                          |
| `data.title`   | string  | Yes      | Human-readable name for the node (max 255 characters)                      |
| `data.url`     | string  | Yes      | Target endpoint URL with http:// or https:// protocol (max 255 characters) |
| `data.headers` | array   | No       | HTTP headers for POST requests (max 10 items)                              |
| `data.body`    | string  | No       | Request body template with attribute references (max 4000 characters)      |

### Body template syntax

The webhook body supports attribute references using `"attribute_name"` syntax:

**Syntax rules:**

* Reference attributes from upstream nodes: `"device_id"`, `"temperature"`
* Create nested JSON structures: `"location.latitude"`
* Null attributes output as JSON null: `"attribute": null`

{% tabs %}
{% tab title="Example body template" %}
```
{
  "device_id": "device_id",
  "temperature": "temperature",
  "location": {
    "lat": "latitude",
    "lng": "longitude"
  },
  "timestamp": "message_time"
}
```
{% endtab %}

{% tab title="Real-world example (ticket creation system)" %}
```
{
  "properties": {
    "subject": "Device maintenance \"device_id\"",
    "content": "Device communication failure. Diagnostic required.",
    "priority": "HIGH",
    "category": "Maintenance",
    "device_id": "\"device_id\""
  }
}
```
{% endtab %}
{% endtabs %}

### Headers configuration

Headers must be explicitly specified, including `Content-Type`. Common authentication patterns:

{% tabs %}
{% tab title="Bearer token authentication" %}
```
{
  "headers": [
    {
      "key": "Content-Type",
      "value": "application/json"
    },
    {
      "key": "Authorization",
      "value": "Bearer your_token_here"
    }
  ]
}
```
{% endtab %}

{% tab title="API key authentication" %}
```
{
  "headers": [
    {
      "key": "Content-Type",
      "value": "application/json"
    },
    {
      "key": "X-API-Key",
      "value": "your_api_key_here"
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Usage notes

#### Execution behavior

**Request processing:**

* Each incoming message triggers one HTTP POST request immediately
* Requests execute asynchronously without waiting for response
* Failed requests are not retried automatically

**Data availability:**

* Access to all attributes from connected upstream nodes
* Direct attribute references only (expressions not supported in body template)

#### Tips

* Webhook nodes function as **terminal nodes** - they do not pass data to downstream nodes
* Requests use **fire-and-forget** model without response validation or retry logic
* Use HTTPS protocol for production endpoints to ensure data security
* All headers including `Content-Type` must be explicitly specified
* Common configuration errors to avoid:
  * Missing `Content-Type` header when sending JSON
  * Incorrect authentication method (verify against receiving endpoint requirements)
  * Body format mismatch (validate template against target API specification)
  * URL protocol omission (always include `https://` or `http://`)
  * Attribute name mismatches (ensure referenced attributes exist in upstream nodes)
* The Webhook node enables integration with RESTful APIs, webhook platforms (Zapier, Make, n8n), ticketing systems, CRM platforms, and custom internal systems
* For more information on webhook configuration, see [Webhook node user guide](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/webhook-node)

## Device action node (`action`)

This node executes automated commands when triggered by incoming data. It transforms data flows into device control actions, enabling automated responses to conditions detected in earlier nodes.

{% openapi-schemas spec="iot-logic" schemas="NodeAction" grouped="true" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-schemas %}

#### Device action node structure

```json
{
  "id": 4,
  "type": "action",
  "data": {
    "title": "Engine Control on Overspeed",
    "actions": [
      {
        "type": "set_output",
        "number": 1,
        "value": false
      },
      {
        "type": "send_gprs_command",
        "command": "engineoff",
        "reliable": true
      }
    ]
  },
  "view": {
    "position": { "x": 600, "y": 300 }
  }
}
```

#### Key properties

| Property       | Type    | Required | Description                                |
| -------------- | ------- | -------- | ------------------------------------------ |
| `id`           | integer | Yes      | Unique identifier within the flow          |
| `type`         | string  | Yes      | Must be "action"                           |
| `data.title`   | string  | Yes      | Human-readable name for the node           |
| `data.actions` | array   | Yes      | Array of action definitions (max 10 items) |

### Action types

The Device action node supports two types of automated responses:

#### Set Output action

Controls device outputs by switching them on or off.

```json
{
  "number": 1,
  "value": true
}
```

**Properties:**

* `number` (integer, required): Output number (1-8) as shown in device UI
* `value` (boolean, required): The state to set (true = on, false = off)

#### Send Command action

Transmits custom GPRS commands directly to devices.

```json
{
  "command": "engine_block",
  "reliable": true
}
```

**Properties:**

* `command` (string, required): Custom command string (1-512 characters)
* `reliable` (boolean, optional, default: true): Whether to retry if device is offline

### Usage notes

* Device action nodes function as **terminal nodes** - they do not pass data to downstream nodes
* Actions execute **sequentially** in the order they appear in the `actions` array
* Commands are sent only to **devices that provided the triggering data**
* Each node can contain **up to 10 actions** of mixed types
* When connected to Logic nodes, actions execute only for devices where the condition evaluated to `true`
* Device compatibility varies - ensure your devices support the specific outputs or commands being configured

#### Action execution behavior

**Device targeting**

* Actions are sent only to devices that provided data in the current trigger event
* This ensures commands reach only the specific devices involved in the condition
* Prevents unnecessary commands to unaffected devices in the fleet

**Sequential processing**

* Multiple actions within a node execute in configured order (top to bottom)
* Each action completes transmission before the next action begins
* Total execution time is typically within seconds of receiving the trigger

**Device validation**

* Individual devices process received commands according to their capabilities
* Supported commands execute immediately upon receipt
* Unsupported commands are received but ignored by the device
* Device safety mechanisms may prevent inappropriate commands (e.g., engine shutdown while moving)

#### Connection patterns

**With Logic nodes (recommended)**

When connected to Logic nodes, actions execute only for devices where the logical condition evaluated to true, providing precise conditional automation.

**Direct connections**

When connected directly to other node types (Data Source, Initiate Attribute), actions execute for all devices in the data stream each time data is received.

### Device compatibility

Action execution depends on individual device capabilities:

* Ensure your devices support the specific outputs or commands you're configuring
* Consult manufacturer documentation for supported command lists
* Test actions in a controlled environment before deploying to production flows
* For device compatibility information, refer to [Navixy integrated devices](https://www.navixy.com/devices/)

## Output endpoint node (`output_endpoint`)

This node defines where your data will be sent. It's the termination point for data flow paths.

{% openapi-schemas spec="iot-logic" schemas="NodeOutputEndpoint" grouped="true" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-schemas %}

#### Output types

The output endpoint node supports different destination types:

**Default output for sending data to Navixy**

```json
{
  "id": 3,
  "type": "output_endpoint",
  "data": {
    "title": "Your Title Here",
    "output_endpoint_type": "output_default"
  },
  "view": {
    "position": { "x": 250, "y": 50 }
  }
}
```

**MQTT output for sending data to to external systems**

```json
{
  "id": 4,
  "type": "output_endpoint",
  "data": {
    "title": "Your Title Here",
    "output_endpoint_type": "output_mqtt_client",
    "output_endpoint_id": 45678
  },
  "view": {
    "position": { "x": 250, "y": 150 }
  }
}
```

#### Key properties

| Property                    | Type    | Required      | Description                                                               |
| --------------------------- | ------- | ------------- | ------------------------------------------------------------------------- |
| `id`                        | integer | Yes           | Unique identifier within the flow                                         |
| `type`                      | string  | Yes           | Must be `"output_endpoint"`                                               |
| `data.title`                | string  | Yes           | Human-readable name for the node                                          |
| `data.output_endpoint_type` | string  | Yes           | Type of output destination (`"output_default"` or `"output_mqtt_client"`) |
| `data.output_endpoint_id`   | integer | For MQTT only | Reference to a previously created endpoint                                |

### Output endpoint types

| Type                 | Description                       | Use Case                              |
| -------------------- | --------------------------------- | ------------------------------------- |
| `output_default`     | Default output to Navixy platform | Sending processed data back to Navixy |
| `output_mqtt_client` | External MQTT broker connection   | Integrating with third-party systems  |

<details>

<summary>MQTT endpoint properties</summary>

| Property        | Type             | Required                  | Description                 | Example                           |
| --------------- | ---------------- | ------------------------- | --------------------------- | --------------------------------- |
| `protocol`      | string           | Yes                       | Protocol of messages        | `"NGP"` (Navixy Generic Protocol) |
| `domain`        | string           | Yes                       | MQTT broker domain/IP       | `"mqtt.example.com"`              |
| `port`          | integer          | Yes                       | MQTT port                   | `1883`                            |
| `client_id`     | string           | Yes                       | Client identifier           | `"navixy-client-1"`               |
| `qos`           | integer          | Yes                       | Quality of Service (0 or 1) | `1`                               |
| `topics`        | array of strings | Yes                       | Topic names                 | `["iot/data"]`                    |
| `version`       | string           | Yes                       | MQTT version                | `"5.0"` or `"3.1.1"`              |
| `use_ssl`       | boolean          | Yes                       | Whether to use SSL          | `true`                            |
| `mqtt_auth`     | boolean          | Yes                       | Whether auth is required    | `true`                            |
| `user_name`     | string           | Only if `mqtt_auth: true` | MQTT username               | `"mqtt_user"`                     |
| `user_password` | string           | Only if `mqtt_auth: true` | MQTT password               | `"mqtt_password"`                 |

**MQTT QoS levels**

| Level     | Description                                      | Use Case                                                           |
| --------- | ------------------------------------------------ | ------------------------------------------------------------------ |
| **QoS 0** | "At most once" delivery (fire and forget)        | High-volume, non-critical data where occasional loss is acceptable |
| **QoS 1** | "At least once" delivery (acknowledged delivery) | Important messages that must be delivered, can handle duplicates   |
| **QoS 2** | Not currently supported by the API               | -                                                                  |

**MQTT protocol versions**

| Version        | Description                          | Features                                                          |
| -------------- | ------------------------------------ | ----------------------------------------------------------------- |
| **MQTT 3.1.1** | Widely supported version             | Basic pub/sub functionality, broad broker compatibility           |
| **MQTT 5.0**   | Newer version with enhanced features | Message expiry, topic aliases, shared subscriptions, reason codes |

</details>

### Usage notes

* Every flow must have at least one output endpoint node to be functional
* The `output_default` type doesn't require a referenced endpoint (built-in)
* The `output_mqtt_client` type requires an `output_endpoint_id` referencing a previously created endpoint
* Multiple output nodes can be used to send the same data to different destinations
* Output nodes are "terminal" - they don't connect to any downstream nodes
