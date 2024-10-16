---
title: Equipment
description: An API call to get the list of available equipment.
---

# Equipment

API call to get the list of all available equipment.


## Equipment object

```json
{
  "equip_id": 33, 
  "model_name": "SPT10 SB", 
  "model_code": "pt10",
  "vendor": "3. NAVIXY S Series (personal)",
  "name": "NAVIXY S10"
}
```

* `equip_id` - int. Equipment ID.
* `model_name` - string. A model's original name.
* `model_code` - string. A model code which should be inserted to tracker bundles.
* `vendor` - string. A vendor's name.
* `name` - string. A model's name used by a vendor.


## API actions

API path: `panel/equipment`.

### `list`

Returns list of all equipment which can be assigned to tracker bundles. 

*required permissions*: `tracker_bundles: "read"`.

#### Parameters

Only session `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/equipment/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/equipment/list?hash=fa7bf873fab9333144e171372a321b06
    ```

#### Response

```json
{
    "success": true,
    "list" : [{
        "equip_id": 33, 
        "model_name": "SPT10 SB", 
        "model_code": "pt10",
        "vendor": "3. NAVIXY S Series (personal)",
        "name": "NAVIXY S10"
    }] 
}
```

#### Errors

[General](../../user-api/backend-api/getting-started/errors.md#error-codes) types only.