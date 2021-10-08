---
title: Entity fields
description: Contains field object description and API calls to interact with it.
---

# Entity fields

Contains field object description and API calls to interact with it.

<hr>

## Field object

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
* `type` - [enum](../../../getting-started.md#data-types). Type of field, see below.
* `required` - boolean. Whether field required to be filled or not.
* `description` - string. Additional info about the field, max 512 characters.
* `params` - object. Type-specific parameters. If no specific params, this field should be omitted.

**field types**:

Without *Special params:*

* `text` - text field up to 700 unicode symbols.
* `bigtext` - bigger text field, up to 20000 unicode symbols with reduced search and sorting capabilities.
* `email` - field for storing email, validated to contain valid email address.
* `phone` - field for storing phone number, validated to contain valid phone number.
* `decimal` - decimal number from -999999999999.999999 to 999999999999.999999 . Values stored up to the sixth decimal place.
* `integer` - integer number from `-2^63` to `2^63 - 1`.

With *Special params:*

* `employee` - link to employee.

*Special params:*

```json
{
"responsible": true
}
```

`responsible` - boolean. Entities with this set to `true` can be shown to the employee in the mobile app. Only one 
employee field can have this value set to `true`.
If there's an [employee assigned](../../tracking/tracker/employee.md#assign) to a Mobile Tracker App 
([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)),
and a [place](../../field_service/place/index.md) has a custom field of type "responsible employee", 
such place will be available in the mobile app to view.
Thus, field employee can view all places assigned to him to visit them, etc.

<hr>

## Fields actions

API path: `/entity/fields`.

Field allows adding custom information to a customizable entity. Each field belongs to one entity.

### read(entity_id)

Gets a set of custom fields associated with the specified entity. Note that you must know entity id, which can be 
obtained from [entity/list](./index.md#list).

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| entity_id | ID of an entity. | int |

#### examples

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

#### response

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

#### errors

* 201 - Not found in the database - if there is no entity with such ID.

<hr>

### update(entity_id, fields, delete_missing)

Updates a set of custom fields associated with the specified entity.

**required sub-user rights**: `places_custom_fields_update` for fields associated with `place` entity.

Fields passed with `id` equal to `null` will be created. If field already exists, its `type` must be equal to type of
already stored field (i.e. you can't change a type of field).

All fields associated with the same entity must have different `label`s.

Passing fields with `id` from non-existent fields or fields bound to another entity will result in an error.

!!! warning "If `delete_missing` is `true`, all existing fields which are missing from the `fields` list will be permanently deleted! Otherwise, they are unaffected."

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| entity_id | ID of an entity. | int |
| fields | List of new/existing fields to be created/updated. | JSON object |
| delete_missing | Optional. Default is `false`. Delete fields not present in `fields` list. | boolean |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/fields/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "entity_id": 131312, "fields": {"label": "Additional info", "type":  "employee", "required": false, "description": "Responsibility", "params": {"responsible": true}}'
    ```

#### response

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

#### errors

* 201 - Not found in the database – if there is no entity with such ID.
* 7 - Invalid parameters - if fields violate restrictions described above.
