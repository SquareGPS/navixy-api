---
title: Vehicle status listing
description: Vehicle status listing
---

# Vehicle status listing

API path: `/vehicle/status/listing`.

## Vehicle status listing

```json
{
    "id": 1,
    "order": 0,
    "label": "label123",
    "color": "FFFFFF"
}
```

* `id` - int. An id of the status.
* `order` - int. Position of the status. Ignored when update because statuses already have position in an array.
* `label` - string. Status's name (description).
* `color` - string. RGB-color.

### read

Gets all of user's vehicle statuses.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/status/listing/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/status/listing/read?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
        "id": 1,
        "order": 0,
        "label": "label123",
        "color": "FFFFFF"
    }]
}
```

#### errors

[General](../../../../getting-started.md#error-codes) types only.

### update

Updates user's vehicle statuses.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| statuses| List of vehicle_status_entry objects. If status's id is not null, then update, else create new vehicle status. | array of objects |

Old vehicle statuses, which are not present in `statuses` array, will be deleted.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/status/listing/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "statuses": [{"id": 1, "order": 0, "label": "label123", "color": "FFFFFF"}]}'
    ```

#### response

```json
{ "success": true }
```

#### errors

[General](../../../../getting-started.md#error-codes) types only.