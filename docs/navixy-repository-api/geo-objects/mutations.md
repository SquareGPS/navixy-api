# Geo objects — Mutations

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

### geoObjectCreate

Creates a new geo object.

```graphql
geoObjectCreate(
    input: GeoObjectCreateInput!
  ): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectCreateInput!` | The input fields for creating the geo object. |

**Input types:**

<details>

<summary>GeoObjectCreateInput</summary>

Input for creating a new geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the geo object. |
| `typeId` | `ID!` | The geo object type ID. |
| `title` | `String!` | The geo object display name. |
| `geojsonData` | `GeoJSON!` | The GeoJSON geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#type-customfieldspatchinput) | The custom field values. |

</details>

<details>

<summary>CustomFieldsPatchInput</summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |
| `setPrimary` | `[Code!]` | Field codes to mark as primary (replaces previous primary of the same field type). |
| `unsetPrimary` | `[Code!]` | Field codes to unmark as primary. |

</details>

**Output types:**

<details>

<summary>GeoObjectPayload</summary>

The result of a geo object mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](types.md#type-geoobject)! | The created or updated geo object. |

</details>

<details>

<summary>GeoObject (entity)</summary>

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Customizable](../common.md#type-customizable), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](types.md#type-geoobjecttype)! | The geo object type classification. |
| `geojsonData` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. System-reserved codes (`geojson_data`, `schedule_data`) are excluded from this map and exposed through dedicated typed fields on the entity instead. |
| `containsPoints` | [[PointContainmentResult](types.md#type-pointcontainmentresult)!]! | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

</details>

---

### geoObjectUpdate

Updates an existing geo object.

```graphql
geoObjectUpdate(
    input: GeoObjectUpdateInput!
  ): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectUpdateInput!` | The input fields for updating the geo object. |

**Input types:**

<details>

<summary>GeoObjectUpdateInput</summary>

Input for updating an existing geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `geojsonData` | `GeoJSON` | The new geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#type-customfieldspatchinput) | The custom field changes. |

</details>

<details>

<summary>CustomFieldsPatchInput</summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |
| `setPrimary` | `[Code!]` | Field codes to mark as primary (replaces previous primary of the same field type). |
| `unsetPrimary` | `[Code!]` | Field codes to unmark as primary. |

</details>

**Output types:**

<details>

<summary>GeoObjectPayload</summary>

The result of a geo object mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](types.md#type-geoobject)! | The created or updated geo object. |

</details>

<details>

<summary>GeoObject (entity)</summary>

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Customizable](../common.md#type-customizable), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](types.md#type-geoobjecttype)! | The geo object type classification. |
| `geojsonData` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. System-reserved codes (`geojson_data`, `schedule_data`) are excluded from this map and exposed through dedicated typed fields on the entity instead. |
| `containsPoints` | [[PointContainmentResult](types.md#type-pointcontainmentresult)!]! | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

</details>

---

### geoObjectDelete

Deletes a geo object.

```graphql
geoObjectDelete(
    input: GeoObjectDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectDeleteInput!` | The input fields for deleting the geo object. |

**Input types:**

<details>

<summary>GeoObjectDeleteInput</summary>

Input for deleting a geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

</details>

**Output types:**

<details>

<summary>DeletePayload</summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

### geoObjectTypeCreate

Creates a new geo object type.

```graphql
geoObjectTypeCreate(
    input: GeoObjectTypeCreateInput!
  ): GeoObjectTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectTypeCreateInput!` | The input fields for creating the geo object type. |

**Input types:**

<details>

<summary>GeoObjectTypeCreateInput</summary>

Input for creating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions for this geo object type. Only `create` is allowed when creating a new catalog item. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

<details>

<summary>CustomFieldDefinitionInput</summary>

A single operation on a custom field definition within the parent catalog item.
Exactly one action must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `create` | [CustomFieldDefinitionCreateData](../custom-fields.md#type-customfielddefinitioncreatedata) | Create a new custom field definition. |
| `update` | [CustomFieldDefinitionUpdateData](../custom-fields.md#type-customfielddefinitionupdatedata) | Update an existing custom field definition. |
| `delete` | [CustomFieldDefinitionDeleteData](../custom-fields.md#type-customfielddefinitiondeletedata) | Delete a custom field definition. |
| `archive` | [CustomFieldDefinitionArchiveData](../custom-fields.md#type-customfielddefinitionarchivedata) | Archive a custom field definition (non-destructive deactivation). |
| `restore` | [CustomFieldDefinitionRestoreData](../custom-fields.md#type-customfielddefinitionrestoredata) | Restore a previously archived custom field definition. |

</details>

<details>

<summary>CustomFieldDefinitionCreateData</summary>

Data for creating a custom field definition within its parent catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. Codes `geojson_data` and `schedule_data` are reserved by the platform. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType](../custom-fields.md#type-fieldtype)! | The data type. Immutable after creation. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput)! | The type-specific parameters. Exactly one variant must be provided. |

</details>

<details>

<summary>FieldParamsInput</summary>

Field parameters input. Exactly one field must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](../custom-fields.md#type-stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](../custom-fields.md#type-textfieldparamsinput) | Parameters for TEXT field type. |
| `decimal` | [DecimalFieldParamsInput](../custom-fields.md#type-decimalfieldparamsinput) | Parameters for DECIMAL field type. |
| `integer` | [IntegerFieldParamsInput](../custom-fields.md#type-integerfieldparamsinput) | Parameters for INTEGER field type. |
| `boolean` | [BooleanFieldParamsInput](../custom-fields.md#type-booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](../custom-fields.md#type-datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](../custom-fields.md#type-datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](../custom-fields.md#type-geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](../custom-fields.md#type-schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](../custom-fields.md#type-optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](../custom-fields.md#type-devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](../custom-fields.md#type-referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](../custom-fields.md#type-catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](../custom-fields.md#type-tagfieldparamsinput) | Parameters for TAG field type. |

</details>

<details>

<summary>StringFieldParamsInput</summary>

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultString` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>TextFieldParamsInput</summary>

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultText` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>DecimalFieldParamsInput</summary>

Parameters for DECIMAL field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minDecimal` | `Decimal` | The minimum allowed value. |
| `maxDecimal` | `Decimal` | The maximum allowed value. |
| `scale` | `Int!` | Digits after the decimal point. Must be >= 0. Values sent with more fractional digits than `scale` are rounded using HALF_UP before storage. |
| `defaultDecimal` | `Decimal` | The default value. |

</details>

<details>

<summary>IntegerFieldParamsInput</summary>

Parameters for INTEGER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minInteger` | `Long` | The minimum allowed value. |
| `maxInteger` | `Long` | The maximum allowed value. |
| `defaultInteger` | `Long` | The default value. |

</details>

<details>

<summary>BooleanFieldParamsInput</summary>

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultBoolean` | `Boolean` | The default value. |

</details>

<details>

<summary>DateFieldParamsInput</summary>

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultDate` | `Date` | The default value. |

</details>

<details>

<summary>DateTimeFieldParamsInput</summary>

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultDatetime` | `DateTime` | The default value. |

</details>

<details>

<summary>GeoJsonFieldParamsInput</summary>

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](types.md#type-geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

</details>

<details>

<summary>ScheduleFieldParamsInput</summary>

Parameters for SCHEDULE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>OptionsFieldParamsInput</summary>

Parameters for OPTIONS field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple options can be selected. |
| `options` | [[FieldOptionInput](../custom-fields.md#type-fieldoptioninput)!]! | The available options. |
| `defaultOptions` | `Code` | The default option code. |

</details>

<details>

<summary>FieldOptionInput</summary>

Input for an option definition.
When updating options: if an entry without `code` is provided, a new option is created.
If the label already exists within this field, an error is returned.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The unique code. Auto-generated from label if omitted. |
| `label` | `String!` | The display label. Must be unique within the custom field. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

</details>

<details>

<summary>DeviceFieldParamsInput</summary>

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>ReferenceFieldParamsInput</summary>

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

</details>

<details>

<summary>CatalogFieldParamsInput</summary>

Parameters for CATALOG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple items can be selected. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultCatalog` | `Code` | The default item code. |

</details>

<details>

<summary>TagFieldParamsInput</summary>

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultTag` | `Code` | The default tag code. |

</details>

<details>

<summary>CustomFieldDefinitionUpdateData</summary>

Data for updating an existing custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to update. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

</details>

<details>

<summary>CustomFieldDefinitionDeleteData</summary>

Data for permanently deleting a custom field definition.

If entities have values for this field, the default behavior is to reject the deletion.
Use `onValues: CASCADE` to explicitly allow deletion with all associated values.

Prefer archiving for non-destructive deactivation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to delete. |
| `onValues` | [CustomFieldDefinitionDeleteBehavior](../custom-fields.md#type-customfielddefinitiondeletebehavior) | What to do when existing entities have values for this field. Defaults to `REJECT` to prevent accidental data loss. |

</details>

<details>

<summary>CustomFieldDefinitionArchiveData</summary>

Data for archiving or restoring a custom field definition.

Archiving deactivates the field without data loss:
- The field definition and all its values are preserved.
- The field no longer appears in forms and accepts no new values.
- Existing values remain readable and visible in history/exports.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to archive. |

</details>

<details>

<summary>CustomFieldDefinitionRestoreData</summary>

Data for restoring a previously archived custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to restore. |

</details>

**Output types:**

<details>

<summary>GeoObjectTypePayload</summary>

The result of a geo object type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](types.md#type-geoobjecttype)! | The created or updated geo object type. |

</details>

<details>

<summary>GeoObjectType (entity)</summary>

A classification type for geographic objects.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#type-customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

</details>

---

### geoObjectTypeUpdate

Updates a geo object type.

```graphql
geoObjectTypeUpdate(
    input: GeoObjectTypeUpdateInput!
  ): GeoObjectTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectTypeUpdateInput!` | The input fields for updating the geo object type. |

**Input types:**

<details>

<summary>GeoObjectTypeUpdateInput</summary>

Input for updating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions belonging to this geo object type. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

<details>

<summary>CustomFieldDefinitionInput</summary>

A single operation on a custom field definition within the parent catalog item.
Exactly one action must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `create` | [CustomFieldDefinitionCreateData](../custom-fields.md#type-customfielddefinitioncreatedata) | Create a new custom field definition. |
| `update` | [CustomFieldDefinitionUpdateData](../custom-fields.md#type-customfielddefinitionupdatedata) | Update an existing custom field definition. |
| `delete` | [CustomFieldDefinitionDeleteData](../custom-fields.md#type-customfielddefinitiondeletedata) | Delete a custom field definition. |
| `archive` | [CustomFieldDefinitionArchiveData](../custom-fields.md#type-customfielddefinitionarchivedata) | Archive a custom field definition (non-destructive deactivation). |
| `restore` | [CustomFieldDefinitionRestoreData](../custom-fields.md#type-customfielddefinitionrestoredata) | Restore a previously archived custom field definition. |

</details>

<details>

<summary>CustomFieldDefinitionCreateData</summary>

Data for creating a custom field definition within its parent catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. Codes `geojson_data` and `schedule_data` are reserved by the platform. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType](../custom-fields.md#type-fieldtype)! | The data type. Immutable after creation. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput)! | The type-specific parameters. Exactly one variant must be provided. |

</details>

<details>

<summary>FieldParamsInput</summary>

Field parameters input. Exactly one field must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](../custom-fields.md#type-stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](../custom-fields.md#type-textfieldparamsinput) | Parameters for TEXT field type. |
| `decimal` | [DecimalFieldParamsInput](../custom-fields.md#type-decimalfieldparamsinput) | Parameters for DECIMAL field type. |
| `integer` | [IntegerFieldParamsInput](../custom-fields.md#type-integerfieldparamsinput) | Parameters for INTEGER field type. |
| `boolean` | [BooleanFieldParamsInput](../custom-fields.md#type-booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](../custom-fields.md#type-datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](../custom-fields.md#type-datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](../custom-fields.md#type-geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](../custom-fields.md#type-schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](../custom-fields.md#type-optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](../custom-fields.md#type-devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](../custom-fields.md#type-referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](../custom-fields.md#type-catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](../custom-fields.md#type-tagfieldparamsinput) | Parameters for TAG field type. |

</details>

<details>

<summary>StringFieldParamsInput</summary>

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultString` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>TextFieldParamsInput</summary>

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultText` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>DecimalFieldParamsInput</summary>

Parameters for DECIMAL field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minDecimal` | `Decimal` | The minimum allowed value. |
| `maxDecimal` | `Decimal` | The maximum allowed value. |
| `scale` | `Int!` | Digits after the decimal point. Must be >= 0. Values sent with more fractional digits than `scale` are rounded using HALF_UP before storage. |
| `defaultDecimal` | `Decimal` | The default value. |

</details>

<details>

<summary>IntegerFieldParamsInput</summary>

Parameters for INTEGER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minInteger` | `Long` | The minimum allowed value. |
| `maxInteger` | `Long` | The maximum allowed value. |
| `defaultInteger` | `Long` | The default value. |

</details>

<details>

<summary>BooleanFieldParamsInput</summary>

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultBoolean` | `Boolean` | The default value. |

</details>

<details>

<summary>DateFieldParamsInput</summary>

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultDate` | `Date` | The default value. |

</details>

<details>

<summary>DateTimeFieldParamsInput</summary>

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultDatetime` | `DateTime` | The default value. |

</details>

<details>

<summary>GeoJsonFieldParamsInput</summary>

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](types.md#type-geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

</details>

<details>

<summary>ScheduleFieldParamsInput</summary>

Parameters for SCHEDULE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>OptionsFieldParamsInput</summary>

Parameters for OPTIONS field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple options can be selected. |
| `options` | [[FieldOptionInput](../custom-fields.md#type-fieldoptioninput)!]! | The available options. |
| `defaultOptions` | `Code` | The default option code. |

</details>

<details>

<summary>FieldOptionInput</summary>

Input for an option definition.
When updating options: if an entry without `code` is provided, a new option is created.
If the label already exists within this field, an error is returned.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The unique code. Auto-generated from label if omitted. |
| `label` | `String!` | The display label. Must be unique within the custom field. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

</details>

<details>

<summary>DeviceFieldParamsInput</summary>

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>ReferenceFieldParamsInput</summary>

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

</details>

<details>

<summary>CatalogFieldParamsInput</summary>

Parameters for CATALOG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple items can be selected. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultCatalog` | `Code` | The default item code. |

</details>

<details>

<summary>TagFieldParamsInput</summary>

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultTag` | `Code` | The default tag code. |

</details>

<details>

<summary>CustomFieldDefinitionUpdateData</summary>

Data for updating an existing custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to update. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

</details>

<details>

<summary>CustomFieldDefinitionDeleteData</summary>

Data for permanently deleting a custom field definition.

If entities have values for this field, the default behavior is to reject the deletion.
Use `onValues: CASCADE` to explicitly allow deletion with all associated values.

Prefer archiving for non-destructive deactivation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to delete. |
| `onValues` | [CustomFieldDefinitionDeleteBehavior](../custom-fields.md#type-customfielddefinitiondeletebehavior) | What to do when existing entities have values for this field. Defaults to `REJECT` to prevent accidental data loss. |

</details>

<details>

<summary>CustomFieldDefinitionArchiveData</summary>

Data for archiving or restoring a custom field definition.

Archiving deactivates the field without data loss:
- The field definition and all its values are preserved.
- The field no longer appears in forms and accepts no new values.
- Existing values remain readable and visible in history/exports.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to archive. |

</details>

<details>

<summary>CustomFieldDefinitionRestoreData</summary>

Data for restoring a previously archived custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to restore. |

</details>

**Output types:**

<details>

<summary>GeoObjectTypePayload</summary>

The result of a geo object type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](types.md#type-geoobjecttype)! | The created or updated geo object type. |

</details>

<details>

<summary>GeoObjectType (entity)</summary>

A classification type for geographic objects.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#type-customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

</details>

---

### geoObjectTypeDelete

Deletes a geo object type.

```graphql
geoObjectTypeDelete(
    input: CatalogItemDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the geo object type. |

**Input types:**

<details>

<summary>CatalogItemDeleteInput</summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

</details>

**Output types:**

<details>

<summary>DeletePayload</summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---
