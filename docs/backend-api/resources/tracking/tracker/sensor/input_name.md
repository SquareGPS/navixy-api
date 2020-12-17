---
title: Input name
description: Input name
---

# Input name

API base path: `/tracker/sensor/input_name`

### list

Returns descriptions of all sensor inputs existing in the system. 

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/input_name' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/input_name?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

For every input following properties returned: `input_name` and `description`.

`input_name` is an enum member, same as in [sensor object](./index.md).

`description` is made in current user's language (according to [locale settings](../../../commons/user/settings/index.md)).

```json
{
  "success": true,
  "list": [{
    "input_name": "analog_1", 
    "description": "Sensor analógico #1"
  },
  {
    "input_name": "can_coolant_t",
	"description": "CAN: Temperatura del refrigerante"
  }]
}
```

#### errors

No specific errors.
