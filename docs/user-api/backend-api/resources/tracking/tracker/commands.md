---
description: >-
  Create, manage, and execute custom device commands and HTTP POST webhooks for
  individual trackers.
---

# Commands

Commands let you define reusable commands for a tracker and execute them on demand. Two command types are supported:

* **Hardware** — sends a protocol-level command string directly to the device (e.g. to reboot firmware or toggle a relay).
* **HTTP** — sends an HTTP POST request with a JSON body to any URL, optionally embedding live device attributes in the payload.

Commands are stored per tracker and can be executed at any time from the [Commands block](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/devices-and-settings/object-management/output-control-block) in the platform UI.

{% hint style="info" %}
Commands is designed for manual, on-demand actions targeting a single tracker. For automated, rule-based command sending across multiple devices, use [IoT Logic](https://app.gitbook.com/o/YVLWhgAwCZPoU5vlRsCs/s/tx3J5BxnWyPV0nP2xr0z/) with the **Device action** or **Webhook** nodes.
{% endhint %}

### Object structure

Each command has a common set of fields. The `config` object differs by `type`.

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

* `id` - int. Unique command ID. Assigned by the server on creation. Read-only.
* `name` - string. Human-readable label shown in the Commands block (e.g. `"engine_stop"`).
* `type` - string. Always `"hardware"` for this variant.
* `config` - object. Hardware command configuration.
  * `command` - string. The exact protocol-level command string sent to the device (e.g. `"RELAY,1#"`). Valid values are device-specific — refer to your device manufacturer's documentation.
  * `reliable` - boolean. If `true`, the platform requests delivery confirmation (acknowledgement) from the device before marking the command as successfully sent.
{% endtab %}

{% tab title="HTTP" %}
```json
{
  "id": 20,
  "name": "Notify Slack",
  "type": "http",
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

* `id` - int. Unique command ID. Assigned by the server on creation. Read-only.
* `name` - string. Human-readable label shown in the Commands block (e.g. `"webhook_action"`).
* `type` - string. Always `"http"` for this variant.
* `config` - object. HTTP command configuration.
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

## API actions

API base path: `/tracker/command`.

{% hint style="info" %}
All API calls require authentication. Pass your **API key** or **user session hash** as the `hash` parameter in the request body, as a query string parameter, or in the `Authorization: NVX <value>` header. API keys are recommended for integrations — they don't expire and can be managed independently. See [Authentication](../../authentication.md) for details.
{% endhint %}

### create

Creates a new command for a tracker.

**Required sub-user rights:** `tracker_update`.

#### Parameters

| name        | description                                                                        | type   | format           |
| ----------- | ---------------------------------------------------------------------------------- | ------ | ---------------- |
| hash        | API key or user session hash.                                                      | string | `"your_api_key"` |
| tracker\_id | ID of the tracker to create the command for.                                       | int    | `70074765`       |
| command     | Command object without `id`. See [object structure](commands.md#object-structure). | object | See examples     |

#### Examples

{% tabs %}
{% tab title="cURL — hardware" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/command/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "command": {
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

{% tab title="cURL — http" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/command/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "command": {
            "name": "webhook_action",
            "type": "http",
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

#### Response

Returns the created command object, including the server-assigned `id`.

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
* `value` - object. The created command. See [object structure](commands.md#object-structure).

#### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if no tracker with the given `tracker_id` belongs to the current user.

[General error codes](../../../errors.md)

***

### update

Updates an existing command. The full object including `id` must be provided.

**Required sub-user rights:** `tracker_update`.

#### Parameters

| name        | description                                                                                  | type   | format           |
| ----------- | -------------------------------------------------------------------------------------------- | ------ | ---------------- |
| hash        | API key or user session hash.                                                                | string | `"your_api_key"` |
| tracker\_id | ID of the tracker that owns the command.                                                     | int    | `70074765`       |
| command     | Updated command object including `id`. See [object structure](commands.md#object-structure). | object | See example      |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/command/update' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "command": {
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

#### Response

Returns the updated command object.

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
* `value` - object. The updated command. See [object structure](commands.md#object-structure).

#### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if the command or tracker does not exist.

[General error codes](../../../errors.md)

***

### execute

Executes a command immediately. For hardware commands, the command string is sent to the device. For HTTP commands, an HTTP POST request is dispatched to the configured URL with the current device attribute values substituted into the body.

**Required sub-user rights:** `tracker_update`.

#### Parameters

| name        | description                              | type   | format           |
| ----------- | ---------------------------------------- | ------ | ---------------- |
| hash        | API key or user session hash.            | string | `"your_api_key"` |
| tracker\_id | ID of the tracker that owns the command. | int    | `70074765`       |
| command\_id | ID of the command to execute.            | int    | `3`              |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/command/execute' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "command_id": 3
    }'
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true
}
```

* `success` - boolean. Always `true` for successful responses.

#### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if the command or tracker does not exist.

[General error codes](../../../errors.md)

***

### delete

Deletes a command.

**Required sub-user rights:** `tracker_update`.

#### Parameters

| name        | description                              | type   | format           |
| ----------- | ---------------------------------------- | ------ | ---------------- |
| hash        | API key or user session hash.            | string | `"your_api_key"` |
| tracker\_id | ID of the tracker that owns the command. | int    | `70074765`       |
| command\_id | ID of the command to delete.             | int    | `5`              |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/command/delete' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "tracker_id": 70074765,
        "command_id": 5
    }'
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true
}
```

* `success` - boolean. Always `true` for successful responses.

#### Errors

* 7 - Invalid parameters – if required fields are missing or malformed.
* 201 - Not found in the database – if the command or tracker does not exist.

[General error codes](../../../errors.md)

***

## Batch operations

API path: `/tracker/batch_get_commands`.

### batch\_get\_commands

Returns all commands for the specified trackers, grouped by tracker ID. If `trackers` is omitted or empty, returns commands for all trackers accessible to the current user.

**Required sub-user rights:** `tracker_update`.

#### Parameters

| name     | description                                                                                               | type      | format                 |
| -------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------------------- |
| hash     | API key or user session hash.                                                                             | string    | `"your_api_key"`       |
| trackers | Optional. List of tracker IDs to retrieve commands for. If omitted, all accessible trackers are included. | int array | `[70074765, 70074766]` |

#### Examples

{% tabs %}
{% tab title="cURL — specific trackers" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/batch_get_commands' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key",
        "trackers": [70074765]
    }'
```
{% endtab %}

{% tab title="cURL — all trackers" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/batch_get_commands' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "your_api_key"
    }'
```
{% endtab %}
{% endtabs %}

#### Response

Returns a `result` object whose keys are tracker IDs (as strings) and values are arrays of command objects for that tracker. Trackers with no configured commands return an empty array.

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
        "type": "http",
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
* `result` - object. Keys are tracker IDs (string). Values are arrays of command objects. See [object structure](commands.md#object-structure).

#### Errors

* 7 - Invalid parameters – if the `trackers` array contains invalid values.

[General error codes](../../../errors.md)
