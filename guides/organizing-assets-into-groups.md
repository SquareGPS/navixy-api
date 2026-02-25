---
description: >-
  Organize assets into typed, color-coded collections for fleet segmentation,
  reporting, and access control.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
---

# Organizing assets into groups

Asset groups let you organize assets into named collections — by depot, project, customer, vehicle class, or any other category that makes sense for your operations. A "Hamburg Depot" group, for example, might contain all trucks assigned to that location.

The grouping system has two layers. An **asset group type** acts as a template: it classifies groups and optionally restricts which kinds of assets can join them. An **asset group** is an instance of that template — a named collection tied to a specific type. You create the type once, then create as many groups of that type as you need.

The API also maintains a full membership **history**: every time an asset joins or leaves a group, the event is recorded with timestamps. This lets you audit past assignments — for example, to find which depot a truck belonged to during a specific period.

If you haven't created assets yet, start with [Working with assets](working-with-assets.md).

### Before you start

You need your organization's ID for all asset group operations. Use the `me` query to retrieve it:

```graphql
query GetMyOrganization {
  me {
    memberships {
      organization {
        id
        title
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
      "memberships": [
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
```

In most cases, you'll have one organization in the response. Use its `id` for all asset operations.

### Check available asset group types

Every asset group must belong to a group type. Check which types already exist in your organization before creating it with this query:

```graphql
query ListGroupTypes {
  assetGroupTypes(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
  ) {
    nodes {
      id
      code
      title
    }
  }
}
```

You'll get an array of types, if any exist:

```json
{
  "data": {
    "assetGroupTypes": {
      "nodes": [
        {
          "id": "f3a1cc20-8b2e-4d91-a73f-1ec8d0bc4e55",
          "code": "depot",
          "title": "Depot"
        }
      ]
    }
  }
}
```

