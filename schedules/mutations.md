# Schedules — Mutations

### scheduleCreate

Creates a new schedule.

```graphql
scheduleCreate("The input fields for creating the schedule." input: ScheduleCreateInput!): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleCreateInput](types.md#schedulecreateinput)! | The input fields for creating the schedule. |

**Input types:**

<details>

<summary><code>ScheduleCreateInput</code></summary>

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

<summary><code>CustomFieldsPatchInput</code></summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>SchedulePayload</code></summary>

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](types.md#schedule)! | The created or updated schedule. |

</details>

<details>

<summary><code>Schedule (entity)</code></summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this schedule. |
| `type` | [ScheduleType](types.md#scheduletype)! | The schedule type classification. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule.
  This is an alias for the `schedule_data` custom field. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

</details>

---

### scheduleUpdate

Updates an existing schedule.

```graphql
scheduleUpdate("The input fields for updating the schedule." input: ScheduleUpdateInput!): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleUpdateInput](types.md#scheduleupdateinput)! | The input fields for updating the schedule. |

**Input types:**

<details>

<summary><code>ScheduleUpdateInput</code></summary>

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

<summary><code>CustomFieldsPatchInput</code></summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>SchedulePayload</code></summary>

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](types.md#schedule)! | The created or updated schedule. |

</details>

<details>

<summary><code>Schedule (entity)</code></summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this schedule. |
| `type` | [ScheduleType](types.md#scheduletype)! | The schedule type classification. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule.
  This is an alias for the `schedule_data` custom field. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

</details>

---

### scheduleDelete

Deletes a schedule.

```graphql
scheduleDelete("The input fields for deleting the schedule." input: ScheduleDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleDeleteInput](types.md#scheduledeleteinput)! | The input fields for deleting the schedule. |

**Input types:**

<details>

<summary><code>ScheduleDeleteInput</code></summary>

Input for deleting a schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

### scheduleTypeCreate

Creates a new schedule type.

```graphql
scheduleTypeCreate("The input fields for creating the schedule type." input: ScheduleTypeCreateInput!): ScheduleTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleTypeCreateInput](types.md#scheduletypecreateinput)! | The input fields for creating the schedule type. |

**Input types:**

<details>

<summary><code>ScheduleTypeCreateInput</code></summary>

Input for creating a schedule type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>ScheduleTypePayload</code></summary>

The result of a schedule type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `scheduleType` | [ScheduleType](types.md#scheduletype)! | The created or updated schedule type. |

</details>

<details>

<summary><code>ScheduleType (entity)</code></summary>

A classification type for schedules.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

</details>

---

### scheduleTypeUpdate

Updates a schedule type.

```graphql
scheduleTypeUpdate("The input fields for updating the schedule type." input: ScheduleTypeUpdateInput!): ScheduleTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleTypeUpdateInput](types.md#scheduletypeupdateinput)! | The input fields for updating the schedule type. |

**Input types:**

<details>

<summary><code>ScheduleTypeUpdateInput</code></summary>

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

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>ScheduleTypePayload</code></summary>

The result of a schedule type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `scheduleType` | [ScheduleType](types.md#scheduletype)! | The created or updated schedule type. |

</details>

<details>

<summary><code>ScheduleType (entity)</code></summary>

A classification type for schedules.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

</details>

---

### scheduleTypeDelete

Deletes a schedule type.

```graphql
scheduleTypeDelete("The input fields for deleting the schedule type." input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../catalogs/catalog-items.md#catalogitemdeleteinput)! | The input fields for deleting the schedule type. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---
