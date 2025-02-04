---
title: Entity
description: Contains entity object description and API calls to interact with it. Entity describes a class of objects for which representation and editable fields can be customized.
---

# Entity actions

This page provides an overview of entity object descriptions and the API calls used to interact with them. In Navixy, an entity represents a class of objects for which representation and editable fields can be customized. 

For example, you can add custom fields to the **places** entity or rearrange existing fields to suit your needs. This flexibility allows for tailored data representation and enhanced data management within the platform.

## Entity object

```json
{
    "id": 123,
    "type": "place",
    "settings": {
      "layout": {
        "sections": [{
          "label": "Section label",
          "field_order": [
            "label",
            "location",
            "131212",
            "tags",
            "description"
          ]
        }]
      }
    }
}
```

* `id` - int. Entity identifier.
* `type` - [enum](../../../getting-started/introduction.md#data-types). Currently, only "place" is supported.
* `layout` - object describes layout of fields for entity.
    * `sections` - array of objects. Each section can contain one or more fields. At least one section must exist in a layout.
    * `label` - string. Name of section.
    * `field_order` - string array. Built-in fields and IDs of custom fields (as strings).

**Entity types**:

**place** - a place object, the same as is available through [place API](../../field_service/place/index.md).

Builtin fields:

* label.
* location.
* tags.
* description.


## API actions

API path: `/entity`.

### `list`

Get list of entities which are available for customization.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/entity/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
      "id": 123,
      "type": "place",
      "settings": {
        "layout": {
          "sections": [{
            "label": "Section label",
            "field_order": [
              "label",
              "location",
              "131212",
              "tags",
              "description"
            ]
          }]
        }
      }
    }]
}
```

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.


### `read`

Gets entity by the ID or by type.

#### Parameters

| name | description                                       | type   |
|:-----|:--------------------------------------------------|:-------|
| id   | ID of an entity.                                  | int    |
| type | Type of an entity. Entity type string, see above. | string |

!!! note "Exactly one of these parameters must be specified. They can't be both null or both non-null."

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 131312}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/entity/read?hash=a6aa75587e5c59c32d347da438505fc3&id=131312
    ```

#### Response

```json
{
    "success": true,
    "entity": {
        "id": 123,
        "type": "place",
        "settings": {
            "layout": {
                    "sections": [{
                        "label": "Section label",
                        "field_order": [
                          "label",
                          "location",
                          "131212",
                          "tags",
                          "description"
                        ]
                    }]
            }
        }
    }, 
    "fields": [{
       "id": 131312,
       "label": "Additional info", 
       "type":  "text",
       "required": true,
       "description": "Info about place"
    }]
}
```

* `fields` - array of objects. Fields associated with this entity. Described in [field object](fields.md#field-object).

#### Errors

* 201 - Not found in the database – if there is no entity with such ID.


### `update`

Updates settings of customizable entity. Entity must have a valid ID.

**required sub-user rights**: `places_custom_fields_update` for entities with type `place`.

!!! warning "`entity.settings.layout.sections` must contain IDs of all builtin and custom fields which are associated with this entity. No fields can be omitted from layout, only reordering allowed. Fields cannot be duplicated, even in different sections."

#### Parameters

| name   | description                               | type        |
|:-------|:------------------------------------------|:------------|
| entity | Entity object with valid ID and settings. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "entity": {"id": 123, "type": "place", "settings": {"layout": {"sections": [{"label": "Section label", "field_order": ["label", "location", "131212", "tags", "description"]}]}}}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 - Not found in the database – if there is no entity with such ID.
* 7 - Invalid parameters - if entity object violates restrictions described above.