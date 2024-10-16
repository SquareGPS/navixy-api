---
title: Entity search conditions
description: Contains search conditions object description and condition types. Search conditions used to search and filter list of certain entities by built-in and/or custom fields.
---

# Entity Search Conditions

This page provides an overview of the search conditions object description and the types of conditions that can be used. Search conditions are employed to filter and retrieve a list of specific entities based on both built-in and custom fields.

## Search conditions object

Search conditions are represented by an array of conditions, where each condition is evaluated to either true or false. Boolean operations such as AND or OR can be applied to these conditions. All conditions in the top-level array are joined using the AND operator by default.

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

!!! warning “A maximum of 72 conditions can be used at once, including nested conditions.”


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


#### `OR` Condition

This condition evaluates all specified sub-conditions and joins them using the OR boolean operator.

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