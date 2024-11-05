---
title: Asset groups
description: Contains API calls to interact with asset groups.
---

# Asset groups

Contains API calls to interact with asset groups.


## Asset group entry
```json
{
  "id" : 64584,
  "name" : "group_1",
  "assets" : [<asset>]
}
```

* `id` - int. ID of the group.
* `name` - string. Name of the group.
* `assets` - list of Asset objects described [below](#asset-entry). Can be empty.


## Asset entry
```json
{
  "id" : 36558,
  "type" : "employee"
}
```

* `id` - int. ID of the asset.
* `type` - string. Type of the asset. Can be one of `employee`, `vehicle`.

## API actions

API path: `/asset_group`.

### `create`

Create new asset group.

#### Parameters

| name           | description                                                                                                                        | type                            |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| name           | Optional. If not set, defaults to the new entry ID. Name of the group.                                                             | string                          |
| assets         | Assets to include to group. Only one assets of each type is allowed.                                                               | array of [assets](#asset-entry) |
| force_reassign | Optional. Default is `false`. If `true`, assets will be reassigned to the created group even if they were assigned to another one. | boolean                         |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/asset_group/create' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "assets": [{"id": 36558, "type": "employee"}, {"id": 45685, "type": "vehicle"}]
    }'
    ```

#### Response

```json
{
  "id": 25684,
  "success": true
}
```

* `id` - int. ID of the group.

#### Errors

* 201 - Not found in the database - when there are no assets in the db.
* 285 - Asset already assigned to a group - if `force_reassign` is `false` and asset is already assigned to a group.

### `list`

List asset groups by ids.

#### Parameters

| name   | description       | type      |
|:-------|:------------------|:----------|
| groups | IDs of the groups | int array |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/asset_group/list' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "groups": [25684, 25685]
    }'
    ```

#### Response

```json
{
  "list": [<asset_group>],
  "success": true
}
```

* `list` - object array. Asset objects described [here](#asset-entry).

#### Errors

* 201 - Not found in the database - when there are no group in the db.


### `read`

Read asset group by asset.

#### Parameters

| name  | description        | type                         |
|:------|:-------------------|:-----------------------------|
| asset | Asset to search by | [asset object](#asset-entry) |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/asset_group/read' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "asset": {"id": 36558, "type": "employee"}
    }'
    ```

#### Response

```json
{
  "value": {<asset_group>},
  "success": true
}
```

* `value` - object. Asset object described [here](#asset-entry).

#### Errors

* 201 - Not found in the database - when there are no asset or no group with asset in the db.


### `set`

Set assets to existing group.

#### Parameters

| name           | description                                                                                                                       | type                            |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| id             | ID of the group.                                                                                                                  | int                             |
| assets         | Assets to set to group. Only one assets for each type is allowed.                                                                 | array of [assets](#asset-entry) |
| force_reassign | Optional. Default is `false`. If `true`, assets will be reassigned to the group even if they were assigned to another one.        | boolean                         |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/asset_group/set' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "id": 25684,
    "assets": [{"id": 36558, "type": "employee"}, {"id": 45685, "type": "vehicle"}]
    }'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 - Not found in the database - when there are no asset or no group with asset in the db.
* 285 - Asset already assigned to a group - if `force_reassign` is `false` and asset is already assigned to a group.


### `remove`

Remove assets from group.

#### Parameters

| name           | description                                                                                                                | type                            |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| id             | ID of the group.                                                                                                           | int                             |
| assets         | Assets to remove from group. Only one assets for each type is allowed.                                                     | array of [assets](#asset-entry) |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/asset_group/remove' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "id": 25684,
    "assets": [{"id": 36558, "type": "employee"}, {"id": 45685, "type": "vehicle"}]
    }'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 - Not found in the database - when there are no asset or no group with asset in the db.
* 286 - All Assets must be present in the group - if not all assets are present in the group.


### `update`

Update asset group name.

#### Parameters

| name | description        | type   |
|:-----|:-------------------|:-------|
| id   | ID of the group.   | int    |
| name | Name of the group. | string |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/asset_group/update' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "id": 25684,
    "name": "new_name"
    }'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 - Not found in the database - when there are no group in the db.


### `delete`

Delete asset group.

#### Parameters

| name | description        | type   |
|:-----|:-------------------|:-------|
| id   | ID of the group.   | int    |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/asset_group/delete' \
        -H 'Content-Type: application/json' \
        -d '{
    "hash":"59be129c1855e34ea9eb272b1e26ef1d",
    "id": 25684,
    }'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 - Not found in the database - when there are no group in the db.
