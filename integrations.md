# Integrations

Third-party integrations and external system connections.

## Queries

### integration

Retrieves an integration by its ID.

```graphql
integration(id: ID!): Integration
```

**Arguments**

| Name | Type  | Description                            |
| ---- | ----- | -------------------------------------- |
| `id` | `ID!` | The ID of the integration to retrieve. |

**Output types:**

<details>

<summary><code>Integration</code></summary>

| Field           | Type                                                            | Description                                          |
| --------------- | --------------------------------------------------------------- | ---------------------------------------------------- |
| `id`            | `ID!`                                                           |                                                      |
| `version`       | `Int!`                                                          |                                                      |
| `title`         | `String!`                                                       |                                                      |
| `organization`  | [Organization](core-api-reference/organizations/#organization)! | The organization this integration belongs to.        |
| `credentialRef` | `String`                                                        | A reference to credentials stored in a secure vault. |
| `isActive`      | `Boolean!`                                                      | Whether this integration is active.                  |

</details>

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

| Name             | Type                                                   | Description                                                                                   |
| ---------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                                  | The organization to retrieve integrations for.                                                |
| `filter`         | [IntegrationFilter](integrations.md#integrationfilter) | Filtering options for the returned integrations.                                              |
| `first`          | `Int`                                                  | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                               | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                                  | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                               | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [IntegrationOrder](integrations.md#integrationorder)   | The ordering options for the returned integrations.                                           |

**Input types:**

<details>

<summary><code>IntegrationFilter</code></summary>

| Field      | Type      | Description              |
| ---------- | --------- | ------------------------ |
| `isActive` | `Boolean` | Filter by active status. |

</details>

<details>

<summary><code>IntegrationOrder</code></summary>

| Field       | Type                                                                     | Description             |
| ----------- | ------------------------------------------------------------------------ | ----------------------- |
| `field`     | [IntegrationOrderField](integrations.md#integrationorderfield)!          | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>IntegrationConnection</code></summary>

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[IntegrationEdge](integrations.md#integrationedge)!]!       | A list of edges.                                           |
| `nodes`    | \[[Integration](integrations.md#integration)!]!               | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Integration (node)</code></summary>

| Field           | Type                                                            | Description                                          |
| --------------- | --------------------------------------------------------------- | ---------------------------------------------------- |
| `id`            | `ID!`                                                           |                                                      |
| `version`       | `Int!`                                                          |                                                      |
| `title`         | `String!`                                                       |                                                      |
| `organization`  | [Organization](core-api-reference/organizations/#organization)! | The organization this integration belongs to.        |
| `credentialRef` | `String`                                                        | A reference to credentials stored in a secure vault. |
| `isActive`      | `Boolean!`                                                      | Whether this integration is active.                  |

</details>

## Mutations

### integrationCreate

Creates a new integration.

```graphql
integrationCreate(
  input: IntegrationCreateInput!
): IntegrationPayload
```

**Arguments**

| Name    | Type                                                              | Description                                    |
| ------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| `input` | [IntegrationCreateInput](integrations.md#integrationcreateinput)! | The input fields for creating the integration. |

**Input types:**

<details>

<summary><code>IntegrationCreateInput</code></summary>

| Field            | Type      | Description                                     |
| ---------------- | --------- | ----------------------------------------------- |
| `organizationId` | `ID!`     | The organization that will own the integration. |
| `title`          | `String!` | The display name.                               |
| `credentialRef`  | `String`  | A reference to credentials in a secure vault.   |

</details>

**Output types:**

<details>

<summary><code>IntegrationPayload</code></summary>

| Field         | Type                                        | Description                         |
| ------------- | ------------------------------------------- | ----------------------------------- |
| `integration` | [Integration](integrations.md#integration)! | The created or updated integration. |

</details>

<details>

<summary><code>Integration (entity)</code></summary>

| Field           | Type                                                            | Description                                          |
| --------------- | --------------------------------------------------------------- | ---------------------------------------------------- |
| `id`            | `ID!`                                                           |                                                      |
| `version`       | `Int!`                                                          |                                                      |
| `title`         | `String!`                                                       |                                                      |
| `organization`  | [Organization](core-api-reference/organizations/#organization)! | The organization this integration belongs to.        |
| `credentialRef` | `String`                                                        | A reference to credentials stored in a secure vault. |
| `isActive`      | `Boolean!`                                                      | Whether this integration is active.                  |

</details>

### integrationUpdate

Updates an existing integration.

```graphql
integrationUpdate(
  input: IntegrationUpdateInput!
): IntegrationPayload
```

**Arguments**

| Name    | Type                                                              | Description                                    |
| ------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| `input` | [IntegrationUpdateInput](integrations.md#integrationupdateinput)! | The input fields for updating the integration. |

**Input types:**

<details>

<summary><code>IntegrationUpdateInput</code></summary>

| Field           | Type      | Description                                 |
| --------------- | --------- | ------------------------------------------- |
| `id`            | `ID!`     | The integration ID to update.               |
| `version`       | `Int!`    | The current version for optimistic locking. |
| `title`         | `String`  | The new display name.                       |
| `credentialRef` | `String`  | The new credential reference.               |
| `isActive`      | `Boolean` | The new active status.                      |

</details>

**Output types:**

<details>

<summary><code>IntegrationPayload</code></summary>

| Field         | Type                                        | Description                         |
| ------------- | ------------------------------------------- | ----------------------------------- |
| `integration` | [Integration](integrations.md#integration)! | The created or updated integration. |

</details>

<details>

<summary><code>Integration (entity)</code></summary>

| Field           | Type                                                            | Description                                          |
| --------------- | --------------------------------------------------------------- | ---------------------------------------------------- |
| `id`            | `ID!`                                                           |                                                      |
| `version`       | `Int!`                                                          |                                                      |
| `title`         | `String!`                                                       |                                                      |
| `organization`  | [Organization](core-api-reference/organizations/#organization)! | The organization this integration belongs to.        |
| `credentialRef` | `String`                                                        | A reference to credentials stored in a secure vault. |
| `isActive`      | `Boolean!`                                                      | Whether this integration is active.                  |

</details>

### integrationDelete

Deletes an integration.

```graphql
integrationDelete(
  input: IntegrationDeleteInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                              | Description                                    |
| ------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| `input` | [IntegrationDeleteInput](integrations.md#integrationdeleteinput)! | The input fields for deleting the integration. |

**Input types:**

<details>

<summary><code>IntegrationDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The integration ID to delete.               |
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

### IntegrationConnection

A paginated list of Integration items.

**Implements:** [`Connection`](core-api-reference/common-resources.md#connection)

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[IntegrationEdge](integrations.md#integrationedge)!]!       | A list of edges.                                           |
| `nodes`    | \[[Integration](integrations.md#integration)!]!               | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### IntegrationEdge

An edge in the Integration connection.

**Implements:** [`Edge`](core-api-reference/common-resources.md#edge)

| Field    | Type                                        | Description                             |
| -------- | ------------------------------------------- | --------------------------------------- |
| `cursor` | `String!`                                   | An opaque cursor for this edge.         |
| `node`   | [Integration](integrations.md#integration)! | The integration at the end of the edge. |

### Integration

An external system integration with API access.

**Implements:** [`Actor`](access-control/types.md#actor), [`Node`](core-api-reference/common-resources.md#node), [`Versioned`](core-api-reference/common-resources.md#versioned), [`Titled`](core-api-reference/common-resources.md#titled)

| Field           | Type                                                            | Description                                          |
| --------------- | --------------------------------------------------------------- | ---------------------------------------------------- |
| `id`            | `ID!`                                                           |                                                      |
| `version`       | `Int!`                                                          |                                                      |
| `title`         | `String!`                                                       |                                                      |
| `organization`  | [Organization](core-api-reference/organizations/#organization)! | The organization this integration belongs to.        |
| `credentialRef` | `String`                                                        | A reference to credentials stored in a secure vault. |
| `isActive`      | `Boolean!`                                                      | Whether this integration is active.                  |

### IntegrationPayload

The result of an integration mutation.

| Field         | Type                                        | Description                         |
| ------------- | ------------------------------------------- | ----------------------------------- |
| `integration` | [Integration](integrations.md#integration)! | The created or updated integration. |

## Inputs

### IntegrationFilter

Filtering options for integrations.

| Field      | Type      | Description              |
| ---------- | --------- | ------------------------ |
| `isActive` | `Boolean` | Filter by active status. |

### IntegrationOrder

Ordering options for integrations.

| Field       | Type                                                                     | Description             |
| ----------- | ------------------------------------------------------------------------ | ----------------------- |
| `field`     | [IntegrationOrderField](integrations.md#integrationorderfield)!          | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

### IntegrationCreateInput

Input for creating a new integration.

| Field            | Type      | Description                                     |
| ---------------- | --------- | ----------------------------------------------- |
| `organizationId` | `ID!`     | The organization that will own the integration. |
| `title`          | `String!` | The display name.                               |
| `credentialRef`  | `String`  | A reference to credentials in a secure vault.   |

### IntegrationUpdateInput

Input for updating an existing integration.

| Field           | Type      | Description                                 |
| --------------- | --------- | ------------------------------------------- |
| `id`            | `ID!`     | The integration ID to update.               |
| `version`       | `Int!`    | The current version for optimistic locking. |
| `title`         | `String`  | The new display name.                       |
| `credentialRef` | `String`  | The new credential reference.               |
| `isActive`      | `Boolean` | The new active status.                      |

### IntegrationDeleteInput

Input for deleting an integration.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The integration ID to delete.               |
| `version` | `Int!` | The current version for optimistic locking. |

## Enums

### IntegrationOrderField

Fields available for ordering integrations.

| Value   | Description     |
| ------- | --------------- |
| `TITLE` | Order by title. |
