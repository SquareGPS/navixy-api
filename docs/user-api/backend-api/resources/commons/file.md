---
title: File
description: Contains an API call to get user's file statistic.
---

# File

## API actions

API path: `/file`.

### stats/read

Gets user's files statistic.

#### Parameters

Only API key `hash`.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/file/stats/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
```http
https://api.eu.navixy.com/v2/file/stats/read?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true,
  "value": {
    "file_count": 24,
    "total_size": 40192953,
    "quota": 104857600
  }
}
```

* `file_count` - int. Count of all uploaded files.
* `total_size` - int. Total files size in bytes.
* `quota` - int. Space available to the user in bytes.

#### Errors

* [General](../../errors.md#error-codes) types only.
