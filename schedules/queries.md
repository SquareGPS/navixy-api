# Schedules — Queries

### scheduleTypes

Lists schedule types for an organization.

```graphql
scheduleTypes(
    organizationId: ID!
    filter: CatalogItemFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
  ): ScheduleTypeConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` |  |
| `filter` | [CatalogItemFilter](../catalogs/catalog-items.md#catalogitemfilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [CatalogItemOrder](../catalogs/catalog-items.md#catalogitemorder) |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | `[Code!]` | Match any of these codes. |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](../catalogs/catalog-items.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>ScheduleTypeConnection</code></summary>

A paginated list of ScheduleType items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ScheduleTypeEdge](types.md#scheduletypeedge)!]! | A list of edges. |
| `nodes` | [[ScheduleType](types.md#scheduletype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>PageInfo (entity)</code></summary>

Information about the current page in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after the current page. |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page. |
| `startCursor` | `String` | The cursor pointing to the first item in the current page. |
| `endCursor` | `String` | The cursor pointing to the last item in the current page. |

</details>

---

### schedule

Retrieves a schedule by its ID.

```graphql
schedule("The ID of the schedule to retrieve." id: ID!): Schedule
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the schedule to retrieve. |

**Output types:**

<details>

<summary><code>Schedule</code></summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this schedule. |
| `type` | [ScheduleType](types.md#scheduletype)! | The schedule type classification. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule.
  This is an alias for the `schedule_data` custom field. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

</details>

<details>

<summary><code>Organization (entity)</code></summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `filter` | [OrganizationChildrenFilter](../organizations.md#organizationchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned children. |
| `filter` | [MemberFilter](../organizations/members.md#memberfilter) | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned members. |
| `filter` | [DeviceFilter](../devices/types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |
| `filter` | [AssetFilter](../assets/types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [GeoObjectFilter](../geo-objects/types.md#geoobjectfilter) | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned geo objects. |
| `filter` | [ScheduleFilter](types.md#schedulefilter) | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned schedules. |

</details>

---

### schedules

Lists schedules for an organization.

```graphql
schedules(
    organizationId: ID!
    filter: ScheduleFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: ScheduleOrder = { field: TITLE, direction: ASC }
  ): ScheduleConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` |  |
| `filter` | [ScheduleFilter](types.md#schedulefilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [ScheduleOrder](types.md#scheduleorder) |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary><code>ScheduleFilter</code></summary>

Filtering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by schedule types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values. |

</details>

<details>

<summary><code>CustomFieldFilter</code></summary>

A filter condition for a custom field value.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The custom field code to filter by. |
| `operator` | [FieldOperator](../custom-fields.md#fieldoperator)! | The comparison operator. |
| `value` | `JSON` | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

</details>

<details>

<summary><code>ScheduleOrder</code></summary>

Ordering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ScheduleOrderField](types.md#scheduleorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>ScheduleConnection</code></summary>

A paginated list of Schedule items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ScheduleEdge](types.md#scheduleedge)!]! | A list of edges. |
| `nodes` | [[Schedule](types.md#schedule)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>PageInfo (entity)</code></summary>

Information about the current page in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after the current page. |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page. |
| `startCursor` | `String` | The cursor pointing to the first item in the current page. |
| `endCursor` | `String` | The cursor pointing to the last item in the current page. |

</details>

---
