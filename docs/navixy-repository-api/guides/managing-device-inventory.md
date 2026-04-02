---
description: >-
  Create inventories, assign devices to them, transfer devices, and track
  assignment history.
---

# Managing device inventory

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

An inventory in Navixy Repository API is a named container that represents a physical location where devices are stored — a warehouse, a service depot, a regional office, or any other place your organization keeps hardware. Inventories give you visibility into where each device physically is at any point in time, and the assignment history lets you trace where it has been.

A device can be assigned to at most one inventory at a time. Assigning it to a new inventory automatically implies it has left the previous one, which must be explicitly unlinked first. The full history of all past assignments is preserved on the device regardless of current status.

This guide continues the FleetOps Ltd scenario from [Working with devices](activating-a-device.md). The company has registered a batch of Teltonika FMB003 trackers. Now the hardware operations team needs to track which warehouse holds each device as units move from central stock to regional depots ahead of installation.

## Before you start

You need your organization's ID for all asset operations. Use the `me` query to retrieve it:

```graphql
query GetMyOrganization {
  me {
    ... on User {
      memberships {
        nodes {
          organization {
            id
            title
          }
        }
      }
    }
  }
}
```

You'll receive a response:

```json
{
  "data": {
    "me": {
      "memberships": {
        "nodes": [
          {
            "organization": {
              "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
              "title": "TransLog GmbH"
            }
          }
        ]
      }
    }   
  }
}
```

Use the `id` of the organization you want to work with for all subsequent asset operations.

## Example scenario: Managing warehouse stock

FleetOps Ltd operates two hardware locations: a central warehouse in Berlin that receives new shipments, and a regional depot in Amsterdam that supplies the local installation team. This scenario walks through setting up both inventories, receiving a device shipment into Berlin, transferring a device to Amsterdam, and auditing the assignment history.

{% stepper %}
{% step %}
### Create inventories

Create an inventory for each physical location. Inventories only require a title.

{% hint style="info" %}
`version` is optional — omitting it applies the update unconditionally without conflict detection. Include it whenever you want to guard against overwriting concurrent changes. See [Optimistic locking](../optimistic-locking.md) for details. In this example, we'll be using this field.
{% endhint %}

Run this mutation:

```graphql
mutation CreateInventories {
  berlin: inventoryCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    title: "Berlin Warehouse"
  }) {
    inventory { id version title }
  }
  amsterdam: inventoryCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    title: "Amsterdam Depot"
  }) {
    inventory { id version title }
  }
}
```

Response:

```json
{
  "data": {
    "berlin": {
      "inventory": {
        "id": "a1b2c3d4-1234-5678-abcd-111222333444",
        "version": 1,
        "title": "Berlin Warehouse"
      }
    },
    "amsterdam": {
      "inventory": {
        "id": "b2c3d4e5-2345-6789-bcde-222333444555",
        "version": 1,
        "title": "Amsterdam Depot"
      }
    }
  }
}
```

Save both IDs — you'll need them when assigning and transferring devices.&#x20;
{% endstep %}

{% step %}
### Assign devices to an inventory

When the shipment of FMB003 trackers arrives at Berlin Warehouse, assign each device to that inventory using `deviceInventoryLink`. You can batch multiple assignments in a single request:

```graphql
mutation ReceiveShipment {
  unit001: deviceInventoryLink(input: {
    deviceId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    inventoryId: "a1b2c3d4-1234-5678-abcd-111222333444"
  }) {
    deviceInventoryRelation {
      id
      device { id title }
      inventory { title }
      assignedAt
      assignedBy { title }
    }
  }
  unit002: deviceInventoryLink(input: {
    deviceId: "f2c7d5e4-5b6f-8c9a-d011-555666777888"
    inventoryId: "a1b2c3d4-1234-5678-abcd-111222333444"
  }) {
    deviceInventoryRelation {
      id
      device { id title }
      inventory { title }
      assignedAt
      assignedBy { title }
    }
  }
}
```

Response:

