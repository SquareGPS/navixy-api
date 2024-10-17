---
title: Form templates
description: Form is an one-shot entity; after it was filled by someone, it cannot be reused. It's stored along with filled fields for future reference. Usually people need to fill forms with the same fields over an over again, so forms created on the basis of form templates. It's similar to paper forms - each paper form can be filled only once, but there's an electronic document, a template, on basis of which all paper forms printed.
---

# Form templates

Form is a "one-shot" entity; after it was filled by someone, it cannot be reused. It's stored along with filled fields 
for future reference. Usually people need to fill forms with the same fields over an over again, so forms created on 
the basis of form templates. It's similar to paper forms: each paper form can be filled only once, but there's an 
electronic document, a template, on basis of which all paper forms printed.  
 
The reason for such API design is that template fields can be changed over time (deleted, removed, reordered, etc.)  
and it should not affect already filled forms. By separating filled forms and templates, one can always view filled form 
in exactly same state regardless of how template changed.
 
User can assign form to the task or checkin by choosing template without the need to create all form fields every time.


## Form template object

```json
{
  "id": 1,
  "label": "Order form",
  "fields":[{
     "id": "Text-1",
     "label": "Name", 
     "description": "Your full name",
     "required": true, 
     "type": "text", 
     "min_length": 5, 
     "max_length": 255
  }],
  "created": "2017-03-15 12:36:27",
  "submit_in_zone": true,
  "updated": "2017-03-16 15:22:53",
  "default": false
}
```

* `id` - int. An ID of a template.
* `label` - string. User-defined template label, from 1 to 100 characters.
* `fields` - array of multiple [form_field](field-types.md) objects.
* `created` - [date/time](../../../getting-started/introduction.md#data-types). Date when this template created. The read-only field.
* `submit_in_zone` - boolean. If `true`, form can be submitted only in task zone.
* `updated` - [date/time](../../../getting-started/introduction.md#data-types). Date when this template last modified. The read-only field.
* `default` - boolean. This form will be chosen default for all new tasks with form if `true`.


## API actions

API path: `/form/template`.

### `list`

Gets all form templates belonging to current master user.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/template/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/form/template/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list":[{
      "id": 1,
      "label": "Order form",
        "fields":[{
           "id": "Text-1",
           "label": "Name", 
           "description": "Your full name",
           "required": true, 
           "type": "text", 
           "min_length": 5, 
           "max_length": 255
        }],
      "created": "2017-03-15 12:36:27",
      "submit_in_zone": true,
      "updated": "2017-03-16 15:22:53",
      "default": false
    }]
}
```

* `list` - ordered array of [form_template objects](#form-template-object).

#### Errors

[General](../../../getting-started/errors.md#error-codes) types only.


### `create`

Creates new form template.

**required sub-user rights**: `form_template_update`.

#### Parameters

| name     | description                                                              | type        |
|:---------|:-------------------------------------------------------------------------|:------------|
| template | Non-null form template object without `id`, `created`, `updated` fields. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/template/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "template": {"label": "Order form", "fields": [{"id": "Text-1", "label": "Name", "description": "Your full name", "required": true, "type": "text", "min_length": 5, "max_length": 255}], "submit_in_zone": true, "default": false}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An ID of the created form template.

#### Errors

* 101 – In demo mode this function disabled - if current user has "demo" flag.


### `read`

Gets form template belonging to current master user by specified ID.

#### Parameters

| name        | description              | type |
|:------------|:-------------------------|:-----|
| template_id | ID of the form template. | int  |


#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/template/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "template_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/form/template/read?hash=a6aa75587e5c59c32d347da438505fc3&template_id=111
    ```

#### Response

```json
{
    "success": true,
    "list":[{
      "id": 1,
      "label": "Order form",
      "fields": [{
        "id": "Text-1",
        "label": "Name", 
        "description": "Your full name",
        "required": true, 
        "type": "text", 
        "min_length": 5, 
        "max_length": 255
      }],
      "created": "2017-03-15 12:36:27",
      "submit_in_zone": true,
      "updated": "2017-03-16 15:22:53",
      "default": false
    }]
}
```

* `list` - ordered array of [form_template objects](#form-template-object).

#### Errors

* 201 – Not found in the database - if there is no template with such an ID.


### `update`

Updates existing form template.

**required sub-user rights**: `form_template_update`.

#### Parameters

| name     | description                                                        | type        |
|:---------|:-------------------------------------------------------------------|:------------|
| template | Non-null form template object without `created`, `updated` fields. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/template/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "template": {"id": 111, label": "Order form", "fields": [{"id": "Text-1", "label": "Name", "description": "Your full name", "required": true, "type": "text", "min_length": 5, "max_length": 255}], "submit_in_zone": true, "default": false}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if template with the specified ID does not exist.
* 101 – In demo mode this function disabled - if current user has "demo" flag.


### `delete`

Deletes form template.

**required sub-user rights**: `form_template_update`.

#### Parameters

| name        | description              | type |
|:------------|:-------------------------|:-----|
| template_id | ID of the form template. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/template/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "template_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/form/template/delete?hash=a6aa75587e5c59c32d347da438505fc3&template_id=111
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if template with the specified ID does not exist.
* 101 – In demo mode this function disabled - if current user has "demo" flag.


### `stats/read`

Returns template usage statistics.

**required sub-user rights**: none.

#### Parameters

| name        | description              | type |
|:------------|:-------------------------|:-----|
| template_id | ID of the form template. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/template/stats/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "template_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/form/template/stats/read?hash=a6aa75587e5c59c32d347da438505fc3&template_id=111
    ```

#### Response

```json
{
  "success": true,
  "tasks": {
    "unassigned": 0,
    "assigned": 6,
    "done": 0,
    "failed": 0,
    "delayed": 9,
    "arrived": 0,
    "faulty": 0
  },
  "scheduled": 2
}
```

* `tasks` - maps task status to number of tasks with this status which use specified template.
* `scheduled` - int. Number of task schedules using this template.

#### Errors

* 201 – Not found in the database - if template with the specified ID does not exist.
