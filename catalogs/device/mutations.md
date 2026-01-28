# Device Catalog — Mutations

### deviceTypeCreate

Creates a new device type.

```graphql
deviceTypeCreate(
  input: DeviceTypeCreateInput!
): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceTypeCreateInput](./types.md#devicetypecreateinput)! | The input fields for creating the device type. |

**Input types:**

<details>

<summary><code>DeviceTypeCreateInput</code></summary>

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

<summary><code>DeviceTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](./types.md#devicetype)! | The created or updated device type. |

</details>

<details>

<summary><code>DeviceType (entity)</code></summary>

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
| `customFieldDefinitions` | [[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

</details>

### deviceTypeUpdate

Updates a device type.

```graphql
deviceTypeUpdate(
  input: DeviceTypeUpdateInput!
): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceTypeUpdateInput](./types.md#devicetypeupdateinput)! | The input fields for updating the device type. |

**Input types:**

<details>

<summary><code>DeviceTypeUpdateInput</code></summary>

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

<summary><code>DeviceTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](./types.md#devicetype)! | The created or updated device type. |

</details>

<details>

<summary><code>DeviceType (entity)</code></summary>

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
| `customFieldDefinitions` | [[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

</details>

### deviceTypeDelete

Deletes a device type.

```graphql
deviceTypeDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../README.md#catalogitemdeleteinput)! | The input fields for deleting the device type. |

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

### deviceStatusCreate

Creates a new device status.

```graphql
deviceStatusCreate(
  input: DeviceStatusCreateInput!
): DeviceStatusPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceStatusCreateInput](./types.md#devicestatuscreateinput)! | The input fields for creating the device status. |

**Input types:**

<details>

<summary><code>DeviceStatusCreateInput</code></summary>

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

<summary><code>DeviceStatusPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](./types.md#devicestatus)! | The created or updated device status. |

</details>

<details>

<summary><code>DeviceStatus (entity)</code></summary>

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

</details>

### deviceStatusUpdate

Updates a device status.

```graphql
deviceStatusUpdate(
  input: DeviceStatusUpdateInput!
): DeviceStatusPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceStatusUpdateInput](./types.md#devicestatusupdateinput)! | The input fields for updating the device status. |

**Input types:**

<details>

<summary><code>DeviceStatusUpdateInput</code></summary>

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

<summary><code>DeviceStatusPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](./types.md#devicestatus)! | The created or updated device status. |

</details>

<details>

<summary><code>DeviceStatus (entity)</code></summary>

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

</details>

### deviceStatusDelete

Deletes a device status.

```graphql
deviceStatusDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../README.md#catalogitemdeleteinput)! | The input fields for deleting the device status. |

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
