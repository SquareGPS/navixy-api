# Asset groups — Queries

{% include "../../.gitbook/includes/navixy-repository-api-is-a-....md" %}

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
| `filter` | `CatalogItemFilter` | Filtering options for the returned asset group types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned asset group types. |

**Input types:**

<details>

<summary>CatalogItemFilter</summary>

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | `[Code!]` | Match any of these codes. |

</details>

<details>

<summary>CatalogItemOrder</summary>

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](../../catalogs/catalog-items.md#type-catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AssetGroupTypeConnection</summary>

A paginated list of AssetGroupType items.

**Implements:** [Connection](../../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupTypeEdge](types.md#type-assetgrouptypeedge)!]! | A list of edges. |
| `nodes` | [[AssetGroupType](types.md#type-assetgrouptype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#type-countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary>PageInfo (entity)</summary>

Information about the current page in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after the current page. |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page. |
| `startCursor` | `String` | The cursor pointing to the first item in the current page. |
| `endCursor` | `String` | The cursor pointing to the last item in the current page. |

</details>

---

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

<summary>AssetGroup</summary>

A group of assets.

**Implements:** [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations/README.md#type-organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](types.md#type-assetgrouptype) | The group type with membership constraints. Immutable after creation. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../types.md#type-assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](types.md#type-assetgroupitemconnection)! | The full membership history for this group. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../../organizations/README.md#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../../organizations/README.md#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](../../organizations/README.md#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](../../organizations/members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../../devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../../geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

</details>

---

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
| `filter` | `AssetGroupFilter` | Filtering options for the returned asset groups. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetGroupOrder` | The ordering options for the returned asset groups. |

**Input types:**

<details>

<summary>AssetGroupFilter</summary>

Filtering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by group types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary>AssetGroupOrder</summary>

Ordering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupOrderField](types.md#type-assetgrouporderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AssetGroupConnection</summary>

A paginated list of AssetGroup items.

**Implements:** [Connection](../../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupEdge](types.md#type-assetgroupedge)!]! | A list of edges. |
| `nodes` | [[AssetGroup](types.md#type-assetgroup)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#type-countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary>PageInfo (entity)</summary>

Information about the current page in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after the current page. |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page. |
| `startCursor` | `String` | The cursor pointing to the first item in the current page. |
| `endCursor` | `String` | The cursor pointing to the last item in the current page. |

</details>

---
