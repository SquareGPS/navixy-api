---
description: Create, manage, and execute custom device commands and HTTP POST webhooks for individual trackers.
icon: terminal
---

# Output control

Output control lets you define reusable commands for a tracker and execute them on demand. Two command types are supported:

* **Hardware** — sends a protocol-level command string directly to the device (e.g. to reboot firmware or toggle a relay).
* **Software** — sends an HTTP POST request with a JSON body to any URL, optionally embedding live device attributes in the payload.

Commands are stored per tracker and can be executed at any time from the [Output control widget](../../../../../user/guide/devices-and-settings/output-control-widget.md) in the platform UI.

{% hint style="info" %}
Output control is designed for manual, on-demand actions targeting a single tracker. For automated, rule-based command sending across multiple devices, use [IoT Logic](../../../../../iot-logic/) with the **Device action** or **Webhook** nodes.
{% endhint %}

## Object structure

Each output control entry has a common set of fields. The `config` object differs by `type`.

{% tabs %}
{% tab title="Hardware" %}
```json
{
  "id": 19,
  "name": "Reboot",
  "type": "hardware",
  "config": {
    "command": "cpureset",
    "reliable": true
  }
}
```

* `id` - int. Unique output control ID. Assigned by the server on creation. Read-only.
* `name` - string. Human-readable label shown in the Object widget (e.g. `"engine_stop"`).
* `type` - string. Always `"hardware"` for this variant.
* `config` - object. Hardware command configuration.
  * `command` - string. The exact protocol-level command string sent to the device (e.g. `"RELAY,1#"`). Valid values are device-specific — refer to your device manufacturer's documentation.
  * `reliable` - boolean. If `true`, the platform requests delivery confirmation (acknowledgement) from the device before marking the command as successfully sent.
{% endtab %}

{% tab title="Software" %}
```json
{
  "id": 20,
  "name": "Notify Slack",
  "type": "software",
  "config": {
    "url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXX",
    "headers": [
      {
        "key": "Authorization",
        "value": "Bearer <TOKEN>"
      },
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "body": "{\"text\": \"Device {{device_id}}: speed {{speed}} km/h at {{latitude}}, {{longitude}}\"}"
  }
}
```

* `id` - int. Unique output control ID. Assigned by the server on creation. Read-only.
* `name` - string. Human-readable label shown in the Object widget (e.g. `"webhook_action"`).
* `type` - string. Always `"software"` for this variant.
* `config` - object. Software command configuration.
  * `url` - string. The full endpoint URL that will receive the HTTP POST request.
  * `headers` - array of objects. HTTP request headers to include. Can be empty.
    * `key` - string. Header name (e.g. `"Authorization"`).
    * `value` - string. Header value (e.g. `"Bearer <TOKEN>"`).
  * `body` - string. The JSON payload sent in the POST request body. Use `{{attribute_name}}` placeholders to embed live device data — they are replaced with current values at execution time.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Hardware command strings are device-specific. Always refer to your device manufacturer's documentation for valid values. Sending an incorrect command string may have unintended effects on the device.
{% endhint %}

# API actions

API base path: `/tracker/output_control`.

{% hint style="info" %}
All API calls require authentication. Pass your **API key** or **user session hash** as the `hash` parameter in the request body, as a query string parameter, or in the `Authorization: NVX <value>` header. API keys are recommended for integrations — they don't expire and can be managed independently. See [Authentication](../../authentication.md) for details.
{% endhint %}

## create

Creates a new output control for a tracker.

**Required sub-user rights:** `tracker_update`.

### Parameters

