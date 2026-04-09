---
description: Create and manage assets — vehicles, equipment, and other tracked objects.
---

# Working with assets

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

Assets in Navixy Repository API represent the physical or logical objects your organization tracks and manages. The most common example is a vehicle, but assets can be anything you need to monitor: construction equipment, forklifts, generators, shipping containers, leased machinery, or fixed infrastructure. If your organization has a reason to record it, assign attributes to it, or link a GPS device to it, it's a good candidate for an asset.

Each asset is defined by the **asset type**, which acts as a template: it classifies the asset and determines which custom fields are available for it. For example, a "Delivery Truck" type might have fields for license plate, fuel capacity, and assigned driver, while a "Generator" type might have fields for power output, last service date, and installation site.

To organize assets into named collections, such as grouping vehicles by depot or equipment by project, see [Organizing assets into groups](organizing-assets-into-groups.md).

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

{% hint style="info" %}
The `... on User` inline fragment is required because `me` returns the [Actor interface](../actors/#actor-1), which can resolve to either a [User](../actors/users.md#user) or an [Integration](../actors/integrations.md#integration-2). The `memberships` field only exists on `User`, so the fragment ensures the query is valid for both actor types. If you authenticate as an `Integration`, the `memberships` block is omitted from the response.
{% endhint %}

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

### Check available asset types

Before creating an asset, request the available asset types for your organization:

```graphql
query ListAssetTypes {
  assetTypes(
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
    "assetTypes": {
      "nodes": [
        {
          "id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
          "code": "VEHICLE",
          "title": "Vehicle"
        }
      ]
    }
  }
}
```

If you need a type that doesn't exist yet, you can create it as described in [the scenario below](working-with-assets.md#create-an-asset-type).

If you're working with an existing type and need to know which custom fields it has, query [customFieldDefinitions](../custom-fields.md#customfielddefinition) on the type:

```graphql
query GetTruckTypeFields {
  assetTypes(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: { codes: ["delivery_truck"] }
  ) {
    nodes {
      id
      title
      customFieldDefinitions {
        code
        title
        fieldType
        params {
          isRequired
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
    "assetTypes": {
      "nodes": [
        {
          "id": "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22",
          "title": "Delivery Truck",
          "customFieldDefinitions": [
            {
              "code": "license_plate",
              "title": "License Plate",
              "fieldType": "STRING",
              "params": {
                "isRequired": true
              }
            },
            {
              "code": "fuel_capacity_l",
              "title": "Fuel Capacity (L)",
              "fieldType": "NUMBER",
              "params": {
                "isRequired": false
              }
            }
          ]
        }
      ]
    }
  }
}
```

The `code` values here are exactly what you use as keys in `customFields.set` when creating or updating assets of this type. For type-specific parameters like maximum string length or the list of valid options, see [Implementing custom fields](implementing-custom-fields.md).

## Understanding assets

### Asset types

An asset type classifies assets and defines which custom fields they have. It is a [catalog item](../catalogs/catalog-items.md): it has a [code](../common.md#code) (a stable machine-readable identifier), a `title` (the display name), and `meta` properties for UI customization. The `customFieldDefinitions` field lists all custom fields available on assets of that type.

{% hint style="warning" %}
Before creating a type, remember that `code` is immutable after creation. Choose it carefully, since it's what integrations and filters will use to reference the type.
{% endhint %}

{% hint style="info" %}
Before deleting an asset type, check `meta.canBeDeleted`. The API rejects deletion if the type still has dependent assets or is system-managed. Query `meta { canBeDeleted }` on the type to verify before calling `assetTypeDelete`.
{% endhint %}

Types can originate from three places: predefined by the platform (`SYSTEM`), created by your organization (`ORGANIZATION`), or inherited from a parent organization in the dealer hierarchy (`PARENT_ORGANIZATION`). The origin is exposed as `meta.origin` on the type. You can only create, update, and delete types with `ORGANIZATION` origin — system and inherited types are read-only. The `organization` field on an asset type is `null` for `SYSTEM`-origin types, since they're not owned by any single organization.

For the full field reference, see [AssetType](../assets/types.md#assettype).

### Asset fields

An asset has a `title`, belongs to an organization, and is classified by an asset type. Its dynamic attributes are listed in `customFields`. Devices are linked to assets through custom fields the `DEVICE` type: the `primaryDevice` field returns the one marked as primary, while `devices` returns all linked devices. Assets also have a `groups` connection field that returns the asset groups they belong to, with optional filtering, ordering, and pagination arguments.

For the full field reference, see [Asset object](../assets/types.md#asset).

### Custom fields

Assets store their domain-specific attributes in the `customFields` field. When creating or updating an asset, you pass custom field changes using [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput), which has two sub-fields:

<table><thead><tr><th width="136.111083984375">Field</th><th width="105.66668701171875">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>set</code></td><td><a href="../common.md#json">JSON</a></td><td>Key-value map of fields to create or overwrite.</td></tr><tr><td><code>unset</code></td><td>[<a href="../common.md#code">Code</a>!]</td><td>List of field codes to clear.</td></tr><tr><td><code>setPrimary</code></td><td>[<a href="../common.md#code">Code</a>!]</td><td>Field codes to mark as primary (for <code>DEVICE</code>-type fields).</td></tr><tr><td><code>unsetPrimary</code></td><td>[<a href="../common.md#code">Code</a>!]</td><td>Field codes to unmark as primary.</td></tr></tbody></table>

`customFields` is always a patch operation: fields you don't mention are left unchanged. To update one field without touching others, include only that field in `set`. To remove a value entirely, list its code in `unset`.

See [Implementing custom fields](implementing-custom-fields.md) for details on defining field definitions and the supported field types.

### Linking devices

Assets connect to devices through custom fields of `DEVICE` type. Unlike the built-in fields (`geojson_data`, `schedule_data`), device fields are user-defined: you create them as custom field definitions for the asset type, which means you control the field code, can have multiple device fields per type, and can designate one as primary.

The `Asset` type exposes two convenience fields that resolve these links:

<table><thead><tr><th width="169.88885498046875">Field</th><th width="126.333251953125">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>primaryDevice</code></td><td><a href="../devices/types.md#device">Device</a></td><td>The device whose <code>DEVICE</code>-type field is marked as primary. <code>null</code> if no primary device is set.</td></tr><tr><td><code>devices</code></td><td>[<a href="../devices/types.md#device">Device</a>!]!</td><td>All devices linked through <code>DEVICE</code>-type custom fields.</td></tr></tbody></table>

To link a device, set the value of your `DEVICE`-type custom field. You can also mark it as primary if you wish:

```graphql
customFields: {
  set: { tracker: "<device-id>" }
  setPrimary: ["tracker"]
}
```

To unlink a device and clear its primary status:

```graphql
customFields: {
  unset: ["tracker"]
  unsetPrimary: ["tracker"]
}
```

Here, `tracker` is the code you chose when creating the DEVICE-type custom field definition for the asset type, not a fixed keyword. Each device can be linked to only one asset; attempting to assign a device that is already linked elsewhere returns a [409 Duplicate](../error-handling.md#duplicate-409) error.

The reverse lookup is also available: `Device.asset` returns the asset a device is linked to. See [Working with devices](activating-a-device.md) for details.

## Example scenario: Registering a logistics fleet

TransLog GmbH is setting up their asset registry. They need to track both their delivery trucks (with GPS devices) and warehouse forklifts (without GPS devices). This scenario walks through creating an asset type, registering assets, and maintaining the registry over time.

{% stepper %}
{% step %}
### **Create an asset type**

Start by creating a "Delivery Truck" asset type for your organization. Be careful when choosing the `code` — it's immutable after creation and will be used to reference this type in integrations and filters.

{% hint style="info" %}
`version` is optional — omitting it applies the update unconditionally without conflict detection. Include it whenever you want to guard against overwriting concurrent changes. See [Optimistic locking](../optimistic-locking.md) for details. In this example, we'll be using this field.
{% endhint %}

Run this mutation:

```graphql
mutation CreateTruckType {
  assetTypeCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    code: "delivery_truck"
    title: "Delivery Truck"
    order: 10
    meta: {
      description: "Long-haul and last-mile delivery vehicles"
    }
  }) {
    assetType {
      id
      version
      code
      title
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetTypeCreate": {
      "assetType": {
        "id": "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22",
        "version": 1,
        "code": "delivery_truck",
        "title": "Delivery Truck"
      }
    }
  }
}
```

Save the `id` — you'll need it in the next step. You can also save `version` if you later need to update or delete the type.

{% hint style="info" %}
The `order` field controls how types appear in UI lists. Lower numbers appear first. If display order doesn't matter for your use case, you can omit it to calculate the position automatically.
{% endhint %}
{% endstep %}

{% step %}
### Define custom fields

With the type created, add custom fields to be used by the assets of this type. Each delivery truck needs a license plate and a linked GPS device. Add both definitions in a single [assetTypeUpdate](../assets/mutations.md#assettypeupdate) call:

```graphql
mutation AddLicensePlateField {
  assetTypeUpdate(input: {
    id: "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"
    version: 1
    customFieldDefinitions: [
      {
        create: {
          code: "license_plate"
          title: "License Plate"
          fieldType: STRING
          params: { string: { isRequired: true } }
        }
      }
    ]
  }) {
    assetType {
      id
      version
      customFieldDefinitions {
        code
        title
        fieldType
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetTypeUpdate": {
      "assetType": {
        "id": "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22",
        "version": 2,
        "customFieldDefinitions": [
          {
            "code": "license_plate",
            "title": "License Plate",
            "fieldType": "STRING"
          }
        ]
      }
    }
  }
}
```

Save the `version` — you'll need it if you later update or delete the type. The `code` values in `customFieldDefinitions` are exactly what you'll use as keys in `customFields.set` when creating or updating assets of this type. The `tracker` field is the one you'll use later to link a GPS device to the truck.

For the full list of supported field types and their parameters, see [Implementing custom fields](implementing-custom-fields.md).
{% endstep %}

{% step %}
### **Create an asset**

Create the first truck in the registry. Pass custom field values using the `set` map inside `customFields`. In this example, the "Delivery Truck" type has a `license_plate` field.

Run this mutation:

```graphql
mutation RegisterTruck {
  assetCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"
    title: "Truck B-44 (Hamburg–Berlin)"
    customFields: {
      set: {
        license_plate: "HH-TL 4421"
      }
    }
  }) {
    asset {
      id
      version
      title
    }
  }
}
```

Response:

```json
{
  "data": {
    "assetCreate": {
      "asset": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 1,
        "title": "Truck B-44 (Hamburg–Berlin)"
      }
    }
  }
}
```

Save the `id` and `version` — you'll need them for updates.
{% endstep %}

{% step %}
### **Verify the asset**

Query the asset to confirm it was created correctly:

```graphql
query GetTruck {
  asset(id: "019a6b2f-793e-807b-8001-555345529b44") {
    id
    version
    title
    type {
      code
      title
    }
    customFields
    primaryDevice {
      id
      title
    }
    devices {
      id
      title
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
      "version": 1,
      "title": "Truck B-44 (Hamburg–Berlin)",
      "type": {
        "code": "delivery_truck",
        "title": "Delivery Truck"
      },
      "customFields": {
        "license_plate": "HH-TL 4421"
      },
      "primaryDevice": null,
      "devices": []
    }
  }
}
```

`primaryDevice` is `null` and `devices` is empty because no GPS unit has been assigned yet. `customFields` returns a raw JSON object keyed by field code — the same keys you use in `set` and `unset`.

To keep the response clean, you can request only specific custom field codes:

```graphql
query GetTruckLicensePlate {
  asset(id: "019a6b2f-793e-807b-8001-555345529b44") {
    title
    customFields(codes: ["license_plate"])
  }
}
```
{% endstep %}

{% step %}
### Assign a device

A GPS unit has been installed in the truck. To link it, you need a `DEVICE`-type custom field on the asset type. If you haven't created one yet, add it via `assetTypeUpdate` (see Implementing[ custom fields](implementing-custom-fields.md)). In this example, the "Delivery Truck" type has a field with the code `tracker`.

To create a device or find its id, see [Working with devices](activating-a-device.md).

Assign the device using `assetUpdate` with the device ID in `customFields.set`, and mark the field as primary with `setPrimary`:

```graphql
mutation AssignTruckDevice {
  assetUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 1
    customFields: {
      set: {
        tracker: "c3hhef22-2f3e-6hj1-ee9g-9ee2eg713d44"
      }
      setPrimary: ["tracker"]
    }
  }) {
    asset {
      id
      version
      primaryDevice {
        id
        title
      }
      devices {
        id
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
    "assetUpdate": {
      "asset": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 2,
        "primaryDevice": {
          "id": "c3hhef22-2f3e-6hj1-ee9g-9ee2eg713d44",
          "title": "GPS Unit #117"
        },
        "devices": [
          {
            "id": "c3hhef22-2f3e-6hj1-ee9g-9ee2eg713d44",
            "title": "GPS Unit #117"
          }
        ]
      }
    }
  }
}
```

Note that version increments to `2` after a successful update. Use this new version for any further mutations.

To unassign the device (e.g., if the unit is removed for maintenance), use `unset`:

```graphql
mutation UnlinkForkliftDevice {
  assetUpdate(input: {
    id: "029b7c40-804f-918c-9112-666456630d55"
    version: 2
    customFields: {
      unset: ["tracker"]
      unsetPrimary: ["tracker"]
    }
  }) {
    asset {
      id
      version
      primaryDevice { id }
      devices { id }
    }
  }
}
```

After unlinking, `primaryDevice` returns `null` and `devices` returns an empty array.
{% endstep %}

{% step %}
### **Delete the asset**

{% hint style="danger" %}
Asset deletion is permanent. Unlike some other entity types in the API, assets don't support soft delete and cannot be restored after deletion. Make sure you no longer need the record before proceeding.
{% endhint %}

When the truck is decommissioned and you no longer need its record, run the [assetDelete](../assets/mutations.md#assetdelete) mutation:

```graphql
mutation DecommissionTruck {
  assetDelete(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
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
    "assetDelete": {
      "deletedId": "019a6b2f-793e-807b-8001-555345529b44"
    }
  }
}
```

Including `version` ensures you don't accidentally delete an asset that someone else has modified. It's optional, but recommended. For more information on versioning, see [Optimistic locking](../optimistic-locking.md).
{% endstep %}
{% endstepper %}

## Listing assets

To list all assets for an organization, run the following query:

```graphql
query ListAssets {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      title
      type {
        code
        title
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

### Filtering

Use [AssetFilter](../assets/queries.md#assetfilter) to narrow results by type, linked GPS device, title, or custom field values. Conditions across different fields are combined with AND, while multiple values within a single field are combined with OR. For the full filter field reference and custom field filter operators, see [Filtering and sorting](../filtering-and-sorting.md#operators).

```graphql
query ListTrucks {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"]
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

To find all assets linked to a specific GPS device, run this query:

```graphql
query FindAssetByDevice {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      deviceIds: ["c3hhef22-2f3e-6hj1-ee9g-9ee2eg713d44"]
    }
    first: 5
  ) {
    nodes {
      id
      title
      primaryDevice {
        id
        title
      }
      devices {
        id
        title
      }
    }
  }
}
```

To filter assets by a custom field value, pass conditions to `customFields` in the filter. Each condition specifies a field `code`, a comparison `operator`, and a `value`. The following query finds all delivery trucks with a specific license plate:

```graphql
query FindTruckByPlate {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"]
      customFields: [
        { code: "license_plate", operator: EQ, value: { string: "HH-TL 4421" } }
      ]
    }
    first: 5
  ) {
    nodes {
      id
      title
      customFields(codes: ["license_plate"])
    }
  }
}
```

Multiple conditions in the `customFields` array are combined with AND.

### Ordering

Assets can be ordered by title (the default) or by any custom field using `customFieldCode`:

```graphql
query AssetsByLicensePlate {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    orderBy: { customFieldCode: "license_plate", direction: ASC }
    first: 20
  ) {
    nodes {
      id
      title
      customFields(codes: ["license_plate"])
    }
  }
}
```

{% hint style="warning" %}
`field` (an `AssetOrderField` enum) and `customFieldCode` are mutually exclusive — use one or the other. Valid values for `field` are defined in the [AssetOrderField enum](../assets/types.md#assetorderfield).
{% endhint %}

For details on pagination, see [Pagination](../pagination.md).

## Handling version conflicts

If you include `version` in your mutation and the entity has been modified since you last fetched it, the API returns a [conflict error](../error-handling.md#version-conflict-409):

```json
{
  "errors": [
    {
      "message": "Entity has been modified by another request",
      "path": ["assetUpdate"],
      "extensions": {
        "type": "https://api.navixy.com/errors/conflict",
        "title": "Optimistic Lock Conflict",
        "status": 409,
        "code": "CONFLICT",
        "entityType": "Asset",
        "entityId": "019a6b2f-793e-807b-8001-555345529b44",
        "expectedVersion": 1,
        "currentVersion": 2,
        "traceId": "0af7651916cd43dd8448eb211c80319c"
      }
    }
  ]
}
```

To resolve this, query the asset to get its current version and state, merge your intended changes, and retry the mutation with the updated version.

For a full explanation of how versioning works, see [Optimistic locking](../optimistic-locking.md).

### See also

* [Asset types and operations](../assets/): Complete reference for all asset operations and types
* [Organizing assets into groups](organizing-assets-into-groups.md): Collect assets into named groups by depot, project, or any other dimension
* [Implementing custom fields](implementing-custom-fields.md): Define the properties available to each asset type
