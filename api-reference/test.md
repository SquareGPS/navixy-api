# test

Queries retrieve data from the Navixy platform without modifying it.

## General

### node

Fetch any entity by ID using Node interface. Returns null if not found or no permission.

```graphql
node(id: UUID!): Node
```

**Arguments** [Test Link](/broken/pages/87b2de11c9b28a408ba4d23469810d22bffa4482#devicevendor/)

| Name | Type                                                                          | Description |
| ---- | ----------------------------------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/87b2de11c9b28a408ba4d23469810d22bffa4482#devicevendor/) |             |

**Returns:** [Node](/broken/pages/87b2de11c9b28a408ba4d23469810d22bffa4482#devicevendor/)

### me

Returns currently authenticated user

```graphql
me: User!
```

**Returns:** [User!](/broken/pages/85b97473468fdac6e2dd46261330d3b3db6bd8e5#user/)



## Devices

### deviceVendor

Fetch device vendor by ID. Returns null if not found.

```graphql
deviceVendor(id: UUID!): DeviceVendor
```

**Arguments**

| Name | Type                                                                          | Description |
| ---- | ----------------------------------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/6c264ffed958b282523993a66940ff39bc0f7e0d#devicevendor/) |             |

**Returns:** [DeviceVendor](/broken/pages/6c264ffed958b282523993a66940ff39bc0f7e0d#devicevendor)

### deviceVendors

List all device vendors

```graphql
deviceVendors: [DeviceVendor!]!
```

**Returns:** [\[DeviceVendor!\]!](/broken/pages/6c264ffed958b282523993a66940ff39bc0f7e0d#devicevendor)

### deviceModel

Fetch device model by ID. Returns null if not found.

```graphql
deviceModel(id: UUID!): DeviceModel
```

**Arguments**

| Name | Type                                                                 | Description |
| ---- | -------------------------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/477c545e93ca417cba0c4d704eedfe0b8bcb61a0#uuid) |             |

**Returns:** [DeviceModel](/broken/pages/6c264ffed958b282523993a66940ff39bc0f7e0d#devicemodel)
