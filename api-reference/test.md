# test

Queries retrieve data from the Navixy platform without modifying it.

## General

### node

Fetch any entity by ID using Node interface. Returns null if not found or no permission.

```graphql
node(id: UUID!): Node
```

**Arguments** [Test Link](objects.md#devicevendor/)

| Name | Type                              | Description |
| ---- | --------------------------------- | ----------- |
| `id` | [UUID!](objects.md#devicevendor/) |             |

**Returns:** [Node](../guides/api-reference/objects.md#devicevendor/)

### me

Returns currently authenticated user

```graphql
me: User!
```

**Returns:** [User!](../guides/objects/#user/)

## Devices

### deviceVendor

Fetch device vendor by ID. Returns null if not found.

```graphql
deviceVendor(id: UUID!): DeviceVendor
```

**Arguments**

| Name | Type                            | Description |
| ---- | ------------------------------- | ----------- |
| `id` | [UUID!](objects/#devicevendor/) |             |

**Returns:** [DeviceVendor](objects/#devicevendor)

### deviceVendors

List all device vendors

```graphql
deviceVendors: [DeviceVendor!]!
```

**Returns:** [\[DeviceVendor!\]!](objects/#devicevendor)

### deviceModel

Fetch device model by ID. Returns null if not found.

```graphql
deviceModel(id: UUID!): DeviceModel
```

**Arguments**

| Name | Type                           | Description |
| ---- | ------------------------------ | ----------- |
| `id` | [UUID!](../guides/types/#uuid) |             |

**Returns:** [DeviceModel](../guides/api-reference/objects/#devicemodel)
