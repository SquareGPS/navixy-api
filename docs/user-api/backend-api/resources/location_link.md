---
title: Geo Links
description: API calls for working with Geo Links. These are special sessions to share the location of mobile objects.
---

# Geo Links

API calls for working with Geo Links. These are special sessions to share the location of mobile objects.
This is a new API replacing Weblocator.


## API actions

API path: `/tracker/location/link`.

### `create`

Creates new Geo Link. There may be up to 10000 geo-links per user account.

**required sub-user rights**: `weblocator_session_create`.

#### Parameters

| name        | description                                           | type                  | restrictions                                |
|:------------|:------------------------------------------------------|:----------------------|---------------------------------------------|
| lifetime    | Start and end of the session.                         | JSON object           | Optional.                                   |
| description | Link's description.                                   | string                | Only printable characters. Max length: 255. |
| trackers    | List of tracker IDs with parameters for each tracker. | array of JSON objects | Allowed length 1 to 100.                    |
| params      | Link parameters.                                      | JSON object           |                                             |

##### lifetime object
```js
{
  "from": "2024-01-29 01:00:00", // optional
  "to": "2024-01-30 01:00:00" // optional
}
```

##### tracker object
```js
{
  "alias": "John Doe", // optional
  "tracker_id": 14,
  "params": {
    "object_data": ["speed", "address"] // speed, address, movement_status, connection_status, driver_name, driver_phone, vehicle_label, vehicle_reg_number
  }
}
```

##### params object
```js
{
  "bounding_zone_ids": [123,...], // 0..100 zone IDs
  "bounding_mode": "inside", // or outside, optional when no bounding zones
  "place_ids": [234,...], // 0..100 place IDs
  "shorten_url": false, // optional, false by default
  "display_options": {
    "map": "roadmap", // or satellite, hybrid, or any other available map
    "autoscale": false, // optional, true by default
    "show_icons": false, // optional, false by default
    "show_driver_info": false, // optional, false by default
    "show_vehicle_info": false, // optional, false by default
    "trace_duration": 30 // in seconds, optional, 5 by default
  }
}
```

#### Example

=== "cURL"

    ```bash
    curl -X POST "{{ extra.api_example_url }}/tracker/location/link/create" \
        -H "Content-Type: application/json" \
        --data-binary @- << EOF
    {
      "hash": "a6aa75587e5c59c32d347da438505fc3",
      "lifetime": {
        "from": "2024-01-29 01:00:00",
        "to": "2024-01-30 01:00:00"
      },
      "description": "One tracker link",
      "trackers": [
        {
          "alias": "John Doe",
          "tracker_id": 14,
          "params": {
            "object_data": ["speed", "address"]
          }
        }
      ],
      "params": {
        "bounding_zone_ids": [123, 234],
        "bounding_mode": "inside",
        "place_ids": [987, 654],
        "display_options": {
          "map": "roadmap",
          "autoscale": false,
          "show_icons": false,
          "show_driver_info": false,
          "show_vehicle_info": false,
          "trace_duration": 30
        }
      }
    }
    EOF
    ```

#### Response

```json
{
  "success": true,
  "value": 104
}
```

#### Errors

* 13 – Operation not permitted – if a user has insufficient rights.
* 204 – Entity not found – if one or more of zones or places are not found.
* 217 – List contains nonexistent entities – if one or more of tracker IDs belong to nonexistent tracker (or to a tracker belonging to different user).
* 236 – Feature unavailable due to tariff restrictions – if there is at least one tracker without `weblocator` tariff feature.
* 268 – Link cannot be created due to quota violation.

### `update`

Updates Geo Link.

#### Parameters

| name        | description                                           | type                  | restrictions                                |
|:------------|:------------------------------------------------------|:----------------------|---------------------------------------------|
| id          | Session ID.                                           | int                   |                                             |
| lifetime    | Optional. Start and end of the session.               | JSON object           | Optional.                                   |
| description | Link's description.                                   | string                | Only printable characters. Max length: 255. |
| trackers    | List of tracker IDs with parameters for each tracker. | array of JSON objects | Allowed length 1 to 100.                    |
| params      | Link parameters.                                      | JSON object           |                                             |

#### Example

