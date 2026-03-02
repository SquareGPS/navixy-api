# Geo objects — Queries

### geoObjectTypes

Lists geo object types for an organization.

```graphql
geoObjectTypes(
    organizationId: ID!
    filter: CatalogItemFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
  ): GeoObjectTypeConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve geo object types for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned geo object types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned geo object types. |

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

<summary>GeoObjectTypeConnection</summary>

A paginated list of GeoObjectType items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectTypeEdge](types.md#geoobjecttypeedge)!]! | A list of edges. |
| `nodes` | [[GeoObjectType](types.md#geoobjecttype)!]! | A list of nodes in the connection (without edge metadata). |
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

### geoObject

Retrieves a geo object by its ID.

```graphql
geoObject(id: ID!): GeoObject
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the geo object to retrieve. |

**Output types:**

<details>

<summary>GeoObject</summary>

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](types.md#geoobjecttype)! | The geo object type classification. |
| `geometry` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry. This is an alias for the `geojson` custom field. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |
| `containsPoints` | [[PointContainmentResult](types.md#pointcontainmentresult)!]! | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

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
| `assets` | [AssetConnection](../assets/types.md#assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](types.md#geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules/types.md#scheduleconnection)! | The schedules owned by this organization. |

</details>

---

### geoObjects

Lists geo objects for an organization.

```graphql
geoObjects(
    organizationId: ID!
    filter: GeoObjectFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: GeoObjectOrder = { field: TITLE, direction: ASC }
  ): GeoObjectConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve geo objects for. |
| `filter` | `GeoObjectFilter` | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder` | The ordering options for the returned geo objects. |

**Input types:**

<details>

<summary>GeoObjectFilter</summary>

Filtering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by geo object types (OR within field). |
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

<summary>GeoObjectOrder</summary>

Ordering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [GeoObjectOrderField](types.md#geoobjectorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>GeoObjectConnection</summary>

A paginated list of GeoObject items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectEdge](types.md#geoobjectedge)!]! | A list of edges. |
| `nodes` | [[GeoObject](types.md#geoobject)!]! | A list of nodes in the connection (without edge metadata). |
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
