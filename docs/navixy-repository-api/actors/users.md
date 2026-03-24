# Users

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

User accounts representing human operators who access the system through the UI or API.

## Mutations

### myProfileUpdate

Updates the current user's profile (name only).

```graphql
myProfileUpdate(
    input: MyProfileUpdateInput!
  ): UserPayload
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
| `name` | [PersonNameInput](#type-personnameinput)! | The structured name components. |

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
| `user` | [User](#type-user)! | The updated user. |

</details>

<details>

<summary>User (entity)</summary>

A human user account authenticated via an identity provider.

**Implements:** [Actor](README.md#type-actor), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](README.md#type-personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | `EmailAddress!` | The user's primary email address. |
| `locale` | `Locale` | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `memberships` | [MemberConnection](../organizations/members.md#type-memberconnection)! | The organization memberships for this user. |

</details>

---

### userCatalogItemCreate

Creates a new user catalog item.

```graphql
userCatalogItemCreate(
    input: UserCatalogItemCreateInput!
  ): UserCatalogItemPayload
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
| `code` | `Code` | The machine-readable code, unique within the catalog and organization. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

**Output types:**

<details>

<summary>UserCatalogItemPayload</summary>

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](#type-usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary>UserCatalogItem (entity)</summary>

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [HierarchicalCatalogItem](../catalogs/catalog-items.md#type-hierarchicalcatalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `parent` | [UserCatalogItem](#type-usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](#type-usercatalogitemconnection)! | The child items in the hierarchy. |

</details>

---

### userCatalogItemUpdate

Updates a user catalog item.

```graphql
userCatalogItemUpdate(
    input: UserCatalogItemUpdateInput!
  ): UserCatalogItemPayload
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
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

**Output types:**

<details>

<summary>UserCatalogItemPayload</summary>

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](#type-usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary>UserCatalogItem (entity)</summary>

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [HierarchicalCatalogItem](../catalogs/catalog-items.md#type-hierarchicalcatalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `parent` | [UserCatalogItem](#type-usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](#type-usercatalogitemconnection)! | The child items in the hierarchy. |

</details>

---

### userCatalogItemDelete

Deletes a user catalog item.

```graphql
userCatalogItemDelete(
    input: CatalogItemDeleteInput!
  ): DeletePayload
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

<a id="type-usercatalogitem"></a>

### UserCatalogItem

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [HierarchicalCatalogItem](../catalogs/catalog-items.md#type-hierarchicalcatalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `parent` | [UserCatalogItem](#type-usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](#type-usercatalogitemconnection)! | The child items in the hierarchy. |

---

<a id="type-user"></a>

### User

A human user account authenticated via an identity provider.

**Implements:** [Actor](README.md#type-actor), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](README.md#type-personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | `EmailAddress!` | The user's primary email address. |
| `locale` | `Locale` | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `memberships` | [MemberConnection](../organizations/members.md#type-memberconnection)! | The organization memberships for this user. |

---

<a id="type-userpayload"></a>

### UserPayload

The result of a user profile mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `user` | [User](#type-user)! | The updated user. |

---

<a id="type-usercatalogitempayload"></a>

### UserCatalogItemPayload

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](#type-usercatalogitem)! | The created or updated user catalog item. |

---

## Inputs

<a id="type-myprofileupdateinput"></a>

### MyProfileUpdateInput

Input for updating the current user's profile.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput](#type-personnameinput)! | The structured name components. |

---

<a id="type-personnameinput"></a>

### PersonNameInput

Input for structured person name components.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s). |
| `familyNames` | `String!` | The family name(s). |
| `middleName` | `String` | The middle name or patronymic. |

---

<a id="type-usercatalogitemcreateinput"></a>

### UserCatalogItemCreateInput

Input for creating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | `Code` | The machine-readable code, unique within the catalog and organization. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

<a id="type-usercatalogitemupdateinput"></a>

### UserCatalogItemUpdateInput

Input for updating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

## Pagination types

<a id="type-usercatalogitemconnection"></a>

### UserCatalogItemConnection

A paginated list of UserCatalogItem items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserCatalogItemEdge](#type-usercatalogitemedge)!]! | A list of edges. |
| `nodes` | [[UserCatalogItem](#type-usercatalogitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-usercatalogitemedge"></a>

### UserCatalogItemEdge

An edge in the UserCatalogItem connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [UserCatalogItem](#type-usercatalogitem)! | The user catalog item at the end of the edge. |

---

<a id="type-userconnection"></a>

### UserConnection

A paginated list of User items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserEdge](#type-useredge)!]! | A list of edges. |
| `nodes` | [[User](#type-user)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-useredge"></a>

### UserEdge

An edge in the User connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [User](#type-user)! | The user at the end of the edge. |

---
