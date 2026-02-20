---
description: Define and use custom fields to attach domain-specific data to entities.
---

# Implementing custom fields

Devices, assets, geo objects, and schedules each come with a set of built-in fields such as `title`, `organization`, and `type`. These cover the core data the platform needs to function.

Custom fields let you extend any entity type with additional data specific to your operation. A fleet management company might need to track a vehicle's VIN number, fuel type, and next maintenance date on each asset. A logistics operator might want to record a SIM card number on each GPS device, or tag geo objects with access restriction levels. Custom fields make this possible without any schema changes on the platform side.

Custom fields are supported for devices, assets, geo objects, and schedules.

## How custom fields work

The [CustomFieldDefinition object](../custom-fields.md#customfielddefinition) describes the field you want to create: its machine-readable code, displayed title, data type, and validation rules. Think of it as designing a template: you decide what fields it has, what type of data each field accepts, and whether a value is required. You create definitions once, at the entity-type level.

Each individual record contains a value. When you create or update a device, an asset, or any other entity with a custom field, you supply values through the `customFields` field in the create or update mutation input. The API validates each value against the corresponding field's definition.

### Predefined and custom definitions

Definitions can be predefined or custom.

**Predefined definitions** already exist in the platform. The platform has the following predefined custom fields: `geojson`, `schedule_data` , and `device`.

**Custom definitions** are created by you and applied only to entities of a specific type. For example, a `vin` field defined on the [AssetType](../assets/types.md#assettype) called `vehicle` appears only on vehicle assets, not on equipment or employee assets. This is what you create and manage through the API, and what this guide covers.

## Scenario: Enriching fleet records with metadata

A logistics company is building an integration with Navixy Repository API. Their platform already uses devices, assets, and geo objects, but they need to store additional operational data on each entity type to support internal workflows and reporting.

Specifically, they need to track:

* On **vehicle assets**: the VIN number for compliance, the fuel type for route planning, and the next scheduled service date for maintenance management.
* On **GPS devices**: the SIM card number for connectivity troubleshooting and installation notes for field technicians.
* On **geo objects in the operations area**: access restrictions for dispatch rules and the date these restrictions come into effect.

Follow these steps to implement this metadata:

{% stepper %}
{% step %}
### Choose a field type

Before creating a definition, decide which `FieldType` best matches your data.

<details>

<summary>Field types reference</summary>

| Field type  | Use for                              | Key params                                                     | Example value                                      |
| ----------- | ------------------------------------ | -------------------------------------------------------------- | -------------------------------------------------- |
| `STRING`    | Short text, codes, identifiers       | `isRequired`, `minLength`, `maxLength`, `defaultValue`, `trim` | `"1HGBH41JXMN109186"`                              |
| `TEXT`      | Long descriptions, notes             | `isRequired`, `maxLength`, `defaultValue`, `trim`              | `"Installed under dashboard, driver side"`         |
| `NUMBER`    | Quantities, measurements             | `isRequired`, `min`, `max`, `precision`, `defaultValue`        | `42`, `3.14`                                       |
| `BOOLEAN`   | Flags, yes/no attributes             | `isRequired`, `defaultValue`                                   | `true`                                             |
| `DATE`      | Calendar dates                       | `isRequired`, `defaultValue`                                   | `"2025-06-01"`                                     |
| `DATETIME`  | Timestamps                           | `isRequired`, `defaultValue`                                   | `"2025-06-01T09:00:00Z"`                           |
| `OPTIONS`   | Predefined choices (single or multi) | `isRequired`, `isMulti`, `options[]`, `defaultValue`           | `"diesel"`                                         |
| `GEOJSON`   | Geometry data                        | `isRequired`, `allowedTypes`                                   | `{"type":"Point","coordinates":[...]}`             |
| `SCHEDULE`  | References to schedule definitions   | `isRequired`                                                   | [Schedule object](../schedules/types.md#schedule)  |
| `DEVICE`    | Links to device records              | `isRequired`, `isMulti`                                        | `"019a6a3f-..."`                                   |
| `REFERENCE` | Links to other entity records        | `isRequired`, `isMulti`, `refEntityTypeCode`                   | `"019a6a3f-..."`                                   |
| `CATALOG`   | Links to catalog items               | `isRequired`, `isMulti`, `refCatalogCode`                      | `"ITEM_CODE"`                                      |
| `TAG`       | Tags from a tag catalog              | `isRequired`, `isMulti`                                        | `"TAG_CODE"`                                       |

</details>

{% hint style="warning" %}
`fieldType` is immutable after creation. If you need to change a field's type, delete the definition and create a new one. Values already stored under that code in entity records remain in the JSON but will no longer have a backing definition.
{% endhint %}
{% endstep %}

{% step %}
### Create field definitions

To create a definition, you need three IDs:

* `organizationId` : the organization that owns the definition
* `ownerCatalogItemId`: the specific type the field belongs to (e.g., the `AssetType` for "vehicle", the `DeviceType` for "gps\_tracker")
* `targetEntityTypeId` : the broader entity type category (e.g., the `EntityType` for "asset", "device", or "geo\_object")

#### Check the existing definitions

Before adding new fields, check what's already defined in a type by querying `customFieldDefinitions` on the type object:

```graphql
query GetVehicleTypeFields {
  assetType(id: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11") {
    title
    customFieldDefinitions {
      code
      title
      fieldType
    }
  }
}
```

This works the same way for `deviceType`, `geoObjectType`, and `scheduleType`.

#### How field codes work

The [code](../common.md#code) you provide becomes the key used to read and write values in all entity mutations and queries. A code can contain ASCII letters, digits, underscores, dots, and hyphens, and must start with a letter or digit (max 64 characters). Uniqueness checks are case-insensitive. Predefined system fields use UPPER\_SNAKE\_CASE — user-defined codes can follow any valid format, though lowercase snake\_case is conventional.

#### How to create a STRING field (VIN on vehicle assets)

```graphql
mutation CreateVinField {
  customFieldDefinitionCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    ownerCatalogItemId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    targetEntityTypeId: "b2ffca99-1c0b-4ef8-bb6d-6bb9bd380a33"
    code: "vin"
    title: "VIN Number"
    description: "17-character Vehicle Identification Number"
    fieldType: STRING
    order: 1
    params: {
      string: {
        isRequired: true
        minLength: 17
        maxLength: 17
        trim: true
      }
    }
  }) {
    customFieldDefinition {
      id
      code
      fieldType
    }
  }
}
```

The response confirms creation and returns the definition's ID:

```json
{
  "data": {
    "customFieldDefinitionCreate": {
      "customFieldDefinition": {
        "id": "019b1c3d-905f-827b-8003-777567741d66",
        "code": "vin",
        "fieldType": "STRING"
      }
    }
  }
}
```

{% hint style="warning" %}
The `params` input uses the `@oneOf` directive — you must provide exactly one variant matching your `fieldType`.&#x20;

For `STRING`, provide `params: { string: { ... } }`.&#x20;

For `OPTIONS`, provide `params: { options: { ... } }`.&#x20;

Providing the wrong variant returns a validation error.
{% endhint %}

#### How to create an OPTIONS field (fuel type on vehicle assets)

```graphql
mutation CreateFuelTypeField {
  customFieldDefinitionCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    ownerCatalogItemId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    targetEntityTypeId: "b2ffca99-1c0b-4ef8-bb6d-6bb9bd380a33"
    code: "fuel_type"
    title: "Fuel Type"
    fieldType: OPTIONS
    order: 2
    params: {
      options: {
        isRequired: true
        isMulti: false
        options: [
          { code: "diesel",   label: "Diesel" }
          { code: "electric", label: "Electric" }
          { code: "hybrid",   label: "Hybrid" }
        ]
        defaultValue: "diesel"
      }
    }
  }) {
    customFieldDefinition {
      id
      code
    }
  }
}
```

Set `isMulti: true` if an entity can support more than one option. See [multi-value fields and filtering](working-with-custom-fields.md#constraints-and-considerations) for how this affects queries.

#### How to create a DATE field (next service date on vehicle assets)

```graphql
mutation CreateServiceDateField {
  customFieldDefinitionCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    ownerCatalogItemId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    targetEntityTypeId: "b2ffca99-1c0b-4ef8-bb6d-6bb9bd380a33"
    code: "next_service_date"
    title: "Next Service Date"
    fieldType: DATE
    order: 3
    params: {
      date: {
        isRequired: false
      }
    }
  }) {
    customFieldDefinition {
      id
      code
    }
  }
}
```

#### How to create fields for other entity types

The same pattern applies to devices and geo objects: only `ownerCatalogItemId`, `targetEntityTypeId`, and the `params` variant change.

**TEXT field for a GPS device type**:

```graphql
mutation CreateInstallationNotesField {
  customFieldDefinitionCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    ownerCatalogItemId: "c3eebc99-9c0b-4ef8-bb6d-6bb9bd380a44"
    targetEntityTypeId: "d4eebc99-9c0b-4ef8-bb6d-6bb9bd380a55"
    code: "installation_notes"
    title: "Installation Notes"
    fieldType: TEXT
    order: 1
    params: {
      text: {
        isRequired: false
        maxLength: 1000
        trim: false
      }
    }
  }) {
    customFieldDefinition {
      id
      code
    }
  }
}
```

**OPTIONS field for a geo object type**:

```graphql
mutation CreateAccessLevelField {
  customFieldDefinitionCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    ownerCatalogItemId: "e5eebc99-9c0b-4ef8-bb6d-6bb9bd380a66"
    targetEntityTypeId: "f6eebc99-9c0b-4ef8-bb6d-6bb9bd380a77"
    code: "access_level"
    title: "Access Level"
    fieldType: OPTIONS
    order: 1
    params: {
      options: {
        isRequired: true
        isMulti: false
        options: [
          { code: "open",       label: "Open" }
          { code: "restricted", label: "Restricted" }
          { code: "locked",     label: "Locked" }
        ]
        defaultValue: "open"
      }
    }
  }) {
    customFieldDefinition {
      id
      code
    }
  }
}
```
{% endstep %}

{% step %}
### Set and update values

Pass `customFields` in the create mutation with the initial values under `set`. The following example creates a vehicle asset with all three fields populated:

```graphql
mutation CreateVehicleAsset {
  assetCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Truck 12"
    customFields: {
      set: {
        "vin":               "1HGBH41JXMN109186"
        "fuel_type":         "diesel"
        "next_service_date": "2025-09-01"
      }
    }
  }) {
    asset {
      id
      version
      customFields
    }
  }
}
```

The same pattern applies to `deviceCreate`, `geoObjectCreate`, and `scheduleCreate`.
{% endstep %}

{% step %}
### Update custom field values

Custom field updates use a **patch model** — you only specify what changes. Include a code in `set` to add or overwrite it, include it in `unset` to remove it, or omit it entirely to leave it unchanged.

The following example updates the SIM card number on a device and removes its installation notes:

```graphql
mutation UpdateTrackerFields {
  deviceUpdate(input: {
    id: "019a6c3f-894e-817b-8002-666456630c55"
    version: 3
    customFields: {
      set:   { "sim_card": "8931010000000000001" }
      unset: ["installation_notes"]
    }
  }) {
    device {
      id
      version
      customFields
    }
  }
}
```

{% hint style="info" %}
All entity update mutations require the current `version` for [optimistic locking](https://claude.ai/chat/optimistic-locking.md). Fetch the entity first if you don't have the latest version.
{% endhint %}
{% endstep %}

{% step %}
### Read custom field values

`customFields` on any entity returns a JSON object keyed by field code. By default, all fields are returned.

```graphql
query GetAssetFields {
  asset(id: "019a6b2f-793e-807b-8001-555345529b44") {
    title
    customFields
  }
}
```

Response:

```json
{
  "data": {
    "asset": {
      "title": "Truck 12",
      "customFields": {
        "vin": "1HGBH41JXMN109186",
        "fuel_type": "diesel",
        "next_service_date": "2025-09-01"
      }
    }
  }
}
```

To retrieve only specific fields, pass the `codes` argument. This keeps response payloads smaller when an entity type has many fields:

```graphql
query GetVehicleKeyFields {
  asset(id: "YOUR_ASSET_ID") {
    title
    customFields(codes: ["vin", "fuel_type"])
  }
}
```
{% endstep %}

{% step %}
### Filter entities by custom field value

All entity list queries support filtering by custom field values through [CustomFieldFilter](../custom-fields.md#customfieldfilter). Add one or more conditions to the `customFields` filter array. Multiple conditions are applied as AND.

#### How to filter by an OPTIONS value

Find all electric vehicle assets:

```graphql
query FindElectricVehicles {
  assets(filter: {
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    customFields: [
      { code: "fuel_type", operator: EQ, value: "electric" }
    ]
  }) {
    nodes {
      id
      title
      customFields(codes: ["fuel_type", "next_service_date"])
    }
  }
}
```

#### How to filter by a DATE value

Find vehicles with a service date before a deadline:

```graphql
query FindOverdueVehicles {
  assets(filter: {
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    customFields: [
      { code: "next_service_date", operator: LT, value: "2025-07-01" }
    ]
  }) {
    nodes {
      id
      title
      customFields(codes: ["next_service_date"])
    }
  }
}
```

#### Combine multiple conditions

Find devices with a specific SIM card prefix that don't yet have installation notes:

```graphql
query FindUndocumentedTrackers {
  devices(filter: {
    typeId: "c3eebc99-9c0b-4ef8-bb6d-6bb9bd380a44"
    customFields: [
      { code: "sim_card",           operator: CONTAINS, value: "8931" }
      { code: "installation_notes", operator: IS_NULL               }
    ]
  }) {
    nodes {
      id
      title
    }
  }
}
```

{% hint style="info" %}
Omit `value` (or set it to `null`) when using the `IS_NULL` and `IS_NOT_NULL` operators.
{% endhint %}

For the full operator list and value formats by field type, see [Filtering and sorting](https://claude.ai/chat/filtering-and-sorting.md#custom-field-filtering).
{% endstep %}
{% endstepper %}

## Managing definitions

### Updating a definition

You can update the `title`, `description`, `order`, and `params`. The `code` and `fieldType` cannot be changed after creation. Updates use [optimistic locking](../optimistic-locking.md) and require the current `version`:

```graphql
mutation UpdateVinField {
  customFieldDefinitionUpdate(input: {
    id: "019b1c3d-905f-827b-8003-777567741d66"
    version: 1
    title: "VIN"
    description: "Vehicle Identification Number (17 characters, no I/O/Q)"
    params: {
      string: {
        isRequired: true
        minLength: 17
        maxLength: 17
        trim: true
      }
    }
  }) {
    customFieldDefinition {
      id
      version
      title
    }
  }
}
```

For OPTIONS fields, you can add new options or archive existing ones. Archiving an option (`isArchived: true`) hides it from new selections without affecting records that already carry it:

```graphql
params: {
  options: {
    isRequired: true
    isMulti: false
    options: [
      { code: "diesel",   label: "Diesel",   isArchived: false }
      { code: "electric", label: "Electric", isArchived: false }
      { code: "hybrid",   label: "Hybrid",   isArchived: false }
      { code: "hydrogen", label: "Hydrogen", isArchived: false }
      { code: "lpg",      label: "LPG",      isArchived: true  }
    ]
  }
}
```

### Deleting a definition

Use this query:

```graphql
mutation DeleteDefinition {
  customFieldDefinitionDelete(input: {
    id: "YOUR_DEFINITION_ID"
    version: 2
  }) {
    deletedId
  }
}
```

{% hint style="info" %}
Deleting a definition removes its key from the `customFields` JSON on all entity records. If you create a new definition with the same `code` later, existing records will not retain any value for it — the data is not preserved.
{% endhint %}

## Constraints and considerations

Keep in mind the following:

* **`fieldType` is immutable:** To change a field's type, delete the definition and create a new one. Existing values stored under that code become orphaned but are not erased.
* **`code` is stable once in use:** `code` must be unique within the owner type and organization. As this is the key used to read and write values across all entity mutations and queries, avoid recreating it under a different name if records contain values paired with it.
* **`params` requires exactly one variant:** `FieldParamsInput` uses the `@oneOf` directive, so you must provide exactly the variant that matches your `fieldType`. Providing `string: { ... }` when `fieldType` is `NUMBER` returns a validation error.
* **Multi-value fields and filtering:** For fields with `isMulti: true`, a filter matches if _any_ value in the array satisfies the condition. For example, if an asset has `fuel_type: ["diesel", "hybrid"]`, filtering with `EQ: "diesel"` will match it.
* **Predefined fields:** Predefined definitions (like `geojson` and `schedule_data`) are platform-managed and appear in `customFields` responses alongside your definitions. Do not use codes that conflict with predefined field codes.

### See also

* [Filtering and sorting](https://claude.ai/chat/filtering-and-sorting.md): full operator reference and value formats for custom field filters
* [Optimistic locking](https://claude.ai/chat/optimistic-locking.md): how `version` works in update and delete mutations
