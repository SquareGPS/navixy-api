# Mutations

### deviceCreate

Creates a new device.

```graphql
deviceCreate(input: DeviceCreateInput!): DevicePayload
```

**Arguments**

| Name    | Type                                             | Description                               |
| ------- | ------------------------------------------------ | ----------------------------------------- |
| `input` | [DeviceCreateInput](types.md#devicecreateinput)! | The input fields for creating the device. |

**Input types:**

<details>

<summary><code>DeviceCreateInput</code></summary>

| Field            | Type                                                                 | Description                                |
| ---------------- | -------------------------------------------------------------------- | ------------------------------------------ |
| `organizationId` | `ID!`                                                                | The organization that will own the device. |
| `typeId`         | `ID!`                                                                | The device type ID.                        |
| `modelId`        | `ID!`                                                                | The device model ID.                       |
| `statusId`       | `ID!`                                                                | The initial device status ID.              |
| `title`          | `String!`                                                            | The device display name.                   |
| `identifiers`    | \[[DeviceIdentifierInput](types.md#deviceidentifierinput)!]          | The hardware identifiers.                  |
| `customFields`   | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values.                   |

</details>

<details>

<summary><code>DeviceIdentifierInput</code></summary>

| Field       | Type                                                   | Description                                                     |
| ----------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| `type`      | [DeviceIdType](types.md#deviceidtype)!                 | The type of identifier.                                         |
| `value`     | `String!`                                              | The identifier value.                                           |
| `namespace` | [Code](../core-api-reference/common-resources.md#code) | The namespace for uniqueness scope. Null means globally unique. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                                       | Description                                 |
| ------- | ---------------------------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](../core-api-reference/common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](../core-api-reference/common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>DevicePayload</code></summary>

| Field    | Type                       | Description                    |
| -------- | -------------------------- | ------------------------------ |
| `device` | [Device](types.md#device)! | The created or updated device. |

</details>

<details>

<summary><code>Device (entity)</code></summary>

| Field              | Type                                                                                    | Description                                                                        |
| ------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`               | `ID!`                                                                                   |                                                                                    |
| `version`          | `Int!`                                                                                  |                                                                                    |
| `title`            | `String!`                                                                               |                                                                                    |
| `organization`     | [Organization](../core-api-reference/organizations/#organization)!                      | The organization that owns this device.                                            |
| `type`             | [DeviceType](../catalogs/device/types.md#devicetype)!                                   | The device type classification.                                                    |
| `model`            | [DeviceModel](../catalogs/device/types.md#devicemodel)!                                 | The specific device model.                                                         |
| `status`           | [DeviceStatus](../catalogs/device/types.md#devicestatus)!                               | The current operational status.                                                    |
| `customFields`     | [JSON](../core-api-reference/common-resources.md#json)!                                 |                                                                                    |
| `identifiers`      | \[[DeviceIdentifier](types.md#deviceidentifier)!]!                                      | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory`        | [Inventory](../inventory.md#inventory)                                                  | The inventory this device is currently assigned to.                                |
| `relationsFrom`    | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The outgoing relationships from this device to other devices.                      |
| `relationsTo`      | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The incoming relationships from other devices to this device.                      |
| `inventoryHistory` | [DeviceInventoryRelationConnection](../inventory.md#deviceinventoryrelationconnection)! | The history of inventory assignments for this device.                              |

</details>

### deviceUpdate

Updates an existing device.

```graphql
deviceUpdate(input: DeviceUpdateInput!): DevicePayload
```

**Arguments**

| Name    | Type                                             | Description                               |
| ------- | ------------------------------------------------ | ----------------------------------------- |
| `input` | [DeviceUpdateInput](types.md#deviceupdateinput)! | The input fields for updating the device. |

**Input types:**

<details>

<summary><code>DeviceUpdateInput</code></summary>

| Field          | Type                                                                 | Description                                 |
| -------------- | -------------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                                | The device ID to update.                    |
| `version`      | `Int!`                                                               | The current version for optimistic locking. |
| `modelId`      | `ID`                                                                 | The new device model.                       |
| `statusId`     | `ID`                                                                 | The new device status.                      |
| `title`        | `String`                                                             | The new display name.                       |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                                       | Description                                 |
| ------- | ---------------------------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](../core-api-reference/common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](../core-api-reference/common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>DevicePayload</code></summary>

| Field    | Type                       | Description                    |
| -------- | -------------------------- | ------------------------------ |
| `device` | [Device](types.md#device)! | The created or updated device. |

</details>

<details>

<summary><code>Device (entity)</code></summary>

| Field              | Type                                                                                    | Description                                                                        |
| ------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`               | `ID!`                                                                                   |                                                                                    |
| `version`          | `Int!`                                                                                  |                                                                                    |
| `title`            | `String!`                                                                               |                                                                                    |
| `organization`     | [Organization](../core-api-reference/organizations/#organization)!                      | The organization that owns this device.                                            |
| `type`             | [DeviceType](../catalogs/device/types.md#devicetype)!                                   | The device type classification.                                                    |
| `model`            | [DeviceModel](../catalogs/device/types.md#devicemodel)!                                 | The specific device model.                                                         |
| `status`           | [DeviceStatus](../catalogs/device/types.md#devicestatus)!                               | The current operational status.                                                    |
| `customFields`     | [JSON](../core-api-reference/common-resources.md#json)!                                 |                                                                                    |
| `identifiers`      | \[[DeviceIdentifier](types.md#deviceidentifier)!]!                                      | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory`        | [Inventory](../inventory.md#inventory)                                                  | The inventory this device is currently assigned to.                                |
| `relationsFrom`    | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The outgoing relationships from this device to other devices.                      |
| `relationsTo`      | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The incoming relationships from other devices to this device.                      |
| `inventoryHistory` | [DeviceInventoryRelationConnection](../inventory.md#deviceinventoryrelationconnection)! | The history of inventory assignments for this device.                              |

</details>

### deviceDelete

Deletes a device.

```graphql
deviceDelete(input: DeviceDeleteInput!): DeletePayload
```

**Arguments**

| Name    | Type                                             | Description                               |
| ------- | ------------------------------------------------ | ----------------------------------------- |
| `input` | [DeviceDeleteInput](types.md#devicedeleteinput)! | The input fields for deleting the device. |

**Input types:**

<details>

<summary><code>DeviceDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The device ID to delete.                    |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### deviceIdentifierAdd

Adds an identifier to a device.

```graphql
deviceIdentifierAdd(
  input: DeviceIdentifierAddInput!
): DeviceIdentifierPayload
```

**Arguments**

| Name    | Type                                                           | Description                                 |
| ------- | -------------------------------------------------------------- | ------------------------------------------- |
| `input` | [DeviceIdentifierAddInput](types.md#deviceidentifieraddinput)! | The input fields for adding the identifier. |

**Input types:**

<details>

<summary><code>DeviceIdentifierAddInput</code></summary>

| Field        | Type                                                     | Description             |
| ------------ | -------------------------------------------------------- | ----------------------- |
| `deviceId`   | `ID!`                                                    | The device ID.          |
| `identifier` | [DeviceIdentifierInput](types.md#deviceidentifierinput)! | The identifier details. |

</details>

<details>

<summary><code>DeviceIdentifierInput</code></summary>

| Field       | Type                                                   | Description                                                     |
| ----------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| `type`      | [DeviceIdType](types.md#deviceidtype)!                 | The type of identifier.                                         |
| `value`     | `String!`                                              | The identifier value.                                           |
| `namespace` | [Code](../core-api-reference/common-resources.md#code) | The namespace for uniqueness scope. Null means globally unique. |

</details>

**Output types:**

<details>

<summary><code>DeviceIdentifierPayload</code></summary>

| Field              | Type                                           | Description                  |
| ------------------ | ---------------------------------------------- | ---------------------------- |
| `deviceIdentifier` | [DeviceIdentifier](types.md#deviceidentifier)! | The added device identifier. |

</details>

<details>

<summary><code>DeviceIdentifier (entity)</code></summary>

| Field       | Type                                                   | Description                                                                       |
| ----------- | ------------------------------------------------------ | --------------------------------------------------------------------------------- |
| `id`        | `ID!`                                                  |                                                                                   |
| `device`    | [Device](types.md#device)!                             | The device this identifier belongs to.                                            |
| `type`      | [DeviceIdType](types.md#deviceidtype)!                 | The type of identifier.                                                           |
| `value`     | `String!`                                              | The identifier value.                                                             |
| `namespace` | [Code](../core-api-reference/common-resources.md#code) | The namespace for uniqueness scope. Null means the identifier is globally unique. |

</details>

### deviceIdentifierRemove

Removes an identifier from a device.

```graphql
deviceIdentifierRemove(
  input: DeviceIdentifierRemoveInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                                 | Description                                   |
| ------- | -------------------------------------------------------------------- | --------------------------------------------- |
| `input` | [DeviceIdentifierRemoveInput](types.md#deviceidentifierremoveinput)! | The input fields for removing the identifier. |

**Input types:**

<details>

<summary><code>DeviceIdentifierRemoveInput</code></summary>

| Field          | Type  | Description                  |
| -------------- | ----- | ---------------------------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### deviceRelationCreate

Creates a relationship between devices.

```graphql
deviceRelationCreate(
  input: DeviceRelationCreateInput!
): DeviceRelationPayload
```

**Arguments**

| Name    | Type                                                             | Description                                     |
| ------- | ---------------------------------------------------------------- | ----------------------------------------------- |
| `input` | [DeviceRelationCreateInput](types.md#devicerelationcreateinput)! | The input fields for creating the relationship. |

**Input types:**

<details>

<summary><code>DeviceRelationCreateInput</code></summary>

| Field      | Type  | Description               |
| ---------- | ----- | ------------------------- |
| `firstId`  | `ID!` | The first device ID.      |
| `secondId` | `ID!` | The second device ID.     |
| `typeId`   | `ID!` | The relationship type ID. |

</details>

**Output types:**

<details>

<summary><code>DeviceRelationPayload</code></summary>

| Field            | Type                                       | Description                      |
| ---------------- | ------------------------------------------ | -------------------------------- |
| `deviceRelation` | [DeviceRelation](types.md#devicerelation)! | The created device relationship. |

</details>

<details>

<summary><code>DeviceRelation (entity)</code></summary>

| Field    | Type                                                                  | Description                            |
| -------- | --------------------------------------------------------------------- | -------------------------------------- |
| `id`     | `ID!`                                                                 |                                        |
| `first`  | [Device](types.md#device)!                                            | The first device in the relationship.  |
| `second` | [Device](types.md#device)!                                            | The second device in the relationship. |
| `type`   | [DeviceRelationType](../catalogs/device/types.md#devicerelationtype)! | The type of relationship.              |

</details>

### deviceRelationRemove

Removes a device relationship.

```graphql
deviceRelationRemove(
  input: DeviceRelationRemoveInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                             | Description                                     |
| ------- | ---------------------------------------------------------------- | ----------------------------------------------- |
| `input` | [DeviceRelationRemoveInput](types.md#devicerelationremoveinput)! | The input fields for removing the relationship. |

**Input types:**

<details>

<summary><code>DeviceRelationRemoveInput</code></summary>

| Field | Type  | Description                    |
| ----- | ----- | ------------------------------ |
| `id`  | `ID!` | The relationship ID to remove. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>
