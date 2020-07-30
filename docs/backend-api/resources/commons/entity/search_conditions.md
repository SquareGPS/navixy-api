---
title: Entity search conditions
description: Entity search conditions
---

# Entity search Conditions

API path: `/entity/search_conditions`.

Search conditions are used to search and filter list of certain entities by built-in and/or custom fields.

Example: 

```js
<search_conditions> = [
    {"type":"and", "conditions":[
        {"type":"or", "conditions":[
                {
                      "type": "eq",
                      "field":"18",
                      "value": 1111
                },
                {
                      "type": "contains",
                      "field":"27",
                      "value": "qqq"
                }
            ]
        },
        {
            "type": "contains",
            "field":"label",
            "value": "who"
        }
     ]
    }
]
```

Conditions are represented by an array, each condition during search is evaluated, and the result is either `true` or `false`.
Thus, boolean operations such as `AND` or `OR` can be applied to them. All conditions in a top-level array are joined using `AND` operator.

**WARNING**: A maximum of 72 conditions can be used at once, including nested conditions.

### Condition types

##### And
```js
<and_condition> = {
    "type":"and", 
    "conditions":[
            <list of other conditions here...>
    ]
}
```

Evaluates all specified conditions and joins them using `AND` boolean operator.

##### Or
```js
<or_condition> = {
    "type":"or", 
    "conditions":[
            <list of other conditions here...>
    ]
}
```

Evaluates all specified conditions and joins them using `OR` boolean operator.

##### Number equals
```js
<eq_condition> = {
      "type": "eq",
      "field":"18", //built-in field or field id
      "value": 1111 //number value to which field is matched against. Can be decimal. 
                    //Must be between -2^63 and 2^63-1. No more than 6 fraction digits
}
```

Checks if specified field is equal to provided number value. Works for text fields too (e.q. "111" is considered equal to 111).
 For linked entity fields, it matches linked entity id to number value.

##### Contains string

```js
<contains_condition> = {
    "type": "contains",
    "field":"label", //built-in field or field id
    "value": "who" //string value to which field is matched against. 
                   //Cannot  be null or empty, max length is 760
}
```

Checks if specified field contains substring equal to provided value. Works for number fields too, e.g. (123123 contains "123").
For linked entity fields, it matches value against linked entity label or other similar field (first name, last name, etc.)