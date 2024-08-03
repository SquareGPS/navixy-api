---
title: Vehicle import
description: API calls to import vehicles.
---

## API actions

API calls to import vehicles.


## API actions

API path: `/vehicle/import/`.

### start

Starting the background process of importing vehicles.

#### Parameters

| name         | description                                                                                       | type         |
|:-------------|:--------------------------------------------------------------------------------------------------|:-------------|
| filename     | Name of file preloaded with [/data/spreadsheet/parse](../../commons/data.md#dataspreadsheetparse) | string       |
| headers      | List of files' headers, see available fields above                                                | string array |
| user_headers | Optional. List of user labels for headers                                                         | string array |

Available fields:

* `label`
* `model`
* `max_speed`
* `type`
* `subtype`
* `garage`
* `trailer`
* `manufacture_year`
* `color`
* `additional_info`
* `trailer_reg_number`
* `reg_number`
* `chassis_number`
* `frame_number`
* `vin`
* `passengers`
* `payload_weight`
* `payload_height`
* `payload_width`
* `payload_length`
* `gross_weight`
* `fuel_grade`
* `fuel_tank_volume`
* `fuel_cost`
* `norm_avg_fuel_consumption`
* `fuel_type`
* `tyre_size`
* `tyres_number`
* `wheel_arrangement`
* `free_insurance_policy_number`
* `liability_insurance_policy_number`
* `free_insurance_valid_till`
* `liability_insurance_valid_till`
* `tracker_label`
* `tags`
* `undefined` (if a meaning of a field is not known)

#### Response

```json
{
  "success": true,
  "id": <int>
}
```

#### Example

=== "cURL"

```bash
curl -X POST "{{ extra.api_example_url }}/vehicle/import/start" \
    -H "Content-Type: application/json" \
    --data-binary @- << EOF
{
    "hash": "a6aa75587e5c59c32d347da438505fc3",
    "filename": "tmp-sheet640571613016981796.tsv",
    "headers": ["label", "model", "max_speed", "type", "subtype", "reg_number", "fuel_grade", "fuel_tank_volume", "free_insurance_policy_number", "free_insurance_valid_till", "tracker_label", "tags"],
    "user_headers": [ "Model", "Max speed", "Type", "Subtype", "Reg. number", "Fuel grade", "Fuel tank volume", "Free insurance policy number", "Free insurance valid till", "Object", "Tags"]
}
EOF
```

#### Errors

* 15 - Too many requests (rate limit exceeded) - if too many imports in progress
* 233 - No data file
* 234 - Invalid data format
* 247 - Entity already exists - there is another identical import with the same file

### `read`

Returns an import process with specified ID.

#### Parameters

| name       | description | type |
|:-----------|:------------|:-----|
| process_id | Process ID  | int  |

#### Response

```json
{
  "success": true,
  "value": {
    "id": <int>,
    "user_id": <int>,
    "created": <date>,
    "type": "Vehicle",
    "params": {
      "headers": [<string>, <string>,...] // List of files' headers
    },
    "filename": <string>, // Name of preloaded TSV.
    "status": <string>, // created | in_progress | done | failed | finished
    "status_change_date": <date>,
    "progress": {
      "imported": <int>,
      "failed": <int>,
      "percent": <int>, // approximate percentage of processed
      "processed_lines": <int>,
      "warnings": [{line:<int>, error: <string>}], // first 25
      "errors": [{line:<int>, error: <string>}], // first 25
    }
  }
}
```

#### Example

=== "cURL"

```bash
curl -X POST "{{ extra.api_example_url }}/vehicle/import/read" \
    -H "Content-Type: application/json" \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "process_id": 1}'
```

#### Errors

* 201 – Not found in database (if import is not found)

### `list`

Returns the list of the user's vehicle import processes.

#### Response

```json
{
  "success" : true,
  "list" : [ {
    "id": <int>,
    "user_id": <int>,
    "created": <date>,
    "type": "Vehicle",
    "params": {
      "headers": [<string>, <string>,...] // List of files' headers
    },
    "filename": <string>, // Name of preloaded TSV.
    "status": <string>, // created | in_progress | done | failed
    "status_change_date": <date>,
    "progress": {
      "imported": <int>,
      "failed": <int>,
      "percent": <int>, // approximate percentage of processed
      "processed_lines": <int>,
      "warnings": [{line:<int>, error: <string>}], // first 25
      "errors": [{line:<int>, error: <string>}], // first 25
    }
  }, ...]
}
```

#### Example

=== "cURL"

```bash
curl -X POST "{{ extra.api_example_url }}/vehicle/import/list" \
    -H "Content-Type: application/json" \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

### `download_failed`

Retrieve a file with lines that contained errors and did not pass validation.

#### Parameters

| name       | description | type |
|:-----------|:------------|:-----|
| process_id | Process ID  | int  |

#### Response

File (standard file download).

#### Example

=== "cURL"

```bash
curl -X POST "{{ extra.api_example_url }}/vehicle/import/download_failed" \
    -H "Content-Type: application/json" \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "process_id": 7}'
```

#### Errors

* 201 – Not found in database (if import is not found)
* 204 – Entity not found (if file is not found)
