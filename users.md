# Users

User accounts for system access and authentication.

## Queries

### me

Retrieves the currently authenticated actor.

```graphql
me: Actor!
```

**Output types:**

<details>

<summary><code>Actor</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `title` | `String!` | The display name of the actor. |

</details>

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
| `input` | [MyProfileUpdateInput](./users.md#myprofileupdateinput)! | The input fields for updating the profile. |

**Input types:**

<details>

<summary><code>MyProfileUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput](./users.md#personnameinput)! | The structured name components. |

</details>

<details>

<summary><code>PersonNameInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s). |
| `familyNames` | `String!` | The family name(s). |
| `middleName` | `String` | The middle name or patronymic. |

</details>

**Output types:**

<details>

<summary><code>UserPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `user` | [User](./users.md#user)! | The updated user. |

</details>

<details>

<summary><code>User (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](./users.md#personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | [EmailAddress](./common.md#emailaddress)! | The user's primary email address. |
| `locale` | [Locale](./common.md#locale) | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `memberships` | [MemberConnection](./members.md#memberconnection)! | The organization memberships for this user. |

</details>

## Types

### UserConnection

A paginated list of User items.

**Implements:** [`Connection`](./common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserEdge](./users.md#useredge)!]! | A list of edges. |
| `nodes` | [[User](./users.md#user)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](./common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](./common.md#countinfo) | The total count of items matching the filter. |

### UserEdge

An edge in the User connection.

**Implements:** [`Edge`](./common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [User](./users.md#user)! | The user at the end of the edge. |

### PersonName

Structured person name components following W3C Personal Names guidance.
See: https://www.w3.org/International/questions/qa-personal-names

Examples by culture:
- US: givenNames="John", familyNames="Smith", middleName="Robert"
- Russia: givenNames="Иван", familyNames="Иванов", middleName="Петрович" (patronymic)
- Spain: givenNames="Juan Carlos", familyNames="García López" (paternal + maternal)
- China: givenNames="明" (Ming), familyNames="王" (Wang) — note: family name first in native order
- Iceland: givenNames="Björk", familyNames="Guðmundsdóttir" (patronymic as family name)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s), also known as first name(s). May contain multiple names separated by spaces. |
| `familyNames` | `String!` | The family name(s), also known as surname(s) or last name(s). May contain multiple names. |
| `middleName` | `String` | The middle name, patronymic, or additional name component. |
| `fullName` | `String!` | The full name formatted according to the user's locale preferences. |

### SystemActor

The built-in system actor used for automated operations.

**Implements:** [`Actor`](./access-control/types.md#actor), [`Node`](./common.md#node), [`Titled`](./common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `title` | `String!` |  |

### User

A human user account authenticated via an identity provider.

**Implements:** [`Actor`](./access-control/types.md#actor), [`Node`](./common.md#node), [`Versioned`](./common.md#versioned), [`Titled`](./common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` | The display name for the user. This is the user's full name for display purposes. |
| `name` | [PersonName](./users.md#personname)! | The structured name components from the identity provider. |
| `identityProvider` | `String!` | The identity provider name (keycloak, auth0, okta, etc.). |
| `identityProviderId` | `String!` | The user's unique ID in the identity provider. |
| `email` | [EmailAddress](./common.md#emailaddress)! | The user's primary email address. |
| `locale` | [Locale](./common.md#locale) | The user's preferred locale. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this user account is active. |
| `memberships` | [MemberConnection](./members.md#memberconnection)! | The organization memberships for this user. |

### UserPayload

The result of a user profile mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `user` | [User](./users.md#user)! | The updated user. |

## Inputs

### MyProfileUpdateInput

Input for updating the current user's profile.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput](./users.md#personnameinput)! | The structured name components. |

### PersonNameInput

Input for structured person name components.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s). |
| `familyNames` | `String!` | The family name(s). |
| `middleName` | `String` | The middle name or patronymic. |
