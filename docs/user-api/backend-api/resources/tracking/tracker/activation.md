---
title: Activation
---

# Activation

## API actions

API base path: `/tracker/activation`.

### schema/read

Reads a JSON schema for a tracker activation form.

#### Parameters

| name  | description        | type   |
|-------|--------------------|--------|
| model | Tracker model code | string |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/activation/schema/read?model=telfmb920' \
    -H 'Authorization: NVX a6aa75587e5c59c32d347da438505fc3'
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "value": {
    "oneOf": [
      {
        "type": "object",
        "title": "bundled_sim",
        "required": ["iccid"],
        "properties": { "iccid": { "type": "string", "pattern": "89[0-9]{17,18}" } }
      },
      {
        "type": "object",
        "title": "optional_activation_phone",
        "required": ["phone"],
        "properties": {
          "apn_name": { "type": "string", "pattern": "[-a-zA-Z0-9_.@ ]*" },
          "apn_user": { "type": "string", "pattern": "[-a-zA-Z0-9_.@ ]*" },
          "apn_password": { "type": "string", "pattern": "^[^\\p{Cntrl}\\uD800-\\uDFFF\\uE000-\\uF8FF]+$" },
          "phone": { "type": "string", "pattern": "^[0-9]{8,20}$" },
          "activation_code": { "type": "string", "pattern": "[0-9]{3,20}" }
        }
      }
    ]
  },
  "success": true
}
```

#### Errors

* 220 — Unknown device model.
