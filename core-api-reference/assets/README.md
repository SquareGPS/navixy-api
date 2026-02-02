# Assets

Assets represent trackable items like vehicles, equipment, or personnel that can be associated with devices.

## Queries

### asset

Retrieves an asset by its ID.

```graphql
asset(id: ID!): Asset
```

**Arguments**

| Name | Type  | Description                      |
| ---- | ----- | -------------------------------- |
| `id` | `ID!` | The ID of the asset to retrieve. |

**Output types:**

<details>

<summary><code>Asset</code></summary>

| Field          | Type                                                                | Description                            |
| -------------- | ------------------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                               |                                        |
| `version`      | `Int!`                                                              |                                        |
| `title`        | `String!`                                                           |                                        |
| `organization` | [Organization](../organizations/#organization)!                     | The organization that owns this asset. |
| `type`         | [AssetType](../../catalogs/entity-types/types.md#assettype)!        | The asset type classification.         |
| `customFields` | [JSON](../common-resources.md#json)!                                |                                        |
| `device`       | [Device](../../devices/types.md#device)                             |                                        |
| `groups`       | [AssetGroupConnection](asset-groups/types.md#assetgroupconnection)! | The groups this asset belongs to.      |

</details>

### assets

Lists assets for an organization.

```graphql
assets(
  organizationId: ID!
  filter: AssetFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AssetOrder = { field: TITLE, direction: ASC }
): AssetConnection!
```

**Arguments**

| Name             | Type                          | Description                                                                                   |
| ---------------- | ----------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                         | The organization to retrieve assets for.                                                      |
| `filter`         | [AssetFilter](./#assetfilter) | Filtering options for the returned assets.                                                    |
| `first`          | `Int`                         | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                      | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                         | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                      | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [AssetOrder](./#assetorder)   | The ordering options for the returned assets.                                                 |

**Input types:**

<details>

<summary><code>AssetFilter</code></summary>

| Field           | Type                                                              | Description                                         |
| --------------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| `typeIds`       | `[ID!]`                                                           | Filter by asset types (OR within field).            |
| `deviceIds`     | `[ID!]`                                                           | Filter by linked devices (OR within field).         |
| `titleContains` | `String`                                                          | Partial match on title (case-insensitive contains). |
| `customFields`  | \[[CustomFieldFilter](../../custom-fields.md#customfieldfilter)!] | Filter by custom field values.                      |

</details>

<details>

<summary><code>CustomFieldFilter</code></summary>

| Field      | Type                                                   | Description                                                                   |
| ---------- | ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| `code`     | [Code](../common-resources.md#code)!                   | The custom field code to filter by.                                           |
| `operator` | [FieldOperator](../../custom-fields.md#fieldoperator)! | The comparison operator.                                                      |
| `value`    | [JSON](../common-resources.md#json)                    | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

</details>

<details>

<summary><code>AssetOrder</code></summary>

| Field             | Type                                                     | Description                                                                |
| ----------------- | -------------------------------------------------------- | -------------------------------------------------------------------------- |
| `field`           | [AssetOrderField](./#assetorderfield)                    | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](../common-resources.md#code)                      | The custom field code to order by. Mutually exclusive with `field`.        |
| `direction`       | [OrderDirection](../common-resources.md#orderdirection)! | The direction to order.                                                    |

</details>

**Output types:**

<details>

<summary><code>AssetConnection</code></summary>

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AssetEdge](./#assetedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[Asset](./#asset)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Asset (node)</code></summary>

| Field          | Type                                                                | Description                            |
| -------------- | ------------------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                               |                                        |
| `version`      | `Int!`                                                              |                                        |
| `title`        | `String!`                                                           |                                        |
| `organization` | [Organization](../organizations/#organization)!                     | The organization that owns this asset. |
| `type`         | [AssetType](../../catalogs/entity-types/types.md#assettype)!        | The asset type classification.         |
| `customFields` | [JSON](../common-resources.md#json)!                                |                                        |
| `device`       | [Device](../../devices/types.md#device)                             |                                        |
| `groups`       | [AssetGroupConnection](asset-groups/types.md#assetgroupconnection)! | The groups this asset belongs to.      |

</details>

## Mutations

### assetCreate

Creates a new asset.

```graphql
assetCreate(input: AssetCreateInput!): AssetPayload
```

**Arguments**

| Name    | Type                                     | Description                              |
| ------- | ---------------------------------------- | ---------------------------------------- |
| `input` | [AssetCreateInput](./#assetcreateinput)! | The input fields for creating the asset. |

**Input types:**

<details>

<summary><code>AssetCreateInput</code></summary>

| Field            | Type                                                                    | Description                               |
| ---------------- | ----------------------------------------------------------------------- | ----------------------------------------- |
| `organizationId` | `ID!`                                                                   | The organization that will own the asset. |
| `typeId`         | `ID!`                                                                   | The asset type ID.                        |
| `title`          | `String!`                                                               | The asset display name.                   |
| `customFields`   | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field values.                  |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                    | Description                                 |
| ------- | --------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](../common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](../common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>AssetPayload</code></summary>

| Field   | Type               | Description                   |
| ------- | ------------------ | ----------------------------- |
| `asset` | [Asset](./#asset)! | The created or updated asset. |

</details>

<details>

<summary><code>Asset (entity)</code></summary>

| Field          | Type                                                                | Description                            |
| -------------- | ------------------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                               |                                        |
| `version`      | `Int!`                                                              |                                        |
| `title`        | `String!`                                                           |                                        |
| `organization` | [Organization](../organizations/#organization)!                     | The organization that owns this asset. |
| `type`         | [AssetType](../../catalogs/entity-types/types.md#assettype)!        | The asset type classification.         |
| `customFields` | [JSON](../common-resources.md#json)!                                |                                        |
| `device`       | [Device](../../devices/types.md#device)                             |                                        |
| `groups`       | [AssetGroupConnection](asset-groups/types.md#assetgroupconnection)! | The groups this asset belongs to.      |

</details>

### assetUpdate

Updates an existing asset.

```graphql
assetUpdate(input: AssetUpdateInput!): AssetPayload
```

**Arguments**

| Name    | Type                                     | Description                              |
| ------- | ---------------------------------------- | ---------------------------------------- |
| `input` | [AssetUpdateInput](./#assetupdateinput)! | The input fields for updating the asset. |

**Input types:**

<details>

<summary><code>AssetUpdateInput</code></summary>

| Field          | Type                                                                    | Description                                 |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                                   | The asset ID to update.                     |
| `version`      | `Int!`                                                                  | The current version for optimistic locking. |
| `title`        | `String`                                                                | The new display name.                       |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                    | Description                                 |
| ------- | --------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](../common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](../common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>AssetPayload</code></summary>

| Field   | Type               | Description                   |
| ------- | ------------------ | ----------------------------- |
| `asset` | [Asset](./#asset)! | The created or updated asset. |

</details>

<details>

<summary><code>Asset (entity)</code></summary>

| Field          | Type                                                                | Description                            |
| -------------- | ------------------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                               |                                        |
| `version`      | `Int!`                                                              |                                        |
| `title`        | `String!`                                                           |                                        |
| `organization` | [Organization](../organizations/#organization)!                     | The organization that owns this asset. |
| `type`         | [AssetType](../../catalogs/entity-types/types.md#assettype)!        | The asset type classification.         |
| `customFields` | [JSON](../common-resources.md#json)!                                |                                        |
| `device`       | [Device](../../devices/types.md#device)                             |                                        |
| `groups`       | [AssetGroupConnection](asset-groups/types.md#assetgroupconnection)! | The groups this asset belongs to.      |

</details>

### assetDelete

Deletes an asset.

```graphql
assetDelete(input: AssetDeleteInput!): DeletePayload
```

**Arguments**

| Name    | Type                                     | Description                              |
| ------- | ---------------------------------------- | ---------------------------------------- |
| `input` | [AssetDeleteInput](./#assetdeleteinput)! | The input fields for deleting the asset. |

**Input types:**

<details>

<summary><code>AssetDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The asset ID to delete.                     |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

## Types

### AssetConnection

A paginated list of Asset items.

**Implements:** [`Connection`](../common-resources.md#connection)

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AssetEdge](./#assetedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[Asset](./#asset)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

### AssetEdge

An edge in the Asset connection.

**Implements:** [`Edge`](../common-resources.md#edge)

| Field    | Type               | Description                       |
| -------- | ------------------ | --------------------------------- |
| `cursor` | `String!`          | An opaque cursor for this edge.   |
| `node`   | [Asset](./#asset)! | The asset at the end of the edge. |

### Asset

A physical or logical asset being tracked.

**Implements:** [`Node`](../common-resources.md#node), [`Titled`](../common-resources.md#titled), [`Customizable`](../common-resources.md#customizable), [`Versioned`](../common-resources.md#versioned)

| Field          | Type                                                                | Description                            |
| -------------- | ------------------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                               |                                        |
| `version`      | `Int!`                                                              |                                        |
| `title`        | `String!`                                                           |                                        |
| `organization` | [Organization](../organizations/#organization)!                     | The organization that owns this asset. |
| `type`         | [AssetType](../../catalogs/entity-types/types.md#assettype)!        | The asset type classification.         |
| `customFields` | [JSON](../common-resources.md#json)!                                |                                        |
| `device`       | [Device](../../devices/types.md#device)                             |                                        |
| `groups`       | [AssetGroupConnection](asset-groups/types.md#assetgroupconnection)! | The groups this asset belongs to.      |

### AssetPayload

The result of an asset mutation.

| Field   | Type               | Description                   |
| ------- | ------------------ | ----------------------------- |
| `asset` | [Asset](./#asset)! | The created or updated asset. |

## Inputs

### AssetFilter

Filtering options for assets.

| Field           | Type                                                              | Description                                         |
| --------------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| `typeIds`       | `[ID!]`                                                           | Filter by asset types (OR within field).            |
| `deviceIds`     | `[ID!]`                                                           | Filter by linked devices (OR within field).         |
| `titleContains` | `String`                                                          | Partial match on title (case-insensitive contains). |
| `customFields`  | \[[CustomFieldFilter](../../custom-fields.md#customfieldfilter)!] | Filter by custom field values.                      |

### AssetOrder

Ordering options for assets.

| Field             | Type                                                     | Description                                                                |
| ----------------- | -------------------------------------------------------- | -------------------------------------------------------------------------- |
| `field`           | [AssetOrderField](./#assetorderfield)                    | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](../common-resources.md#code)                      | The custom field code to order by. Mutually exclusive with `field`.        |
| `direction`       | [OrderDirection](../common-resources.md#orderdirection)! | The direction to order.                                                    |

### AssetCreateInput

Input for creating a new asset.

| Field            | Type                                                                    | Description                               |
| ---------------- | ----------------------------------------------------------------------- | ----------------------------------------- |
| `organizationId` | `ID!`                                                                   | The organization that will own the asset. |
| `typeId`         | `ID!`                                                                   | The asset type ID.                        |
| `title`          | `String!`                                                               | The asset display name.                   |
| `customFields`   | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field values.                  |

### AssetUpdateInput

Input for updating an existing asset.

| Field          | Type                                                                    | Description                                 |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                                   | The asset ID to update.                     |
| `version`      | `Int!`                                                                  | The current version for optimistic locking. |
| `title`        | `String`                                                                | The new display name.                       |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

### AssetDeleteInput

Input for deleting an asset.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The asset ID to delete.                     |
| `version` | `Int!` | The current version for optimistic locking. |

## Enums

### AssetOrderField

Fields available for ordering assets.

| Value   | Description     |
| ------- | --------------- |
| `TITLE` | Order by title. |
