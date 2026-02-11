# Integrations

Integration accounts for API clients, automated systems, and third-party service connections.

## Queries

### integration

Retrieves an integration by its ID.

```graphql
integration(id: ID!): Integration
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the integration to retrieve. |

**Output types:**

<details>

<summary>Integration</summary>

An external system integration with API access.

**Implements:** [Actor](../../actors.md#actor), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The display name of the actor. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization this integration belongs to. |
| `credentialRef` | `String` | A reference to credentials stored in a secure vault. |
| `isActive` | `Boolean!` | Whether this integration is active. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../../organizations.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../../organizations.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `filter` | [OrganizationChildrenFilter](../../organizations.md#organizationchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned children. |
| `filter` | [MemberFilter](../../organizations/members.md#memberfilter) | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned members. |
| `filter` | [DeviceFilter](../../devices/types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |
| `filter` | [AssetFilter](../../assets/types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [GeoObjectFilter](../../geo-objects/types.md#geoobjectfilter) | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned geo objects. |
| `filter` | [ScheduleFilter](../../schedules/types.md#schedulefilter) | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned schedules. |

</details>

---

### integrations

Lists integrations for an organization.

```graphql
integrations(
    organizationId: ID!
    filter: IntegrationFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: IntegrationOrder = { field: TITLE, direction: ASC }
  ): IntegrationConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` |  |
| `filter` | `IntegrationFilter` |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | `IntegrationOrder` |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary>IntegrationFilter</summary>

Filtering options for integrations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isActive` | `Boolean` | Filter by active status. |

</details>

<details>

<summary>IntegrationOrder</summary>

Ordering options for integrations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [IntegrationOrderField](../integrations.md#integrationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>IntegrationConnection</summary>

A paginated list of Integration items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[IntegrationEdge](../integrations.md#integrationedge)!]! | A list of edges. |
| `nodes` | [[Integration](../integrations.md#integration)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

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

## Mutations

### integrationCreate

Creates a new integration.

```graphql
integrationCreate(input: IntegrationCreateInput!): IntegrationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `IntegrationCreateInput!` | The input fields for creating the integration. |

**Input types:**

<details>

<summary>IntegrationCreateInput</summary>

Input for creating a new integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the integration. |
| `title` | `String!` | The display name. |
| `credentialRef` | `String` | A reference to credentials in a secure vault. |

</details>

**Output types:**

<details>

<summary>IntegrationPayload</summary>

The result of an integration mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `integration` | [Integration](../integrations.md#integration)! | The created or updated integration. |

</details>

<details>

<summary>Integration (entity)</summary>

An external system integration with API access.

**Implements:** [Actor](../../actors.md#actor), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The display name of the actor. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization this integration belongs to. |
| `credentialRef` | `String` | A reference to credentials stored in a secure vault. |
| `isActive` | `Boolean!` | Whether this integration is active. |

</details>

---

### integrationUpdate

Updates an existing integration.

```graphql
integrationUpdate(input: IntegrationUpdateInput!): IntegrationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `IntegrationUpdateInput!` | The input fields for updating the integration. |

**Input types:**

<details>

<summary>IntegrationUpdateInput</summary>

Input for updating an existing integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `credentialRef` | `String` | The new credential reference. |
| `isActive` | `Boolean` | The new active status. |

</details>

**Output types:**

<details>

<summary>IntegrationPayload</summary>

The result of an integration mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `integration` | [Integration](../integrations.md#integration)! | The created or updated integration. |

</details>

<details>

<summary>Integration (entity)</summary>

An external system integration with API access.

**Implements:** [Actor](../../actors.md#actor), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The display name of the actor. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization this integration belongs to. |
| `credentialRef` | `String` | A reference to credentials stored in a secure vault. |
| `isActive` | `Boolean!` | Whether this integration is active. |

</details>

---

### integrationDelete

Deletes an integration.

```graphql
integrationDelete(input: IntegrationDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `IntegrationDeleteInput!` | The input fields for deleting the integration. |

**Input types:**

<details>

<summary>IntegrationDeleteInput</summary>

Input for deleting an integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary>DeletePayload</summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

## Objects

### Integration

An external system integration with API access.

**Implements:** [Actor](../../actors.md#actor), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The display name of the actor. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization this integration belongs to. |
| `credentialRef` | `String` | A reference to credentials stored in a secure vault. |
| `isActive` | `Boolean!` | Whether this integration is active. |

---

### IntegrationPayload

The result of an integration mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `integration` | [Integration](../integrations.md#integration)! | The created or updated integration. |

---

## Inputs

### IntegrationFilter

Filtering options for integrations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isActive` | `Boolean` | Filter by active status. |

---

### IntegrationOrder

Ordering options for integrations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [IntegrationOrderField](../integrations.md#integrationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

---

### IntegrationCreateInput

Input for creating a new integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the integration. |
| `title` | `String!` | The display name. |
| `credentialRef` | `String` | A reference to credentials in a secure vault. |

---

### IntegrationUpdateInput

Input for updating an existing integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `credentialRef` | `String` | The new credential reference. |
| `isActive` | `Boolean` | The new active status. |

---

### IntegrationDeleteInput

Input for deleting an integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

## Enums

### IntegrationOrderField

Fields available for ordering integrations.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

### IntegrationConnection

A paginated list of Integration items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[IntegrationEdge](../integrations.md#integrationedge)!]! | A list of edges. |
| `nodes` | [[Integration](../integrations.md#integration)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### IntegrationEdge

An edge in the Integration connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Integration](../integrations.md#integration)! | The integration at the end of the edge. |

---
