---
title: Entity fields
description: Contains field object description and API calls to interact with it.
---

# Entity Fields

This page provides an overview of the field object and the API calls used to interact with it. Fields are used to add custom information to entities, allowing for enhanced customization and data management.


## Field Object

The field object contains the following attributes:

```json
{
    "id": 131312,
    "label": "Additional info", 
    "type":  "employee",
    "required": false,
    "description": "Responsibility",
    "params": {"responsible": true}
}
```

* `id` - int. Field identifier. Null for the new object.
* `label` -  string. Name of the field.
* `type` - [enum](../../../getting-started/introduction.md#data-types). Type of field, see below.
* `required` - boolean.  Whether the field is required to be filled or not.
* `description` - string. Additional information about the field, up to 512 characters.
* `params` - object. Type-specific parameters. This field should be omitted if no specific params are needed.

**Field Types**:

**Without Special Params:

* `text` - Text field up to 700 Unicode symbols.
* `bigtext` - Larger text field, up to 20,000 Unicode symbols, with reduced search and sorting capabilities.
* `email` - Field for storing an email address, validated to ensure it is a valid email.
* `phone` - Field for storing a phone number, validated to ensure it is a valid phone number.
* `decimal` - Decimal number from -999999999999.999999 to 999999999999.999999, stored up to six decimal places.
* `integer` - integer number from `-2^63` to `2^63 - 1`.

**With Special Params**

* `employee` - Link to an employee.

*Special params:*

```json
{
"responsible": true
}
```

- `responsible` - boolean. Entities with this set to true can be shown to the employee in the mobile app. Only one employee field can have this value set to true. If there’s an [employee assigned](../../tracking/tracker/employee.md#assign) to a Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)), and a [place](../../field_service/place/index.md) has a custom field of type “responsible employee”, such place will be available in the mobile app for viewing. This allows the employee to view all places assigned to them to visit, etc.

## Fields actions

API path: `/entity/fields`.

Fields allow adding custom information to a customizable entity. Each field belongs to one entity.

### `read`

Gets a set of custom fields associated with the specified entity. Note that you must know the entity ID, which can be obtained from [entity/list](index.md#list).

#### Parameters

| name      | description      | type |
|:----------|:-----------------|:-----|
| entity_id | ID of an entity. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/fields/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "entity_id": 131312}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/entity/fields/read?hash=a6aa75587e5c59c32d347da438505fc3&entity_id=131312
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 131312,
         "label": "Additional info", 
         "type":  "employee",
         "required": false,
         "description": "Responsibility",
         "params": {"responsible": true}
    }]
}
```

#### Errors

* 201 - Not found in the database - if there is no entity with such ID.


### `update`

Updates a set of custom fields associated with the specified entity.

**required sub-user rights**: `places_custom_fields_update` for fields associated with `place` entity.

Fields passed with `id` equal to `null` will be created. If field already exists, its `type` must be equal to type of
already stored field (i.e. you can't change a type of field).

All fields associated with the same entity must have different `label`s.

Passing fields with `id` from non-existent fields or fields bound to another entity will result in an error.

!!! warning "If `delete_missing` is `true`, all existing fields which are missing from the `fields` list will be permanently deleted! Otherwise, they are unaffected."

#### Parameters

| name           | description                                                               | type        |
|:---------------|:--------------------------------------------------------------------------|:------------|
| entity_id      | ID of an entity.                                                          | int         |
| fields         | List of new/existing fields to be created/updated.                        | JSON object |
| delete_missing | Optional. Default is `false`. Delete fields not present in `fields` list. | boolean     |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/fields/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "entity_id": 131312, "fields": {"label": "Additional info", "type":  "employee", "required": false, "description": "Responsibility", "params": {"responsible": true}}'
    ```

#### Response

A list of **all** fields associated with the specified entity. Newly created fields will have their IDs filled.

```json
{
    "success": true,
    "list": [{
         "id": 131312,
         "label": "Additional info", 
         "type":  "employee",
         "required": false,
         "description": "Responsibility",
         "params": {"responsible": true}
    }]
}
```

#### Errors

* 201 - Not found in the database – if there is no entity with such ID.
* 7 - Invalid parameters - if fields violate restrictions described above.
