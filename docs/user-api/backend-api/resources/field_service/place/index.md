---
title: Working with points of interest (POI)
description: Place object and API calls to work with points of interest (POI). "Places" are business-specific points of interest like shops, delivery points, warehouses, etc. - which are visited by user's employees and drivers.
---

# Working with points of interest (POI)

"Places" are business-specific points of interest (POI) like shops, delivery points, warehouses, etc. - which are visited 
by user's employees. Place entities can be extended with [custom fields](../../commons/entity/fields.md) to make them 
even more useful. 

In case an event happened at the POI, in various reports name of the POI will be specified after the address.

If there's an [employee](../employee) [assigned](../../tracking/tracker/employee.md#assign) to a Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)),
and a POI has a custom field of type "responsible employee", such point of interest will be available in the mobile app to view.
Thus, field employee/driver can view all points of interest assigned to him to visit them, etc.

Working with POIs requires several actions so we described them in our [guides](../../../guides/places/manage-pois.md).


## Place object

```json
{
  "id": 1,
  "icon_id": 55,
  "avatar_file_name": null,
  "location": {
    "lat": 52.366,
    "lng": 4.895,
    "address": "730 5th Ave, New York, NY 10019, Unites States",
    "radius": 500
  },
  "fields": {
    "131312": {
      "type": "text",
      "value": "I love text!"
    }
  },
  "label": "Crown Building",
  "description": "Here we buy our goods",
  "tags": [ 1, 2 ],
  "external_id": "1"
}
```   

* `id` - int. An ID of a POI.
* `icon_id` - optional int. Can be 1 to 255. Can only be updated via [avatar/assign](avatar.md).
* `avatar_file_name` - optional string. Name of the avatar file. Can be null.
* `location` - required information about place location.
    * `lat` - required, float. The latitude. 
    * `lng` - required, float. The longitude.
    * `address` - required, string, max length 255. The address of place.
    * `radius` - required, int, 1..300000. The radius of place in meters.
* `fields` - optional object. A map, each key of which is a custom field ID *as a string*. See [entity/fields](../../commons/entity/fields.md)
* `label` - string. POI name.
* `description` - optional string. POI description.
* `tags` - optional int array. A list of tag_ids. Non-empty.
* `external_id` - optional string. Max length 32.


## API actions

API path: `/place`.

### `read`

Gets POI by ID.

#### Parameters

| name     | description    | type |
|:---------|:---------------|:-----|
| place_id | ID of the POI. | int  |

#### Examples

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

#### Response

```json
{
  "success": true,
  "value": {
    "id": 1,
    "icon_id": 55,
    "avatar_file_name": null,
    "location": {
      "lat": 40.773998,
      "lng": -73.66003,
      "address": "730 5th Ave, New York, NY 10019, Unites States",
      "radius": 50
    },
    "fields": {
      "131312": {
        "type": "text",
        "value": "I love text!"
      }
    },
    "label": "Crown Building",
    "description": "Here we buy our goods",
    "tags": [ 1, 2 ],
    "external_id": "1"
  }
}
```

#### Errors

* 201 - Not found in the database – if there is no POI with such ID.


### `list`

Get POIs belonging to user.

#### Parameters

| name       | description                                                                                                                                                                                         | type             |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| place_ids  | Optional. List of POI IDs.                                                                                                                                                                          | int array        |
| filter     | Optional. Filter for all built-in and custom fields. If used with conditions, both filter and conditions must match for every returned POI.                                                         | string           |
| conditions | Optional. Search conditions to apply to list. Array of search conditions, see [Search conditions](../../commons/entity/search_conditions.md).                                                       | array of objects |
| order_by   | Optional. Built-in or custom field according to which output should be sorted. Entity field name, e.g "label" (builtin) or "123" (field ID as string, see [entity/](../../commons/entity/index.md). | string           |
| ascending  | Optional. If `false` – descending order.                                                                                                                                                            | boolean          |
| limit      | Optional. Limit.                                                                                                                                                                                    | int              |
| offset     | Optional. offset, default is 0.                                                                                                                                                                     | int              |
| tag_ids    | Optional. Tag IDs assigned to the place. The places found must include all the tags from the list.                                                                                                  | int array        |

#### Examples

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

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 1,
      "icon_id": 55,
      "avatar_file_name": null,
      "location": {
        "lat": 40.773998,
        "lng": -73.66003,
        "address": "730 5th Ave, New York, NY 10019, Unites States",
        "radius": 50
      },
      "fields": {
        "131312": {
          "type": "text",
          "value": "I love text!"
        }
      },
      "label": "Crown Building",
      "description": "Here we buy our goods",
      "tags": [ 1, 2 ],
      "external_id": "1"
    }
  ],
  "count": 1
}
```

* `count` - int. Found POIs count.

#### Errors

[General](../../../getting-started/errors.md#error-codes) types only.


### `create`

Creates a new POI.

**required sub-user rights:** `place_update`.

#### Parameters

| name                  | description                                                                                         | type        |
|:----------------------|:----------------------------------------------------------------------------------------------------|:------------|
| place                 | A place object without `id` field.                                                                  | JSON object |
| ignore_missing_fields | Optional (default is false). If `true`, POI can be created even without all required custom fields. | boolean     |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place": {"icon_id" : 55, "avatar_file_name": null, "location": {"lat": 40.773998, "lng": -73.66003, "address": "730 5th Ave, New York, NY 10019, Unites States", "radius": 50}, "fields": {"131312": {"type": "text", "value": "I love text!"}}, "label": "Crown Building", "description": "Here we buy our goods", "tags": [1, 2], "external_id": "1"}'
    ```

