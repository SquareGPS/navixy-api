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

<summary>Actor</summary>

An entity that can perform actions and have permissions assigned.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled)

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
myProfileUpdate(input: MyProfileUpdateInput!): UserPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MyProfileUpdateInput!` | The input fields for updating the profile. |

**Input types:**

<details>

<summary>MyProfileUpdateInput</summary>

Input for updating the current user's profile.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput](#personnameinput)! | The structured name components. |

</details>

<details>

<summary>PersonNameInput</summary>

Input for structured person name components.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s). |
| `familyNames` | `String!` | The family name(s). |
| `middleName` | `String` | The middle name or patronymic. |

</details>

**Output types:**

<details>

<summary>UserPayload</summary>

The result of a user profile mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `user` | [User](#user)! | The updated user. |

</details>

<details>

<summary>User (entity)</summary>

A human user account authenticated via an identity provider.

**Implements:** [Actor](README.md#actor), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](README.md#personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | `EmailAddress!` | The user's primary email address. |
| `locale` | `Locale` | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `memberships` | [MemberConnection](../organizations/members.md#memberconnection)! | The organization memberships for this user. |

</details>

---

### userCatalogItemCreate

Creates a new user catalog item.

```graphql
userCatalogItemCreate(input: UserCatalogItemCreateInput!): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserCatalogItemCreateInput!` | The input fields for creating the item. |

**Input types:**

<details>

<summary>UserCatalogItemCreateInput</summary>

Input for creating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | `Code!` | The machine-readable code, unique within the catalog and organization. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

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

<summary>UserCatalogItemPayload</summary>

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](#usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary>UserCatalogItem (entity)</summary>

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [HierarchicalCatalogItem](../catalogs/README.md#hierarchicalcatalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `parent` | [UserCatalogItem](#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](#usercatalogitemconnection)! | The child items in the hierarchy. |

</details>

---

### userCatalogItemUpdate

Updates a user catalog item.

```graphql
userCatalogItemUpdate(input: UserCatalogItemUpdateInput!): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserCatalogItemUpdateInput!` | The input fields for updating the item. |

**Input types:**

<details>

<summary>UserCatalogItemUpdateInput</summary>

Input for updating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

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

<summary>UserCatalogItemPayload</summary>

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](#usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary>UserCatalogItem (entity)</summary>

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [HierarchicalCatalogItem](../catalogs/README.md#hierarchicalcatalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `parent` | [UserCatalogItem](#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](#usercatalogitemconnection)! | The child items in the hierarchy. |

</details>

---

### userCatalogItemDelete

Deletes a user catalog item.

```graphql
userCatalogItemDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the item. |

**Input types:**

<details>

<summary>CatalogItemDeleteInput</summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
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

### UserCatalogItem

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [HierarchicalCatalogItem](../catalogs/README.md#hierarchicalcatalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `parent` | [UserCatalogItem](#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](#usercatalogitemconnection)! | The child items in the hierarchy. |

---

### User

A human user account authenticated via an identity provider.

**Implements:** [Actor](README.md#actor), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](README.md#personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | `EmailAddress!` | The user's primary email address. |
| `locale` | `Locale` | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `memberships` | [MemberConnection](../organizations/members.md#memberconnection)! | The organization memberships for this user. |

---

### UserPayload

The result of a user profile mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `user` | [User](#user)! | The updated user. |

---

### UserCatalogItemPayload

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](#usercatalogitem)! | The created or updated user catalog item. |

---

## Inputs

### MyProfileUpdateInput

Input for updating the current user's profile.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput](#personnameinput)! | The structured name components. |

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
| `order` | `Int` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

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
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Pagination types

### UserCatalogItemConnection

A paginated list of UserCatalogItem items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserCatalogItemEdge](#usercatalogitemedge)!]! | A list of edges. |
| `nodes` | [[UserCatalogItem](#usercatalogitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### UserCatalogItemEdge

An edge in the UserCatalogItem connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [UserCatalogItem](#usercatalogitem)! | The user catalog item at the end of the edge. |

---

### UserConnection

A paginated list of User items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserEdge](#useredge)!]! | A list of edges. |
| `nodes` | [[User](#user)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### UserEdge

An edge in the User connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [User](#user)! | The user at the end of the edge. |

---
