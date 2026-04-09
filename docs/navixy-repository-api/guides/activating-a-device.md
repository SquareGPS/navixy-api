---
description: Register and manage GPS trackers, sensors, and other hardware devices.
---

# Working with devices

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

A device in Navixy Repository API represents a physical hardware unit — a GPS tracker, sensor, beacon, or any other piece of trackable hardware. Devices carry the identifying information, such as IMEI numbers and serial numbers, that connects physical hardware to the rest of your platform data. When linked to an asset through a DEVICE-type custom field, a device enables tracking data to flow from the field into the platform. You can traverse this link from either direction: the asset exposes its linked devices via `primaryDevice` and `devices`, while the device exposes its parent asset via the `asset` field.

This guide covers the full device lifecycle: looking up catalog prerequisites, registering a device, managing its identifiers, creating device relations, updating device properties, and decommissioning it.

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

Use the `id` of the organization you want to work with for all subsequent device operations.

You also need IDs for three catalog entities before you can create a device:

* **Device type**: a classification you define (for example, "GPS Tracker" or "Beacon")
* **Device status**: an operational state you define (for example, "In Stock", "Active", or "Decommissioned")
* **Device model**: the specific hardware model, sourced from the read-only model catalog

To check what types and statuses already exist in your organization:

```graphql
query GetDeviceCatalog {
  deviceTypes(organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7") {
    nodes { id title code }
  }
  deviceStatuses(organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7") {
    nodes { id title code }
  }
}
```

If the results are empty, create the entries you need:

```graphql
mutation CreateDeviceCatalog {
  deviceTypeCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    title: "GPS Tracker"
    code: "gps_tracker"
  }) {
    deviceType { id code }
  }
  deviceStatusCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    title: "In Stock"
    code: "in_stock"
  }) {
    deviceStatus { id code }
  }
}
```

To look up a hardware model, query the read-only model catalog. You can filter by title or vendor:

```graphql
query FindDeviceModel {
  deviceModels(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: { titleContains: "FMB003" }
  ) {
    nodes { id title code vendor { id title } }
  }
}
```

If you need to browse models by manufacturer first, use the `deviceVendors` query to get vendor IDs, then pass them to `deviceModels` via `filter.vendorIds`.

Save the returned IDs — you'll need all three to create a device.

## Understanding devices

### Device identifiers

Each device can carry one or more hardware identifiers that serve as the bridge between the platform record and the physical hardware. Telematics servers and provisioning systems use these identifiers to look up a device.

