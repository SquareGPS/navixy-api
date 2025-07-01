---
title: Base
description: Contains API calls to health-check and send email.
---

# Base

## API actions

API path: `/base`.

### nothing

The report for health-check. It will do nothing.

#### Parameters

Only API key `hash`.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/base/nothing' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
```http
{{ extra.api_example_url }}/base/nothing?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* [General](../../errors.md#error-codes) types only.

### send\_email

Sends email from the platform to any email address with specified title and text. Needs ROOT access level.

#### Parameters

| name          | description         | type   |
| ------------- | ------------------- | ------ |
| from          | From email address. | string |
| to            | To email address.   | string |
| title         | Title of the email. | string |
| message       | Text of the email.  | string |
| service\_id   | Service parameter.  | int    |
| service\_pass | Service parameter.  | int    |

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/base/send_email' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "gps@navixy.com", "to" : "customer@email.com", "title": "test email", "message": "this email for test", "service_id": 1, "service_pass": 28}'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* [General](../../errors.md#error-codes) types only.
