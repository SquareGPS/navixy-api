# Members

Organization membership and user-organization relationships.

## Queries

### member

Retrieves a member by its ID.

```graphql
member(id: ID!): Member
```

**Arguments**

| Name | Type  | Description                       |
| ---- | ----- | --------------------------------- |
| `id` | `ID!` | The ID of the member to retrieve. |

**Output types:**

<details>

<summary><code>Member</code></summary>

| Field          | Type                                         | Description                                                        |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| `id`           | `ID!`                                        |                                                                    |
| `version`      | `Int!`                                       |                                                                    |
| `user`         | [User](../../users.md#user)!                 | The user.                                                          |
| `organization` | [Organization](./#organization)!             | The organization the user belongs to.                              |
| `isActive`     | `Boolean!`                                   | Whether this membership is active.                                 |
| `assignedAt`   | [DateTime](../common-resources.md#datetime)! | The date and time when the user was assigned to this organization. |
| `customFields` | [JSON](../common-resources.md#json)!         | Membership-specific custom fields such as position and department. |

</details>

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

| Name             | Type                                    | Description                                                                                   |
| ---------------- | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                   | The organization to retrieve members for.                                                     |
| `filter`         | [MemberFilter](members.md#memberfilter) | Filtering options for the returned members.                                                   |
| `first`          | `Int`                                   | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                   | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [MemberOrder](members.md#memberorder)   | The ordering options for the returned members.                                                |

**Input types:**

<details>

<summary><code>MemberFilter</code></summary>

| Field      | Type      | Description                        |
| ---------- | --------- | ---------------------------------- |
| `userIds`  | `[ID!]`   | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status.           |

</details>

<details>

<summary><code>MemberOrder</code></summary>

| Field       | Type                                                     | Description             |
| ----------- | -------------------------------------------------------- | ----------------------- |
| `field`     | [MemberOrderField](members.md#memberorderfield)!         | The field to order by.  |
| `direction` | [OrderDirection](../common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>MemberConnection</code></summary>

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[MemberEdge](members.md#memberedge)!]!      | A list of edges.                                           |
| `nodes`    | \[[Member](members.md#member)!]!              | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Member (node)</code></summary>

| Field          | Type                                         | Description                                                        |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| `id`           | `ID!`                                        |                                                                    |
| `version`      | `Int!`                                       |                                                                    |
| `user`         | [User](../../users.md#user)!                 | The user.                                                          |
| `organization` | [Organization](./#organization)!             | The organization the user belongs to.                              |
| `isActive`     | `Boolean!`                                   | Whether this membership is active.                                 |
| `assignedAt`   | [DateTime](../common-resources.md#datetime)! | The date and time when the user was assigned to this organization. |
| `customFields` | [JSON](../common-resources.md#json)!         | Membership-specific custom fields such as position and department. |

</details>

## Mutations

### memberCreate

Adds a user to an organization as a member.

```graphql
memberCreate(input: MemberCreateInput!): MemberPayload
```

**Arguments**

| Name    | Type                                               | Description                                   |
| ------- | -------------------------------------------------- | --------------------------------------------- |
| `input` | [MemberCreateInput](members.md#membercreateinput)! | The input fields for creating the membership. |

**Input types:**

<details>

<summary><code>MemberCreateInput</code></summary>

| Field            | Type                                                                    | Description                            |
| ---------------- | ----------------------------------------------------------------------- | -------------------------------------- |
| `organizationId` | `ID!`                                                                   | The organization ID.                   |
| `userId`         | `ID!`                                                                   | The user ID to add.                    |
| `customFields`   | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The membership-specific custom fields. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                    | Description                                 |
| ------- | --------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](../common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](../common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>MemberPayload</code></summary>

| Field    | Type                         | Description                        |
| -------- | ---------------------------- | ---------------------------------- |
| `member` | [Member](members.md#member)! | The created or updated membership. |

</details>

<details>

<summary><code>Member (entity)</code></summary>

| Field          | Type                                         | Description                                                        |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| `id`           | `ID!`                                        |                                                                    |
| `version`      | `Int!`                                       |                                                                    |
| `user`         | [User](../../users.md#user)!                 | The user.                                                          |
| `organization` | [Organization](./#organization)!             | The organization the user belongs to.                              |
| `isActive`     | `Boolean!`                                   | Whether this membership is active.                                 |
| `assignedAt`   | [DateTime](../common-resources.md#datetime)! | The date and time when the user was assigned to this organization. |
| `customFields` | [JSON](../common-resources.md#json)!         | Membership-specific custom fields such as position and department. |

</details>

### memberUpdate

Updates a membership.

```graphql
memberUpdate(input: MemberUpdateInput!): MemberPayload
```

**Arguments**

| Name    | Type                                               | Description                                   |
| ------- | -------------------------------------------------- | --------------------------------------------- |
| `input` | [MemberUpdateInput](members.md#memberupdateinput)! | The input fields for updating the membership. |

**Input types:**

<details>

<summary><code>MemberUpdateInput</code></summary>

| Field          | Type                                                                    | Description                                 |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                                   | The membership ID to update.                |
| `version`      | `Int!`                                                                  | The current version for optimistic locking. |
| `isActive`     | `Boolean`                                                               | The new active status.                      |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                    | Description                                 |
| ------- | --------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](../common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](../common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>MemberPayload</code></summary>

| Field    | Type                         | Description                        |
| -------- | ---------------------------- | ---------------------------------- |
| `member` | [Member](members.md#member)! | The created or updated membership. |

</details>

<details>

<summary><code>Member (entity)</code></summary>

| Field          | Type                                         | Description                                                        |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| `id`           | `ID!`                                        |                                                                    |
| `version`      | `Int!`                                       |                                                                    |
| `user`         | [User](../../users.md#user)!                 | The user.                                                          |
| `organization` | [Organization](./#organization)!             | The organization the user belongs to.                              |
| `isActive`     | `Boolean!`                                   | Whether this membership is active.                                 |
| `assignedAt`   | [DateTime](../common-resources.md#datetime)! | The date and time when the user was assigned to this organization. |
| `customFields` | [JSON](../common-resources.md#json)!         | Membership-specific custom fields such as position and department. |

</details>

### memberRemove

Removes a user from an organization.

```graphql
memberRemove(input: MemberRemoveInput!): DeletePayload
```

**Arguments**

| Name    | Type                                               | Description                                   |
| ------- | -------------------------------------------------- | --------------------------------------------- |
| `input` | [MemberRemoveInput](members.md#memberremoveinput)! | The input fields for removing the membership. |

**Input types:**

<details>

<summary><code>MemberRemoveInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The membership ID to remove.                |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

## Types

### MemberConnection

A paginated list of Member items.

**Implements:** [`Connection`](../common-resources.md#connection)

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[MemberEdge](members.md#memberedge)!]!      | A list of edges.                                           |
| `nodes`    | \[[Member](members.md#member)!]!              | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

### MemberEdge

An edge in the Member connection.

**Implements:** [`Edge`](../common-resources.md#edge)

| Field    | Type                         | Description                        |
| -------- | ---------------------------- | ---------------------------------- |
| `cursor` | `String!`                    | An opaque cursor for this edge.    |
| `node`   | [Member](members.md#member)! | The member at the end of the edge. |

### Member

A user's membership in an organization.

**Implements:** [`Node`](../common-resources.md#node), [`Customizable`](../common-resources.md#customizable), [`Versioned`](../common-resources.md#versioned)

| Field          | Type                                         | Description                                                        |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| `id`           | `ID!`                                        |                                                                    |
| `version`      | `Int!`                                       |                                                                    |
| `user`         | [User](../../users.md#user)!                 | The user.                                                          |
| `organization` | [Organization](./#organization)!             | The organization the user belongs to.                              |
| `isActive`     | `Boolean!`                                   | Whether this membership is active.                                 |
| `assignedAt`   | [DateTime](../common-resources.md#datetime)! | The date and time when the user was assigned to this organization. |
| `customFields` | [JSON](../common-resources.md#json)!         | Membership-specific custom fields such as position and department. |

### MemberPayload

The result of a membership mutation.

| Field    | Type                         | Description                        |
| -------- | ---------------------------- | ---------------------------------- |
| `member` | [Member](members.md#member)! | The created or updated membership. |

## Inputs

### MemberFilter

Filtering options for members.

| Field      | Type      | Description                        |
| ---------- | --------- | ---------------------------------- |
| `userIds`  | `[ID!]`   | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status.           |

### MemberOrder

Ordering options for members.

| Field       | Type                                                     | Description             |
| ----------- | -------------------------------------------------------- | ----------------------- |
| `field`     | [MemberOrderField](members.md#memberorderfield)!         | The field to order by.  |
| `direction` | [OrderDirection](../common-resources.md#orderdirection)! | The direction to order. |

### MemberCreateInput

Input for creating a membership.

| Field            | Type                                                                    | Description                            |
| ---------------- | ----------------------------------------------------------------------- | -------------------------------------- |
| `organizationId` | `ID!`                                                                   | The organization ID.                   |
| `userId`         | `ID!`                                                                   | The user ID to add.                    |
| `customFields`   | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The membership-specific custom fields. |

### MemberUpdateInput

Input for updating a membership.

| Field          | Type                                                                    | Description                                 |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                                   | The membership ID to update.                |
| `version`      | `Int!`                                                                  | The current version for optimistic locking. |
| `isActive`     | `Boolean`                                                               | The new active status.                      |
| `customFields` | [CustomFieldsPatchInput](../../custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

### MemberRemoveInput

Input for removing a membership.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The membership ID to remove.                |
| `version` | `Int!` | The current version for optimistic locking. |

## Enums

### MemberOrderField

Fields available for ordering members.

| Value         | Description               |
| ------------- | ------------------------- |
| `ASSIGNED_AT` | Order by assignment date. |