#### Response

```json
{
  "success": true,
  "id": 111
}
```

* `id` - int. An ID of the created POI.

#### Errors

* 268 - Over quota – if the user's quota for POIs exceeded.


### `search_location`

Gets all POI IDs and names within which a specified coordinates are located inside.

#### Parameters

| name     | description                                                                                                   | type        |
|:---------|:--------------------------------------------------------------------------------------------------------------|:------------|
| location | Location coordinates (see: [data types description section](../../../getting-started/introduction.md#data-types) section). | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/search_location' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "location": {"lat": 34.178868, "lng": -118.599672}}'
    ```

#### Response

```json
{
  "list": [
    {
      "id": 1201,
      "label": "place 1"
    },
    {
      "id": 3574,
      "label": "place 2"
    }
  ],
  "success": true
}
```

* `id` - int. Place ID that containing a searched location.
* `label` - string. Place name.


### `update`

Updates existing POI.

**required sub-user rights:** `place_update`.

#### Parameters

| name  | description     | type        |
|:------|:----------------|:------------|
| place | A place object. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place": {"id": 111, "icon_id" : 55, "avatar_file_name": null, "location": {"lat": 40.773998, "lng": -73.66003, "address": "730 5th Ave, New York, NY 10019, Unites States", "radius": 50}, "fields": {"131312": {"type": "text", "value": "I love text!"}}, "label": "Crown Building", "description": "Here we buy our goods", "tags": [1, 2], "external_id": "1"}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if there is no POI with such ID.


### `delete`

Deletes POI with the specified ID.

**required sub-user rights:** `place_update`.

#### Parameters

| name     | description              | type |
|:---------|:-------------------------|:-----|
| place_id | ID of the POI to delete. | int  |

#### Examples

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

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if there is no POI with such ID.


### `batch_convert`

Converts batch of tab-delimited POIs and return list of checked POIs with errors.

**Required sub-user rights:** `place_update`.

#### Parameters

| name           | description                                                                                                       | type         |
|:---------------|:------------------------------------------------------------------------------------------------------------------|:-------------|
| batch          | Batch of tab-delimited POIs.                                                                                      | string       |
| file_id        | Preloaded file ID.                                                                                                | string       |
| fields         | Optional. Array of field names, default is `["label", "address", "lat", "lng", "radius", "description", "tags"]`. | string array |
| geocoder       | Geocoder type.                                                                                                    | string       |
| default_radius | Optional. Radius for point in meters. Default is 100.                                                             | int          |

If `file_id` is set – `batch` parameter will be ignored.

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 1,
      "icon_id": 55,
      "avatar_file_name": null,
      "location": {
        "lat": 40.773998,
        "lng": -73.66003,
        "address": "730 5th Ave, New York, NY 10019, Unites States",
        "radius": 50
      },
      "fields": {
        "131312": {
          "type": "text",
          "value": "I love text!"
        }
      },
      "label": "Crown Building",
      "description": "Here we buy our goods",
      "tags": [ 1, 2 ],
      "external_id": "1",
      "errors": <array_of_objects>,
      "tag_names": <array_of_strings>
    }
  ],
  "limit_exceeded": false
}
```

* `list` - a list of <checked_place> objects.
    * `errors` - optional array of objects. Errors found during check.
    * `tag_names` - optional string array. Tag names of the POI.
* `limit_exceeded` - boolean. `true` if given batch constrained by a limit.

#### Errors

* 234 - Invalid data format.


### `upload`

Upload POIs.

**Required sub-user rights**: `place_update`.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a CSV file upload (with the name "file").

CSV column separator is `;`, columns header required – `label;address;lat;lng;radius;external_id;description`.

#### Parameters

| name             | description                                                                                                                       | type        |
|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------|:------------|
| file             | A CSV file upload containing POIs data.                                                                                           | File upload |
| error_policy     | `ignore` or `fail`.                                                                                                               | string      |
| duplicate_policy | `skip` or `update` or `fail`, **belongs only to external_id duplicates**.                                                         | string      |
| default_radius   | Optional, radius for point, meters, default is 100.                                                                               | int         |
| geocoder         | Geocoder type.                                                                                                                    | string      |
| redirect_target  | Optional URL to redirect. If `redirect_target` passed return redirect to `<redirect_target>?response=<urlencoded_response_json>`. | string      |

#### Response

```json
{
  "success": true,
  "total": 1,
  "errors": 0
}
```

#### Errors

* 233 - No data file – if file part is missing.
* 234 - Invalid data format.
* 247 - Entity already exists – if uploaded POI contains `external_id` and POI with this ID already exists and `duplicate_policy=fail`.
* 268 - Over quota – if the user's quota for POIs exceeded.
