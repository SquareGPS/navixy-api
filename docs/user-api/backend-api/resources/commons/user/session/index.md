---
title: User session
description: Contains a call to prolong user session.
---

# User session

## API actions

API path: `/user/session`.

### renew

Prolongs current user session.\
Works only with standard user session (not with API key).

#### Parameters

Only session `hash`.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/user/session/renew' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```sh
https://api.eu.navixy.com/v2/user/session/renew?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true
}
```
