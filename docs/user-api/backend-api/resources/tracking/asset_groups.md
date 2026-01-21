---
title: Asset groups
description: API calls to interact with asset groups
---

# Asset groups

Contains API calls to interact with asset groups.

## Asset group entry

```json
{
  "id": 64584,
  "name": "group_1",
  "assets": [<asset>]
}
```

- **id** - `integer`. ID of the group.
- **name** - `string`. Name of the group.
- **assets** - `array` of asset objects described [below](#asset-entry). Can be empty.

## Asset group object entry

```json
{
  "asset": {<asset>},
  "group_id": 64584
}
```

- **asset** - asset described [below](#asset-entry).
- **group_id** - `integer`. ID of the group.

## Asset entry

```json
{
  "id": 36558,
  "type": "employee"
}
```

- **id** - `integer`. ID of the asset.
- **type** - `string`. Type of the asset. Can be one of `employee`, `vehicle`.

## API actions

**API path:** `/asset_group`

### create

Create new asset group.

#### Parameters

| Name | Description | Type |
|------|-------------|------|
| name | Optional. If not set, defaults to the new entry ID. Name of the group. | `string` |
| assets | Assets to include to group. Only one assets of each type is allowed. | `array` of assets |
| force_reassign | Optional. Default is `false`. If `true`, assets will be assigned even if they were assigned to another group, and their previous assignments will be removed. | `boolean` |

#### Example

```bash
curl -X POST 'https://api.navixy.com/v2/asset_group/create' \
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

- **id** - `integer`. ID of the group.
- **reassigned_assets** - `array` of asset group objects described [here](#asset-group-object-entry) that were removed during reassignment. Optional.

#### Errors

- **291** - All assets in the request must be accessible - if there are assets in the request that are not accessible to the user.
- **290** - Asset already assigned to a group - if `force_reassign` is `false` and asset is already assigned to a group. Response will contain `assigned_assets` - list of asset group objects described [here](#asset-group-object-entry) that are already assigned to a group.

### list

List asset groups by ids or asset.

#### Parameters

| Name | Description | Type |
|------|-------------|------|
| group_ids | IDs of the groups to search by | `integer` array |
| asset | Asset to search by | asset object |

> **Note:** Exactly one parameter must be specified: `group_ids` or `asset`.

#### Example

```bash
curl -X POST 'https://api.navixy.com/v2/asset_group/list' \
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

- **list** - `array` of objects. Asset groups described [here](#asset-group-entry).

### set

Set assets to existing group.

#### Parameters

| Name | Description | Type |
|------|-------------|------|
| id | ID of the group. | `integer` |
| assets | Assets to set to group. Only one assets for each type is allowed. | `array` of assets |
| force_reassign | Optional. Default is `false`. If `true`, assets will be assigned even if they were assigned to another group, and their previous assignments will be removed. | `boolean` |

#### Example

```bash
curl -X POST 'https://api.navixy.com/v2/asset_group/set' \
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

- **reassigned_assets** - `array` of asset group objects described [here](#asset-group-object-entry) that were removed during reassignment. Optional.

#### Errors

- **201** - Not found in the database - if there is no group in the db.
- **291** - All assets in the request must be accessible - if there are assets in the request that are not accessible to the user.
- **290** - Asset already assigned to a group - if `force_reassign` is `false` and asset is already assigned to a group. Response will contain `assigned_assets` - list of asset group objects described [here](#asset-group-object-entry) that are already assigned to a group.

### remove

Remove assets from group.

#### Parameters

| Name | Description | Type |
|------|-------------|------|
| id | ID of the group. | `integer` |
| assets | Assets to remove from group. Only one assets for each type is allowed. | `array` of assets |

#### Example

```bash
curl -X POST 'https://api.navixy.com/v2/asset_group/remove' \
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

- **201** - Not found in the database - if there is no group in the db.
- **286** - All assets must be present in the group - if not all assets are present in the group.
- **287** - if the group contains no assets accessible to the user.

### update

Update asset group name.

#### Parameters

| Name | Description | Type |
|------|-------------|------|
| id | ID of the group. | `integer` |
| name | New name for the group. | `string` |

#### Example

```bash
curl -X POST 'https://api.navixy.com/v2/asset_group/update' \
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

- **201** - Not found in the database - if there is no group in the db.
- **287** - At least 1 asset in the group must be accessible - if the group contains no assets accessible to the user.

### delete

Delete asset group.

#### Parameters

| Name | Description | Type |
|------|-------------|------|
| id | ID of the group. | `integer` |

> **Note:** The group will be marked as deleted, but its history will remain intact.

#### Example

```bash
curl -X POST 'https://api.navixy.com/v2/asset_group/delete' \
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

- **201** - Not found in the database - if there is no group in the db.
- **289** - All assets in the group must be accessible - if there are assets in the group that are not accessible to the user.