| name | description | type | format |
| --- | --- | --- | --- |
| hash | API key or user session hash. | string | `"your_api_key"` |
| tracker_id | ID of the tracker to create the output control for. | int | `70074765` |
| output_control | Output control object without `id`. See [object structure](#object-structure). | object | See examples |

### Examples

{% tabs %}
{% tab title="cURL — hardware" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/output_control/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "output_control": {
            "name": "engine_stop",
            "type": "hardware",
            "config": {
                "command": "RELAY,1#",
                "reliable": true
            }
        }
    }'
```
{% endtab %}

{% tab title="cURL — software" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/output_control/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "output_control": {
            "name": "webhook_action",
            "type": "software",
            "config": {
                "url": "https://example.com/webhook",
                "headers": [
                    {
                        "key": "Authorization",
                        "value": "Bearer <TOKEN>"
                    },
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": "{\"tracker_id\": {{device_id}}, \"action\": \"execute_output_control\"}"
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Response

Returns the created output control object, including the server-assigned `id`.

```json
{
  "success": true,
  "value": {
    "id": 19,
    "name": "engine_stop",
    "type": "hardware",
    "config": {
      "command": "RELAY,1#",
      "reliable": true
    }
  }
}
```

* `success` - boolean. Always `true` for successful responses.
* `value` - object. The created output control. See [object structure](#object-structure).

### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if no tracker with the given `tracker_id` belongs to the current user.

[General error codes](../../errors.md)

---

## update

Updates an existing output control. The full object including `id` must be provided.

**Required sub-user rights:** `tracker_update`.

### Parameters

| name | description | type | format |
| --- | --- | --- | --- |
| hash | API key or user session hash. | string | `"your_api_key"` |
| tracker_id | ID of the tracker that owns the output control. | int | `70074765` |
| output_control | Updated output control object including `id`. See [object structure](#object-structure). | object | See example |

### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/output_control/update' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "output_control": {
            "id": 2,
            "name": "engine_stop_updated",
            "type": "hardware",
            "config": {
                "command": "RELAY,0#",
                "reliable": true
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Response

Returns the updated output control object.

```json
{
  "success": true,
  "value": {
    "id": 2,
    "name": "engine_stop_updated",
    "type": "hardware",
    "config": {
      "command": "RELAY,0#",
      "reliable": true
    }
  }
}
```

* `success` - boolean. Always `true` for successful responses.
* `value` - object. The updated output control. See [object structure](#object-structure).

### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if the output control or tracker does not exist.

[General error codes](../../errors.md)

---

## execute

Executes an output control immediately. For hardware commands, the command string is sent to the device. For software commands, an HTTP POST request is dispatched to the configured URL with the current device attribute values substituted into the body.

**Required sub-user rights:** `tracker_update`.

### Parameters

| name | description | type | format |
| --- | --- | --- | --- |
| hash | API key or user session hash. | string | `"your_api_key"` |
| tracker_id | ID of the tracker that owns the output control. | int | `70074765` |
| id | ID of the output control to execute. | int | `3` |

### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/output_control/execute' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "id": 3
    }'
```
{% endtab %}
{% endtabs %}

### Response

```json
{
  "success": true
}
```

* `success` - boolean. Always `true` for successful responses.

### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if the output control or tracker does not exist.

[General error codes](../../errors.md)

---

## delete

Deletes an output control.

**Required sub-user rights:** `tracker_update`.

### Parameters

| name | description | type | format |
| --- | --- | --- | --- |
| hash | API key or user session hash. | string | `"your_api_key"` |
| tracker_id | ID of the tracker that owns the output control. | int | `70074765` |
| id | ID of the output control to delete. | int | `5` |

### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/output_control/delete' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "id": 5
    }'
```
{% endtab %}
{% endtabs %}

### Response

```json
{
  "success": true
}
```

* `success` - boolean. Always `true` for successful responses.

### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if the output control or tracker does not exist.

[General error codes](../../errors.md)

---

# Batch operations

API path: `/tracker/batch_get_output_controls`.

## batch\_get\_output\_controls

Returns all output controls for the specified trackers, grouped by tracker ID. If `trackers` is omitted or empty, returns controls for all trackers accessible to the current user.

**Required sub-user rights:** `tracker_update`.

### Parameters

| name | description | type | format |
| --- | --- | --- | --- |
| hash | API key or user session hash. | string | `"your_api_key"` |
| trackers | Optional. List of tracker IDs to retrieve output controls for. If omitted, all accessible trackers are included. | int array | `[70074765, 70074766]` |

### Examples

{% tabs %}
{% tab title="cURL — specific trackers" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/batch_get_output_controls' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "trackers": [70074765]
    }'
```
{% endtab %}

{% tab title="cURL — all trackers" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/batch_get_output_controls' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key"
    }'
```
{% endtab %}
{% endtabs %}

### Response

Returns a `result` object whose keys are tracker IDs (as strings) and values are arrays of output control objects for that tracker. Trackers with no configured controls return an empty array.

```json
{
  "result": {
    "3234961": [
      {
        "id": 19,
        "name": "Reboot",
        "type": "hardware",
        "config": {
          "command": "cpureset",
          "reliable": true
        }
      },
      {
        "id": 20,
        "name": "Notify Slack",
        "type": "software",
        "config": {
          "url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
          "headers": [],
          "body": "{\n  \"text\": \"Device {{device_id}}: speed {{speed}} km/h at {{latitude}}, {{longitude}}\"\n}"
        }
      }
    ],
    "3490965": [],
    "3302273": []
  },
  "success": true
}
```

* `success` - boolean. Always `true` for successful responses.
* `result` - object. Keys are tracker IDs (string). Values are arrays of output control objects. See [object structure](#object-structure).

### Errors

* 7 - Invalid parameters – if the `trackers` array contains invalid values.

[General error codes](../../errors.md)
