---
title: Entity search conditions
description: Contains search conditions object description and condition types. Search conditions used to search and filter list of certain entities by built-in and/or custom fields.
---

# Entity Search Conditions

This page provides an overview of the search conditions object description and the types of conditions that can be used. Search conditions are employed to filter and retrieve a list of specific entities based on both built-in and custom fields.

## Search conditions object

Search conditions are represented by an array of conditions, where each condition is evaluated to either true or false. Boolean operations such as `AND` or `OR` can be applied to these conditions. All conditions in the top-level array are joined using the `AND` operator by default.

```json
[
    {"type":"and", 
        "conditions":[
          {"type":"or", 
             "conditions":[
                {
                      "type": "eq",
                      "field":"18",
                      "value": 1111
                },
                {
                      "type": "contains",
                      "field":"27",
                      "value": "qqq"
                }]
          },
        {
            "type": "contains",
            "field":"label",
            "value": "who"
        }]
    }
]
```

!!! warning "A maximum of 72 conditions can be used at once, including nested conditions."


## Condition Types

### `AND` Condition

This condition evaluates all specified sub-conditions and joins them using the `AND` boolean operator.

```json
{
    "type":"and", 
    "conditions":[{
        "type": "eq",
        "field":"18",
        "value": 1111
    },
    {
        "type": "contains",
        "field":"27",
        "value": "qqq"
    }]
}
```

* `conditions` - array. Contains from 2 to 60 sub-conditions to be joined.

### `OR` Condition

This condition evaluates all specified sub-conditions and joins them using the `OR` boolean operator.

```json
{
    "type":"or", 
    "conditions":[{
         "type": "eq",
         "field":"18",
         "value": 1111
    },
    {
         "type": "contains",
         "field":"27",
         "value": "qqq"
    }]
}
```

* `conditions` - array. Contains from 2 to 60 sub-conditions to be joined.

### `NOT` Condition

This condition evaluates a sub-condition and negates its result. If the sub-condition evaluates to `true`, the `NOT`
condition will be evaluated as `false`, and vice versa.

```json
{
  "type": "not",
  "condition": {
    "type": "eq",
    "field": "18",
    "value": 1111
  }
}
```

* `condition` - object. A single condition to be negated.

### `NUMBER EQUALS` Condition

This condition checks if the specified field is equal to the provided number value. It also works for text fields (e.g., “111” is considered equal to 111). For linked entity fields, it matches the linked entity ID to the number value.
 
```json
{
      "type": "eq",
      "field":"18",
      "value": 1111
}
```

* `field` - string. A standard field or field ID.
* `value` - int. Number value to match against the field. Can be decimal, must be between -2^63 and 2^63-1, with no more than 6 fractional digits.

### `CONTAINS STRING` Condition

This condition checks if the specified field contains a substring equal to the provided value. It also works for number fields (e.g., 123123 contains “123”). For linked entity fields, it matches the value against the linked entity label or other similar fields (e.g., first name, last name).

```json
{
    "type": "contains",
    "field":"label",
    "value": "who"
}
```

* `field` - string. A standard field or field ID.
* `value` - string. Value to match against the field. Cannot be null or empty, maximum length is 760 characters.

### `IN` Condition

This condition checks if the specified field matches any value within the provided array of values.

```json
{
    "type": "in",
    "field": "18",
    "value": [1111, 2222, 3333]
}
```

* `field` - string. A standard field or field ID.
* `value` - array. Contains a list of values to match against the field. Each value must follow the same rules as in
  `NUMBER EQUALS` or `CONTAINS STRING` conditions, depending on the field type.

### `TIMESTAMP IN THE PERIOD` Condition

This condition checks if the specified timestamp field falls within a given period. The period is inclusive,
meaning it includes both the `from` and `to` timestamps.

```json
{
    "type": "period",
    "field": "creation_date",
    "value": {
        "from": "2023-01-01T00:00:00Z",
        "to": "2023-12-31T23:59:59Z"
    }
}
```

* `field` - string. The name or ID of the timestamp field to evaluate.
* `value` - object. Contains the `from` and `to` values defining the period.
    * `from` - [date/time](../../../getting-started/introduction.md#data-types). The beginning of the period.
    * `to` - [date/time](../../../getting-started/introduction.md#data-types). The end of the period.
