---
title: Tag
description: Information about the tag object and the API calls used to interact with it.
---

# Tag

A tag is a label or keyword used for quick and easy searches. Tags help locate places, geofences, employees, tasks, trackers, and vehicles.&#x20;

For more details on using the tags API, refer to our [how-to guide](../../../guides/fleet-management/use-tags.md).

## Tag object

```json
{
  "id": 3,
  "avatar_file_name": "avatar.jpg",
  "name": "hop",
  "color": "FF0000"
}
```

* `id` - int. Tag ID.
* `avatar_file_name` - optional string. File name with extension.
* `name` - string. Tag's name.
* `color` - string. Tag color in 3-byte RGB hex format.

#### tagged entity types

* place
* task
* task\_schedule
* employee
* vehicle
* zone
* tracker

## API actions

API path: `/tag`.

### create

Creates a new tag.

**required sub-user rights**: `tag_update`.

#### Parameters

| name | description                    | type        |
| ---- | ------------------------------ | ----------- |
| tag  | Tag object without `id` field. | JSON object |

#### Examples

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tag/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag": {"name": "hop", "color": "FF0000"}}'
```
{% endcode %}
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
https://api.eu.navixy.com/v2/tag/create?hash=a6aa75587e5c59c32d347da438505fc3&tag={"name": "hop", "color": "FF0000"}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true,
  "id": 111
}
```

* `id` - int. An ID of the created tag.

#### Errors

[General](../../../errors.md#error-codes) types only.

### delete

Deletes tag with the specified ID.

**required sub-user rights**: `tag_update`.

#### Parameters

To delete tags, only one of the following parameters must be specified.

| name     | description                    | type      |
| -------- | ------------------------------ | --------- |
| tag\_id  | ID of the tag to delete.       | int       |
| tag\_ids | An array of tag IDs to delete. | int array |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tag/delete' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag_id": 1}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
https://api.eu.navixy.com/v2/tag/delete?hash=a6aa75587e5c59c32d347da438505fc3&tag_id=1
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no tag with such an ID. This error will not occur if the tag\_ids parameter is specified, deletion is silent in this case.

### list

Gets all tags belonging to user with optional filtering.

#### Parameters

| name   | description                                            | type   |
| ------ | ------------------------------------------------------ | ------ |
| filter | Optional filter for tag name. 3-60 characters or null. | string |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tag/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
```http
https://api.eu.navixy.com/v2/tag/list?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 3,
      "avatar_file_name": "avatar.jpg",
      "name": "hop",
      "color": "FF0000"
    }
  ]
}
```

#### Errors

[General](../../../errors.md#error-codes) types only.

### search

Search entities that bound with all of specified tags.

#### Parameters

| name          | description                                                      | type         |
| ------------- | ---------------------------------------------------------------- | ------------ |
| tag\_ids      | List of tag IDs to search.                                       | int array    |
| entity\_types | Optional. List of [tagged entity types](index.md#tag) to filter. | string array |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tag/search' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag_ids": [1, 2, 3]}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
https://api.eu.navixy.com/v2/tag/search?hash=a6aa75587e5c59c32d347da438505fc3&tag_ids=[1, 2, 3]
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true,
  "result": {
    "place": [<place>],
    "task": [<task>],
    "task_schedule": [<task_schedule>],
    "employee": [<employee>],
    "vehicle": [<vehicle>],
    "zone": [<zone>],
    "tracker": [<tracker>]
  }
}
```

* `place` - array of objects. List of place objects.
* `task` - array of objects. List of task objects.
* `task_schedule` - array of objects. List of task\_schedule objects.
* `employee` - array of objects. List of employee objects.
* `vehicle` - array of objects. List of vehicle objects.
* `zone` - array of objects. List of zone objects.
* `tracker` - array of objects. List of tracker objects.

#### Errors

[General](../../../errors.md#error-codes) types only.

### update

Updates existing tag.

**required sub-user rights**: `tag_update`.

#### Parameters

| name | description                 | type        |
| ---- | --------------------------- | ----------- |
| tag  | Tag object with `id` field. | JSON object |

#### Examples

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tag/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag": {"id": 3, "name": "hop", "color": "FF0000"}}'
```
{% endcode %}
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
https://api.eu.navixy.com/v2/tag/update?hash=a6aa75587e5c59c32d347da438505fc3&tag={"id": 3, "name": "hop", "color": "FF0000"}'
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no tag with such an ID.
