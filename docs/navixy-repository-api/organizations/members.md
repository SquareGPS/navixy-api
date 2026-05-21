# Members

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

Organization members represent the relationship between users and organizations, including their roles and permissions within each organization.

## Queries

### member

Retrieves a member by its ID.

```graphql
member(id: ID!): Member
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the member to retrieve. |

**Output types:**

<details>

<summary>Member</summary>

A user's membership in an organization.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `user` | [User](../actors/users.md#type-user)! | The user. |
| `organization` | [Organization](README.md#type-organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |

</details>

<details>

<summary>User (entity)</summary>

A human user account authenticated via an identity provider.

**Implements:** [Actor](../actors/README.md#type-actor), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](../actors/README.md#type-personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | `EmailAddress!` | The user's primary email address. |
| `locale` | `Locale` | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `memberships` | [MemberConnection](#type-memberconnection)! | The organization memberships for this user. |

</details>

---

### members

Lists members of an organization.

```graphql
members(
    organizationId: ID!
    filter: MemberFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: MemberOrder = { field: ASSIGNED_AT, direction: DESC }
  ): MemberConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve members for. |
| `filter` | `MemberFilter` | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder` | The ordering options for the returned members. |

**Input types:**

<details>

<summary>MemberFilter</summary>

Filtering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userIds` | `[ID!]` | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

</details>

<details>

<summary>MemberOrder</summary>

Ordering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [MemberOrderField](#type-memberorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>MemberConnection</summary>

A paginated list of Member items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[MemberEdge](#type-memberedge)!]! | A list of edges. |
| `nodes` | [[Member](#type-member)!]! | A list of nodes in the connection (without edge metadata). |
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

## Mutations

### memberCreate

Adds a user to an organization as a member.

```graphql
memberCreate(
    input: MemberCreateInput!
  ): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MemberCreateInput!` | The input fields for creating the membership. |

**Input types:**

<details>

<summary>MemberCreateInput</summary>

Input for creating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `userId` | `ID!` | The user ID to add. |

</details>

**Output types:**

<details>

<summary>MemberPayload</summary>

The result of a membership mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `member` | [Member](#type-member)! | The created or updated membership. |

</details>

<details>

<summary>Member (entity)</summary>

A user's membership in an organization.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `user` | [User](../actors/users.md#type-user)! | The user. |
| `organization` | [Organization](README.md#type-organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |

</details>

---

### memberUpdate

Updates a membership.

```graphql
memberUpdate(
    input: MemberUpdateInput!
  ): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MemberUpdateInput!` | The input fields for updating the membership. |

**Input types:**

<details>

<summary>MemberUpdateInput</summary>

Input for updating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `isActive` | `Boolean` | The new active status. |

</details>

**Output types:**

<details>

<summary>MemberPayload</summary>

The result of a membership mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `member` | [Member](#type-member)! | The created or updated membership. |

</details>

<details>

<summary>Member (entity)</summary>

A user's membership in an organization.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `user` | [User](../actors/users.md#type-user)! | The user. |
| `organization` | [Organization](README.md#type-organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |

</details>

---

### memberRemove

Removes a user from an organization.

```graphql
memberRemove(
    input: MemberRemoveInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MemberRemoveInput!` | The input fields for removing the membership. |

**Input types:**

<details>

<summary>MemberRemoveInput</summary>

Input for removing a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to remove. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

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

<a id="type-member"></a>

### Member

A user's membership in an organization.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `user` | [User](../actors/users.md#type-user)! | The user. |
| `organization` | [Organization](README.md#type-organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |

---

<a id="type-memberpayload"></a>

### MemberPayload

The result of a membership mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `member` | [Member](#type-member)! | The created or updated membership. |

---

## Inputs

<a id="type-memberfilter"></a>

### MemberFilter

Filtering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userIds` | `[ID!]` | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

---

<a id="type-memberorder"></a>

### MemberOrder

Ordering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [MemberOrderField](#type-memberorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-membercreateinput"></a>

### MemberCreateInput

Input for creating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `userId` | `ID!` | The user ID to add. |

---

<a id="type-memberupdateinput"></a>

### MemberUpdateInput

Input for updating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `isActive` | `Boolean` | The new active status. |

---

<a id="type-memberremoveinput"></a>

### MemberRemoveInput

Input for removing a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to remove. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

## Enums

<a id="type-memberorderfield"></a>

### MemberOrderField

Fields available for ordering members.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

---

## Pagination types

<a id="type-memberconnection"></a>

### MemberConnection

A paginated list of Member items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[MemberEdge](#type-memberedge)!]! | A list of edges. |
| `nodes` | [[Member](#type-member)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-memberedge"></a>

### MemberEdge

An edge in the Member connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Member](#type-member)! | The member at the end of the edge. |

---
