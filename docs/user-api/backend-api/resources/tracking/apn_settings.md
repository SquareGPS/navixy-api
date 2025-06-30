---
title: APN settings of tracker
description: API call to get APN settings by device's phone number.
---

# APN settings

## API actions

API base path: `/apn_settings`.

### read

Gets the APN name/user/password and mobile operator for registered device by phone number.

#### Parameters

| name  | description                                                            | type   | format       |
| ----- | ---------------------------------------------------------------------- | ------ | ------------ |
| phone | string representing valid international phone number without `+` sign. | string | "1234567890" |

#### Examples

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/apn_settings/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "phone": "1234567890"}'
```
{% endcode %}
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/apn_settings/read?hash=a6aa75587e5c59c32d347da438505fc3&phone=1234567890
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true,
  "value": {
    "name": "internet",
    "user": "",
    "password": "",
    "operator_name": "Deutsche Telekom"
  }
}
```

#### Errors

* 201 – The phone number not found in the database.