The available identifier types are defined by the [DeviceIdType](../devices/types.md#enums) enum:

<table><thead><tr><th width="198">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>IMEI</code></td><td>15-digit International Mobile Equipment Identity</td></tr><tr><td><code>SERIAL_NUMBER</code></td><td>Manufacturer-assigned serial number</td></tr><tr><td><code>MAC_ADDRESS</code></td><td>Network interface MAC address</td></tr><tr><td><code>GUID</code></td><td>GUID/UUID identifier</td></tr><tr><td><code>MEID_HEX</code></td><td>Mobile Equipment Identifier, hexadecimal format</td></tr><tr><td><code>MEID_DEC</code></td><td>Mobile Equipment Identifier, decimal format</td></tr><tr><td><code>CUSTOM</code></td><td>Organization-defined identifier</td></tr></tbody></table>

Identifier uniqueness is enforced globally on the combination of `type`, `value`, and `namespace`. For standard hardware identifier types (`IMEI`, `SERIAL_NUMBER`, `MAC_ADDRESS`, etc.), `namespace` is always `null`, meaning the value must be unique across the entire platform. For `CUSTOM` identifiers, you can set a `namespace` string to scope the uniqueness constraint: two devices can share the same custom value as long as they carry different namespaces. This is useful when integrating with external systems that have their own ID schemes and whose values may overlap.

### Device status and properties

Devices don't support custom fields. The mutable properties are `title`, `modelId`, and `statusId`. Status is the primary way to represent a device's operational state — in stock, deployed, under repair, or decommissioned. You define the statuses that fit your workflow.

The device type is set at creation and cannot be changed afterwards.

#### Asset link

The `asset` field returns the asset this device is currently linked to, or `null` if the device isn't assigned to any asset. This is the reverse of the asset-to-device relationship — assets link to devices through custom fields of type DEVICE, and `Device.asset` resolves that link from the other direction. The link is managed entirely from the asset side. See [Working with assets](working-with-assets.md) for details.

### Device relations

Two devices can be linked with a typed relation. Relation types are system-defined — your organization cannot create new ones. To see what types are available, use the `deviceRelationTypes` query:

```graphql
query GetRelationTypes {
  deviceRelationTypes(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
  ) {
    nodes { id title code }
  }
}
```

A relation has two endpoints: `first` and `second`. The device the relation was created from exposes it under `relationsFrom`, while the device on the other end exposes it under `relationsTo`. The distinction is positional but carries no enforced platform-level meaning — your application decides how to interpret it.

## Example scenario: Onboarding a tracker shipment

FleetOps Ltd receives a shipment of Teltonika FMB003 GPS trackers for installation across their delivery fleet. This scenario walks through registering a device, recording its identifiers, linking it to a companion beacon, updating its status once installed, and decommissioning it at end of life.

{% stepper %}
{% step %}
### Create a device

Register the first device using the type, model, and status IDs from the prerequisites step.

{% hint style="info" %}
`version` is optional — omitting it applies the update unconditionally without conflict detection. Include it whenever you want to guard against overwriting concurrent changes. See [Optimistic locking](../optimistic-locking.md) for details. In this example, we'll be using this field.
{% endhint %}

Run this mutation:

```graphql
mutation RegisterDevice {
  deviceCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "b8e3c1f0-1d2a-4e5b-9c8d-111222333444"
    modelId: "c9f4d2e1-2e3b-5f6c-ad9e-222333444555"
    statusId: "d0a5e3f2-3f4c-6a7d-be0f-333444555666"
    title: "FMB003 — Unit 001"
  }) {
    device {
      id
      version
      title
      type { title }
      model { title vendor { title } }
      status { title }
      asset { id title }
    }
  }
}
```

Response:

```json
{
  "data": {
    "deviceCreate": {
      "device": {
        "id": "e1b6f4a3-4a5d-7b8e-cf10-444555666777",
        "version": 1,
        "title": "FMB003 — Unit 001",
        "type": { "title": "GPS Tracker" },
        "model": { "title": "FMB003", "vendor": { "title": "Teltonika" } },
        "status": { "title": "In Stock" },
        "asset": null
      }
    }
  }
}
```

Save the `id` and `version` — you'll need both for subsequent operations.
{% endstep %}

{% step %}
### Add identifiers

Add the hardware identifiers for the device. Each identifier is added in a separate `deviceIdentifierAdd` call, though you can batch multiple calls in a single request using aliases.

{% hint style="info" %}
Identifiers passed to `deviceCreate` via the `identifiers` input field do not persist in the current implementation. Add them using `deviceIdentifierAdd` after creating the device.
{% endhint %}

```graphql
mutation AddDeviceIdentifiers {
  imei: deviceIdentifierAdd(input: {
    deviceId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    identifier: {
      type: IMEI
      value: "356307042772396"
    }
  }) {
    deviceIdentifier { id type value namespace }
  }
  serial: deviceIdentifierAdd(input: {
    deviceId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    identifier: {
      type: SERIAL_NUMBER
      value: "TLT-2024-00391"
    }
  }) {
    deviceIdentifier { id type value namespace }
  }
}
```

Response:

```json
{
  "data": {
    "imei": {
      "deviceIdentifier": {
        "id": "f2c7a5b4-5b6e-8c9f-d011-555666777888",
        "type": "IMEI",
        "value": "356307042772396",
        "namespace": null
      }
    },
    "serial": {
      "deviceIdentifier": {
        "id": "a3d8b6c5-6c7f-9d0a-e122-666777888999",
        "type": "SERIAL_NUMBER",
        "value": "TLT-2024-00391",
        "namespace": null
      }
    }
  }
}
```

Both identifiers have `namespace: null`, meaning they are globally unique. Attempting to register the same IMEI on another device returns a `409 DUPLICATE` error.

To correct a mistakenly entered identifier, remove it using its `id`:

```graphql
mutation RemoveIdentifier {
  deviceIdentifierRemove(input: {
    identifierId: "f2c7a5b4-5b6e-8c9f-d011-555666777888"
  }) {
    deletedId
  }
}
```
{% endstep %}

{% step %}
### Assign device to an asset

FMB003 Unit 001 will track delivery truck DE-1049. To link the device, update the asset's DEVICE-type custom field. We'll assume the asset's type already has a custom field definition of `DEVICE` type. See [Implementing custom fields](implementing-custom-fields.md) for instructions on setting it up.

```graphql
mutation AssignDeviceToAsset {
  assetUpdate(input: {
    id: "a4c9d5e6-6d8f-4a1b-b234-777888999000"
    version: 1
    customFields: {
      set: { "tracker": "e1b6f4a3-4a5d-7b8e-cf10-444555666777" }
      setPrimary: ["tracker"]
    }
  }) {
    asset {
      id
      title
      primaryDevice { id title }
      devices { id title }
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
        "id": "a4c9d5e6-6d8f-4a1b-b234-777888999000",
        "title": "Truck DE-1049",
        "primaryDevice": {
          "id": "e1b6f4a3-4a5d-7b8e-cf10-444555666777",
          "title": "FMB003 — Unit 001"
        },
        "devices": [
          {
            "id": "e1b6f4a3-4a5d-7b8e-cf10-444555666777",
            "title": "FMB003 — Unit 001"
          }
        ]
      }
    }
  }
}
```

{% hint style="warning" %}
The `tracker` key in `set` is the code of the `DEVICE`-type custom field defined on the asset type, not a fixed keyword. `setPrimary` marks that field as the primary device for the asset, which makes it available through `Asset.primaryDevice`.
{% endhint %}

You can verify the link from the device side:

```graphql
query CheckAssetLink {
  device(id: "e1b6f4a3-4a5d-7b8e-cf10-444555666777") {
    id
    title
    asset { id title }
  }
}
```

Each device can be linked to only one asset. Attempting to assign a device that is already linked to a different asset returns a [409 Duplicate](../error-handling.md#duplicate-409) error.

To unlink the device later without deleting it, use `unset` and `unsetPrimary` on the asset:

```graphql
customFields: {
  unset: ["tracker"]
  unsetPrimary: ["tracker"]
}
```
{% endstep %}

{% step %}
### Create a device relation

FMB003 Unit 001 will be installed in the same vehicle as a Teltonika EYE beacon used for cargo monitoring. Link the two devices with a relation.

Start by looking up the available relation types for your organization:

```graphql
query GetRelationTypes {
  deviceRelationTypes(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
  ) {
    nodes { id title code }
  }
}
```

Then create the relation using the IDs of both devices and the relation type you want:

```graphql
mutation LinkDevices {
  deviceRelationCreate(input: {
    firstId: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    secondId: "b4e9c7d6-7d8a-0e1b-f233-777888999aaa"
    typeId: "c5fad8e7-8e9b-1f2c-a344-888999aaabbb"
  }) {
    deviceRelation {
      id
      first { id title }
      second { id title }
      type { title }
    }
  }
}
```

Response:

```json
{
  "data": {
    "deviceRelationCreate": {
      "deviceRelation": {
        "id": "d6abe9f8-9f0c-2a3d-b455-999aaabbbccc",
        "first": {
          "id": "e1b6f4a3-4a5d-7b8e-cf10-444555666777",
          "title": "FMB003 — Unit 001"
        },
        "second": {
          "id": "b4e9c7d6-7d8a-0e1b-f233-777888999aaa",
          "title": "EYE Beacon — Unit 001"
        },
        "type": { "title": "Primary/Accessory" }
      }
    }
  }
}
```

To remove the relation when the devices are separated, use `deviceRelationRemove` with the relation's `id`:

```graphql
mutation UnlinkDevices {
  deviceRelationRemove(input: {
    id: "d6abe9f8-9f0c-2a3d-b455-999aaabbbccc"
  }) {
    deletedId
  }
}
```
{% endstep %}

{% step %}
#### Update a device

When Unit 001 is installed in a delivery truck, update its status to reflect the change. You can update the title, model, or status in the same mutation.

```graphql
mutation DeployDevice {
  deviceUpdate(input: {
    id: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    version: 1
    statusId: "e2c8f5a4-5a6e-8b9f-c010-444555666778"
    title: "FMB003 — Unit 001 (Truck 14)"
  }) {
    device {
      id
      version
      title
      status { title }
      asset { id title }
    }
  }
}
```

Response:

```json
{
  "data": {
    "deviceUpdate": {
      "device": {
        "id": "e1b6f4a3-4a5d-7b8e-cf10-444555666777",
        "version": 2,
        "title": "FMB003 — Unit 001 (Truck 14)",
        "status": { "title": "Active" },
         "asset": {
          "id": "a4c9d5e6-6d8f-4a1b-b234-777888999000",
          "title": "Truck DE-1049"
        }
      }
    }
  }
}
```

{% hint style="info" %}
Providing `version` enables optimistic locking: if the device has been modified since you last fetched it, the API returns a [409 Conflict](../error-handling.md#version-conflict-409) error instead of silently overwriting the change. Omitting `version` applies the update unconditionally. See [Handling version conflicts](https://claude.ai/chat/6095d343-b927-45b6-9d85-e36725bb212d#handling-version-conflicts) for details.&#x20;
{% endhint %}
{% endstep %}

{% step %}
### Delete a device

When a tracker reaches end of life and needs to be permanently removed, use `deviceDelete`.&#x20;

If the device is still linked to an asset, consider unlinking it first by updating the asset's custom fields. Otherwise, the `DEVICE`-type field value is automatically cleared on deletion, but the asset type retains the field definition. To unlink the asset, run this mutation:

```graphql
mutation UnlinkBeforeDelete {
assetUpdate(input: {
id: "a4c9d5e6-6d8f-4a1b-b234-777888999000"
version: 2
customFields: {
unset: ["tracker"]
unsetPrimary: ["tracker"]
}
}) {
asset { id primaryDevice { id } devices { id } }
}
}
```

Then delete the device:

```graphql
mutation DecommissionDevice {
  deviceDelete(input: {
    id: "e1b6f4a3-4a5d-7b8e-cf10-444555666777"
    version: 2
  }) {
    deletedId
  }
}
```

{% hint style="warning" %}
If the device is still linked to an asset, unlink it first by updating the asset's custom fields. Deleting a device doesn't clear the reference from the asset: the `DEVICE`-type field retains the deleted device's ID, but `primaryDevice` and `devices` resolve to `null` and empty, respectively.
{% endhint %}
{% endstep %}
{% endstepper %}

## Listing devices

To list all devices in an organization:

```graphql
query ListDevices {
  devices(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      title
      type { title }
      model { title vendor { title } }
      status { title }
      identifiers { type value namespace }
      asset { id title }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

## Filtering

Use [DeviceFilter](../devices/types.md#devicefilter) to narrow results. Conditions across different fields are combined with AND; multiple values within a single field are combined with OR. For the full filter reference, see [Filtering and sorting](../filtering-and-sorting.md).

Common filter combinations:

```graphql
query FindActiveTrackers {
  devices(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["b8e3c1f0-1d2a-4e5b-9c8d-111222333444"]
      statusIds: ["e2c8f5a4-5a6e-8b9f-c010-444555666778"]
    }
    first: 20
  ) {
    nodes {
      id
      title
      status { title }
    }
  }
}
```

[DeviceFilter](../devices/types.md#devicefilter) supports the following fields:

| Field                | Description                                             |
| -------------------- | ------------------------------------------------------- |
| `typeIds`            | One or more device type IDs                             |
| `modelIds`           | One or more device model IDs                            |
| `statusIds`          | One or more device status IDs                           |
| `vendorIds`          | One or more manufacturer IDs                            |
| `inventoryIds`       | One or more inventory IDs                               |
| `titleContains`      | Partial, case-insensitive match on the device title     |
| `identifierContains` | Partial, case-insensitive match on any identifier value |

`identifierContains` is particularly useful for looking up a device by a partial IMEI or serial number:

```graphql
query FindByIMEI {
  devices(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: { identifierContains: "356307" }
    first: 5
  ) {
    nodes {
      id
      title
      identifiers { type value }
    }
  }
}
```

## Handling version conflicts

If you provide `version` in `deviceUpdate` or `deviceDelete` and the device has been modified by another request since your last fetch, the API returns a `409 CONFLICT` error:

```json
{
  "errors": [{
    "message": "Entity has been modified by another request",
    "extensions": {
      "code": "CONFLICT",
      "entityType": "Device",
      "entityId": "e1b6f4a3-4a5d-7b8e-cf10-444555666777",
      "expectedVersion": 1,
      "currentVersion": 2
    }
  }]
}
```

To resolve this, fetch the device again to get its current version and state, reconcile any differences with your intended changes, and retry the mutation with the updated version.

For a full explanation of how versioning works, see [Optimistic locking](https://claude.ai/chat/optimistic-locking.md).

### See also

* [Managing device inventory](https://claude.ai/chat/managing-device-inventory.md): Assign devices to inventories and track assignment history, designate a primary device
* [Working with assets](https://claude.ai/chat/working-with-assets.md): Link devices to tracked assets
* [Devices reference](https://claude.ai/chat/6095d343-b927-45b6-9d85-e36725bb212d): Complete reference for all device operations and types
