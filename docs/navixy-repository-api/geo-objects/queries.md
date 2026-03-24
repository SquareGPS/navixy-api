# Geo objects — Queries

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

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
| `field` | [CatalogItemOrderField](../catalogs/catalog-items.md#type-catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>GeoObjectTypeConnection</summary>

A paginated list of GeoObjectType items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectTypeEdge](types.md#type-geoobjecttypeedge)!]! | A list of edges. |
| `nodes` | [[GeoObjectType](types.md#type-geoobjecttype)!]! | A list of nodes in the connection (without edge metadata). |
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

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Customizable](../common.md#type-customizable), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](types.md#type-geoobjecttype)! | The geo object type classification. |
| `geojsonData` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry. This is an alias for the `geojson_data` custom field. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |
| `containsPoints` | [[PointContainmentResult](types.md#type-pointcontainmentresult)!]! | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

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
| `assets` | [AssetConnection](../assets/types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

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
| NUMBER            | `number`     | `{ number: 42.0 }`                     |
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
| `number` | `Float` | Numeric value — for NUMBER fields. |
| `boolean` | `Boolean` | Boolean value — for BOOLEAN fields. |
| `date` | `Date` | Date value — for DATE fields. |
| `datetime` | `DateTime` | Date-time value — for DATETIME fields. |
| `id` | `ID` | ID value — for DEVICE, REFERENCE fields. |
| `stringList` | `[String!]` | List of strings — for IN operator on string-based fields. |
| `idList` | `[ID!]` | List of IDs — for IN operator on reference fields. |

</details>

<details>

<summary>GeoObjectOrder</summary>

Ordering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [GeoObjectOrderField](types.md#type-geoobjectorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>GeoObjectConnection</summary>

A paginated list of GeoObject items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectEdge](types.md#type-geoobjectedge)!]! | A list of edges. |
| `nodes` | [[GeoObject](types.md#type-geoobject)!]! | A list of nodes in the connection (without edge metadata). |
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
