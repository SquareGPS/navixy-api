# Asset Groups — Queries

### assetGroupTypes

Lists asset group types for an organization.

```graphql
assetGroupTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): AssetGroupTypeConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve asset group types for. |
| `filter` | [CatalogItemFilter](../catalogs/README.md#catalogitemfilter) | Filtering options for the returned asset group types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [CatalogItemOrder](../catalogs/README.md#catalogitemorder) | The ordering options for the returned asset group types. |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | [[Code](../common.md#code)!] | Match any of these codes. |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](../catalogs/README.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>AssetGroupTypeConnection</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupTypeEdge](../catalogs/entity-types/types.md#assetgrouptypeedge)!]! | A list of edges. |
| `nodes` | [[AssetGroupType](../catalogs/entity-types/types.md#assetgrouptype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>AssetGroupType (node)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! |  |
| `allowedAssetTypes` | [[AssetGroupTypeConstraint](../catalogs/entity-types/types.md#assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

</details>

### assetGroup

Retrieves an asset group by its ID.

```graphql
assetGroup(id: ID!): AssetGroup
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the asset group to retrieve. |

**Output types:**

<details>

<summary><code>AssetGroup</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](../catalogs/entity-types/types.md#assetgrouptype)! | The group type with membership constraints. |
| `color` | [HexColorCode](../common.md#hexcolorcode) | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../assets.md#assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](./types.md#assetgroupitemconnection)! | The full membership history for this group. |

</details>

### assetGroups

Lists asset groups for an organization.

```graphql
assetGroups(
  organizationId: ID!
  filter: AssetGroupFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AssetGroupOrder = { field: TITLE, direction: ASC }
): AssetGroupConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve asset groups for. |
| `filter` | [AssetGroupFilter](./types.md#assetgroupfilter) | Filtering options for the returned asset groups. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [AssetGroupOrder](./types.md#assetgrouporder) | The ordering options for the returned asset groups. |

**Input types:**

<details>

<summary><code>AssetGroupFilter</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by group types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary><code>AssetGroupOrder</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupOrderField](./types.md#assetgrouporderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>AssetGroupConnection</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupEdge](./types.md#assetgroupedge)!]! | A list of edges. |
| `nodes` | [[AssetGroup](./types.md#assetgroup)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>AssetGroup (node)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](../catalogs/entity-types/types.md#assetgrouptype)! | The group type with membership constraints. |
| `color` | [HexColorCode](../common.md#hexcolorcode) | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../assets.md#assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](./types.md#assetgroupitemconnection)! | The full membership history for this group. |

</details>
