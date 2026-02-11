# Members

Organization members represent the relationship between users and organizations, including their roles and permissions within each organization.

## Queries

### member

Retrieves a member by its ID.

```graphql
member("The ID of the member to retrieve." id: ID!): Member
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the member to retrieve. |

**Output types:**

<details>

<summary><code>Member</code></summary>

A user's membership in an organization.

**Implements:** [Node](../../common.md#node), [Customizable](../../common.md#customizable), [Versioned](../../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `user` | [User](../../actors/users.md#user)! | The user. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

</details>

<details>

<summary><code>User (entity)</code></summary>

A human user account authenticated via an identity provider.

**Implements:** [Actor](../../actors.md#actor), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](../../actors.md#personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | `EmailAddress!` | The user's primary email address. |
| `locale` | `Locale` | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `filter` | [MemberFilter](../members.md#memberfilter) | Filtering options for the returned memberships. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned memberships. |

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
| `organizationId` | `ID!` |  |
| `filter` | [MemberFilter](../members.md#memberfilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [MemberOrder](../members.md#memberorder) |  |
| `direction` | `DESC }` |  |

**Input types:**

<details>

<summary><code>MemberFilter</code></summary>

Filtering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userIds` | `[ID!]` | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

</details>

<details>

<summary><code>MemberOrder</code></summary>

Ordering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [MemberOrderField](../members.md#memberorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>MemberConnection</code></summary>

A paginated list of Member items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[MemberEdge](../members.md#memberedge)!]! | A list of edges. |
| `nodes` | [[Member](../members.md#member)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

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

## Mutations

### memberCreate

Adds a user to an organization as a member.

```graphql
memberCreate("The input fields for creating the membership." input: MemberCreateInput!): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MemberCreateInput](../members.md#membercreateinput)! | The input fields for creating the membership. |

**Input types:**

<details>

<summary><code>MemberCreateInput</code></summary>

Input for creating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `userId` | `ID!` | The user ID to add. |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The membership-specific custom fields. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>MemberPayload</code></summary>

The result of a membership mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `member` | [Member](../members.md#member)! | The created or updated membership. |

</details>

<details>

<summary><code>Member (entity)</code></summary>

A user's membership in an organization.

**Implements:** [Node](../../common.md#node), [Customizable](../../common.md#customizable), [Versioned](../../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `user` | [User](../../actors/users.md#user)! | The user. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

</details>

---

### memberUpdate

Updates a membership.

```graphql
memberUpdate("The input fields for updating the membership." input: MemberUpdateInput!): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MemberUpdateInput](../members.md#memberupdateinput)! | The input fields for updating the membership. |

**Input types:**

<details>

<summary><code>MemberUpdateInput</code></summary>

Input for updating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `isActive` | `Boolean` | The new active status. |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field changes. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>MemberPayload</code></summary>

The result of a membership mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `member` | [Member](../members.md#member)! | The created or updated membership. |

</details>

<details>

<summary><code>Member (entity)</code></summary>

A user's membership in an organization.

**Implements:** [Node](../../common.md#node), [Customizable](../../common.md#customizable), [Versioned](../../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `user` | [User](../../actors/users.md#user)! | The user. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

</details>

---

### memberRemove

Removes a user from an organization.

```graphql
memberRemove("The input fields for removing the membership." input: MemberRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MemberRemoveInput](../members.md#memberremoveinput)! | The input fields for removing the membership. |

**Input types:**

<details>

<summary><code>MemberRemoveInput</code></summary>

Input for removing a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to remove. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

## Objects

### Member

A user's membership in an organization.

**Implements:** [Node](../../common.md#node), [Customizable](../../common.md#customizable), [Versioned](../../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `user` | [User](../../actors/users.md#user)! | The user. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization the user belongs to. |
| `isActive` | `Boolean!` | Whether this membership is active. |
| `assignedAt` | `DateTime!` | The date and time when the user was assigned to this organization. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

---

### MemberPayload

The result of a membership mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `member` | [Member](../members.md#member)! | The created or updated membership. |

---

## Inputs

### MemberFilter

Filtering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userIds` | `[ID!]` | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

---

### MemberOrder

Ordering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [MemberOrderField](../members.md#memberorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

---

### MemberCreateInput

Input for creating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `userId` | `ID!` | The user ID to add. |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The membership-specific custom fields. |

---

### MemberUpdateInput

Input for updating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `isActive` | `Boolean` | The new active status. |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field changes. |

---

### MemberRemoveInput

Input for removing a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to remove. |
| `version` | `Int!` | The current version for optimistic locking. |

---

## Enums

### MemberOrderField

Fields available for ordering members.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

---

## Pagination types

### MemberConnection

A paginated list of Member items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[MemberEdge](../members.md#memberedge)!]! | A list of edges. |
| `nodes` | [[Member](../members.md#member)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### MemberEdge

An edge in the Member connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Member](../members.md#member)! | The member at the end of the edge. |

---
