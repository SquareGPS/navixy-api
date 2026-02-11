# Users

User accounts representing human operators who access the system through the UI or API.

## Queries

### me

Retrieves the currently authenticated actor.

```graphql
me: Actor!
```

**Output types:**

<details>

<summary><code>Actor</code></summary>

An entity that can perform actions and have permissions assigned.

**Implements:** [Node](../../common.md#node), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `title` | `String!` | The display name of the actor. |

</details>

---

## Mutations

### myProfileUpdate

Updates the current user's profile (name only).

```graphql
myProfileUpdate("The input fields for updating the profile." input: MyProfileUpdateInput!): UserPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MyProfileUpdateInput](../users.md#myprofileupdateinput)! | The input fields for updating the profile. |

**Input types:**

<details>

<summary><code>MyProfileUpdateInput</code></summary>

Input for updating the current user's profile.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput](../users.md#personnameinput)! | The structured name components. |

</details>

<details>

<summary><code>PersonNameInput</code></summary>

Input for structured person name components.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s). |
| `familyNames` | `String!` | The family name(s). |
| `middleName` | `String` | The middle name or patronymic. |

</details>

**Output types:**

<details>

<summary><code>UserPayload</code></summary>

The result of a user profile mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `user` | [User](../users.md#user)! | The updated user. |

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
| `filter` | [MemberFilter](../../organizations/members.md#memberfilter) | Filtering options for the returned memberships. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned memberships. |

</details>

---

### userCatalogItemCreate

Creates a new user catalog item.

```graphql
userCatalogItemCreate("The input fields for creating the item." input: UserCatalogItemCreateInput!): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserCatalogItemCreateInput](../users.md#usercatalogitemcreateinput)! | The input fields for creating the item. |

**Input types:**

<details>

<summary><code>UserCatalogItemCreateInput</code></summary>

Input for creating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | `Code!` | The machine-readable code, unique within the catalog and organization. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>UserCatalogItemPayload</code></summary>

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](../users.md#usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary><code>UserCatalogItem (entity)</code></summary>

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [HierarchicalCatalogItem](../../catalogs.md#hierarchicalcatalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `parent` | [UserCatalogItem](../users.md#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `filter` | [CatalogItemChildrenFilter](../../catalogs/catalog-items.md#catalogitemchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder = { field: ORDER, direction: ASC }` | The ordering options for the returned children. |

</details>

---

### userCatalogItemUpdate

Updates a user catalog item.

```graphql
userCatalogItemUpdate("The input fields for updating the item." input: UserCatalogItemUpdateInput!): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserCatalogItemUpdateInput](../users.md#usercatalogitemupdateinput)! | The input fields for updating the item. |

**Input types:**

<details>

<summary><code>UserCatalogItemUpdateInput</code></summary>

Input for updating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>UserCatalogItemPayload</code></summary>

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](../users.md#usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary><code>UserCatalogItem (entity)</code></summary>

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [HierarchicalCatalogItem](../../catalogs.md#hierarchicalcatalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `parent` | [UserCatalogItem](../users.md#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `filter` | [CatalogItemChildrenFilter](../../catalogs/catalog-items.md#catalogitemchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder = { field: ORDER, direction: ASC }` | The ordering options for the returned children. |

</details>

---

### userCatalogItemDelete

Deletes a user catalog item.

```graphql
userCatalogItemDelete("The input fields for deleting the item." input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../../catalogs/catalog-items.md#catalogitemdeleteinput)! | The input fields for deleting the item. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
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

### UserCatalogItem

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [HierarchicalCatalogItem](../../catalogs.md#hierarchicalcatalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `parent` | [UserCatalogItem](../users.md#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `filter` | [CatalogItemChildrenFilter](../../catalogs/catalog-items.md#catalogitemchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder = { field: ORDER, direction: ASC }` | The ordering options for the returned children. |

---

### User

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
| `filter` | [MemberFilter](../../organizations/members.md#memberfilter) | Filtering options for the returned memberships. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned memberships. |

---

### UserPayload

The result of a user profile mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `user` | [User](../users.md#user)! | The updated user. |

---

### UserCatalogItemPayload

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](../users.md#usercatalogitem)! | The created or updated user catalog item. |

---

## Inputs

### MyProfileUpdateInput

Input for updating the current user's profile.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput](../users.md#personnameinput)! | The structured name components. |

---

### PersonNameInput

Input for structured person name components.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s). |
| `familyNames` | `String!` | The family name(s). |
| `middleName` | `String` | The middle name or patronymic. |

---

### UserCatalogItemCreateInput

Input for creating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | `Code!` | The machine-readable code, unique within the catalog and organization. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### UserCatalogItemUpdateInput

Input for updating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Pagination types

### UserCatalogItemConnection

A paginated list of UserCatalogItem items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserCatalogItemEdge](../users.md#usercatalogitemedge)!]! | A list of edges. |
| `nodes` | [[UserCatalogItem](../users.md#usercatalogitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### UserCatalogItemEdge

An edge in the UserCatalogItem connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [UserCatalogItem](../users.md#usercatalogitem)! | The user catalog item at the end of the edge. |

---

### UserConnection

A paginated list of User items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserEdge](../users.md#useredge)!]! | A list of edges. |
| `nodes` | [[User](../users.md#user)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### UserEdge

An edge in the User connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [User](../users.md#user)! | The user at the end of the edge. |

---
