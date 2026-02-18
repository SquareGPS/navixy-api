# Directives

Directives modify the behavior of fields, types, or operations in a GraphQL schema. They are prefixed with `@` and can be applied at various locations.

## Standard directives

These directives are part of the GraphQL specification and available in all queries.

### @skip

Conditionally excludes a field or fragment from the response.

| Argument | Type | Description |
| -------- | ---- | ----------- |
| `if` | `Boolean!` | When `true`, the field is excluded from the response. |

**Locations:** `FIELD`, `FRAGMENT_SPREAD`, `INLINE_FRAGMENT`

**Example:**
```graphql
query GetDevice($skipCustomFields: Boolean!) {
  device(id: "123") {
    title
    customFields @skip(if: $skipCustomFields)
  }
}
```

### @include

Conditionally includes a field or fragment in the response.

| Argument | Type | Description |
| -------- | ---- | ----------- |
| `if` | `Boolean!` | When `true`, the field is included in the response. |

**Locations:** `FIELD`, `FRAGMENT_SPREAD`, `INLINE_FRAGMENT`

**Example:**
```graphql
query GetDevice($includeRelations: Boolean!) {
  device(id: "123") {
    title
    relations @include(if: $includeRelations) {
      edges { node { id } }
    }
  }
}
```

### @deprecated

Marks a field or enum value as deprecated, signaling that it should no longer be used.

| Argument | Type | Description |
| -------- | ---- | ----------- |
| `reason` | `String` | Explanation of why it's deprecated and what to use instead. |

**Locations:** `FIELD_DEFINITION`, `ARGUMENT_DEFINITION`, `INPUT_FIELD_DEFINITION`, `ENUM_VALUE`

**Example:**
```graphql
type Device {
  legacyId: String @deprecated(reason: "Use `id` instead.")
  id: ID!
}
```

### @specifiedBy

Provides a URL to a specification that defines the behavior of a custom scalar.

| Argument | Type | Description |
| -------- | ---- | ----------- |
| `url` | `String!` | URL to the scalar specification document. |

**Locations:** `SCALAR`

**Example:**
```graphql
scalar DateTime @specifiedBy(url: "https://scalars.graphql.org/chillicream/date-time.html")
```

### @oneOf

Indicates that an input object requires exactly one of its fields to be provided. This is useful for creating union-like input types.

**Locations:** `INPUT_OBJECT`

**Example:**
```graphql
input FieldParamsInput @oneOf {
  string: StringFieldParamsInput
  text: TextFieldParamsInput
  number: NumberFieldParamsInput
}
```

## Custom directives

These directives are specific to the Navixy Repository API.

### @trim

Automatically trims leading and trailing whitespace from string input values.

**Locations:** `INPUT_FIELD_DEFINITION`, `ARGUMENT_DEFINITION`
