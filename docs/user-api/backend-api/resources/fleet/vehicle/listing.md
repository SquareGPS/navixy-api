---
title: Status listing
description: Contains vehicle status listing object and API calls to interact with it.
---

# Vehicle status listing

{% hint style="warning" %}
**Deprecated!**\
This API action deprecated and should not be used.
{% endhint %}

## Vehicle status listing object

```json
{
  "id": 1,
  "order": 0,
  "label": "label123",
  "color": "FFFFFF"
}
```

* `id` - int. An ID of the status.
* `order` - int. Position of the status. Ignored when update because statuses already have position in an array.
* `label` - string. Status name (description).
* `color` - string. RGB-color.

## API actions

API path: `/vehicle/status/listing`.

### read

Gets all of user's vehicle statuses.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/vehicle/status/listing/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/vehicle/status/listing/read?hash=a6aa75587e5c59c32d347da438505fc3
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
      "id": 1,
      "order": 0,
      "label": "label123",
      "color": "FFFFFF"
    }
  ]
}
```

#### Errors

[General](../../../errors.md#error-codes) types only.

### update

Updates user's vehicle statuses.

#### Parameters

| name     | description                                                                                                    | type             |
| -------- | -------------------------------------------------------------------------------------------------------------- | ---------------- |
| statuses | List of vehicle\_status\_entry objects. If status ID is not null, then update, else create new vehicle status. | array of objects |

Old vehicle statuses, which are not present in `statuses` array, will be deleted.

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/vehicle/status/listing/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "statuses": [{"id": 1, "order": 0, "label": "label123", "color": "FFFFFF"}]}'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

[General](../../../errors.md#error-codes) types only.