=== "cURL"

    ```bash
    curl -X POST "{{ extra.api_example_url }}/tracker/location/link/update" \
        -H "Content-Type: application/json" \
        --data-binary @- << EOF
    {
      "hash": "a6aa75587e5c59c32d347da438505fc3",
      "id": 104,
      "lifetime": {
        "from": "2024-01-29 01:00:00",
        "to": "2024-01-30 01:00:00"
      },
      "description": "One tracker link",
      "trackers": [
        {
          "alias": "John Doe",
          "tracker_id": 14,
          "params": {
            "object_data": ["speed", "address"]
          }
        }
      ],
      "params": {
        "bounding_zone_ids": [123, 456],
        "bounding_mode": "inside",
        "place_ids": [987, 654],
        "shorten_url": false,
        "display_options": {
          "map": "roadmap",
          "autoscale": false,
          "show_icons": false,
          "show_driver_info": false,
          "show_vehicle_info": false,
          "trace_duration": 30
        }
      }
    }
    EOF
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 13 – Operation not permitted – if a user has insufficient rights.
* 201 – Not found in the database – if link with such an ID does not exist or does not belong to current user.
* 204 – Entity not found – if one or more of zones or places are not found.
* 217 – List contains nonexistent entities – if one or more of tracker IDs belong to nonexistent tracker (or to a tracker belonging to different user).
* 236 – Feature unavailable due to tariff restrictions – if there is at least one tracker without `weblocator` tariff feature.

### `status/change`

Lets to activate and deactivate a link.

#### Parameters

| name      | description                       | type    |
|:----------|:----------------------------------|:--------|
| id        | Session ID.                       | int     |
| is_active | If `false`, a link is deactivated | boolean |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/location/link/status/change' \
        -H 'Content-Type: application/json' \
        -d '{"hash":"a6aa75587e5c59c32d347da438505fc3","id":104,"is_active":false}'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database – if link with such an ID does not exist or does not belong to current user.

### `read`

Returns a link with a specified ID.

#### Parameters

| name | description  | type |
|:-----|:-------------|:-----|
| id   | Session ID.  | int  |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/location/link/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash":"a6aa75587e5c59c32d347da438505fc3","id":103}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/location/link/read?hash=a6aa75587e5c59c32d347da438505fc3&id=103
    ```

#### Response

```json
{
  "success": true,
  "value": {
    "create_date": "2024-01-29 03:00:00",
    "creator_id": 3,
    "description": "Another one tracker",
    "enabled": true,
    "hash": "700d4a5400000000600d4a5400000103",
    "id": 103,
    "lifetime": {
      "from": "2024-01-30 00:00:00",
      "to": "2024-01-30 03:00:00"
    },
    "params": {
      "bounding_mode": "outside",
      "bounding_zone_ids": [
        51
      ],
      "display_options": {
        "autoscale": false,
        "map": "osm",
        "show_driver_info": false,
        "show_icons": false,
        "show_vehicle_info": false,
        "trace_duration": 0
      },
      "place_ids": null
    },
    "trackers": [
      {
        "alias": "Jane Doe",
        "params": {
          "object_data": []
        },
        "tracker_id": 15
      }
    ]
  }
}
```

#### Errors

* 201 – Not found in the database – if link with such an ID does not exist or does not belong to current user.

### `list`

Returns a list of a user's links.

#### Parameters

| name       | description                                                                                                                                                                 | type             |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| filter     | Optional. Filter for all fields. If used with conditions, both filter and conditions must match for every returned links.                                                   | string           |
| conditions | Optional. Search conditions to apply to list. Array of search conditions, see [Search conditions](commons/entity/search_conditions.md). Possible fields listed below. | array of objects |
| offset     | Optional. Offset, default is 0.                                                                                                                                             | int              |
| limit      | Optional. Limit, default is 10,000.                                                                                                                                         | int              |
| sort       | Optional. Each option is a pair of field name and sorting direction, e.g. `["creator=asc", "id=desc"]`. Possible fields listed below.                                       | string array     |

##### condition fields

* `trackers` – labels of all trackers
* `aliases` – aliases of all trackers
* `creator` – full name of creator (only for master user)
* `description`

##### sort fields

* `id`
* `create_date`
* `expire_date`
* `trackers` – labels of all trackers
* `aliases` – aliases of all trackers
* `status` – enabled < inactive < expired < disabled
* `creator` – full name of creator (only for master user)
* `description`
* If no `sort` param is specified, then `sort` option will be "id=asc".

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/location/link/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "offset": 0, "limit": 1000}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/location/link/list?hash=a6aa75587e5c59c32d347da438505fc3&offset=0&limit=1000
    ```

#### Response

```json
{
  "success": true,
  "list": [
    {
      "create_date": "2024-01-29 03:00:00",
      "creator_id": 3,
      "description": "Another one tracker",
      "enabled": true,
      "hash": "700d4a5400000000600d4a5400000103",
      "id": 103,
      "lifetime": {
        "from": "2024-01-30 00:00:00",
        "to": "2024-01-30 03:00:00"
      },
      "params": {
        "bounding_mode": "outside",
        "bounding_zone_ids": [51],
        "display_options": {
          "autoscale": false,
          "map": "osm",
          "show_driver_info": false,
          "show_icons": false,
          "show_vehicle_info": false,
          "trace_duration": 0
        },
        "place_ids": null
      },
      "trackers": [
        {
          "alias": "Jane Doe",
          "params": {
            "object_data": []
          },
          "tracker_id": 15
        }
      ]
    }
  ]
}
```

### `delete`

Deletes a link with a specified ID.

#### Parameters

| name | description  | type |
|:-----|:-------------|:-----|
| id   | Session ID.  | int  |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/location/link/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "id": 103}'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database – if link with such an ID does not exist or does not belong to current user.
