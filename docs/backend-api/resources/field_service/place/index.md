---
title: Working with places
description: Working with places
---

# Working with places

"Places" are business-specific points of interest like shops, delivery points, warehouses, etc - which are visited 
by user's employees. Place entities can be extended with [custom fields](../../commons/entity/fields.md) to make them 
even more useful. 

In case an event happened at the place, in various reports name of the place will be specified after the address.

If there's an [employee](../employee) assigned to a Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)),
and a place has a custom field of type "responsible employee", such place will be available in the mobile app to view.
Thus, field employee can view all places assigned to him to visit them, etc.

### Place object

```json
{
    "id": 1,
    "icon_id" : 55,
    "avatar_file_name": null,
    "location": {
        "lat": 52.366,
        "lng": 4.895,
        "address": "730 5th Ave, New York, NY 10019, Unites States",
        "radius": 500
    },
   "fields": {
        "131312" : {
             "type": "text",
             "value":  "I love text!"
        }
   },
    "label": "Crown Building",
    "description": "Here we buy our goods",
    "tags": [ 1, 2 ],
    "external_id": "1"
}
```   

* `id` - int. An id of a place.
* `icon_id` - optional int. Can be 1 to 255. Can only be updated via [avatar/assign](./avatar.md).
* `avatar_file_name` - optional string. Name of the avatar file. Can be null.
* `fields` - optional object. A map, each key of which is a custom field id *as a string*. See [entity/fields](../../commons/entity/fields.md)
* `label` - string. The name of the place.
* `description` - optional string. Description of the place.
* `tags` - optional array of int. A list of tag_ids. Non-empty.
* `external_id` - optional string. Max length 32.

## API actions

API base path: `/place`.

### read

Gets place by ID.

#### parameters

|name |description |type |
|:--- |:--- |:--- |
|place_id |ID of the place. |int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place_id": 122304}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/place/read?hash=a6aa75587e5c59c32d347da438505fc3&place_id=122304
    ```

#### response

```json
{
    "success": true,
    "value": {
         "id": 1,
         "icon_id" : 55,
         "avatar_file_name": null,
         "location": {
              "lat": 40.773998,
              "lng": -73.66003,
             "address": "730 5th Ave, New York, NY 10019, Unites States",
             "radius": 50
         },
        "fields": {
             "131312" : {
                  "type": "text",
                  "value":  "I love text!"
             }
        }
         "label": "Crown Building",
         "description": "Here we buy our goods",
         "tags": [ 1, 2 ],
         "external_id": "1"
    }
}
```

#### errors

* 201 (Not found in the database) – if there is no place with such ID.

### list

Get places belonging to user.

#### parameters

|name |description |type |
|:--- |:--- |:--- |
| place_ids | Optional. List of place IDs. | array of int |
| filter | Optional. Filter for all built-in and custom fields. If used with conditions, both filter and conditions must match for every returned place. | string |
| conditions | Optional. Search conditions to apply to list. Array of search conditions, see [Search conditions](../../commons/entity/search_conditions.md). | array of objects |
| order_by | Optional. Built-in or custom field according to which output should be sorted. Entity field name, e.g "label" (builtin) or "123" (field id as string, see [entity/](../../commons/entity/index.md). | string |
| ascending | Optional. If `false` – descending order. | boolean |
| limit | Optional. Limit. | int |
| offset | Optional. offset, default is 0. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/place/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```
#### response

```json
{
    "success": true,
    "list": [{
          "id": 1,
          "icon_id" : 55,
          "avatar_file_name": null,
          "location": {
              "lat": 40.773998,
              "lng": -73.66003,
              "address": "730 5th Ave, New York, NY 10019, Unites States",
              "radius": 50
          },
         "fields": {
              "131312" : {
                   "type": "text",
                   "value":  "I love text!"
              }
         },
          "label": "Crown Building",
          "description": "Here we buy our goods",
          "tags": [ 1, 2 ],
          "external_id": "1"
    }],
    "count": 1
}
```

* `count` - int. Found places count.

#### errors

