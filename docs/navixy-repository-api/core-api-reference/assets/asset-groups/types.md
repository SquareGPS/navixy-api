# Types

## Types

### AssetGroupConnection

A paginated list of AssetGroup items.

**Implements:** [`Connection`](../../common-resources.md#connection)

| Field      | Type                                             | Description                                                |
| ---------- | ------------------------------------------------ | ---------------------------------------------------------- |
| `edges`    | \[[AssetGroupEdge](types.md#assetgroupedge)!]!   | A list of edges.                                           |
| `nodes`    | \[[AssetGroup](types.md#assetgroup)!]!           | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../common-resources.md#countinfo) | The total count of items matching the filter.              |

### AssetGroupEdge

An edge in the AssetGroup connection.

**Implements:** [`Edge`](../../common-resources.md#edge)

| Field    | Type                               | Description                             |
| -------- | ---------------------------------- | --------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.         |
| `node`   | [AssetGroup](types.md#assetgroup)! | The asset group at the end of the edge. |

### AssetGroupItemConnection

A paginated list of AssetGroupItem items.

**Implements:** [`Connection`](../../common-resources.md#connection)

| Field      | Type                                                   | Description                                                |
| ---------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| `edges`    | \[[AssetGroupItemEdge](types.md#assetgroupitemedge)!]! | A list of edges.                                           |
| `nodes`    | \[[AssetGroupItem](types.md#assetgroupitem)!]!         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common-resources.md#pageinfo)!        | Information about the current page.                        |
| `total`    | [CountInfo](../../common-resources.md#countinfo)       | The total count of items matching the filter.              |

### AssetGroupItemEdge

An edge in the AssetGroupItem connection.

**Implements:** [`Edge`](../../common-resources.md#edge)

| Field    | Type                                       | Description                                  |
| -------- | ------------------------------------------ | -------------------------------------------- |
| `cursor` | `String!`                                  | An opaque cursor for this edge.              |
| `node`   | [AssetGroupItem](types.md#assetgroupitem)! | The asset group item at the end of the edge. |

### AssetGroup

A group of assets.

**Implements:** [`Node`](../../common-resources.md#node), [`Versioned`](../../common-resources.md#versioned), [`Titled`](../../common-resources.md#titled)

| Field           | Type                                                                      | Description                                     |
| --------------- | ------------------------------------------------------------------------- | ----------------------------------------------- |
| `id`            | `ID!`                                                                     |                                                 |
| `version`       | `Int!`                                                                    |                                                 |
| `title`         | `String!`                                                                 |                                                 |
| `organization`  | [Organization](../../organizations/#organization)!                        | The organization that owns this group.          |
| `type`          | [AssetGroupType](../../../catalogs/entity-types/types.md#assetgrouptype)! | The group type with membership constraints.     |
| `color`         | [HexColorCode](../../common-resources.md#hexcolorcode)                    | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../#assetconnection)!                                   | The assets currently in this group.             |
| `history`       | [AssetGroupItemConnection](types.md#assetgroupitemconnection)!            | The full membership history for this group.     |

### AssetGroupItem

A record of an asset's membership in a group.

**Implements:** [`Node`](../../common-resources.md#node)

| Field        | Type                                            | Description                                                                                              |
| ------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `id`         | `ID!`                                           |                                                                                                          |
| `group`      | [AssetGroup](types.md#assetgroup)!              | The group containing the asset.                                                                          |
| `asset`      | [Asset](../#asset)!                             | The asset in the group.                                                                                  |
| `attachedAt` | [DateTime](../../common-resources.md#datetime)! | The date and time when the asset was added to the group.                                                 |
| `detachedAt` | [DateTime](../../common-resources.md#datetime)  | The date and time when the asset was removed from the group. Null means the asset is currently attached. |

### AssetGroupPayload

The result of an asset group mutation.

| Field        | Type                               | Description                         |
| ------------ | ---------------------------------- | ----------------------------------- |
| `assetGroup` | [AssetGroup](types.md#assetgroup)! | The created or updated asset group. |

### AssetGroupItemPayload

The result of an asset group item mutation.

| Field            | Type                                       | Description                          |
| ---------------- | ------------------------------------------ | ------------------------------------ |
| `assetGroupItem` | [AssetGroupItem](types.md#assetgroupitem)! | The created group membership record. |

## Inputs

### AssetGroupFilter

Filtering options for asset groups.

| Field           | Type     | Description                                         |
| --------------- | -------- | --------------------------------------------------- |
| `typeIds`       | `[ID!]`  | Filter by group types (OR within field).            |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

### AssetGroupOrder

Ordering options for asset groups.

| Field       | Type                                                        | Description             |
| ----------- | ----------------------------------------------------------- | ----------------------- |
| `field`     | [AssetGroupOrderField](types.md#assetgrouporderfield)!      | The field to order by.  |
| `direction` | [OrderDirection](../../common-resources.md#orderdirection)! | The direction to order. |

### AssetGroupItemFilter

Filtering options for asset group items.

| Field        | Type      | Description                                    |
| ------------ | --------- | ---------------------------------------------- |
| `activeOnly` | `Boolean` | If true, return only currently attached items. |

### AssetGroupItemOrder

Ordering options for asset group items.

| Field       | Type                                                           | Description             |
| ----------- | -------------------------------------------------------------- | ----------------------- |
| `field`     | [AssetGroupItemOrderField](types.md#assetgroupitemorderfield)! | The field to order by.  |
| `direction` | [OrderDirection](../../common-resources.md#orderdirection)!    | The direction to order. |

### AssetGroupCreateInput

Input for creating a new asset group.

| Field            | Type                                                   | Description                               |
| ---------------- | ------------------------------------------------------ | ----------------------------------------- |
| `organizationId` | `ID!`                                                  | The organization that will own the group. |
| `typeId`         | `ID!`                                                  | The group type ID.                        |
| `title`          | `String!`                                              | The group display name.                   |
| `color`          | [HexColorCode](../../common-resources.md#hexcolorcode) | The color for UI display.                 |

### AssetGroupUpdateInput

Input for updating an existing asset group.

| Field     | Type                                                   | Description                                 |
| --------- | ------------------------------------------------------ | ------------------------------------------- |
| `id`      | `ID!`                                                  | The asset group ID to update.               |
| `version` | `Int!`                                                 | The current version for optimistic locking. |
| `title`   | `String`                                               | The new display name.                       |
| `color`   | [HexColorCode](../../common-resources.md#hexcolorcode) | The new color.                              |

### AssetGroupDeleteInput

Input for deleting an asset group.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The asset group ID to delete.               |
| `version` | `Int!` | The current version for optimistic locking. |

### AssetGroupItemAddInput

Input for adding an asset to a group.

| Field     | Type  | Description          |
| --------- | ----- | -------------------- |
| `groupId` | `ID!` | The group ID.        |
| `assetId` | `ID!` | The asset ID to add. |

### AssetGroupItemRemoveInput

Input for removing an asset from a group.

| Field     | Type  | Description             |
| --------- | ----- | ----------------------- |
| `groupId` | `ID!` | The group ID.           |
| `assetId` | `ID!` | The asset ID to remove. |

## Enums

### AssetGroupOrderField

Fields available for ordering asset groups.

| Value   | Description     |
| ------- | --------------- |
| `TITLE` | Order by title. |

### AssetGroupItemOrderField

Fields available for ordering asset group items.

| Value         | Description               |
| ------------- | ------------------------- |
| `ATTACHED_AT` | Order by attachment date. |
