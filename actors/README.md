# Actors

Actors represent entities that can perform actions in the system. This includes users (human operators) and integrations (API clients and automated systems).

## Objects

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

---

### SystemActor

The built-in system actor used for automated operations.

**Implements:** [Actor](../actors.md#actor), [Node](../common.md#node), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `title` | `String!` | The display name of the actor. |

---

## Interfaces

### Actor

An entity that can perform actions and have permissions assigned.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `title` | `String!` | The display name of the actor. |

---
