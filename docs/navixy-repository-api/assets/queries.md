# Assets — Queries

### assetTypes

Lists asset types for an organization.

```graphql
assetTypes(
    organizationId: ID!
    filter: CatalogItemFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
  ): AssetTypeConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve asset types for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned asset types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned asset types. |

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
| `field` | [CatalogItemOrderField](../catalogs/catalog-items.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AssetTypeConnection</summary>

A paginated list of AssetType items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetTypeEdge](types.md#assettypeedge)!]! | A list of edges. |
| `nodes` | [[AssetType](types.md#assettype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

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

### asset

Retrieves an asset by its ID.

```graphql
asset(id: ID!): Asset
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the asset to retrieve. |

**Output types:**

<details>

<summary>Asset</summary>

A physical or logical asset being tracked.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#organization)! | The organization that owns this asset. |
| `type` | [AssetType](types.md#assettype)! | The asset type classification. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |
| `device` | [Device](../devices/types.md#device) | The primary tracking device linked to this asset. This is an alias for the `device` custom field. |
| `groups` | [AssetGroupConnection](groups/types.md#assetgroupconnection)! | The groups this asset belongs to. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations/README.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations/README.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](../organizations/README.md#organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](../organizations/members.md#memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](types.md#assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules/types.md#scheduleconnection)! | The schedules owned by this organization. |

</details>

---

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve assets for. |
| `filter` | `AssetFilter` | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder` | The ordering options for the returned assets. |

**Input types:**

<details>

<summary>AssetFilter</summary>

Filtering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by asset types (OR within field). |
| `deviceIds` | `[ID!]` | Filter by linked devices (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values. |

</details>

<details>

<summary>CustomFieldFilter</summary>

A filter condition for a custom field value.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The custom field code to filter by. |
| `operator` | [FieldOperator](../custom-fields.md#fieldoperator)! | The comparison operator. |
| `value` | `JSON` | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

</details>

<details>

<summary>AssetOrder</summary>

Ordering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetOrderField](types.md#assetorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AssetConnection</summary>

A paginated list of Asset items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetEdge](types.md#assetedge)!]! | A list of edges. |
| `nodes` | [[Asset](types.md#asset)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

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
