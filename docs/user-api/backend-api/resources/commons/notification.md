---
title: Notification
description: Contains an API call to get list of user notifications.
---

# Notification

## API actions

API path: `/notification`.

### list

Lists user notifications.

#### Parameters

Only API key `hash`.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/notification/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/notification/list?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 12451529,
      "message": "notification",
      "show_till": "2020-12-31 17:27:28"
    }
  ]
}
```

* `id` - int. An ID of notification.
* `message` - string. Message of notification.
* `show_till` - date/time. Date until notification should be shown.

#### Errors

* [General](../../errors.md#error-codes) types only.