If no group types exist, read how to create them in the [example scenario](organizing-assets-into-groups.md#example-scenario-setting-up-a-depot-fleet-structure).

## Understanding asset groups

### Asset group types

An asset group type is a catalog item that classifies groups and defines membership constraints. Like asset types, it has a `code` (stable machine-readable identifier), a `title` (display name), and `meta` properties for UI customization.

{% hint style="warning" %}
`code` is immutable after creation. Choose it carefully — it's what integrations and filters will use to reference the type.
{% endhint %}

The key field on a group type is `allowedAssetTypes`: an optional list of constraints that controls which asset types can be added to groups of this type, and how many of each. Each constraint pairs an asset type with an optional `maxItems` cap — null means unlimited. If `allowedAssetTypes` is empty, groups of that type accept any asset regardless of its type.

Types can originate from three places: predefined by the platform (`SYSTEM`), created by your organization (`ORGANIZATION`), or inherited from a parent organization (`PARENT_ORGANIZATION`), exposed as `meta.origin`. You can only create, update, and delete types with `ORGANIZATION` origin — system and inherited types are read-only.

For the full field reference, see AssetGroupType.

### Asset groups

An asset group is a named collection that belongs to an organization and conforms to a group type. For example, a "Depot" type (created once) might have three instances: "Hamburg Depot", "Berlin Depot", and "Munich Depot" — each a separate group, all sharing the same membership constraints defined by the type.

Groups have an optional `color` for visual identification in UIs, and expose two ways to query their members: `currentAssets` returns only the assets in the group right now, while `history` returns the full membership timeline including past members.

For the full field reference, see AssetGroup.

### Membership records

Every add and remove operation creates or closes an `AssetGroupItem` record. This object tracks when an asset joined (`attachedAt`) and when it left (`detachedAt`). A null `detachedAt` means the asset is currently in the group. The history is preserved even after removal — removal is a soft delete that sets `detachedAt` rather than destroying the record — so you can reconstruct past group composition at any point in time.

For the full field reference, see AssetGroupItem.

## Example scenario: Setting up a depot fleet structure

TransLog GmbH wants to organize their delivery trucks by regional depot. They'll create a "Depot" group type that only accepts delivery trucks, then create a Hamburg Depot group and assign trucks to it.

\{% stepper %\} \{% step %\}

#### Create an asset group type

Start by creating the "Depot" group type. This type constrains membership to delivery trucks only, with no cap on how many can join a group.

```graphql
mutation CreateDepotGroupType {
  assetGroupTypeCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    code: "depot"
    title: "Depot"
    order: 10
    allowedAssetTypes: [
      {
        assetTypeId: "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"
        maxItems: null
      }
    ]
    meta: {
      description: "Groups trucks by regional depot location"
      backgroundColor: "#1E3A5F"
      textColor: "#FFFFFF"
    }
  }) {
    assetGroupType {
      id
      code
      title
      allowedAssetTypes {
        assetType {
          code
          title
        }
        maxItems
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetGroupTypeCreate": {
      "assetGroupType": {
        "id": "f3a1cc20-8b2e-4d91-a73f-1ec8d0bc4e55",
        "code": "depot",
        "title": "Depot",
        "allowedAssetTypes": [
          {
            "assetType": {
              "code": "delivery_truck",
              "title": "Delivery Truck"
            },
            "maxItems": null
          }
        ]
      }
    }
  }
}
```

Save the `id` — you'll need it to create groups of this type.

\{% hint style="info" %\} To create a group type with no asset type restrictions, omit `allowedAssetTypes` or pass an empty array. Groups of that type will then accept any asset regardless of its type. \{% endhint %\} \{% endstep %\}

\{% step %\}

#### Create an asset group

Create the Hamburg Depot group using the type you just created.

```graphql
mutation CreateHamburgDepot {
  assetGroupCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "f3a1cc20-8b2e-4d91-a73f-1ec8d0bc4e55"
    title: "Hamburg Depot"
    color: "#1E3A5F"
  }) {
    assetGroup {
      id
      version
      title
      type {
        code
        title
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetGroupCreate": {
      "assetGroup": {
        "id": "a9d4f810-3c67-4b02-b891-2d47e0fa3c11",
        "version": 1,
        "title": "Hamburg Depot",
        "type": {
          "code": "depot",
          "title": "Depot"
        }
      }
    }
  }
}
```

Save the group `id` and `version`. \{% endstep %\}

\{% step %\}

#### Add assets to the group

Add Truck B-44 to the Hamburg Depot group. The `assetGroupItemAdd` mutation creates a membership record and returns it.

```graphql
mutation AddTruckToHamburg {
  assetGroupItemAdd(input: {
    groupId: "a9d4f810-3c67-4b02-b891-2d47e0fa3c11"
    assetId: "019a6b2f-793e-807b-8001-555345529b44"
  }) {
    assetGroupItem {
      id
      asset {
        id
        title
      }
      attachedAt
      detachedAt
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetGroupItemAdd": {
      "assetGroupItem": {
        "id": "cc82e140-a021-4f9e-9b33-8e1f6c005d77",
        "asset": {
          "id": "019a6b2f-793e-807b-8001-555345529b44",
          "title": "Truck B-44 (Berlin–Warsaw)"
        },
        "attachedAt": "2024-03-15T09:00:00Z",
        "detachedAt": null
      }
    }
  }
}
```

`detachedAt: null` confirms the truck is currently a member of the group.

**Constraint violations** return a `VALIDATION_ERROR` (400). This applies both when the asset's type isn't permitted by `allowedAssetTypes` and when `maxItems` for the type has already been reached. The `field` property in the error extensions will identify which constraint failed.

\{% hint style="warning" %\} The exact `VALIDATION_ERROR` structure for constraint violations (wrong asset type, `maxItems` exceeded) is pending confirmation from the development team. Verify the `field` and `detail` values before writing constraint-aware error handling. \{% endhint %\}

**Adding an asset already in the group** returns a `DUPLICATE` (409) error, as the membership record must be unique. The `constraint` field in the error extensions identifies which uniqueness rule was violated. \{% endstep %\}

\{% step %\}

#### Verify membership

You can verify group membership from either side — by querying the group's `currentAssets`, or by querying the asset's `groups` field.

**From the group's perspective:**

```graphql
query GetDepotMembers {
  assetGroup(id: "a9d4f810-3c67-4b02-b891-2d47e0fa3c11") {
    id
    title
    currentAssets(first: 20) {
      nodes {
        id
        title
        type {
          code
        }
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetGroup": {
      "id": "a9d4f810-3c67-4b02-b891-2d47e0fa3c11",
      "title": "Hamburg Depot",
      "currentAssets": {
        "nodes": [
          {
            "id": "019a6b2f-793e-807b-8001-555345529b44",
            "title": "Truck B-44 (Berlin–Warsaw)",
            "type": {
              "code": "delivery_truck"
            }
          }
        ]
      }
    }
  }
}
```

**From the asset's perspective:**

```graphql
query GetAssetGroups {
  asset(id: "019a6b2f-793e-807b-8001-555345529b44") {
    id
    title
    groups(first: 10) {
      nodes {
        id
        title
        type {
          code
        }
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "asset": {
      "id": "019a6b2f-793e-807b-8001-555345529b44",
      "title": "Truck B-44 (Berlin–Warsaw)",
      "groups": {
        "nodes": [
          {
            "id": "a9d4f810-3c67-4b02-b891-2d47e0fa3c11",
            "title": "Hamburg Depot",
            "type": {
              "code": "depot"
            }
          }
        ]
      }
    }
  }
}
```

An asset can belong to multiple groups simultaneously — for example, a truck can be in both a regional depot group and a maintenance-status group at the same time. The `groups` field returns all groups the asset is currently assigned to, across all group types.

\{% hint style="warning" %\} Whether an asset can belong to multiple groups of the **same type** at once (for example, two depot groups) is pending confirmation from the development team. \{% endhint %\} \{% endstep %\}

\{% step %\}

#### Update the group

The Hamburg depot is being rebranded. Update the group's title and color. Note the `version` field — it's required for optimistic locking and must match the current version of the group.

```graphql
mutation RenameDepot {
  assetGroupUpdate(input: {
    id: "a9d4f810-3c67-4b02-b891-2d47e0fa3c11"
    version: 1
    title: "Hamburg & Kiel Depot"
    color: "#0F2D52"
  }) {
    assetGroup {
      id
      version
      title
      color
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetGroupUpdate": {
      "assetGroup": {
        "id": "a9d4f810-3c67-4b02-b891-2d47e0fa3c11",
        "version": 2,
        "title": "Hamburg & Kiel Depot",
        "color": "#0F2D52"
      }
    }
  }
}
```

The `version` increments to `2`. Use this version for any further mutations on this group.

\{% hint style="info" %\} You can only update a group's `title` and `color`. Its `type` is fixed at creation and cannot be changed. \{% endhint %\} \{% endstep %\}

\{% step %\}

#### Remove an asset from the group

Truck B-44 has been reassigned to the Berlin depot. Remove it from the Hamburg & Kiel group.

```graphql
mutation RemoveTruckFromHamburg {
  assetGroupItemRemove(input: {
    groupId: "a9d4f810-3c67-4b02-b891-2d47e0fa3c11"
    assetId: "019a6b2f-793e-807b-8001-555345529b44"
  }) {
    deletedId
  }
}
```

Response:

```json
{
  "data": {
    "assetGroupItemRemove": {
      "deletedId": "cc82e140-a021-4f9e-9b33-8e1f6c005d77"
    }
  }
}
```

The membership record is closed: its `detachedAt` is set to the current timestamp, and the truck moves out of `currentAssets`. The record itself is preserved in the group's `history` — the removal is a soft delete.

**Removing an asset that isn't currently in the group** returns a `NOT_FOUND` (404) error. \{% endstep %\}

\{% step %\}

#### Query membership history

After a period of reassignments, query the full membership history of the group to see all past and current members:

```graphql
query GetDepotHistory {
  assetGroup(id: "a9d4f810-3c67-4b02-b891-2d47e0fa3c11") {
    title
    history(
      first: 20
      orderBy: { field: ATTACHED_AT, direction: DESC }
    ) {
      nodes {
        asset {
          id
          title
        }
        attachedAt
        detachedAt
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetGroup": {
      "title": "Hamburg & Kiel Depot",
      "history": {
        "nodes": [
          {
            "asset": {
              "id": "019a6b2f-793e-807b-8001-555345529b44",
              "title": "Truck B-44 (Berlin–Warsaw)"
            },
            "attachedAt": "2024-03-15T09:00:00Z",
            "detachedAt": "2024-06-01T14:30:00Z"
          }
        ]
      }
    }
  }
}
```

To narrow history to only currently attached assets, pass the `activeOnly` filter. This returns the same set as `currentAssets`, but with `attachedAt` timestamps included:

```graphql
history(
  filter: { activeOnly: true }
  first: 20
)
```

\{% endstep %\}

\{% step %\}

#### Delete the group

When a depot closes and you no longer need the group, delete it using its current `version`.

```graphql
mutation CloseDepot {
  assetGroupDelete(input: {
    id: "a9d4f810-3c67-4b02-b891-2d47e0fa3c11"
    version: 2
  }) {
    deletedId
  }
}
```

Response:

```json
{
  "data": {
    "assetGroupDelete": {
      "deletedId": "a9d4f810-3c67-4b02-b891-2d47e0fa3c11"
    }
  }
}
```

\{% hint style="warning" %\} Whether the group's membership history records are preserved or removed when a group is deleted is pending confirmation from the development team. \{% endhint %\} \{% endstep %\} \{% endstepper %\}

### Listing asset groups

To list all groups for an organization:

```graphql
query ListAssetGroups {
  assetGroups(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      title
      color
      type {
        code
        title
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    total {
      count
    }
  }
}
```

#### Filtering

Use `AssetGroupFilter` to narrow results by type or title. To list only depot-type groups, filter by the group type ID:

```graphql
query ListDepotGroups {
  assetGroups(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["f3a1cc20-8b2e-4d91-a73f-1ec8d0bc4e55"]
      titleContains: "hamburg"
    }
    first: 20
  ) {
    nodes {
      id
      title
    }
  }
}
```

Multiple values in `typeIds` are combined with OR, so you can retrieve groups matching any of the specified types in a single query. The `typeIds` and `titleContains` conditions are combined with AND.

#### Listing available group types

To see which group types are available in your organization before creating groups:

```graphql
query ListGroupTypes {
  assetGroupTypes(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      code
      title
      allowedAssetTypes {
        assetType {
          code
          title
        }
        maxItems
      }
    }
  }
}
```

Like asset types, group types can originate from the platform (`SYSTEM`), your organization (`ORGANIZATION`), or a parent organization (`PARENT_ORGANIZATION`) — visible as `meta.origin`. You can only create, update, and delete types with `ORGANIZATION` origin; system and inherited types are read-only.

For details on pagination, see Pagination.

### Handling version conflicts

Asset groups use optimistic locking. If another client updates a group between when you fetched it and when you submit your mutation, the API returns a `CONFLICT` (409) error:

```json
{
  "errors": [
    {
      "message": "Entity has been modified by another request",
      "path": ["assetGroupUpdate"],
      "extensions": {
        "type": "https://api.navixy.com/errors/conflict",
        "title": "Optimistic Lock Conflict",
        "status": 409,
        "code": "CONFLICT",
        "entityType": "AssetGroup",
        "entityId": "a9d4f810-3c67-4b02-b891-2d47e0fa3c11",
        "expectedVersion": 1,
        "currentVersion": 2,
        "traceId": "0af7651916cd43dd8448eb211c80319c"
      }
    }
  ]
}
```

To resolve this: re-fetch the group to get its current `version` and state, merge your intended changes, and retry the mutation with the updated version.

For a full explanation of how versioning works, see Optimistic locking.

### See also

* Asset groups — Queries: Full reference for `assetGroup`, `assetGroups`, and `assetGroupTypes`
* Asset groups — Mutations: Full reference for all 8 group mutations
* Working with assets: Create and manage the assets that go into groups
* Implementing custom fields: Define type-specific attributes for assets
