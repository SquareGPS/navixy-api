---
description: Preventing lost updates with version-based concurrency control
---

# Optimistic locking

Navixy Repository API uses a `version` field for optimistic concurrency control, preventing lost updates when multiple clients simultaneously edit the same entity.

### How optimistic locking works

Every versioned entity includes a `version` field:

```graphql
type Device {
  id: ID!
  version: Int!
  name: String!
  # ...
}
```

The version starts at 1 when an entity is created and increments with each successful update.

Update mutations require version:

```graphql
input UpdateDeviceInput {
  version: Int!   # required
  name: String
  # ...
}
```

Delete mutations don't require version:

```graphql
input DeleteDeviceInput {
  id: ID!
  # version not required
}
```

### Supported entities

Optimistic locking applies to:

<table><thead><tr><th width="180">Entity</th><th>Description</th></tr></thead><tbody><tr><td><a href="api-reference/objects.md#device">Device</a></td><td>GPS trackers, sensors, beacons</td></tr><tr><td><a href="api-reference/objects.md#asset">Asset</a></td><td>Vehicles, equipment, employees</td></tr><tr><td><a href="api-reference/objects.md#assetgroup">AssetGroup</a></td><td>Asset collections</td></tr><tr><td><a href="api-reference/objects.md#geoobject">GeoObject</a></td><td>Geofences, POIs, routes</td></tr><tr><td><a href="api-reference/objects.md#schedule">Schedule</a></td><td>Work hours, maintenance windows</td></tr><tr><td><a href="api-reference/objects.md#inventory-1">Inventory</a></td><td>Warehouse records</td></tr><tr><td><a href="api-reference/objects.md#organization">Organization</a></td><td>Organization hierarchy nodes</td></tr><tr><td><a href="api-reference/objects.md#customfielddefinition">CustomFieldDefinition</a></td><td>Custom field metadata</td></tr><tr><td><a href="api-reference/interfaces.md#catalogitem">CatalogItem</a></td><td>All system and user-defined catalog items</td></tr></tbody></table>

#### Operations by type

<table><thead><tr><th width="360">Sample operation</th><th width="213.60003662109375">Version in input</th><th>Behavior</th></tr></thead><tbody><tr><td><a href="api-reference/mutations.md#createdevice">createDevice</a>, <a href="api-reference/mutations.md#createasset">createAsset</a></td><td>Not required</td><td>Returns version: 1</td></tr><tr><td><a href="api-reference/mutations.md#updatedevice">updateDevice</a>, <a href="api-reference/mutations.md#updateasset">updateAsset</a></td><td>Required</td><td>409 on mismatch</td></tr><tr><td><a href="api-reference/mutations.md#deletedevice">deleteDevice</a>, <a href="api-reference/mutations.md#deleteasset">deleteAsset</a></td><td>Not required</td><td>—</td></tr><tr><td><a href="api-reference/mutations.md#restoredevice">restoreDevice</a>, <a href="api-reference/mutations.md#restoreasset">restoreAsset</a></td><td>Not required</td><td>—</td></tr><tr><td><a href="api-reference/mutations.md#bulkdeletedevices">bulkDeleteDevices</a>, <a href="api-reference/mutations.md#bulkdeleteassets">bulkDeleteAssets</a></td><td>Not used</td><td>Last write wins</td></tr></tbody></table>

Delete operations don't require version because if a client decides to delete an entity, that intent doesn't change based on other field modifications.

#### Subscriptions

When receiving entity updates through [subscriptions](api-reference/subscriptions.md), the payload includes the current version for use in subsequent mutations:

```graphql
subscription {
  deviceUpdated(id: "...") {
    id
    version  # for the next mutation
    name
  }
}
```

#### Handling conflicts

If the entity was modified since you fetched it, the API returns a `409 Conflict` error:

```json
{
  "errors": [{
    "message": "Entity has been modified by another request",
    "extensions": {
      "code": "CONFLICT",
      "entityType": "Device",
      "entityId": "550e8400-e29b-41d4-a716-446655440001",
      "expectedVersion": 5,
      "currentVersion": 6
    }
  }]
}
```

If you receive a conflict error:

1. Fetch the entity again to see what changed
2. Merge the other user's changes with yours if needed
3. Retry your update with the new version

### Concurrent editing example

Here's what happens when two users edit the same device:

<figure><img src=".gitbook/assets/{AA1FDEB4-9D8E-4219-8928-610A1D262069}.png" alt=""><figcaption></figcaption></figure>

User A's update succeeds first. User B's update fails because the version changed. After refetching, User B can successfully update with the current version.

### Handling conflicts

If the entity was modified since you fetched it, the API returns a `409 Conflict` error:

```json
{
  "errors": [{
    "message": "Entity has been modified by another request",
    "extensions": {
      "code": "CONFLICT",
      "entityType": "Device",
      "entityId": "550e8400-e29b-41d4-a716-446655440001",
      "expectedVersion": 5,
      "currentVersion": 6
    }
  }]
}
```

If you receive a conflict error:

1. Fetch the entity again to see what changed
2. Merge the other user's changes with yours if needed
3. Retry your update with the new version

### Subscriptions

When receiving entity updates through [subscriptions](api-reference/subscriptions.md), the payload includes the current version for use in subsequent mutations:

```graphql
subscription {
  deviceUpdated(id: "...") {
    id
    version  # for the next mutation
    name
  }
}
```

