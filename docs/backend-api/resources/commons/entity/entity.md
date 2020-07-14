---
title: /entity
description: /entity
---

# entity actions:

Entity describes a class of objects for which representation and editable fields can be customized.
For example, you can add your own custom fields to **places** entity or rearrange existing fields.

**entity** is:
```js
<entity> = {
    "id": 123, //identifier
    "type": "place", //currently, only "place" is supported
    "settings": {
        "layout": { //describes layout of fields for entity.
                "sections": [ //each section can contain one or more fields. At least one section must exist in layout.
                  {
                    "label": "Section label",
                    "field_order": [ //built-in fields and ids of custom fields (as strings)
                      "label",
                      "location",
                      "131212",
                      "tags",
                      "description"
                    ]
                  }
                ]
              }
    }
}
```

**entity types**:
* **place** - a place object, the same that is available through [place/](../../field_service/place/place.md) API

  Builtin fields:

  * label
  * location
  * tags
  * description  
  


## list(…)

Get list of entities which are available for customization.

#### parameters:

none

#### return:

```js
{
    "success": true,
    "list": [ <entity>, ... ]
}
```

#### errors:

Standard errors only.



## read(…)
Get entity by id or by type

#### parameters:

name      | description     | type
---       | ---             | ---
id        | ID of an entity | int
type      | type of an entity | entity type string, see above

**Exactly one of these parameters must be specified. They can't be both null or both non-null.**

#### return:
```js
{
    "success": true,
    "entity": <entity>, 
    "fields": [ //fields associated with this entity
        <field>,
        ...
    ]
}
```
#### errors:
* 201 (Not found in database) – if there is no entity with such ID


## update(entity)
Updates settings of customizable entity. Entity must have a valid id.

**required subuser rights**: places_custom_fields_update for entities with type `place`

**WARNING**: `entity.settings.layout.sections` must contain ids of all builtin and custom fields which are associated 
with this entity. No fields can be omitted from layout, only reordering is allowed. Fields cannot be duplicated, even 
in different sections.

#### parameters:
name      | description                              | type
---       | ---                                      | ---
entity    | Entity object with valid id and settings | \<entity\> object 

#### errors:
* 201 (Not found in database) – if there is no entity with such ID
* 7 (Invalid parameters) - if entity object violates restrictions described above

#### return:
```js
{
    "success": true
}
```