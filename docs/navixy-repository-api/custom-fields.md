# Custom fields

{% include ".gitbook/includes/navixy-repository-api-is-a-....md" %}

Custom field definitions allow extending entities with organization-specific data fields.

## Objects

<a id="type-customfielddefinition"></a>

### CustomFieldDefinition

A custom field definition that specifies the metadata for a custom field.

{% hint style="warning" %}
The `fieldType` property is immutable after creation. To change the field type, delete the definition and create a new one.
{% endhint %}

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String!` | The human-readable display name. |
| `code` | `Code!` | The machine-readable code, unique per owner and organization. |
| `description` | `String` | A description of the field for UI hints. |
| `order` | `Int!` | The display order within the owner context. |
| `fieldType` | [FieldType](#type-fieldtype)! | The data type determining validation rules and UI rendering. This property is immutable and cannot be changed after creation. |
| `params` | [FieldParams](#type-fieldparams)! | The type-specific parameters for validation, defaults, and options. |
| `isArchived` | `Boolean!` | Whether this field definition is archived. Archived fields preserve existing values but no longer appear in forms and accept no new input. Use the `archive` / `restore` actions in the parent catalog item's `customFieldDefinitions` input to toggle this state. |

---

<a id="type-fieldparamsstring"></a>

### FieldParamsString

Parameters for STRING field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean!` | Whether to trim leading and trailing whitespace. |

---

<a id="type-fieldparamstext"></a>

### FieldParamsText

Parameters for TEXT field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean!` | Whether to trim leading and trailing whitespace. |

---

<a id="type-fieldparamsnumber"></a>

### FieldParamsNumber

Parameters for NUMBER field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

---

<a id="type-fieldparamsboolean"></a>

### FieldParamsBoolean

Parameters for BOOLEAN field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `defaultValue` | `Boolean` | The default value. |

---

<a id="type-fieldparamsdate"></a>

### FieldParamsDate

Parameters for DATE field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `defaultValue` | `Date` | The default value. |

---

<a id="type-fieldparamsdatetime"></a>

### FieldParamsDatetime

Parameters for DATETIME field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `defaultValue` | `DateTime` | The default value. |

---

<a id="type-fieldparamsgeojson"></a>

### FieldParamsGeojson

Parameters for GEOJSON field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `allowedTypes` | [[GeoJsonGeometryType](geo-objects/types.md#type-geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

---

<a id="type-fieldparamsschedule"></a>

### FieldParamsSchedule

Parameters for SCHEDULE field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |

---

<a id="type-fieldparamsoptions"></a>

### FieldParamsOptions

Parameters for OPTIONS field type.

**Implements:** [FieldParams](#type-fieldparams), [MultiValue](common.md#type-multivalue)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |
| `options` | [[FieldOption](#type-fieldoption)!]! | The available options to choose from. |
| `defaultValue` | `Code` | The default option code. |

---

<a id="type-fieldoption"></a>

### FieldOption

A single option in an OPTIONS field.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The unique code for this option within the field. |
| `label` | `String!` | The display label. |
| `description` | `String` | A description of the option. |
| `isArchived` | `Boolean!` | Whether this option is archived and should not be shown for new selections. |

---

<a id="type-fieldparamsdevice"></a>

### FieldParamsDevice

Parameters for DEVICE field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |

---

<a id="type-fieldparamsreference"></a>

### FieldParamsReference

Parameters for REFERENCE field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

---

<a id="type-fieldparamscatalog"></a>

### FieldParamsCatalog

Parameters for CATALOG field type.

**Implements:** [FieldParams](#type-fieldparams), [MultiValue](common.md#type-multivalue)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultValue` | `Code` | The default item code. |

---

<a id="type-fieldparamstag"></a>

### FieldParamsTag

Parameters for TAG field type.

