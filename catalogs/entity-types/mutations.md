# Entity Types Catalog — Mutations

### assetTypeCreate

Creates a new asset type.

```graphql
assetTypeCreate(
  input: AssetTypeCreateInput!
): AssetTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetTypeCreateInput](./types.md#assettypecreateinput)! | The input fields for creating the asset type. |

**Input types:**

<details>

<summary><code>AssetTypeCreateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code](../../common.md#code)! | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>AssetTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetType` | [AssetType](./types.md#assettype)! | The created or updated asset type. |

</details>

<details>

<summary><code>AssetType (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../../organizations.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../README.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this asset type, ordered by display order. |

</details>

### assetTypeUpdate

Updates an asset type.

```graphql
assetTypeUpdate(
  input: AssetTypeUpdateInput!
): AssetTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetTypeUpdateInput](./types.md#assettypeupdateinput)! | The input fields for updating the asset type. |

**Input types:**

<details>

<summary><code>AssetTypeUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>AssetTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetType` | [AssetType](./types.md#assettype)! | The created or updated asset type. |

</details>

<details>

<summary><code>AssetType (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../../organizations.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../README.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this asset type, ordered by display order. |

</details>

### assetTypeDelete

Deletes an asset type.

```graphql
assetTypeDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../README.md#catalogitemdeleteinput)! | The input fields for deleting the asset type. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

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
| `input` | [ScheduleTypeCreateInput](./types.md#scheduletypecreateinput)! | The input fields for creating the schedule type. |

**Input types:**

<details>

<summary><code>ScheduleTypeCreateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code](../../common.md#code)! | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>ScheduleTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `scheduleType` | [ScheduleType](./types.md#scheduletype)! | The created or updated schedule type. |

</details>

<details>

<summary><code>ScheduleType (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../../organizations.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../README.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

</details>

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
| `input` | [ScheduleTypeUpdateInput](./types.md#scheduletypeupdateinput)! | The input fields for updating the schedule type. |

**Input types:**

<details>

<summary><code>ScheduleTypeUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>ScheduleTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `scheduleType` | [ScheduleType](./types.md#scheduletype)! | The created or updated schedule type. |

</details>

<details>

<summary><code>ScheduleType (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../../organizations.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../README.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

</details>

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
| `input` | [CatalogItemDeleteInput](../README.md#catalogitemdeleteinput)! | The input fields for deleting the schedule type. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>