```json
{
  "data": {
    "unit001": {
      "deviceInventoryRelation": {
        "id": "c3d4e5f6-3456-789a-cdef-333444555666",
        "device": { "id": "e1b6f4a3-4a5d-7b8e-cf10-444555666777", "title": "FMB003 — Unit 001" },
        "inventory": { "title": "Berlin Warehouse" },
        "assignedAt": "2025-03-10T09:15:00Z",
        "assignedBy": { "title": "Anna Müller" }
      }
    },
    "unit002": {
      "deviceInventoryRelation": {
        "id": "d4e5f6a7-4567-89ab-def0-444555666777",
        "device": { "id": "f2c7d5e4-5b6f-8c9a-d011-555666777888", "title": "FMB003 — Unit 002" },
        "inventory": { "title": "Berlin Warehouse" },
        "assignedAt": "2025-03-10T09:15:01Z",
        "assignedBy": { "title": "Anna Müller" }
      }
    }
  }
}
```

`deviceInventoryLink` is idempotent: calling it again with the same device and inventory returns success without creating a duplicate record.

{% hint style="info" %}
`assignedBy` records the actor who made the API call. It is nullable and may be `null` in automated contexts where no authenticated user is associated with the request.
{% endhint %}
{% endstep %}

{% step %}
### Query inventory contents

To see which devices are currently assigned to Berlin Warehouse, query the `devices` field on the inventory. You can apply the same filters and ordering as the top-level `devices` query.

```graphql
query BerlinStock {
  inventory(id: "a1b2c3d4-1234-5678-abcd-111222333444") {
    title
    devices(first: 50) {
      nodes {
        id
        title
        status { title }
        identifiers { type value }
      }
      total { count }
    }
  }
}
```

Response:

```json
{
  "data": {
    "inventory": {
      "title": "Berlin Warehouse",
      "devices": {
        "nodes": [
          {
            "id": "e1b6f4a3-4a5d-7b8e-cf10-444555666777",
            "title": "FMB003 — Unit 001",
            "status": { "title": "In Stock" },
            "identifiers": [
              { "type": "IMEI", "value": "356307042772396" }
            ]
          },
          {
            "id": "f2c7d5e4-5b6f-8c9a-d011-555666777888",
            "title": "FMB003 — Unit 002",
            "status": { "title": "In Stock" },
            "identifiers": [
              { "type": "IMEI", "value": "356307042883407" }
            ]
          }
        ],
        "total": { "count": 2 }
      }
    }
  }
}
```

Alternatively, use the top-level `devices` query with `filter.inventoryIds` to query devices across multiple inventories at once:

```graphql
query AllWarehouseStock {
  devices(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      inventoryIds: [
        "a1b2c3d4-1234-5678-abcd-111222333444"
        "b2c3d4e5-2345-6789-bcde-222333444555"
      ]
    }
    first: 50
  ) {
    nodes {
      id
      title
      inventory { title }
      status { title }
    }
  }
}
```
{% endstep %}

{% step %}
### Transfer a device to another inventory

The Amsterdam installation team requests Unit 001 for a local job. Transferring a device is a two-step operation: unlink it from its current inventory, then link it to the destination.

First, unlink from Berlin Warehouse:

```graphql
mutation UnlinkFromBerlin {
  deviceInventoryUnlink(input: {
    deviceId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
  }) {
    deletedId
  }
}
```

Then assign to Amsterdam Depot:

```graphql
mutation LinkToAmsterdam {
  deviceInventoryLink(input: {
    deviceId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    inventoryId: "b2c3d4e5-2345-6789-bcde-222333444555"
  }) {
    deviceInventoryRelation {
      device { title }
      inventory { title }
      assignedAt
    }
  }
}
```

Both calls can be combined into a single request using aliases, since `deviceInventoryUnlink` is idempotent and safe to call even if the device happens not to be assigned:

