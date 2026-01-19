# GraphQL basics

This article introduces GraphQL for developers who are new to it. If you've worked with REST APIs before, you'll find GraphQL takes a different approach to requesting and modifying data.

For detailed information, see [the official GraphQL documentation](https://graphql.org/learn/) and [GraphQL specification](https://spec.graphql.org/).

{% include ".gitbook/includes/try-it-out-yourself.-use-ou....md" %}

### What is GraphQL?

GraphQL is a query language for APIs. The key idea behind it is that **you specify exactly what data you need, and the API returns only that data**. This is different from REST APIs, where each endpoint returns a fixed structure, and you often get more data than you need (or have to make multiple requests to get everything you need).

### How GraphQL differs from REST

If you've used REST APIs, you're familiar with this pattern:

* Different endpoints for different resources (`/devices`, `/devices/123`, `/assets`)
* HTTP methods determine the action (GET to read, POST to create, PUT to update, DELETE to remove)
* Each endpoint returns a predefined data structure

GraphQL works differently:

| Aspect             | REST                                       | GraphQL                                     |
| ------------------ | ------------------------------------------ | ------------------------------------------- |
| Endpoints          | Multiple (`/devices`, `/assets`, `/users`) | Single (`/graphql`)                         |
| Data returned      | Fixed structure per endpoint               | You specify exactly what fields you want    |
| Multiple resources | Multiple requests needed                   | One request can fetch related data          |
| HTTP methods       | GET, POST, PUT, DELETE                     | Always POST (with query or mutation inside) |

#### Sample request

Imagine you need to display a device's title, its status name, and the organization it belongs to.

With REST, you might need multiple requests:

```bash
GET /devices/123     # returns device data including status_id and organization_id

GET /statuses/456    # returns status data

GET /organizations/789    # returns organization data
```

With GraphQL, you make one request and specify exactly what you need:

```graphql
query {
  device(id: "123") {
    title
    status {
      title
    }
    organization {
      title
    }
  }
}
```

The response contains only what you asked for:

```json
{
  "data": {
    "device": {
      "title": "Truck 42",
      "status": {
        "title": "Active"
      },
      "organization": {
        "title": "Berlin Fleet"
      }
    }
  }
}
```

### Single endpoint

Navixy Repository API has one endpoint:

```
https://api.navixy.com/v4/graphql
```

Every request — reading data, creating something, or subscribing to updates — goes to this same URL. The request body tells the API what you want to do.

### Operations

GraphQL supports three types of operations:

| Operation    | Purpose                        | Similar to REST      |
| ------------ | ------------------------------ | -------------------- |
| Query        | Read data                      | GET                  |
| Mutation     | Create, update, or delete data | POST, PUT, DELETE    |
| Subscription | Receive real-time updates      | WebSocket connection |

#### Queries

A **query** retrieves data without changing anything. It's the GraphQL equivalent of a REST GET request.

Here's a simple query that fetches a device:

```graphql
query {
  device(id: "550e8400-e29b-41d4-a716-446655440001") {
    id
    title
  }
}
```

Let's break this down:

* `query` tells GraphQL you want to read data
* `device` is the name of the query (what you're fetching)
* `(id: "550e8400-...")` is an argument that specifies which device
* `{ id title }` lists the fields you want returned

The response mirrors your query structure:

```json
{
  "data": {
    "device": {
      "id": "550e8400-e29b-41d4-a716-446655440001",
      "title": "Truck 42"
    }
  }
}
```

Notice that the response contains only `id` and `title` — exactly what you requested. If you also need the device's status, add it to your query:

```graphql
query {
  device(id: "550e8400-e29b-41d4-a716-446655440001") {
    id
    title
    status {
      code
      title
    }
  }
}
```

The `status` field returns an object, so you specify which fields of that object you want (`code` and `title`).

#### Mutations

A **mutation** modifies data, creating, updating, or deleting something. It combines what REST does with POST, PUT, and DELETE into one operation type.

Here's a mutation that updates a device's title:

```graphql
mutation {
  deviceUpdate(input: {
    id: "550e8400-e29b-41d4-a716-446655440001"
    version: 5
    title: "Truck 42 - Berlin"
  }) {
    device {
      id
      version
      title
    }
  }
}
```

Let's break this down:

* `mutation` tells GraphQL you want to change data
* `deviceUpdate` is the name of the mutation
* `input: { ... }` provides the data for the update, including the current `version` for optimistic locking
* `{ device { ... } }` specifies what to return after the update

The response shows the updated data:

```json
{
  "data": {
    "deviceUpdate": {
      "device": {
        "id": "550e8400-e29b-41d4-a716-446655440001",
        "version": 6,
        "title": "Truck 42 - Berlin"
      }
    }
  }
}
```

This is useful because you can confirm the change and get the new version number without making a separate query.

Here's a mutation that creates a new asset:

```graphql
mutation {
  createAsset(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Delivery Van 7"
  }) {
    id
    title
    createdAt
  }
}
```

#### Subscriptions

A **subscription** opens a persistent connection to receive updates as they happen. Instead of polling the API repeatedly, you tell it what events you're interested in, and it pushes data to you.

At the moment, Navixy Repository API doesn't support subscriptions.

### Fields

Fields are the pieces of data you can request from an object. When you write a query, you're selecting which fields to include in the response.

Every object type in the API has a defined set of fields. For example, a `Device` has fields like:

* `id` — the unique identifier
* `title` — the display name
* `status` — the current status (which is itself an object with its own fields)
* `organization` — the organization that owns it
* `customFields` — custom data specific to your setup

You only get the fields you ask for. If you don't need `customFields`, don't include it in your query, and it won't be in the response.

#### Nested fields

Some fields return objects rather than simple values. When a field returns an object, you must specify which fields of that object you want.

```graphql
query {
  device(id: "550e8400-e29b-41d4-a716-446655440001") {
    title
    status {
      code
      title
    }
    organization {
      title
      features
    }
  }
}
```

Here, `status` and `organization` are objects, so we specify their fields inside curly braces. The `title` and `code` fields return simple values (strings), so they don't need nested fields. The `features` field returns an array of enum values.

### Arguments

Arguments allow you to filter or configure what data a query returns. You pass them in parentheses after the field name.

The `device` query requires an `id` argument to know which device to fetch:

```graphql
query {
  device(id: "550e8400-e29b-41d4-a716-446655440001") {
    title
  }
}
```

The `devices` query (plural) can take optional arguments to filter results:

```graphql
query {
  devices(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      statusIds: ["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]
    }
    first: 10
  ) {
    nodes {
      id
      title
    }
  }
}
```

This requests the first 10 devices from a specific organization with a specific status. The `organizationId` is a required argument, and `filter` allows additional criteria like filtering by multiple status IDs.

### Types

Every field in GraphQL has a type that defines what kind of data it holds. It can be predefined, like string or boolean, or API-specific, like `DeviceIdType`. Understanding types helps you read the API reference and write correct queries.

#### Scalar types

Scalars are primitive values — basic building blocks. When calling a GraphQL API, you must specify nested subfields until you return only scalars.

GraphQL has the following built-in scalar types:

| Type      | Description                              | Example                                  |
| --------- | ---------------------------------------- | ---------------------------------------- |
| `String`  | Text                                     | `"Truck 42"`                             |
| `Int`     | Whole number                             | `42`                                     |
| `Float`   | Decimal number                           | `3.14`                                   |
| `Boolean` | True or false                            | `true`                                   |
| `ID`      | Unique identifier (serialized as string) | `"550e8400-e29b-41d4-a716-446655440001"` |

Navixy Repository API adds these custom scalar types:

| Type           | Description                                                           | Example                           |
| -------------- | --------------------------------------------------------------------- | --------------------------------- |
| `DateTime`     | Date and time with timezone (ISO 8601)                                | `"2025-01-15T14:30:00.000Z"`      |
| `Date`         | Date without time (ISO 8601)                                          | `"2025-01-15"`                    |
| `JSON`         | Arbitrary JSON data                                                   | `{"color": "red", "priority": 1}` |
| `Code`         | Machine-readable identifier (lowercase alphanumeric with underscores) | `"truck"`, `"device_type"`        |
| `HexColorCode` | Color in hexadecimal format                                           | `"#FF5733"`                       |

#### Object types

Object types represent the things you can fetch from the API: devices, organizations, assets, users, and so on. Each object type defines a set of fields you can request.

Here's what the `Device` type looks like in the schema:

```graphql
type Device {
  id: ID!
  version: Int!
  title: String!
  status: DeviceStatus!
  organization: Organization!
  customFields: JSON!
  # ... more fields
}
```

This tells you:

* `Device` is an object type
* It has fields like `id`, `version`, `title`, `status`, etc.
* Each field has its own type (`ID!`, `Int!`, `String!`, `DeviceStatus!`)

Some fields return scalar types (`id` returns `ID!`), while others return other object types (`status` returns `DeviceStatus!`). When a field returns an object type, you must specify which of its fields you want:

```graphql
query {
  device(id: "...") {
    title              # String — scalar, no nested fields needed
    status {           # DeviceStatus — object type
      code             # String
      title            # String
    }
  }
}
```

In the API reference, you'll see object types like `Device`, `Organization`, `DeviceStatus`, and many others.

#### Enums

Enums are fixed sets of values. Unlike strings, you can only use the predefined values.

For example, `ActionPermission` is an enum with these values:

* `READ`
* `CREATE`
* `UPDATE`
* `DELETE`

When using an enum in a query, write the value without quotes:

```graphql
mutation {
  grantPermission(input: {
    roleId: "..."
    permissionScopeId: "..."
    actions: [READ, UPDATE]    # Enum values, no quotes
  }) {
    id
  }
}
```

#### Input types

Input types are used for mutation arguments. They look similar to object types but can only be used as inputs, not outputs.

In the API reference, you'll see input types like `CreateDeviceInput`, `UpdateAssetInput`, and `DeviceFilter`. They define what fields you can (or must) provide:

```graphql
mutation {
  createAsset(input: {           # CreateAssetInput
    organizationId: "..."        # Required
    typeId: "..."                # Required
    title: "Delivery Van"        # Required
    customFields: { "vin": "..." }  # Optional
  }) {
    id
  }
}
```

#### Interfaces

Interfaces define a set of fields shared by multiple types. If a type implements an interface, it guarantees those fields exist.

For example, the `Node` interface requires the `id` field. Many types implement it: `Device`, `Asset`, `Organization`, and others. This means you can always request `id` from any of these types.

The `Versioned` interface provides the `version` field used for optimistic locking. Types implementing it will always have this field available for concurrency control.

### Type syntax

The API reference uses special notation to indicate whether fields are required and whether they return single values or lists.

**Required vs nullable**

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

#### Arrays

Square brackets `[]` indicate a list of values:

<table><thead><tr><th width="100">Syntax</th><th>Meaning</th></tr></thead><tbody><tr><td><code>[String]</code></td><td>A list of strings (list and items may be null)</td></tr><tr><td><code>[String!]</code></td><td>A list of non-null strings (list may be null)</td></tr><tr><td><code>[String]!</code></td><td>A non-null list of strings (items may be null)</td></tr><tr><td><code>[String!]!</code></td><td>A non-null list of non-null strings</td></tr></tbody></table>

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

#### Reading complex types

When you see a type like `[DeviceEdge!]!` in the API reference:

1. Start from the inside: `DeviceEdge` — this is an object type
2. Add `!`: `DeviceEdge!` — each item is never null
3. Add `[]`: `[DeviceEdge!]` — it's a list
4. Add outer `!`: `[DeviceEdge!]!` — the list itself is never null

So `[DeviceEdge!]!` means "you'll always get a list, and every item in that list will be a valid DeviceEdge object."

### Understanding responses

GraphQL responses are JSON objects with a consistent structure.

#### Successful responses

A successful response has a `data` field containing your requested data:

```json
{
  "data": {
    "device": {
      "id": "550e8400-e29b-41d4-a716-446655440001",
      "title": "Truck 42"
    }
  }
}
```

The structure inside `data` matches your query structure exactly.

#### Error responses

If something goes wrong, the response includes an `errors` array:

```json
{
  "data": null,
  "errors": [
    {
      "message": "Device not found",
      "extensions": {
        "code": "NOT_FOUND",
        "entityType": "device",
        "entityId": "550e8400-e29b-41d4-a716-446655440001"
      }
    }
  ]
}
```

The `extensions` object contains machine-readable information for handling the error in your code. See Error handling for more information.

### Schema

A GraphQL API has a **schema** that defines all available types, fields, queries, and mutations. The schema is like a contract: it tells you exactly what you can request and what you'll get back.

Navixy Repository API schema _**(add link)**_ is public and available to developers.

### Introspection

GraphQL APIs are self-described. You can explore the schema using tools like our sandbox _**(add link)**_ or by querying the API directly — this is called **introspection**. GraphQL has special built-in fields that start with `__` (double underscore) for this purpose.

For example, to see all fields available on the `Device` type:

```graphql
query {
  __type(name: "Device") {
    name
    fields {
      name
      type { name }
    }
  }
}
```

Learn more about introspection queries in [GraphQL tips and patterns](graphql-basics/graphql-tips-and-patterns.md).

### Next steps

Now that you understand the basics:

* [Check out GraphQL tips and patterns: variables, fragments, aliases, and more](graphql-basics/graphql-tips-and-patterns.md)
* [Learn how to set up authentication and make your first request](getting-started.md)
* [Browse available operations and types](/broken/pages/RhtSpHv4wO3lKb3HNIqI)
