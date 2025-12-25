---
description: Description of Optimistic Locking
---

# Optimistic locking

Navixy Repository API uses ETag/If-Match header pair for optimistic concurrency control.

### How optimistic locking works

When multiple users or systems edit the same entity simultaneously, changes can be lost. Optimistic locking prevents this by detecting when an entity has been modified since you last read it.

The API tracks a version number for each entity. When you update an entity, you tell the API which version you're updating. If someone else modified the entity in the meantime, the versions won't match, and the API rejects your update with a conflict error.

This approach is "optimistic" because it assumes conflicts are rare. Instead of locking records during editing, which would block other users, it checks for conflicts only when saving.

### ETag and If-Match headers

The API uses standard HTTP headers to pass version information:

* **ETag** (response header): Contains the entity's current version after any read or write operation.
* **If-Match** (request header): Contains the version you expect when updating or deleting.

#### ETag format

```
ETag: <entity_type>:<uuid>:<version>
```

Example:

```
ETag: device:550e8400-e29b-41d4-a716-446655440001:5
```

The version starts at 1 when an entity is created and increments with each update.

### Supported entities

Optimistic locking applies to the following entity types:

<table><thead><tr><th width="261.199951171875">Entity</th><th>Description</th></tr></thead><tbody><tr><td>Device</td><td>GPS trackers, sensors, beacons</td></tr><tr><td>Asset</td><td>Vehicles, equipment, employees</td></tr><tr><td>GeoObject</td><td>Geofences, POIs, routes</td></tr><tr><td>Schedule</td><td>Work hours, maintenance windows</td></tr><tr><td>Inventory</td><td>Warehouse records</td></tr><tr><td>Organization</td><td>Organization hierarchy nodes</td></tr><tr><td>AssetGroup</td><td>Asset collections</td></tr><tr><td>CustomFieldDefinition</td><td>Custom field metadata</td></tr><tr><td>Catalog items</td><td>All system and user-defined catalog items</td></tr></tbody></table>

### Workflow

#### Reading an entity

When you fetch an entity, the response includes an `ETag` header with the current version:

**Request:**

```graphql
query {
  device(id: "550e8400-e29b-41d4-a716-446655440001") {
    id
    title
    status { code }
  }
}
```

**Response headers:**

```
ETag: device:550e8400-e29b-41d4-a716-446655440001:5
```

Store this ETag value — you'll need it when updating.

#### Updating an entity

When you update an entity, include the stored ETag in the `If-Match` header:

**Request headers:**

```
If-Match: device:550e8400-e29b-41d4-a716-446655440001:5
```

**Request body:**

```graphql
mutation {
  updateDevice(input: {
    id: "550e8400-e29b-41d4-a716-446655440001"
    title: "Truck 42 - Updated"
  }) {
    id
    title
  }
}
```

**On success**, the response includes an updated ETag with the new version:

```
ETag: device:550e8400-e29b-41d4-a716-446655440001:6
```

Store this new ETag — you'll need it for subsequent updates to the same entity.

#### Handling conflicts

If the entity was modified by another request since you fetched it, the API returns a `409 Conflict` error:

```json
{
  "errors": [{
    "message": "Entity has been modified by another request",
    "extensions": {
      "type": "https://api.navixy.com/errors/conflict",
      "title": "Conflict",
      "status": 409,
      "detail": "Device 550e8400-e29b-41d4-a716-446655440001 was modified. Expected version 5, current version 6.",
      "instance": "/graphql",
      "code": "CONFLICT",
      "entityType": "device",
      "entityId": "550e8400-e29b-41d4-a716-446655440001",
      "expectedVersion": 5,
      "currentVersion": 6,
      "currentETag": "device:550e8400-e29b-41d4-a716-446655440001:6"
    }
  }]
}
```

The error includes `currentETag` so you can retry without fetching the entity again if you don't need to review the changes.

### Conflict resolution

When you receive a 409 conflict error, you have two options:

#### Option 1: Refetch and retry

Fetch the entity again to get the current data, reapply your changes, and retry with the new ETag. This is the safest approach when you need to see what changed.

#### Option 2: Retry with currentETag

If you're confident your changes should overwrite whatever happened, use the `currentETag` from the error response.

Use this approach with caution — you may overwrite someone else's changes.

### Operations without optimistic locking

#### Create operations

When creating a new entity, you don't need to send an `If-Match` header. The response includes an ETag with version 1:

```
ETag: device:550e8400-e29b-41d4-a716-446655440001:1
```

#### Bulk operations

Bulk mutations (`bulkDeleteDevices`, `bulkDeleteAssets`, etc.) do not support optimistic locking. They use "last write wins" semantics for simplicity. If you need conflict detection for bulk operations, process entities individually.

#### Delete and restore

Delete and restore operations require the `If-Match` header, just like updates. This prevents accidentally deleting an entity that was modified after you viewed it.

### Concurrent editing scenario

Here's what happens when two users edit the same device:

<figure><img src=".gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

User A's first update fails because User B already modified the device. After refetching, User A can successfully update with the current version.