[General](../../../getting-started.md#error-codes) types only.

### create

Creates new place.

**required sub-user rights:** `place_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| place | A place object without `id` field. | JSON object |
| ignore_missing_fields | Optional (default is false). If `true`, place can be created even without all required custom fields. | boolean |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place": {"icon_id" : 55, "avatar_file_name": null, "location": {"lat": 40.773998, "lng": -73.66003, "address": "730 5th Ave, New York, NY 10019, Unites States", "radius": 50}, "fields": {"131312": {"type": "text", "value": "I love text!"}} "label": "Crown Building", "description": "Here we buy our goods", "tags": [1, 2], "external_id": "1"}'
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An ID of the created place.

#### errors

* 268 (Over quota) – if the user's quota for places exceeded.

### update

Updates existing place.

**required sub-user rights:** `place_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| place | A place object. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place": {"id": 111, "icon_id" : 55, "avatar_file_name": null, "location": {"lat": 40.773998, "lng": -73.66003, "address": "730 5th Ave, New York, NY 10019, Unites States", "radius": 50}, "fields": {"131312": {"type": "text", "value": "I love text!"}} "label": "Crown Building", "description": "Here we buy our goods", "tags": [1, 2], "external_id": "1"}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if there is no place with such ID.

### delete

Deletes place with the specified ID.

**required sub-user rights:** `place_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| place_id | ID of the place to delete. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place_id": 122304}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/place/delete?hash=a6aa75587e5c59c32d347da438505fc3&place_id=122304
    ```

#### response
```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if there is no place with such ID.

### batch_convert

Converts batch of tab-delimited places and return list of checked places with errors.

**Required sub-user rights:** `place_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| batch | Batch of tab-delimited places. | string |
| file_id | Preloaded file ID. | string |
| fields | Optional. Array of field names, default is `["label", "address", "lat", "lng", "radius", "description", "tags"]`. | array of strings |
| geocoder | Geocoder type. | string |
| default_radius | Optional. Radius for point in meters. Default is 100. | int |

If `file_id` is set – `batch` parameter will be ignored.

#### response

```json
{
    "success": true,
    "list": [{
           "id": 1,
           "icon_id" : 55,
           "avatar_file_name": null,
           "location": {
               "lat": 40.773998,
               "lng": -73.66003,
               "address": "730 5th Ave, New York, NY 10019, Unites States",
               "radius": 50
           },
          "fields": {
               "131312" : {
                    "type": "text",
                    "value":  "I love text!"
               }
          }
           "label": "Crown Building",
           "description": "Here we buy our goods",
           "tags": [ 1, 2 ],
           "external_id": "1"
           "errors": <array_of_objects>,
           "tag_names": <array_of_strings>
    }],
    "limit_exceeded": false
}
```

* `list` - a list of <checked_place> objects.
    * `errors` - optional array of objects. Errors found during check.
    * `tag_names` - optional array of strings. Tag names of the place.
* `limit_exceeded` - boolean. `true` if given batch constrained by a limit.

#### errors

* 234 (Invalid data format).

### upload

Upload places.

**Required sub-user rights**: `place_update`.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a CSV file upload (with the name "file").

CSV column separator is `;`, columns header required – `label;address;lat;lng;radius;external_id;description`

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| file | A CSV file upload containing places data. | File upload |
| error_policy| ignore or fail | string |
| duplicate_policy | skip or update or fail, **belongs only to external_id duplicates** | string |
| default_radius | Optional, radius for point, meters, default is 100. | int |
| geocoder | Geocoder type. | string |
| redirect_target | Optional URL to redirect. If `redirect_target` passed return redirect to `<redirect_target>?response=<urlencoded_response_json>`. | string |

#### response

```json
{
    "success": true,
    "total": 1,
    "errors": 0
}
```

#### errors

* 233 (No data file) – if file part is missing.
* 234 (Invalid data format).
* 247 (Entity already exists) – if uploaded place contains external_id and place with this ID already exists and duplicate_policy=fail.
* 268 (Over quota) – if the user's quota for places exceeded.
