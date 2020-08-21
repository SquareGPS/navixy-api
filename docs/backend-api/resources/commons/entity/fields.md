---
title: Entity fields
description: Entity fields
---

# Entity fields

API path: `/entity/fields`.

## Fields actions

Field allows to add custom information to a customizable entity. Each field belongs to one entity.

**field** is:
```js
<field> = {
    "id": 131312, //identifier, null when new object
    "label": "Additional info", 
    "type":  "text", //type of field, see below    
    "required": false, //whether field is required to be filled or not
    "description": "Info about place", //Additional info about the field, max 250 characters
    "params": { ... } //type-specific. If no specific params, this field should be omitted 
}
```

**field types**:

* `text` - text field up to 700 unicode symbols

  *Special params:* none
  
* `bigtext` - bigger text field, up to 20000 unicode symbols with reduced search and sorting capabilities

  *Special params:* none
  
* `email` - field for storing email, validated to contain valid email address

  *Special params:* none
  
* `phone` - field for storing phone number, validated to contain valid phone number

  *Special params:* none
  
* `decimal` - decimal number from -999999999999.999999 to 999999999999.999999 . Values are stored up to the sixth decimal place

  *Special params:* none
  
* `integer` - integer number from `-2^63` to `2^63 - 1`
 
  *Special params:* none
  
* `employee` - link to employee

  *Special params:* 
  ```js
  {
    "responsible": true //entities with this set to "true" can be shown to the employee in the mobile app.
                      //Only one employee field can have this value set to "true" 
  }
  ```    
  If there's an [employee](../employee) [assigned](../../tracking/tracker/employee.md#assign) to a Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)),
  and a [place](../../field_service/place/index.md) has a custom field of type "responsible employee", such place will be available in mobile app to view.
  Thus, field employee can view all places assigned to him to visit them, etc.

### read(entity_id)
Get a set of custom fields associated with the specified entity. Note that you must know entity id, which can be 
obtained from [entity/list](index.md#list)

#### parameters
name      | description     | type
---       | ---             | ---
entity_id | ID of an entity | int

#### response
```js
{
    "success": true,
    "list": [ <field>, ... ]
}
```

#### errors
* 201 (Not found in database) – if there is no entity with such ID

### update(entity_id, fields, delete_missing)

Update a set of custom fields associated with the specified entity.

**required subuser rights**: places_custom_fields_update for fields associated with `place` entity

Fields passed with `id` equal to `null` will be created. If field already exists, its `type` must be equal to type of 
already stored field (i. e. you cannot change type of a field).

All fields associated with the same entity must have different `label`s.

Passing fields with `id` from non-existent fields or fields bound to another entity will result in an error.

**WARNING** If `delete_missing` is `true`, all existing fields which are missing from the `fields` list will be 
permanently deleted! Otherwise they are unaffected.

#### parameters
name           | description                                                             | type
---            | ---                                                                     | ---
entity_id      | ID of an entity                                                         | int
fields         | List of new/existing fields to be created/updated                       | \<field\>[]
delete_missing | (optional, default is false) delete fields not present in `fields` list | boolean

#### errors
* 201 (Not found in database) – if there is no entity with such ID
* 7 (Invalid parameters) - if fields violate restrictions described above

#### response
A list of **all** fields associated with the specified entity. Newly created fields will have their IDs filled.
```js
{
    "success": true,
    "list": [ <field>, ... ]
}
```