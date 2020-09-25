---
title: Trusted number
description: Trusted number
---
# Trusted number

API base path: `/tracker/trusted_number`

### list

Gets list of trusted numbers for the specified tracker.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 999199 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/trusted_number/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/trusted_number/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": ["496156680000", "496156680001"]
}
```

* `list` - List of strings containing trusted phone numbers in the international format without "+".

#### errors

* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).

### update

Replaces the list of trusted numbers for a specified tracker with the new one.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 999199 |
| list | Array of phone numbers (10-15 digits) represented as strings. | array of string | `[496156680001, 496156680000]` |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/trusted_number/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489", "list": ["496156680001","496156680000"]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/readings/list?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489&list=["496156680001","496156680000"]
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).

