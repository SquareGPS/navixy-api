---
title: Entity search conditions
description: Contains search conditions object description and API calls to interact with it. Search conditions used to search and filter list of certain entities by built-in and/or custom fields.
---

# Entity search Conditions

Contains search conditions object description and API calls to interact with it.<br> 
Search conditions used to search and filter list of certain entities by built-in and/or custom fields.

API path: `/entity/search_conditions`.

## Search conditions object

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

Conditions represented by an array, each condition during search evaluated, and the result is either `true` or `false`.
Thus, boolean operations such as `AND` or `OR` can be applied to them. All conditions in a top-level array joined using `AND` operator.

**WARNING**: A maximum of 72 conditions can be used at once, including nested conditions.

### Condition types

#### "And" condition

Evaluates all specified conditions and joins them using `AND` boolean operator.

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

#### "Or" condition

Evaluates all specified conditions and joins them using `OR` boolean operator.

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

#### "Number equals" condition

Checks if specified field is equal to provided number value. Works for text fields too (e.q. "111" is considered equal to 111).
 For linked entity fields, it matches linked entity id to number value.
 
```json
{
      "type": "eq",
      "field":"18",
      "value": 1111
}
```

* `field` - string. A built-in field or field id.
* `value` - int. Number value to which field matched against. Can be decimal. Must be between `-2^63` and `2^63-1`. No 
more than 6 fractions digits.

#### "Contains string" condition

Checks if specified field contains substring equal to provided value. Works for number fields too, e.g. (123123 contains "123").
For linked entity fields, it matches value against linked entity label or other similar field (first name, last name, etc.)

```json
{
    "type": "contains",
    "field":"label",
    "value": "who"
}
```

* `field` - string. A built-in field or field id.
* `value` - int. String value to which field matched against. Cannot  be null or empty, max length is 760.