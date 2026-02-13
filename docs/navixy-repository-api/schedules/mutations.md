# Schedules — Mutations

### scheduleCreate

Creates a new schedule.

```graphql
scheduleCreate(
    input: ScheduleCreateInput!
  ): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleCreateInput!` | The input fields for creating the schedule. |

**Input types:**

<details>

<summary>ScheduleCreateInput</summary>

Input for creating a new schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the schedule. |
| `typeId` | `ID!` | The schedule type ID. |
| `title` | `String!` | The schedule display name. |
| `scheduleData` | `ScheduleData!` | The schedule data. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

</details>

<details>

<summary>CustomFieldsPatchInput</summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary>SchedulePayload</summary>

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](types.md#schedule)! | The created or updated schedule. |

</details>

<details>

<summary>Schedule (entity)</summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#organization)! | The organization that owns this schedule. |
| `type` | [ScheduleType](types.md#scheduletype)! | The schedule type classification. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule. This is an alias for the `schedule_data` custom field. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |

</details>

---

### scheduleUpdate

Updates an existing schedule.

```graphql
scheduleUpdate(
    input: ScheduleUpdateInput!
  ): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleUpdateInput!` | The input fields for updating the schedule. |

**Input types:**

<details>

<summary>ScheduleUpdateInput</summary>

Input for updating an existing schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `scheduleData` | `ScheduleData` | The new schedule data. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

</details>

<details>

<summary>CustomFieldsPatchInput</summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary>SchedulePayload</summary>

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](types.md#schedule)! | The created or updated schedule. |

</details>

<details>

<summary>Schedule (entity)</summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#organization)! | The organization that owns this schedule. |
| `type` | [ScheduleType](types.md#scheduletype)! | The schedule type classification. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule. This is an alias for the `schedule_data` custom field. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |

</details>

---

### scheduleDelete

Deletes a schedule.

```graphql
scheduleDelete(
    input: ScheduleDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleDeleteInput!` | The input fields for deleting the schedule. |

**Input types:**

<details>

<summary>ScheduleDeleteInput</summary>

Input for deleting a schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to delete. |
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

### scheduleTypeCreate

Creates a new schedule type.

```graphql
scheduleTypeCreate(
    input: ScheduleTypeCreateInput!
  ): ScheduleTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleTypeCreateInput!` | The input fields for creating the schedule type. |

**Input types:**

<details>

<summary>ScheduleTypeCreateInput</summary>

Input for creating a schedule type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>ScheduleTypePayload</summary>

The result of a schedule type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `scheduleType` | [ScheduleType](types.md#scheduletype)! | The created or updated schedule type. |

</details>

<details>

<summary>ScheduleType (entity)</summary>

A classification type for schedules.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

</details>

---

### scheduleTypeUpdate

Updates a schedule type.

```graphql
scheduleTypeUpdate(
    input: ScheduleTypeUpdateInput!
  ): ScheduleTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleTypeUpdateInput!` | The input fields for updating the schedule type. |

**Input types:**

<details>

<summary>ScheduleTypeUpdateInput</summary>

Input for updating a schedule type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>ScheduleTypePayload</summary>

The result of a schedule type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `scheduleType` | [ScheduleType](types.md#scheduletype)! | The created or updated schedule type. |

</details>

<details>

<summary>ScheduleType (entity)</summary>

A classification type for schedules.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

</details>

---

### scheduleTypeDelete

Deletes a schedule type.

```graphql
scheduleTypeDelete(
    input: CatalogItemDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the schedule type. |

**Input types:**

<details>

<summary>CatalogItemDeleteInput</summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
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