```graphql
mutation TransferDevice {
  unlink: deviceInventoryUnlink(input: {
    deviceId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
  }) {
    deletedId
  }
  link: deviceInventoryLink(input: {
    deviceId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    inventoryId: "b2c3d4e5-2345-6789-bcde-222333444555"
  }) {
    deviceInventoryRelation {
      device { title }
      inventory { title }
      assignedAt
    }
  }
}
```

{% hint style="warning" %}
When batching `unlink` and `link` in a single request, GraphQL executes mutations sequentially in declaration order. The unlink always runs before the link.
{% endhint %}
{% endstep %}

{% step %}
### View assignment history

To audit where Unit 001 has been, query its `inventoryHistory`. Records are returned in reverse chronological order by default.

```graphql
query DeviceHistory {
  device(id: "e1b6f4a3-4a5d-7b8e-cf10-444555666777") {
    title
    inventoryHistory(first: 10) {
      nodes {
        inventory { title }
        assignedAt
        assignedBy { title }
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "device": {
      "title": "FMB003 — Unit 001",
      "inventoryHistory": {
        "nodes": [
          {
            "inventory": { "title": "Amsterdam Depot" },
            "assignedAt": "2025-03-12T14:30:00Z",
            "assignedBy": { "title": "Pieter van den Berg" }
          },
          {
            "inventory": { "title": "Berlin Warehouse" },
            "assignedAt": "2025-03-10T09:15:00Z",
            "assignedBy": { "title": "Anna Müller" }
          }
        ]
      }
    }
  }
}
```

History is append-only: every assignment, including past ones, is permanently recorded. Unlinks are represented implicitly by the presence of a subsequent assignment to a different inventory.

To retrieve the oldest assignments first, override the default ordering:

```graphql
inventoryHistory(
  first: 10
  orderBy: { field: ASSIGNED_AT, direction: ASC }
)
```
{% endstep %}

{% step %}
### Update or delete an inventory

To rename an inventory, use `inventoryUpdate` with its current version:

```graphql
mutation RenameInventory {
  inventoryUpdate(input: {
    id: "a1b2c3d4-1234-5678-abcd-111222333444"
    version: 1
    title: "Berlin Central Warehouse"
  }) {
    inventory { id version title }
  }
}
```

To delete an inventory that is no longer needed, use `inventoryDelete`:

```graphql
mutation DeleteInventory {
  inventoryDelete(input: {
    id: "a1b2c3d4-1234-5678-abcd-111222333444"
    version: 2
  }) {
    deletedId
  }
}
```

{% hint style="warning" %}
Before deleting an inventory, unassign all devices from it using `deviceInventoryUnlink`. The behavior when deleting an inventory that still has devices assigned has not been fully verified — unassigning first is the safe approach.
{% endhint %}
{% endstep %}
{% endstepper %}

## Listing inventories

To list all inventories for an organization:

```graphql
query ListInventories {
  inventories(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      title
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Use `filter.titleContains` to search by name:

```graphql
query FindInventory {
  inventories(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: { titleContains: "amsterdam" }
    first: 5
  ) {
    nodes { id title }
  }
}
```

## Handling version conflicts

`inventoryUpdate` and `inventoryDelete` support optimistic locking via the `version` field. If the inventory was modified by another request since your last fetch, the API returns a `409 CONFLICT` error:

```json
{
  "errors": [{
    "message": "Entity has been modified by another request",
    "extensions": {
      "code": "CONFLICT",
      "entityType": "Inventory",
      "entityId": "a1b2c3d4-1234-5678-abcd-111222333444",
      "expectedVersion": 1,
      "currentVersion": 2
    }
  }]
}
```

To resolve this, fetch the inventory again to get its current version and retry. Note that `deviceInventoryLink` and `deviceInventoryUnlink` are idempotent commands and do not use version checks.

For a full explanation of how versioning works, see [Optimistic locking](https://claude.ai/chat/optimistic-locking.md).

### See also

* [Working with devices](https://claude.ai/chat/working-with-devices.md): Register devices and manage their identifiers and relations
* [Inventory reference](https://claude.ai/chat/6095d343-b927-45b6-9d85-e36725bb212d): Complete reference for all inventory operations and types
