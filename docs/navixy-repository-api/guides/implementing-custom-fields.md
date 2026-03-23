---
description: Define and use custom fields to attach domain-specific data to entities.
---

# Implementing custom fields

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

In Navixy Repository API, devices, assets, geo objects, and schedules each come with a set of built-in fields such as `title`, `organization`, and `type`. Custom fields let you extend these entities with additional data specific to your operation, such as a VIN number, a fuel type, an inspection date, or access level, without any changes to the platform schema.

## How custom fields work

Custom fields can be user-defined or predefined. User-defined fields are created by you and scoped to a specific entity type — for example, a `vin` field that only appears in vehicles. Predefined fields are built into the platform for certain entity types, such as `geojson_data` in geo objects.

{% hint style="warning" %}
This guide covers user-defined fields. Avoid using predefined field codes (`geojson_data`, `device`, and `schedule_data`) for creating your own fields.
{% endhint %}

Every custom field has a [FieldType](../custom-fields.md#fieldtype) that determines what kind of data it stores and what validation options are available. You can add any number of fields with different types to a given entity type.

### Field type reference

<table><thead><tr><th width="135.4444580078125">Field type</th><th>Use for</th><th>Key params</th><th>Example value</th></tr></thead><tbody><tr><td><code>STRING</code></td><td>Short text, codes, identifiers</td><td><code>isRequired</code>, <code>minLength</code>, <code>maxLength</code>, <code>defaultValue</code>, <code>trim</code></td><td><code>"1HGBH41JXMN109186"</code></td></tr><tr><td><code>TEXT</code></td><td>Long descriptions, notes</td><td><code>isRequired</code>, <code>maxLength</code>, <code>defaultValue</code>, <code>trim</code></td><td><code>"Installed under dashboard, driver side"</code></td></tr><tr><td><code>NUMBER</code></td><td>Quantities, measurements</td><td><code>isRequired</code>, <code>min</code>, <code>max</code>, <code>precision</code>, <code>defaultValue</code></td><td><code>42</code>, <code>3.14</code></td></tr><tr><td><code>BOOLEAN</code></td><td>Flags, yes/no attributes</td><td><code>isRequired</code>, <code>defaultValue</code></td><td><code>true</code></td></tr><tr><td><code>DATE</code></td><td>Calendar dates</td><td><code>isRequired</code>, <code>defaultValue</code></td><td><code>"2025-06-01"</code></td></tr><tr><td><code>DATETIME</code></td><td>Timestamps</td><td><code>isRequired</code>, <code>defaultValue</code></td><td><code>"2025-06-01T09:00:00Z"</code></td></tr><tr><td><code>OPTIONS</code></td><td>Predefined choices (single or multi)</td><td><code>isRequired</code>, <code>isMulti</code>, <code>options[]</code>, <code>defaultValue</code></td><td><code>"diesel"</code></td></tr><tr><td><code>GEOJSON</code></td><td>Geometry data</td><td><code>isRequired</code>, <code>allowedTypes</code> (<a href="../geo-objects/types.md#geojsongeometrytype">GeoJsonGeometryType</a>)</td><td><code>{"type":"Point","coordinates":[...]}</code></td></tr><tr><td><code>SCHEDULE</code></td><td>References to schedule definitions</td><td><code>isRequired</code></td><td><a href="../schedules.md#schedule">Schedule object</a></td></tr><tr><td><code>DEVICE</code></td><td>Links to device records</td><td><code>isRequired</code>, <code>isMulti</code></td><td><code>"019a6a3f-..."</code></td></tr><tr><td><code>REFERENCE</code></td><td>Links to other entity records</td><td><code>isRequired</code>, <code>isMulti</code>, <code>refEntityTypeCode</code></td><td><code>"019a6a3f-..."</code></td></tr><tr><td><code>CATALOG</code></td><td>Links to catalog items</td><td><code>isRequired</code>, <code>isMulti</code>, <code>refCatalogCode</code></td><td><code>"ITEM_CODE"</code></td></tr><tr><td><code>TAG</code></td><td>Tags from a tag catalog</td><td><code>isRequired</code>, <code>isMulti</code></td><td><code>"TAG_CODE"</code></td></tr></tbody></table>

Each field is defined by [CustomFieldDefinition](../custom-fields.md#customfielddefinition), a metadata record that specifies the field's code, display title, type, and validation rules. When you create or update an entity, you supply field values through the `customFields` field in the mutation input, and the API validates each value against the corresponding definition.

### Writing custom field values

`customFields` in any create or update mutation accepts a [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) with two sub-fields:

<table><thead><tr><th width="169">Field</th><th width="125.44451904296875">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>set</code></td><td><a href="../common.md#json">JSON</a></td><td>Key-value map of fields to create or overwrite.</td></tr><tr><td><code>unset</code></td><td>[<a href="../common.md#code">Code</a>!]</td><td>List of field codes to remove entirely.</td></tr></tbody></table>

This is the **patch model**: fields you don't mention are left unchanged. You can `set` and `unset` in the same mutation. For example, to update a license plate and remove an assigned driver in one call, add this code:

```graphql
customFields: {
  set:   { license_plate: "HH-TL 4421" }
  unset: ["assigned_driver"]
}
```

Omitting `customFields` altogether leaves all existing values untouched.

## Scenario: Enriching fleet records with metadata

A logistics company needs to store operational metadata on their vehicle assets: a VIN number for compliance, a fuel type for route planning, and a next service date for maintenance management. All examples in this guide use these three fields.

Adding this metadata requires the following steps:

{% stepper %}
{% step %}
#### **Choose a field type**

Before creating a definition, pick the `fieldType` that best matches your data. See the [field type reference](implementing-custom-fields.md#field-type-reference).

{% hint style="warning" %}
`fieldType` is immutable after creation. If you need to change a field's type, delete the definition and create a new one. Values already stored under that code in entity records remain in the JSON but will no longer have a backing definition.
{% endhint %}
{% endstep %}

{% step %}
#### **Create field definitions**

Custom field definitions belong to a catalog item. In this scenario, this is an `AssetType` such as "Vehicle". To add definitions, pass them inline when updating the parent type via [assetTypeUpdate](../assets/mutations.md#assettypeupdate). All operations are atomic: the definitions are created, updated, or deleted as part of a single mutation under one parent `version`.

{% hint style="info" %}
The `version` field is optional (see [Optimistic locking](../optimistic-locking.md)) but recommended when modifying a shared catalog item that other users may be editing concurrently.
{% endhint %}

**2.1 Check the existing definitions**

Before adding new fields, check what's already defined in a type by querying `customFieldDefinitions` on the type object:

```graphql
query GetVehicleTypeFields {
  assetType(id: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11") {
    title
    customFieldDefinitions {
      code
      title
      fieldType
      isArchived
    }
  }
}
```

Response (if the fields already exist):

```json
{
  "data": {
    "assetType": {
      "title": "Vehicle",
      "customFieldDefinitions": [
        {
          "code": "vin",
          "title": "VIN Number",
          "fieldType": "STRING",
          "isArchived": false
        },
        {
          "code": "fuel_type",
          "title": "Fuel Type",
          "fieldType": "OPTIONS",
          "isArchived": false
        }
      ]
    }
  }
}
```

If no custom fields have been created yet, `customFieldDefinitions` is an empty array. The query works the same way for `deviceType` and `geoObjectType`.

**2.2 Choose codes for your fields**

Choose a [code](../common.md#code) for each field before creating its definition. The code becomes the key used to read and write values in all entity mutations and queries, so treat it as stable once records carry values under it — changing it later means recreating the definition and losing existing data.

If you omit `code`, it's auto-generated from `title` (transliterated to lowercase Latin, spaces replaced with `_`, truncated at 40 characters, with a numeric suffix on collision). Explicitly setting a code gives you control over how that key appears in your data.

Codes can contain ASCII letters, digits, underscores, dots, and hyphens, and must start with a letter or digit (max 64 characters).

**2.3 Create the field definitions**

Add all three fields in a single mutation. Each entry in `customFieldDefinitions` uses the `create` variant of the [@oneOf](../core-api-reference/directives.md#oneof) input:

```graphql
mutation AddVehicleFields {
  assetTypeUpdate(input: {
    id: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    version: 1
    customFieldDefinitions: [

      # STRING field (VIN number)
      { create: {
          code:        "vin"
          title:       "VIN Number"
          description: "17-character Vehicle Identification Number"
          fieldType:   STRING
          order:       1
          params: {
            string: {
              isRequired: true
              minLength:  17
              maxLength:  17
              trim:       true
            }
          }
      }},

      # OPTIONS field (fuel type with predefined choices)
      { create: {
          code:      "fuel_type"
          title:     "Fuel Type"
          fieldType: OPTIONS
          order:     2
          params: {
            options: {
              isRequired:   true
              isMulti:      false
              defaultValue: "diesel"
              options: [
                { code: "diesel",   label: "Diesel" }
                { code: "electric", label: "Electric" }
                { code: "hybrid",   label: "Hybrid" }
              ]
            }
          }
      }},

      # DATE field (next scheduled service)
      { create: {
          code:      "next_service_date"
          title:     "Next Service Date"
          fieldType: DATE
          order:     3
          params: {
            date: {
              isRequired: false
            }
          }
      }}

    ]
  }) {
    assetType {
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

The response returns the updated type with incremented `version` and the full list of definitions:

```json
{
  "data": {
    "assetTypeUpdate": {
      "assetType": {
        "version": 2,
        "customFieldDefinitions": [
          { "code": "vin",               "title": "VIN Number",       "fieldType": "STRING" },
          { "code": "fuel_type",         "title": "Fuel Type",        "fieldType": "OPTIONS" },
          { "code": "next_service_date", "title": "Next Service Date", "fieldType": "DATE" }
        ]
      }
    }
  }
}
```

{% hint style="warning" %}
The `params` input uses the [@oneOf](../core-api-reference/directives.md#oneof) directive. You must provide exactly one variant matching your `fieldType`.

Each field type has its own named params block. The example above demonstrates this: the VIN field uses `params: { string: { ... } }`, the fuel type field uses `params: { options: { ... } }`, and the service date field uses `params: { date: { ... } }`. Providing the wrong variant returns a [validation error](../error-handling.md#validation-error-400).&#x20;
{% endhint %}

The same pattern applies to [geoObjectTypeUpdate](../geo-objects/mutations.md#geoobjecttypeupdate) — only the parent type's input changes. Only `create` is allowed for a catalog item creation mutation such as [assetTypeCreate](../assets/mutations.md#assettypecreate). The full set of operations (`update`, `delete`, `archive`, `restore`) is available for [assetTypeUpdate](../assets/mutations.md#assettypeupdate).&#x20;

#### **Set and update values**

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

The response returns the created asset's `id`, `version`, and `customFields`:

```json
{
  "data": {
    "assetCreate": {
      "asset": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 1,
        "customFields": {
          "vin": "1HGBH41JXMN109186",
          "fuel_type": "diesel",
          "next_service_date": "2025-09-01"
        }
      }
    }
  }
}
```

{% hint style="warning" %}
If any custom field value fails validation, the entire mutation is rejected with a [validation error](../error-handling.md#validation-error-400). Common causes include a value that violates the field's params constraints (for example, a VIN shorter than 17 characters), an unrecognized field code, or a value of the wrong type. The error response includes a field path and a detail message identifying the problem. See [Error handling](../error-handling.md) for the full error format.
{% endhint %}

The same pattern applies to `geoObjectCreate` and `scheduleCreate`.
{% endstep %}

{% step %}
#### **Set and update values**

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

The response returns the created asset's `id`, `version`, and `customFields`:

```json
{
  "data": {
    "assetCreate": {
      "asset": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 1,
        "customFields": {
          "vin": "1HGBH41JXMN109186",
          "fuel_type": "diesel",
          "next_service_date": "2025-09-01"
        }
      }
    }
  }
}
```

{% hint style="warning" %}
If any custom field value fails validation, the entire mutation is rejected with a [validation error](../error-handling.md#validation-error-400). Common causes include a value that violates the field's `params` constraints (for example, a VIN shorter than 17 characters), an unrecognized field code, or a value of the wrong type. The error response includes a `field` path and a `detail` message identifying the problem. See [Error handling](../error-handling.md) for the full error format.
{% endhint %}

The same pattern applies to `deviceCreate`, `geoObjectCreate`, and `scheduleCreate` fields.
{% endstep %}

{% step %}
#### **Update custom field values**

Use `set` to overwrite specific fields and `unset` to remove them. Fields omitted from both are left unchanged.

The following mutation updates the next service date after a completed maintenance and removes a temporary inspection hold:

```graphql
mutation UpdateVehicleFields {
  assetUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 1
    customFields: {
      set:   { "next_service_date": "2026-03-01" }
      unset: ["inspection_hold"]
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

The response returns the updated device's `id`, `version`, and `customFields`. Fields that were unset no longer appear in the JSON:

```json
{
  "data": {
    "assetUpdate": {
      "asset": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 2,
        "customFields": {
          "vin": "1HGBH41JXMN109186",
          "fuel_type": "diesel",
          "next_service_date": "2026-03-01"
        }
      }
    }
  }
}
```

{% hint style="info" %}
You can include `version` in update mutations to enable [optimistic locking](../optimistic-locking.md). Fetch the entity first if you don't have the latest version.
{% endhint %}
{% endstep %}

{% step %}
#### **Read custom field values**

`customFields` on any entity returns a JSON object keyed by field code. By default, all fields are returned. Run the following query:

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
  asset(id: "019a6b2f-793e-807b-8001-555345529b44") {
    title
    customFields(codes: ["vin", "fuel_type"])
  }
}
```

The response contains only the requested fields:

```json
{
  "data": {
    "asset": {
      "title": "Truck 12",
      "customFields": {
        "vin": "1HGBH41JXMN109186",
        "fuel_type": "diesel"
      }
    }
  }
}
```
{% endstep %}

{% step %}
#### **Filter entities by custom field value**

All entity list queries support filtering by custom field values through [CustomFieldFilter](../custom-fields.md#customfieldfilter). Add one or more conditions to the `customFields` filter array. Multiple conditions are applied as AND.

For the full operator list and value formats by field type, see [Filtering and sorting](../filtering-and-sorting.md#operators).

**How to filter by an OPTIONS value**

Find all electric vehicle assets:

```graphql
query FindElectricVehicles {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]
      customFields: [
        { code: "fuel_type", operator: EQ, value: { string: "electric" } }
      ]
    }
  ) {
    nodes {
      id
      title
      customFields(codes: ["fuel_type", "next_service_date"])
    }
  }
}
```

Response:

```json
{
  "data": {
    "assets": {
      "nodes": [
        {
          "id": "019a6b2f-793e-807b-8001-555345529b44",
          "title": "Truck 12",
          "customFields": {
            "fuel_type": "electric",
            "next_service_date": "2025-09-01"
          }
        }
      ]
    }
  }
}
```

**How to filter by a DATE value**

Find vehicles with a service date before a deadline:

```graphql
query FindOverdueVehicles {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]
      customFields: [
        { code: "next_service_date", operator: LT, value: { date: "2025-07-01" } }
      ]
    }
  ) {
    nodes {
      id
      title
      customFields(codes: ["next_service_date"])
    }
  }
}
```

Response:

```json
{
  "data": {
    "assets": {
      "nodes": [
        {
          "id": "019a6b2f-793e-807b-8001-555345529b44",
          "title": "Truck 12",
          "customFields": {
            "next_service_date": "2025-06-15"
          }
        }
      ]
    }
  }
}
```

**How to combine multiple conditions**

Find devices with a specific SIM card prefix that don't yet have installation notes:

```graphql
query FindOverdueElectricVehicles {
  assets(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]
      customFields: [
        { code: "fuel_type",         operator: EQ, value: { string: "electric" } }
        { code: "next_service_date", operator: LT, value: { date: "2025-07-01" } }
      ]
    }
  ) {
    nodes {
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
    "devices": {
      "nodes": [
        {
          "id": "019a6c3f-894e-817b-8002-666456630c55",
          "title": "Tracker 04"
        }
      ]
    }
  }
}
```

{% hint style="info" %}
Omit `value` (or set it to `null`) when using the `IS_NULL` and `IS_NOT_NULL` operators.
{% endhint %}
{% endstep %}
{% endstepper %}

## Managing definitions

### How to update a custom field definition

You can update the `title`, `description`, `order`, and `params`. The `code` and `fieldType` cannot be changed after creation.

Pass an `update` operation inside the parent type's `customFieldDefinitions` array. The field is identified by its `code`:

```graphql
mutation UpdateVinField {
  assetTypeUpdate(input: {
    id: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    version: 2
    customFieldDefinitions: [
      { update: {
          code:        "vin"
          title:       "VIN"
          description: "Vehicle Identification Number (17 characters, no I/O/Q)"
          params: {
            string: {
              isRequired: true
              minLength:  17
              maxLength:  17
              trim:       true
            }
          }
      }}
    ]
  }) {
    assetType {
      version
      customFieldDefinitions {
        code
        title
        description
      }
    }
  }
}
```

The response returns the updated type with incremented `version` and the updated definition.

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

### How to archive and restore a custom field definition

Archiving is the preferred method of deactivating a field you no longer need. An archived field preserves all existing values (which remain readable and visible in history and exports), but the field stops accepting new input and no longer appears in forms.

To archive a field, run this mutation:

```graphql
mutation ArchiveVinField {
  assetTypeUpdate(input: {
    id: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    version: 3
    customFieldDefinitions: [
      { archive: { code: "vin" } }
    ]
  }) {
    assetType {
      version
      customFieldDefinitions {
        code
        title
        isArchived
      }
    }
  }
}
```

To reactivate an archived field, use `restore`:

```graphql
mutation RestoreVinField {
  assetTypeUpdate(input: {
    id: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    version: 4
    customFieldDefinitions: [
      { restore: { code: "vin" } }
    ]
  }) {
    assetType {
      version
      customFieldDefinitions {
        code
        title
        isArchived
      }
    }
  }
}
```

### How to delete a custom field definition

Deletion is permanent and cannot be undone. Use [archiving](implementing-custom-fields.md#how-to-archive-and-restore-a-custom-field-definition) instead unless you explicitly need to remove the field and its data.

By default, deletion is rejected if any entity currently has a value for the field. Pass `onValues: CASCADE` to force deletion along with all associated values across every entity record:

```graphql
mutation DeleteDefinition {
  assetTypeUpdate(input: {
    id: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    version: 5
    customFieldDefinitions: [
      { delete: {
          code:     "vin"
          onValues: CASCADE
      }}
    ]
  }) {
    assetType {
      version
      customFieldDefinitions {
        code
        title
      }
    }
  }
}
```

The response shows that `vin` no longer appears in the list, confirming that the definition and all its stored values have been removed.

```json
{
  "data": {
    "assetTypeUpdate": {
      "assetType": {
        "version": 6,
        "customFieldDefinitions": [
          { "code": "fuel_type",         "title": "Fuel Type" },
          { "code": "next_service_date", "title": "Next Service Date" }
        ]
      }
    }
  }
}
```

{% hint style="info" %}
`onValues: CASCADE` permanently removes the field's values from every entity record. They cannot be recovered. Use `archive` for non-destructive deactivation.

If you create a new definition with the same `code` later, existing records will not retain any value for it — the data removed by `CASCADE` is not recoverable.
{% endhint %}

## Constraints and considerations

Keep in mind the following:

* Validation errors reject the entire mutation: Mutations that include invalid custom field values are rejected in full. See [Error handling](../error-handling.md) for the error format.
* `fieldType` is immutable: To change a field's type, delete its definition and create a new one. Deleting the definition removes its values from all entity records.
* `code` is stable once in use: `code` must be unique within the owner type and organization. As this is the key used to read and write values across all entity mutations and queries, avoid recreating it under a different name if records contain values paired with it. If you rely on auto-generation, verify the generated code before any records are written under it.
* `params` requires exactly one variant: `FieldParamsInput` uses the [@oneOf](../core-api-reference/directives.md#oneof) directive, so you must provide exactly the variant that matches your `fieldType`. Providing `string: { ... }` when `fieldType` is `NUMBER` returns a validation error.
* Multi-value fields and filtering: For OPTIONS, CATALOG, and TAG fields configured with `isMulti: true`, a filter matches if _any_ value in the array satisfies the condition. For example, if an asset has `fuel_type: ["diesel", "hybrid"]`, filtering with `EQ: "diesel"` will match it.
* Predefined fields: Predefined definitions (like `geojson_data` and `schedule_data`) are platform-managed and appear in `customFields` responses alongside your definitions. Don't use codes that conflict with predefined field codes.

### See also

* [Custom fields types and operations](../custom-fields.md): A complete list of all operations and types related to custom fields
* [Filtering and sorting](../filtering-and-sorting.md): Full operator reference and value formats for custom field filters
* [Optimistic locking](../optimistic-locking.md): How `version` works in update and delete mutations
