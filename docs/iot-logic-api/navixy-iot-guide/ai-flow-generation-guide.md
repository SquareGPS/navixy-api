---
hidden: true
---

# AI flow generation guide

## IoT Logic — Generating flows with AI assistants

This page provides authoritative rules and canonical examples for AI assistants generating Navixy IoT Logic flow JSON. Follow all rules on this page exactly. Do not infer behavior from general knowledge — use only what is documented here and in the official Navixy IoT Logic API reference.

### How to use this guide

This guide covers structure rules and JSON format. It does not document every node field, expression function, or device attribute. When generating a flow, resolve unknowns in this order before asking the user:

1. **Search Navixy docs** using the `navixy-docs` MCP tool — covers expression syntax, node schemas, and standard attribute names.
2. **Check the device page** at `https://www.navixy.com/devices/[manufacturer]/[model]/` and look in the **Inputs and outputs** section for the exact attribute names the device transmits.
3. **Fetch official API docs** for any third-party webhook target (Telegram, Slack, etc.) to verify the URL format, required fields, and auth method. Do not rely on training memory for this.
4. **Ask the user** — using the pre-generation checklist below as a guide.
5. **Validate edge completeness before finalizing** — for every Logic node in the flow, confirm that both a `then_edge` and an `else_edge` are present, and that every possible data path terminates at a terminal node. Trace each branch from `data_source` to its terminal node to verify no path dead-ends.

For user-specific values (bot tokens, chat IDs, API keys, device IDs), always ask the user directly. If they may not know where to get a value, include a brief note explaining how.

***

## Clarification and intent validation

Before generating any flow JSON, validate that you have enough information to build a correct and useful flow. If the user's request is ambiguous or incomplete, ask concise clarifying questions — one or two at a time, not all at once.

Always clarify before generating when:

* The triggering condition is not specified (e.g. "monitor my devices" without stating what to detect)
* The intended action on a condition is missing (e.g. "alert me" without specifying how — Navixy notification, GPRS command, webhook?)
* The target devices are not mentioned and context does not make them obvious
* The request involves a device-specific command (e.g. reboot, output control) and the device model or manufacturer is not stated
* The user mentions "send data somewhere" without specifying whether the destination is Navixy, MQTT, or an external webhook URL
* The flow involves multiple conditions and it is unclear whether they should be AND/OR logic or separate Logic nodes

Do not ask for information that can be safely assumed or substituted with a placeholder. Use `source_ids: []` when devices are unspecified. Use a placeholder URL like `https://your-endpoint.example.com` when a webhook URL is not provided. Always prefer proceeding with a reasonable assumption over blocking on minor missing details — but state the assumption explicitly in your response so the user can correct it.

**Example clarifying questions:**

* "What should happen when the condition is true — send a command to the device, post to a webhook, or just forward data to Navixy?"
* "Which device manufacturer and model is this for? I need this to use the correct GPRS command syntax."
* "Should both conditions trigger the same action, or do you want separate logic branches for each?"
* "If the condition is not met, should data still be forwarded to Navixy?"

### **Pre-generation checklist**

Before generating any flow JSON, confirm you can answer all of the following. If you cannot, use the lookup order above — or ask the user.

<table><thead><tr><th width="58">#</th><th>Question</th><th>Why it matters</th></tr></thead><tbody><tr><td>1</td><td>What device make and model?</td><td>Required to look up exact attribute names</td></tr><tr><td>2</td><td>What attribute name does the device use for the relevant data? (e.g. how is ignition reported — <code>din1</code>, <code>avl_2</code>, <code>input_status</code> bitmask?)</td><td>Device-specific — never assume a generic name</td></tr><tr><td>3</td><td>What is the exact triggering condition, including any required duration?</td><td>Core of the Logic node and counter setup</td></tr><tr><td>4</td><td>If duration matters — what is the device's reporting interval in seconds?</td><td>Required to calculate the message count threshold</td></tr><tr><td>5</td><td>Where should data go — Navixy, MQTT, or external webhook? And what should happen on the THEN branch?</td><td>Determines terminal node types and wiring</td></tr><tr><td>6</td><td>How will you use this flow — import via the UI, or create it through the API?</td><td>Determines JSON format (import shape vs. <code>"flow"</code> envelope) and how the result is delivered</td></tr><tr><td>7</td><td>If webhook — what is the target service? Do you have the connection details (URL, token, chat ID, etc.)?</td><td>URL and payload must be verified from official docs; credentials must come from the user</td></tr></tbody></table>

