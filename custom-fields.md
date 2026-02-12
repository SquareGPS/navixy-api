# Custom fields

Custom field definitions allow extending entities with organization-specific data fields.

## Mutations

### customFieldDefinitionCreate

Creates a custom field definition.

```graphql
customFieldDefinitionCreate(input: CustomFieldDefinitionCreateInput!): CustomFieldDefinitionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CustomFieldDefinitionCreateInput!` | The input fields for creating the definition. |

**Input types:**

<details>

<summary>CustomFieldDefinitionCreateInput</summary>

Input for creating a custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `ownerCatalogItemId` | `ID!` | The owner catalog item ID (EntityType or a specific type like AssetType). |
| `targetEntityTypeId` | `ID!` | The target entity type ID. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType](#fieldtype)! | The data type. Immutable after creation. |
| `order` | `Int` | The display order. |
| `params` | [FieldParamsInput](#fieldparamsinput)! | The type-specific parameters. Exactly one variant must be provided. |

</details>

<details>

<summary>FieldParamsInput</summary>

Field parameters input. Exactly one field must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](#stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](#textfieldparamsinput) | Parameters for TEXT field type. |
| `number` | [NumberFieldParamsInput](#numberfieldparamsinput) | Parameters for NUMBER field type. |
| `boolean` | [BooleanFieldParamsInput](#booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](#datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](#datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](#geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](#schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](#optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](#devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](#referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](#catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](#tagfieldparamsinput) | Parameters for TAG field type. |

</details>

<details>

<summary>StringFieldParamsInput</summary>

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>TextFieldParamsInput</summary>

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>NumberFieldParamsInput</summary>

Parameters for NUMBER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

</details>

<details>

<summary>BooleanFieldParamsInput</summary>

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Boolean` | The default value. |

</details>

<details>

<summary>DateFieldParamsInput</summary>

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Date` | The default value. |

</details>

<details>

<summary>DateTimeFieldParamsInput</summary>

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `DateTime` | The default value. |

</details>

<details>

<summary>GeoJsonFieldParamsInput</summary>

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](geo-objects/types.md#geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

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
| `options` | [[FieldOptionInput](#fieldoptioninput)!]! | The available options. |
| `defaultValue` | `Code` | The default option code. |

</details>

<details>

<summary>FieldOptionInput</summary>

Input for an option definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The unique code. |
| `label` | `String!` | The display label. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

</details>

<details>

<summary>DeviceFieldParamsInput</summary>

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple devices can be selected. |

</details>

<details>

<summary>ReferenceFieldParamsInput</summary>

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple references can be selected. |
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
| `defaultValue` | `Code` | The default item code. |

</details>

<details>

<summary>TagFieldParamsInput</summary>

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple tags can be selected. |
| `defaultValue` | `Code` | The default tag code. |

</details>

**Output types:**

<details>

<summary>CustomFieldDefinitionPayload</summary>

The result of a custom field definition mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `customFieldDefinition` | [CustomFieldDefinition](#customfielddefinition)! | The created or updated custom field definition. |

</details>

<details>

<summary>CustomFieldDefinition (entity)</summary>

A custom field definition that specifies the metadata for a custom field.

Note: The `fieldType` property is immutable after creation.
To change the field type, delete the definition and create a new one.

**Implements:** [Node](common.md#node), [Versioned](common.md#versioned), [Titled](common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `code` | `Code!` | The machine-readable code, unique per owner and organization. |
| `description` | `String` | A description of the field for UI hints. |
| `order` | `Int!` | The display order within the owner context. |
| `organization` | [Organization](organizations/README.md#organization) | The organization that owns this definition. Null for system-level fields. |
| `owner` | [CatalogItem](catalogs/README.md#catalogitem)! | The owner catalog item: EntityType for system fields, or a specific type like AssetType for type-specific fields. |
| `targetEntityType` | [EntityType](catalogs/system.md#entitytype)! | The target entity type this field applies to. |
| `fieldType` | [FieldType](#fieldtype)! | The data type determining validation rules and UI rendering. This property is immutable and cannot be changed after creation. |
| `params` | [FieldParams](#fieldparams)! | The type-specific parameters for validation, defaults, and options. |

</details>

---

### customFieldDefinitionUpdate

Updates a custom field definition. Note: `fieldType` cannot be changed.

```graphql
customFieldDefinitionUpdate(input: CustomFieldDefinitionUpdateInput!): CustomFieldDefinitionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CustomFieldDefinitionUpdateInput!` | The input fields for updating the definition. |

**Input types:**

<details>

<summary>CustomFieldDefinitionUpdateInput</summary>

Input for updating a custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](#fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

</details>

<details>

<summary>FieldParamsInput</summary>

Field parameters input. Exactly one field must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](#stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](#textfieldparamsinput) | Parameters for TEXT field type. |
| `number` | [NumberFieldParamsInput](#numberfieldparamsinput) | Parameters for NUMBER field type. |
| `boolean` | [BooleanFieldParamsInput](#booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](#datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](#datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](#geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](#schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](#optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](#devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](#referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](#catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](#tagfieldparamsinput) | Parameters for TAG field type. |

</details>

<details>

<summary>StringFieldParamsInput</summary>

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>TextFieldParamsInput</summary>

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>NumberFieldParamsInput</summary>

Parameters for NUMBER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

</details>

<details>

<summary>BooleanFieldParamsInput</summary>

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Boolean` | The default value. |

</details>

<details>

<summary>DateFieldParamsInput</summary>

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Date` | The default value. |

</details>

<details>

<summary>DateTimeFieldParamsInput</summary>

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `DateTime` | The default value. |

</details>

<details>

<summary>GeoJsonFieldParamsInput</summary>

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](geo-objects/types.md#geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

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
| `options` | [[FieldOptionInput](#fieldoptioninput)!]! | The available options. |
| `defaultValue` | `Code` | The default option code. |

</details>

<details>

<summary>FieldOptionInput</summary>

Input for an option definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The unique code. |
| `label` | `String!` | The display label. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

</details>

<details>

<summary>DeviceFieldParamsInput</summary>

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple devices can be selected. |

</details>

<details>

<summary>ReferenceFieldParamsInput</summary>

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple references can be selected. |
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
| `defaultValue` | `Code` | The default item code. |

</details>

<details>

<summary>TagFieldParamsInput</summary>

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple tags can be selected. |
| `defaultValue` | `Code` | The default tag code. |

</details>

**Output types:**

<details>

<summary>CustomFieldDefinitionPayload</summary>

The result of a custom field definition mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `customFieldDefinition` | [CustomFieldDefinition](#customfielddefinition)! | The created or updated custom field definition. |

</details>

<details>

<summary>CustomFieldDefinition (entity)</summary>

A custom field definition that specifies the metadata for a custom field.

Note: The `fieldType` property is immutable after creation.
To change the field type, delete the definition and create a new one.

**Implements:** [Node](common.md#node), [Versioned](common.md#versioned), [Titled](common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `code` | `Code!` | The machine-readable code, unique per owner and organization. |
| `description` | `String` | A description of the field for UI hints. |
| `order` | `Int!` | The display order within the owner context. |
| `organization` | [Organization](organizations/README.md#organization) | The organization that owns this definition. Null for system-level fields. |
| `owner` | [CatalogItem](catalogs/README.md#catalogitem)! | The owner catalog item: EntityType for system fields, or a specific type like AssetType for type-specific fields. |
| `targetEntityType` | [EntityType](catalogs/system.md#entitytype)! | The target entity type this field applies to. |
| `fieldType` | [FieldType](#fieldtype)! | The data type determining validation rules and UI rendering. This property is immutable and cannot be changed after creation. |
| `params` | [FieldParams](#fieldparams)! | The type-specific parameters for validation, defaults, and options. |

</details>

---

### customFieldDefinitionDelete

Deletes a custom field definition.

```graphql
customFieldDefinitionDelete(input: CustomFieldDefinitionDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CustomFieldDefinitionDeleteInput!` | The input fields for deleting the definition. |

**Input types:**

<details>

<summary>CustomFieldDefinitionDeleteInput</summary>

Input for deleting a custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

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

## Objects

### CustomFieldDefinition

A custom field definition that specifies the metadata for a custom field.

Note: The `fieldType` property is immutable after creation.
To change the field type, delete the definition and create a new one.

**Implements:** [Node](common.md#node), [Versioned](common.md#versioned), [Titled](common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `code` | `Code!` | The machine-readable code, unique per owner and organization. |
| `description` | `String` | A description of the field for UI hints. |
| `order` | `Int!` | The display order within the owner context. |
| `organization` | [Organization](organizations/README.md#organization) | The organization that owns this definition. Null for system-level fields. |
| `owner` | [CatalogItem](catalogs/README.md#catalogitem)! | The owner catalog item: EntityType for system fields, or a specific type like AssetType for type-specific fields. |
| `targetEntityType` | [EntityType](catalogs/system.md#entitytype)! | The target entity type this field applies to. |
| `fieldType` | [FieldType](#fieldtype)! | The data type determining validation rules and UI rendering. This property is immutable and cannot be changed after creation. |
| `params` | [FieldParams](#fieldparams)! | The type-specific parameters for validation, defaults, and options. |

---

### FieldParamsString

Parameters for STRING field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean!` | Whether to trim leading and trailing whitespace. |

---

### FieldParamsText

Parameters for TEXT field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean!` | Whether to trim leading and trailing whitespace. |

---

### FieldParamsNumber

Parameters for NUMBER field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

---

### FieldParamsBoolean

Parameters for BOOLEAN field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `defaultValue` | `Boolean` | The default value. |

---

### FieldParamsDate

Parameters for DATE field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `defaultValue` | `Date` | The default value. |

---

### FieldParamsDatetime

Parameters for DATETIME field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `defaultValue` | `DateTime` | The default value. |

---

### FieldParamsGeojson

Parameters for GEOJSON field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `allowedTypes` | [[GeoJsonGeometryType](geo-objects/types.md#geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

---

### FieldParamsSchedule

Parameters for SCHEDULE field type.

**Implements:** [FieldParams](#fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |

---

### FieldParamsOptions

Parameters for OPTIONS field type.

**Implements:** [FieldParams](#fieldparams), [MultiValue](common.md#multivalue)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |
| `options` | [[FieldOption](#fieldoption)!]! | The available options to choose from. |
| `defaultValue` | `Code` | The default option code. |

---

### FieldOption

A single option in an OPTIONS field.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The unique code for this option within the field. |
| `label` | `String!` | The display label. |
| `description` | `String` | A description of the option. |
| `isArchived` | `Boolean!` | Whether this option is archived and should not be shown for new selections. |

---

### FieldParamsDevice

Parameters for DEVICE field type.

**Implements:** [FieldParams](#fieldparams), [MultiValue](common.md#multivalue)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |

---

### FieldParamsReference

Parameters for REFERENCE field type.

**Implements:** [FieldParams](#fieldparams), [MultiValue](common.md#multivalue)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

---

### FieldParamsCatalog

Parameters for CATALOG field type.

**Implements:** [FieldParams](#fieldparams), [MultiValue](common.md#multivalue)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultValue` | `Code` | The default item code. |

---

### FieldParamsTag

Parameters for TAG field type.

**Implements:** [FieldParams](#fieldparams), [MultiValue](common.md#multivalue)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |
| `defaultValue` | `Code` | The default tag code. |

---

### CustomFieldDefinitionPayload

The result of a custom field definition mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `customFieldDefinition` | [CustomFieldDefinition](#customfielddefinition)! | The created or updated custom field definition. |

---

## Inputs

### CustomFieldFilter

A filter condition for a custom field value.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The custom field code to filter by. |
| `operator` | [FieldOperator](#fieldoperator)! | The comparison operator. |
| `value` | `JSON` | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

---

### CustomFieldsPatchInput

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

---

### CustomFieldDefinitionCreateInput

Input for creating a custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `ownerCatalogItemId` | `ID!` | The owner catalog item ID (EntityType or a specific type like AssetType). |
| `targetEntityTypeId` | `ID!` | The target entity type ID. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType](#fieldtype)! | The data type. Immutable after creation. |
| `order` | `Int` | The display order. |
| `params` | [FieldParamsInput](#fieldparamsinput)! | The type-specific parameters. Exactly one variant must be provided. |

---

### CustomFieldDefinitionUpdateInput

Input for updating a custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](#fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

---

### CustomFieldDefinitionDeleteInput

Input for deleting a custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

### FieldParamsInput

Field parameters input. Exactly one field must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](#stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](#textfieldparamsinput) | Parameters for TEXT field type. |
| `number` | [NumberFieldParamsInput](#numberfieldparamsinput) | Parameters for NUMBER field type. |
| `boolean` | [BooleanFieldParamsInput](#booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](#datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](#datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](#geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](#schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](#optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](#devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](#referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](#catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](#tagfieldparamsinput) | Parameters for TAG field type. |

---

### StringFieldParamsInput

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

---

### TextFieldParamsInput

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

---

### NumberFieldParamsInput

Parameters for NUMBER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

---

### BooleanFieldParamsInput

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Boolean` | The default value. |

---

### DateFieldParamsInput

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Date` | The default value. |

---

### DateTimeFieldParamsInput

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `DateTime` | The default value. |

---

### GeoJsonFieldParamsInput

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](geo-objects/types.md#geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

---

### ScheduleFieldParamsInput

Parameters for SCHEDULE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

---

### OptionsFieldParamsInput

Parameters for OPTIONS field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple options can be selected. |
| `options` | [[FieldOptionInput](#fieldoptioninput)!]! | The available options. |
| `defaultValue` | `Code` | The default option code. |

---

### FieldOptionInput

Input for an option definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The unique code. |
| `label` | `String!` | The display label. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

---

### DeviceFieldParamsInput

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple devices can be selected. |

---

### ReferenceFieldParamsInput

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple references can be selected. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

---

### CatalogFieldParamsInput

Parameters for CATALOG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple items can be selected. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultValue` | `Code` | The default item code. |

---

### TagFieldParamsInput

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple tags can be selected. |
| `defaultValue` | `Code` | The default tag code. |

---

## Enums

### FieldType

The data type of a custom field, determining validation rules and UI rendering.

| Value | Description |
| ----- | ----------- |
| `STRING` | Single-line text input. Maximum 255 characters. |
| `TEXT` | Multi-line text input. Maximum 65,535 characters. |
| `NUMBER` | Numeric value, supporting both integers and decimals. |
| `BOOLEAN` | Boolean true/false value. |
| `DATE` | Calendar date without time component (YYYY-MM-DD). |
| `DATETIME` | Date and time with timezone information. |
| `GEOJSON` | GeoJSON geometry object (Point, Polygon, LineString, etc.). |
| `SCHEDULE` | Schedule or calendar data with time intervals and recurrence rules. |
| `OPTIONS` | Selection from a predefined list of options. |
| `DEVICE` | Reference to a Device entity. |
| `REFERENCE` | Reference to any entity by its type and ID. |
| `CATALOG` | Reference to a catalog item. |
| `TAG` | Reference to a Tag entity. |

---

### FieldOperator

Comparison operators for filtering by custom field values.

| Value | Description |
| ----- | ----------- |
| `EQ` | Value equals the specified value. |
| `NE` | Value does not equal the specified value. |
| `GT` | Value is greater than the specified value. |
| `GTE` | Value is greater than or equal to the specified value. |
| `LT` | Value is less than the specified value. |
| `LTE` | Value is less than or equal to the specified value. |
| `CONTAINS` | String value contains the specified substring (case-insensitive). |
| `IN` | Value is one of the specified values in the array. |
| `IS_NULL` | Value is null. |
| `IS_NOT_NULL` | Value is not null. |

---

## Interfaces

### FieldParams

The base interface for field parameters.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |

---
