# API reference

Navixy Repository API is a powerful asset management system that enables you to create fully customized trackable assets with any properties you need, assign GPS devices to make them location-aware, and establish relationships between assets to model your exact business operations.

### Overview

This document is a reference sheet for Navixy Repository API. It briefly outlines authentication, server URLs, and endpoint names, methods, and parameters. For a detailed description of endpoints, grouped by resource, see their dedicated pages nested inside this article.

### Authentication

All API requests require OAuth 2.0 Bearer authentication. Include your access token in the Authorization header:

```
Authorization: Bearer <ACCESS_TOKEN>
```

For a detailed authentication flow, see [Authentication](../authentication.md).

### Single endpoint

```
https://api.navixy.com/v4/graphql
```

### Introspection and schema

You can perform introspection against the GraphQL API directly or download the latest version of the public schema (_**add link**_).

Full introspection query (returns all API types and operations):

```graphql
query {
  __schema {
    queryType { name }
    mutationType { name }
    subscriptionType { name }
    types {
      name
      kind
      description
      fields {
        name
        description
        type {
          name
        }
      }
    }
  }
}
```

### Type syntax

The API reference uses special notation to indicate whether fields are required and whether they return single values or lists.

#### **Required vs nullable**

The `!` symbol means a value is required (non-null):

| Syntax    | Meaning                              |
| --------- | ------------------------------------ |
| `String`  | May be null                          |
| `String!` | Never null — always returns a string |

For arguments, `!` means you must provide a value:

```graphql
# id is required (UUID!), you must provide it
device(id: "...")

# title is optional (String without !), you can omit it
devices(filter: { title: "Truck" })
```

#### **Arrays**

Square brackets `[]` indicate a list of values:

| Syntax       | Meaning                                        |
| ------------ | ---------------------------------------------- |
| `[String]`   | A list of strings (list and items may be null) |
| `[String!]`  | A list of non-null strings (list may be null)  |
| `[String]!`  | A non-null list of strings (items may be null) |
| `[String!]!` | A non-null list of non-null strings            |

The most common pattern is `[Type!]!` — a guaranteed list where every item exists:

```graphql
# edges is [DeviceEdge!]! — always returns a list, every item is a valid edge
devices(pagination: { first: 10 }) {
  edges {        # Never null, never contains null items
    node {
      title
    }
  }
}
```

#### **Reading complex types**

When you see a type like `[DeviceEdge!]!` in the API reference:

1. Start from the inside: `DeviceEdge` — this is an object type
2. Add `!`: `DeviceEdge!` — each item is never null
3. Add `[]`: `[DeviceEdge!]` — it's a list
4. Add outer `!`: `[DeviceEdge!]!` — the list itself is never null

So `[DeviceEdge!]!` means "you'll always get a list, and every item in that list will be a valid DeviceEdge object."

### GraphQL operations

TBD

### GraphQL types

TBD
