---
description: Preventing lost updates with version-based concurrency control
---

# Optimistic locking

Navixy Repository API has a `version` field for optimistic concurrency control, preventing lost updates when multiple clients simultaneously edit the same entity.

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

<table><thead><tr><th width="236.39996337890625">Entity</th><th>Description</th></tr></thead><tbody><tr><td>Device</td><td>GPS trackers, sensors, beacons</td></tr><tr><td>Asset</td><td>Vehicles, equipment, employees</td></tr><tr><td>AssetGroup</td><td>Asset collections</td></tr><tr><td>GeoObject</td><td>Geofences, POIs, routes</td></tr><tr><td>Schedule</td><td>Work hours, maintenance windows</td></tr><tr><td>Inventory</td><td>Warehouse records</td></tr><tr><td>Organization</td><td>Organization hierarchy nodes</td></tr><tr><td>CustomFieldDefinition</td><td>Custom field metadata</td></tr><tr><td>Catalog items</td><td>All system and user-defined catalog items</td></tr></tbody></table>

### Operations by type

| Operation | version in input | Behavior           |
| --------- | ---------------- | ------------------ |
| Create    | Not required     | Returns version: 1 |
| Update    | Required         | 409 on mismatch    |
| Delete    | Not required     | —                  |
| Restore   | Not required     | —                  |
| Bulk ops  | Not used         | Last write wins    |

Delete operations don't require version because if a client decides to delete an entity, that intent doesn't change based on other field modifications.

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

When receiving entity updates through [subscriptions](api-reference-old/subscriptions.md), the payload includes the current version for use in subsequent mutations:

```graphql
subscription {
  deviceUpdated(id: "...") {
    id
    version  # for the next mutation
    name
  }
}
```