**Implements:** [FieldParams](#type-fieldparams)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |
| `defaultValue` | `Code` | The default tag code. |

---

## Inputs

<a id="type-customfieldfiltervalue"></a>

### CustomFieldFilterValue

Typed filter value for custom fields. Exactly one field must be set (`@oneOf`).
Choose the variant that matches the custom field's data type:

| FieldType         | Variant      | Example                                |
|-------------------|--------------|----------------------------------------|
| STRING, TEXT      | `string`     | `{ string: "hello" }`                  |
| NUMBER            | `number`     | `{ number: 42.0 }`                     |
| BOOLEAN           | `boolean`    | `{ boolean: true }`                    |
| DATE              | `date`       | `{ date: "2024-01-15" }`              |
| DATETIME          | `datetime`   | `{ datetime: "2024-01-15T10:30:00Z" }`|
| OPTIONS, CATALOG, TAG | `string` | `{ string: "option_code" }`            |
| DEVICE, REFERENCE | `id`         | `{ id: "019a6a3f-..." }`              |
| (IN operator)     | `stringList` | `{ stringList: ["a", "b"] }`           |
| (IN operator)     | `idList`     | `{ idList: ["uuid1", "uuid2"] }`       |

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | `String` | String value — for STRING, TEXT, OPTIONS, CATALOG, TAG fields. |
| `number` | `Float` | Numeric value — for NUMBER fields. |
| `boolean` | `Boolean` | Boolean value — for BOOLEAN fields. |
| `date` | `Date` | Date value — for DATE fields. |
| `datetime` | `DateTime` | Date-time value — for DATETIME fields. |
| `id` | `ID` | ID value — for DEVICE, REFERENCE fields. |
| `stringList` | `[String!]` | List of strings — for IN operator on string-based fields. |
| `idList` | `[ID!]` | List of IDs — for IN operator on reference fields. |

---

<a id="type-customfieldfilter"></a>

### CustomFieldFilter

A filter condition for a custom field value.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The custom field code to filter by. |
| `operator` | [FieldOperator](#type-fieldoperator)! | The comparison operator. |
| `value` | [CustomFieldFilterValue](#type-customfieldfiltervalue) | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

---

<a id="type-customfieldspatchinput"></a>

### CustomFieldsPatchInput

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |
| `setPrimary` | `[Code!]` | Field codes to mark as primary (replaces previous primary of the same field type). |
| `unsetPrimary` | `[Code!]` | Field codes to unmark as primary. |

---

<a id="type-customfielddefinitioninput"></a>

### CustomFieldDefinitionInput

A single operation on a custom field definition within the parent catalog item.
Exactly one action must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `create` | [CustomFieldDefinitionCreateData](#type-customfielddefinitioncreatedata) | Create a new custom field definition. |
| `update` | [CustomFieldDefinitionUpdateData](#type-customfielddefinitionupdatedata) | Update an existing custom field definition. |
| `delete` | [CustomFieldDefinitionDeleteData](#type-customfielddefinitiondeletedata) | Delete a custom field definition. |
| `archive` | [CustomFieldDefinitionArchiveData](#type-customfielddefinitionarchivedata) | Archive a custom field definition (non-destructive deactivation). |
| `restore` | [CustomFieldDefinitionRestoreData](#type-customfielddefinitionrestoredata) | Restore a previously archived custom field definition. |

---

<a id="type-customfielddefinitioncreatedata"></a>

### CustomFieldDefinitionCreateData

Data for creating a custom field definition within its parent catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. Codes `geojson_data` and `schedule_data` are reserved by the platform. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType](#type-fieldtype)! | The data type. Immutable after creation. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `params` | [FieldParamsInput](#type-fieldparamsinput)! | The type-specific parameters. Exactly one variant must be provided. |

---

<a id="type-customfielddefinitionupdatedata"></a>

### CustomFieldDefinitionUpdateData

Data for updating an existing custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to update. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](#type-fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

---

<a id="type-customfielddefinitiondeletedata"></a>

### CustomFieldDefinitionDeleteData

Data for permanently deleting a custom field definition.

If entities have values for this field, the default behavior is to reject the deletion.
Use `onValues: CASCADE` to explicitly allow deletion with all associated values.

Prefer archiving for non-destructive deactivation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to delete. |
| `onValues` | [CustomFieldDefinitionDeleteBehavior](#type-customfielddefinitiondeletebehavior) | What to do when existing entities have values for this field. Defaults to `REJECT` to prevent accidental data loss. |

---

<a id="type-customfielddefinitionarchivedata"></a>

### CustomFieldDefinitionArchiveData

Data for archiving or restoring a custom field definition.

Archiving deactivates the field without data loss:
- The field definition and all its values are preserved.
- The field no longer appears in forms and accepts no new values.
- Existing values remain readable and visible in history/exports.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to archive. |

---

<a id="type-customfielddefinitionrestoredata"></a>

### CustomFieldDefinitionRestoreData

Data for restoring a previously archived custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to restore. |

---

<a id="type-fieldparamsinput"></a>

### FieldParamsInput

Field parameters input. Exactly one field must be provided.

{% hint style="warning" %}
This input type uses `@oneOf` - exactly one field must be provided.
{% endhint %}

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](#type-stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](#type-textfieldparamsinput) | Parameters for TEXT field type. |
| `number` | [NumberFieldParamsInput](#type-numberfieldparamsinput) | Parameters for NUMBER field type. |
| `boolean` | [BooleanFieldParamsInput](#type-booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](#type-datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](#type-datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](#type-geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](#type-schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](#type-optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](#type-devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](#type-referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](#type-catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](#type-tagfieldparamsinput) | Parameters for TAG field type. |

---

<a id="type-stringfieldparamsinput"></a>

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

<a id="type-textfieldparamsinput"></a>

### TextFieldParamsInput

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

---

<a id="type-numberfieldparamsinput"></a>

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

<a id="type-booleanfieldparamsinput"></a>

### BooleanFieldParamsInput

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Boolean` | The default value. |

---

<a id="type-datefieldparamsinput"></a>

### DateFieldParamsInput

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Date` | The default value. |

---

<a id="type-datetimefieldparamsinput"></a>

### DateTimeFieldParamsInput

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `DateTime` | The default value. |

---

<a id="type-geojsonfieldparamsinput"></a>

### GeoJsonFieldParamsInput

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](geo-objects/types.md#type-geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

---

<a id="type-schedulefieldparamsinput"></a>

### ScheduleFieldParamsInput

Parameters for SCHEDULE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

---

<a id="type-optionsfieldparamsinput"></a>

### OptionsFieldParamsInput

Parameters for OPTIONS field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple options can be selected. |
| `options` | [[FieldOptionInput](#type-fieldoptioninput)!]! | The available options. |
| `defaultValue` | `Code` | The default option code. |

---

<a id="type-fieldoptioninput"></a>

### FieldOptionInput

Input for an option definition.
When updating options: if an entry without `code` is provided, a new option is created.
If the label already exists within this field, an error is returned.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The unique code. Auto-generated from label if omitted. |
| `label` | `String!` | The display label. Must be unique within the custom field. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

---

<a id="type-devicefieldparamsinput"></a>

### DeviceFieldParamsInput

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

---

<a id="type-referencefieldparamsinput"></a>

### ReferenceFieldParamsInput

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

---

<a id="type-catalogfieldparamsinput"></a>

### CatalogFieldParamsInput

Parameters for CATALOG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple items can be selected. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultValue` | `Code` | The default item code. |

---

<a id="type-tagfieldparamsinput"></a>

### TagFieldParamsInput

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Code` | The default tag code. |

---

## Enums

<a id="type-fieldtype"></a>

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

<a id="type-customfielddefinitiondeletebehavior"></a>

### CustomFieldDefinitionDeleteBehavior

Controls the behavior when deleting a custom field definition that has existing values.

Prefer archiving for non-destructive deactivation.
Use `CASCADE` only when permanent data removal is explicitly intended.

| Value | Description |
| ----- | ----------- |
| `REJECT` | Reject the deletion with an error if any entity has a value for this field. Default. |
| `CASCADE` | Delete the field definition and permanently remove all associated values. |

---

<a id="type-fieldoperator"></a>

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

<a id="type-fieldparams"></a>

### FieldParams

The base interface for field parameters.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |

---