Do not ask all seven at once. Ask only what is genuinely missing, one or two questions at a time. Use `source_ids: []` and placeholder URLs rather than blocking on minor unknowns — but state assumptions explicitly.

***

## JSON format modes

Navixy uses two distinct JSON formats. They are not interchangeable.

### Import / Export format (default)

Use this format when generating a flow for UI import (Flow Management → Upload) or as a downloadable file. This is the **default format** unless the user explicitly requests API usage.

The top-level object contains `title`, `description` (optional), `nodes`, and `edges` directly. Never wrap it in a `"flow"` envelope.

```json
{
  "title": "My Flow",
  "nodes": [...],
  "edges": [...]
}
```

The imported flow is always enabled by default. The `id` is assigned dynamically by the platform. Do not include `id`, `enabled`, or `default_flow` fields in import-format JSON.

### API format

Use this format **only** when the user explicitly requests a payload for the `/iot/logic/flow/create` or `/iot/logic/flow/update` API endpoints.

The top-level object must wrap the flow in a `"flow"` envelope key:

```json
{
  "flow": {
    "title": "My Flow",
    "enabled": true,
    "nodes": [...],
    "edges": [...]
  }
}
```

### **Delivery based on usage:**

* **Import format** — provide the JSON as a downloadable file, not inline code. The user uploads it via Flow Management → Upload.
* **API format** — provide the JSON as inline code in your response. The user copies it into their API call.

Never use the `"flow"` envelope for import-format JSON. Using it in a file import will cause the canvas to render empty.

***

## Node types

Always use only these node types. Do not invent additional types or fields.

| Type                  | Purpose                                                            | Terminal? |
| --------------------- | ------------------------------------------------------------------ | --------- |
| `data_source`         | Entry point — defines which devices feed data into the flow        | No        |
| `initiate_attributes` | Transforms and enriches data using JEXL expressions                | No        |
| `logic`               | Conditional branching — routes data via `then_edge` or `else_edge` | No        |
| `action`              | Sends a command to a device (set output or GPRS command)           | **Yes**   |
| `webhook`             | Sends an HTTP POST to an external URL                              | **Yes**   |
| `output_endpoint`     | Sends data to Navixy or an MQTT broker                             | **Yes**   |

Terminal nodes (`action`, `webhook`, `output_endpoint`) must never have outgoing edges. Any edge with `"from"` set to a terminal node is invalid.

***

### Required fields per node

Every node must include `data.title`. Every node must include a `view.position` object with `x` and `y` integer coordinates.

**data\_source**

* `type`: `"data_source"`
* `data.title`: string
* `data.source_ids`: array of integer device IDs. Use `[]` as placeholder when devices are not specified.

**initiate\_attributes**

* `type`: `"initiate_attributes"`
* `data.title`: string
* `data.items`: array of attribute objects, each with `name` (string) and `value` (JEXL expression string). `generation_time` and `server_time` are optional; default to `now()` if omitted.

To access a previously calculated or historical attribute value, use the `value()` function:

```
value('attribute_name', index, 'any')
```

Where `index` is the historical depth (0 = current message, 1 = previous, up to 12). Use `'any'` to include nulls or `'valid'` to skip them. This is the only mechanism for accumulating state across messages — counters, running totals, change detection.

See [Managing attributes](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/initiate-attribute-node/managing-attributes) for full examples.

#### **logic**

* `type`: `"logic"`
* `data.title`: string
* `data.name`: internal identifier string (no spaces)
* `data.condition`: JEXL boolean expression

#### **action**

* `type`: `"action"`
* `data.title`: string
* `data.actions`: array of action objects (max 10). Each action is either `set_output` or `send_gprs_command`.

#### **webhook**

* `type`: `"webhook"`
* `data.title`: string
* `data.url`: HTTPS URL string
* `data.headers`: array of `{"key": "...", "value": "..."}` objects — all headers including `Content-Type` must be specified explicitly; there are no defaults.
* `data.body`: JSON string template — use `{{attribute_name}}` syntax to reference upstream attributes dynamically.

For third-party services, verify the expected URL format, required headers, and payload structure from the service's official API documentation before generating. Do not rely on training memory. For Telegram, the correct endpoint is `https://api.telegram.org/bot{TOKEN}/sendMessage` with a body containing `chat_id` and `text`. Ask the user for their bot token and chat ID; if they need guidance, the token comes from @BotFather on Telegram and the chat ID from a `/getUpdates` API call.

