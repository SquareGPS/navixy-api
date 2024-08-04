---
title: Map layer
description: Contains map layer object structure and API calls to interact with it. 
---

# Map layer

Contains map layer object structure and API calls to interact with it.


## Map layer object structure:

```json
{
    "id": 123456,
    "label": "test"
}
```

* `id` - int. Map layer entity ID.
* `label` - string. Map layer name.


## API actions

API path: `/map_layer`.

### `read`

Reads the body of the specified layer.

#### Parameters

| name | description          | type | format |
|:-----|:---------------------|:-----|:-------|
| id   | ID of the map layer. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/map_layer/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/map_layer/read?hash=a6aa75587e5c59c32d347da438505fc3&id=123456
    ```


#### Response

Layer body with content-type: `application/vnd.google-earth.kml+xml; charset=utf-8`.

#### Errors

* 201 - Not found in the database – if there is no map layer with such ID belonging to current user.


### `list`

Returns metadata for all map layers for the user.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/map_layer/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/map_layer/listd?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
  "success": true,
  "list": [{
    "id": 123456,
    "label": "test"
  }]
}
```

#### Errors

No specific errors.


### `upload`

Uploads new map layer.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a KML file upload 
(with the name "file").

#### Parameters

| name            | description                                                                                                                         | type        |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------|:------------|
| label           | Label for a new map layer.                                                                                                          | string      |
| file            | A KML file upload containing map_layer data.                                                                                        | File upload |
| redirect_target | Optional. URL to redirect. If **redirect_target** passed return redirect to `<redirect_target>?response=<urlencoded_response_json>` | string      |

#### Response

```json
{
    "success": true,
    "id": 163
}
```

* `id` - int. ID of the created layer.

#### Errors

* 233 - No data file – if file part is missing.
* 234 - Invalid data format – if file has wrong mime type.
* 242 - Validation error – if uploaded file is not valid KML.
* 268 - Over quota – if the user's quota for map layers exceeded.


### `update`

Updates metadata for the specified map layer.

#### Parameters

| name  | description                                                    | type        |
|:------|:---------------------------------------------------------------|:------------|
| layer | Map layer object described [here](#map-layer-object-structure) | JSON object |

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if there is no map layer with such ID belonging to current user.


### `delete`

Deletes specified layer.

#### Parameters

| name | description          | type | format |
|:-----|:---------------------|:-----|:-------|
| id   | ID of the map layer. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/map_layer/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/map_layer/delete?hash=a6aa75587e5c59c32d347da438505fc3&id=123456
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if there is no map layer with such ID belonging to current user.
