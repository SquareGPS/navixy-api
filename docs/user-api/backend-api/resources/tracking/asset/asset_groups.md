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
* `assets` - list of asset objects described [below](#asset-entry). Can be empty.

## Asset group object entry
```json
{
  "asset" : {<asset>},
  "group_id" : 64584
}
```

* `asset` - asset described [below](#asset-entry).
* `group_id` - int. ID of the group.


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

| name           | description                                                                                                                                                   | type                            |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| name           | Optional. If not set, defaults to the new entry ID. Name of the group.                                                                                        | string                          |
| assets         | Assets to include to group. Only one assets of each type is allowed.                                                                                          | array of [assets](#asset-entry) |
| force_reassign | Optional. Default is `false`. If `true`, assets will be assigned even if they were assigned to another group, and their previous assignments will be removed. | boolean                         |

#### Example

cURL

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
  "reassigned_assets": [<asset_group_object>],
  "success": true
}
```

* `id` - int. ID of the group.
* `reassigned_assets` - list of asset group objects described [here](#asset-group-object-entry) that were removed during reassignment. Optional.

#### Errors

* 291 - All assets in the request must be accessible - if there are assets in the request that are not accessible to the user.
* 290 - Asset already assigned to a group - if `force_reassign` is `false` and asset is already assigned to a group.
Response will contain `assigned_assets` - list of asset group objects described [here](#asset-group-object-entry) that are already assigned to a group.

### `list`

List asset groups by ids or asset.

#### Parameters

| name      | description                    | type                         |
|:----------|:-------------------------------|:-----------------------------|
| group_ids | IDs of the groups to search by | int array                    |
| asset     | Asset to search by             | [asset object](#asset-entry) |

* Exactly one parameter must be specified: `group_ids` or `asset`.

#### Example

cURL

```shell
  curl -X POST '{{ extra.api_example_url }}/asset_group/list' \
      -H 'Content-Type: application/json' \
      -d '{
  "hash":"59be129c1855e34ea9eb272b1e26ef1d",
  "group_ids": [25684, 25685]
  }'
```

#### Response

```json
{
  "list": [<asset_group>],
  "success": true
}
```

* `list` - object array. Asset groups described [here](#asset-group-entry).


### `set`

Set assets to existing group.

#### Parameters

| name           | description                                                                                                                                                   | type                            |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| id             | ID of the group.                                                                                                                                              | int                             |
| assets         | Assets to set to group. Only one assets for each type is allowed.                                                                                             | array of [assets](#asset-entry) |
| force_reassign | Optional. Default is `false`. If `true`, assets will be assigned even if they were assigned to another group, and their previous assignments will be removed. | boolean                         |

#### Example

cURL

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
  "success": true,
  "reassigned_assets": [<asset_group_object>]
}
```

* `reassigned_assets` - list of asset group objects described [here](#asset-group-object-entry) that were removed during reassignment. Optional.

#### Errors

* 201 - Not found in the database - if there is no group in the db.
* 291 - All assets in the request must be accessible - if there are assets in the request that are not accessible to the user.
* 290 - Asset already assigned to a group - if `force_reassign` is `false` and asset is already assigned to a group. 
Response will contain `assigned_assets` - list of asset group objects described [here](#asset-group-object-entry) that are already assigned to a group.


### `remove`

Remove assets from group.

#### Parameters

| name           | description                                                                                                                | type                            |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| id             | ID of the group.                                                                                                           | int                             |
| assets         | Assets to remove from group. Only one assets for each type is allowed.                                                     | array of [assets](#asset-entry) |

#### Example

cURL

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

* 201 - Not found in the database - if there is no group in the db.
* 286 - All assets must be present in the group - if not all assets are present in the group.
* 287 - if the group contains no assets accessible to the user.


### `update`

Update asset group name.

#### Parameters

| name | description             | type   |
|:-----|:------------------------|:-------|
| id   | ID of the group.        | int    |
| name | New name for the group. | string |

#### Example

cURL

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

* 201 - Not found in the database - if there is no group in the db.
* 287 - At least 1 asset in the group must be accessible - if the group contains no assets accessible to the user.


### `delete`

Delete asset group.

#### Parameters

| name | description        | type   |
|:-----|:-------------------|:-------|
| id   | ID of the group.   | int    |

* The group will be marked as deleted, but its history will remain intact.

#### Example

cURL

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

* 201 - Not found in the database - if there is no group in the db.
* 289 - All assets in the group must be accessible - if there are assets in the group that are not accessible to the user.