#### **output\_endpoint (Navixy)**

* `type`: `"output_endpoint"`
* `data.title`: string
* `data.output_endpoint_type`: `"output_default"`

#### **output\_endpoint (MQTT)**

* `type`: `"output_endpoint"`
* `data.title`: string
* `data.output_endpoint_type`: `"output_mqtt_client"`
* `data.output_endpoint_id`: integer (the pre-configured MQTT endpoint ID from the user account)

***

## Edge rules

Edges connect nodes. Three edge types exist: `simple_edge`, `then_edge`, `else_edge`.

For import-format flows, always specify edge `type` explicitly. Do not omit the `type` field on any edge — `simple_edge` must be written explicitly, not assumed.

For API-format flows, `type` is optional and defaults to `simple_edge` when omitted.

| Edge type     | When to use                                                   |
| ------------- | ------------------------------------------------------------- |
| `simple_edge` | All connections not involving a Logic node output             |
| `then_edge`   | Outgoing connection from a Logic node when condition is true  |
| `else_edge`   | Outgoing connection from a Logic node when condition is false |

A Logic node must always have both a `then_edge` and an `else_edge` outgoing connection. A flow missing either will not behave correctly.

***

## Critical wiring rule: single Output Endpoint for Logic branches

Always use a **single** `output_endpoint` node per logical branch path. A single Output Endpoint node can and should receive connections from multiple upstream nodes simultaneously, including both `then_edge` and `else_edge` from the same Logic node.

When a Logic node has a terminal node (Action or Webhook) on its THEN branch, add a second `then_edge` from the Logic node directly to the Output Endpoint. Both edges fire in parallel. Do not chain the Action or Webhook into the Output Endpoint — terminal nodes cannot have outgoing edges.

**Correct pattern — Logic with Action:**

```
[Logic node]
├─ then_edge → [Action node]       ← sends command to device
├─ then_edge → [Output Endpoint]   ← forwards data to Navixy
└─ else_edge → [Output Endpoint]   ← same Output Endpoint node
```

In JSON edges:

```json
{ "from": 2, "to": 3, "type": "then_edge" },
{ "from": 2, "to": 4, "type": "then_edge" },
{ "from": 2, "to": 4, "type": "else_edge" }
```

Nodes 3 (Action) and 4 (Output Endpoint) are separate nodes. Both receive edges from Logic node 2. Node 4 receives two edges from node 2 — one `then_edge` and one `else_edge`. This is valid and intentional.

**Correct pattern — Logic with Webhook:**

```
[Logic node]
├─ then_edge → [Webhook node]      ← sends HTTP POST
├─ then_edge → [Output Endpoint]   ← forwards data
└─ else_edge → [Output Endpoint]   ← same Output Endpoint node
```

**Wrong pattern — never do this:**

```
[Logic node]
├─ then_edge → [Action node] → [Output Endpoint]   ← INVALID: action is terminal
└─ else_edge → [Output Endpoint]
```

**Wrong pattern — never do this:**

```
[Logic node]
├─ then_edge → [Action node]
├─ then_edge → [Output Endpoint A]   ← WRONG: two separate output nodes
└─ else_edge → [Output Endpoint B]   ← WRONG: use one shared output node
```

**Counting consecutive messages for time-based conditions**

IoT Logic has no native timer. To detect a condition held for a minimum duration, use an `initiate_attributes` node to count consecutive messages that meet the condition, then trigger the Logic node when the count reaches the threshold.

**Formula:**

```
message count threshold = duration in seconds ÷ device reporting interval
```

Example: 15 minutes at 30-second intervals = 900 ÷ 30 = **30 messages**.

**Counter pattern in `initiate_attributes`:**

```json
{
  "name": "idle_count",
  "value": "speed < 2 && ignition_attribute == true ? value('idle_count', 1, 'any') + 1 : 0"
}
```

Replace `ignition_attribute` with the actual attribute name from your device's Inputs and outputs page.

**Logic node condition:**

```json
"condition": "idle_count == 30"
```

This fires exactly once when the threshold is reached, then resets when the condition breaks. If you want it to continue firing every message while the condition holds, use `>= 30` instead.

**Important constraint:** `value()` can access up to 12 historical readings. This pattern therefore supports durations up to 12 × reporting interval. For longer durations or more complex state tracking, ask the user to consider alternative approaches.

