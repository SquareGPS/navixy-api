# Assets — Queries

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

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
| `field` | [CatalogItemOrderField](../catalogs/catalog-items.md#type-catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AssetTypeConnection</summary>

A paginated list of AssetType items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetTypeEdge](types.md#type-assettypeedge)!]! | A list of edges. |
| `nodes` | [[AssetType](types.md#type-assettype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

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

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Customizable](../common.md#type-customizable), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this asset. |
| `type` | [AssetType](types.md#type-assettype)! | The asset type classification. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. System-reserved codes (`geojson_data`, `schedule_data`) are excluded from this map and exposed through dedicated typed fields on the entity instead. |
| `primaryDevice` | [Device](../devices/types.md#type-device) | The primary device (isPrimary=true among DEVICE-type custom fields). |
| `devices` | [[Device](../devices/types.md#type-device)!]! | All devices linked via DEVICE-type custom fields. |
| `groups` | [AssetGroupConnection](groups/types.md#type-assetgroupconnection)! | The groups this asset belongs to. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations/README.md#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations/README.md#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](../organizations/README.md#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](../organizations/members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

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
| `customFields` | [[CustomFieldFilter](../custom-fields.md#type-customfieldfilter)!] | Filter by custom field values. |

</details>

<details>

<summary>CustomFieldFilter</summary>

A filter condition for a custom field value.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The custom field code to filter by. |
| `operator` | [FieldOperator](../custom-fields.md#type-fieldoperator)! | The comparison operator. |
| `value` | [CustomFieldFilterValue](../custom-fields.md#type-customfieldfiltervalue) | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

</details>

<details>

<summary>CustomFieldFilterValue</summary>

Typed filter value for custom fields. Exactly one field must be set (`@oneOf`).
Choose the variant that matches the custom field's data type:

| FieldType         | Variant      | Example                                |
|-------------------|--------------|----------------------------------------|
| STRING, TEXT      | `string`     | `{ string: "hello" }`                  |
| DECIMAL           | `decimal`    | `{ decimal: "42.50" }`                 |
| INTEGER           | `integer`    | `{ integer: 42 }`                      |
| BOOLEAN           | `boolean`    | `{ boolean: true }`                    |
| DATE              | `date`       | `{ date: "2024-01-15" }`              |
| DATETIME          | `datetime`   | `{ datetime: "2024-01-15T10:30:00Z" }`|
| OPTIONS, CATALOG, TAG | `string` | `{ string: "option_code" }`            |
| DEVICE, REFERENCE | `id`         | `{ id: "019a6a3f-..." }`              |
| (IN operator)     | `stringList` | `{ stringList: ["a", "b"] }`           |
| (IN operator)     | `idList`     | `{ idList: ["uuid1", "uuid2"] }`       |

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | `String` | String value — for STRING, TEXT, OPTIONS, CATALOG, TAG fields. |
| `decimal` | `Decimal` | Arbitrary-precision decimal value — for DECIMAL fields. |
| `integer` | `Long` | Signed 64-bit integer value — for INTEGER fields. |
| `boolean` | `Boolean` | Boolean value — for BOOLEAN fields. |
| `date` | `Date` | Date value — for DATE fields. |
| `datetime` | `DateTime` | Date-time value — for DATETIME fields. |
| `id` | `ID` | ID value — for DEVICE, REFERENCE fields. |
| `stringList` | `[String!]` | List of strings — for IN operator on string-based fields. |
| `idList` | `[ID!]` | List of IDs — for IN operator on reference fields. |

</details>

<details>

<summary>AssetOrder</summary>

Ordering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetOrderField](types.md#type-assetorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. Supported field types: STRING, TEXT, DECIMAL, INTEGER, DATE, DATETIME. OPTIONS, TAG, BOOLEAN, GEOJSON, SCHEDULE, DEVICE, REFERENCE, CATALOG are not supported for sorting. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AssetConnection</summary>

A paginated list of Asset items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetEdge](types.md#type-assetedge)!]! | A list of edges. |
| `nodes` | [[Asset](types.md#type-asset)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

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
