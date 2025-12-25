# Queries

Queries retrieve data from the Navixy platform without modifying it.

## General

### node

Fetch any entity by ID using Node interface. Returns null if not found or no permission.

```graphql
node(id: UUID!): Node
```

**Arguments**
[Test Link](objects#devicevendor)

| Name | Type                | Description |
| ---- | ------------------- | ----------- |
| `id` | [UUID!](types#uuid) |             |

**Returns:** [Node](types#node)

### me

Returns currently authenticated user

```graphql
me: User!
```

**Returns:** [User!](../objects#user/)

## Devices

### deviceVendor

Fetch device vendor by ID. Returns null if not found.

```graphql
deviceVendor(id: UUID!): DeviceVendor
```

**Arguments**

| Name | Type                   | Description |
| ---- | ---------------------- | ----------- |
| `id` | [UUID!](../types#uuid) |             |

**Returns:** [DeviceVendor](/api-reference/objects#devicevendor)

### deviceVendors

List all device vendors

```graphql
deviceVendors: [DeviceVendor!]!
```

**Returns:** [[DeviceVendor!]!](../api-reference/objects#devicevendor)

### deviceModel

Fetch device model by ID. Returns null if not found.

```graphql
deviceModel(id: UUID!): DeviceModel
```

**Arguments**

| Name | Type                  | Description |
| ---- | --------------------- | ----------- |
| `id` | [UUID!](./types#uuid) |             |

**Returns:** [DeviceModel](./api-reference/objects#devicemodel)