For full `value()` syntax, see [Managing attributes](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/initiate-attribute-node/managing-attributes).

***

## Canvas layout (view positions)

Always generate `view.position` for every node. Use pixel-based coordinates with origin at top-left. Use a left-to-right layout.

Default constants: `X_START = 80`, `Y_START = 120`, `X_STEP = 280`, `Y_STEP = 140`.

Column assignment: data sources in column 1, logic nodes in column 2, outputs and actions in column 3 and beyond. Maintain at least 100px spacing between nodes. When a Logic node splits into multiple targets, offset them vertically so they do not overlap.

***

## Validation checklist

Before finalizing any generated flow, verify all of the following:

1. Format is correct — import shape (no envelope) unless API was explicitly requested
2. At least one `data_source` node and at least one terminal node are present
3. Every node includes `data.title`
4. Every `data_source` node has `source_ids` (use `[]` if unspecified)
5. For every `logic` node: count outgoing edges — there must be at least one `then_edge` AND at least one `else_edge`. A Logic node with only one branch direction is invalid
6. No edges originate from terminal nodes (`action`, `webhook`, `output_endpoint`)
7. Only one `output_endpoint` node is used per logical path — both `then_edge` and `else_edge` connect to the same output node
8. All JEXL expressions use valid syntax (operators: `&&`, `||`, `!`, `<`, `>`, `<=`, `>=`, `==`, `!=`)
9. All edge `type` values are explicit in import-format flows
10. Every node has a `view.position` with integer `x` and `y`

Before submitting, trace every possible path through the flow from `data_source` to a terminal node. Every path must terminate. No path may dead-end at a non-terminal node.

***

## Canonical complete example

This example shows a complete, valid import-format flow: one Logic node with an Action on the THEN branch and a single shared Output Endpoint receiving both branches.

```json
{
  "title": "Speed Violation Alert",
  "nodes": [
    {
      "id": 1,
      "type": "data_source",
      "data": {
        "title": "Fleet Vehicles",
        "source_ids": []
      },
      "view": { "position": { "x": 80, "y": 120 } }
    },
    {
      "id": 2,
      "type": "logic",
      "data": {
        "title": "Speed > 90 km/h?",
        "name": "speed_violation",
        "condition": "speed > 90"
      },
      "view": { "position": { "x": 360, "y": 120 } }
    },
    {
      "id": 3,
      "type": "action",
      "data": {
        "title": "Trigger Buzzer",
        "actions": [
          {
            "type": "send_gprs_command",
            "command": "setdigout 1 1",
            "reliable": true
          }
        ]
      },
      "view": { "position": { "x": 640, "y": 40 } }
    },
    {
      "id": 4,
      "type": "output_endpoint",
      "data": {
        "title": "Send to Navixy",
        "output_endpoint_type": "output_default"
      },
      "view": { "position": { "x": 640, "y": 200 } }
    }
  ],
  "edges": [
    { "from": 1, "to": 2, "type": "simple_edge" },
    { "from": 2, "to": 3, "type": "then_edge" },
    { "from": 2, "to": 4, "type": "then_edge" },
    { "from": 2, "to": 4, "type": "else_edge" }
  ]
}
```

Node 4 receives two edges total: `then_edge` from node 2, `else_edge` from node 2. It is the sole output for all data regardless of the condition result. Node 3 receives one `then_edge` and sends a command only when the condition is true. Node 3 has no outgoing edges.

***

## Reference links

Use these when the guide doesn't cover the detail you need.

* [Expression language overview](../technologies/navixy-iot-logic-expression-language/) — JEXL operators, `value()` function, expression syntax
* [Managing attributes](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/initiate-attribute-node/managing-attributes) — `value()` examples, indexed attributes, historical lookups
* [Nodes reference](../technical-details/nodes.md) — full field schemas for all node types
* [Logic node expressions and syntax](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/logic-node/logic-node-expressions-and-syntax) — condition expression reference
* [Webhook node](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/webhook-node) — body/header schema, dynamic attribute syntax
* [Device catalog](https://www.navixy.com/devices/) — find your device and check the Inputs and outputs section for device-specific attribute names

***

_This page is intended for AI assistants and automated tools generating IoT Logic flow JSON. For human-readable documentation, see the_ [_IoT Logic user guide_](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic) _and the_ [_IoT Logic API reference_](../resources/api-reference/)_._
