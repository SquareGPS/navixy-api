# Geo Objects — Mutations

### geoObjectCreate

Creates a new geo object.

```graphql
geoObjectCreate(
  input: GeoObjectCreateInput!
): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectCreateInput](./types.md#geoobjectcreateinput)! | The input fields for creating the geo object. |

**Input types:**

<details>

<summary><code>GeoObjectCreateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the geo object. |
| `typeId` | `ID!` | The geo object type ID. |
| `title` | `String!` | The geo object display name. |
| `geometry` | [GeoJSON](./types.md#geojson)! | The [GeoJSON](https://geojson.org/) geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | [JSON](../common.md#json) | Fields to set or update as a key-value map. |
| `unset` | [[Code](../common.md#code)!] | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>GeoObjectPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](./types.md#geoobject)! | The created or updated geo object. |

</details>

<details>

<summary><code>GeoObject (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)! | The geo object type classification. |
| `geometry` | [GeoJSON](./types.md#geojson)! |  |
| `customFields` | [JSON](../common.md#json)! |  |
| `containsPoints` | [[PointContainmentResult](./types.md#pointcontainmentresult)!]! |  |

</details>

### geoObjectUpdate

Updates an existing geo object.

```graphql
geoObjectUpdate(
  input: GeoObjectUpdateInput!
): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectUpdateInput](./types.md#geoobjectupdateinput)! | The input fields for updating the geo object. |

**Input types:**

<details>

<summary><code>GeoObjectUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `geometry` | [GeoJSON](./types.md#geojson) | The new geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | [JSON](../common.md#json) | Fields to set or update as a key-value map. |
| `unset` | [[Code](../common.md#code)!] | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>GeoObjectPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](./types.md#geoobject)! | The created or updated geo object. |

</details>

<details>

<summary><code>GeoObject (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)! | The geo object type classification. |
| `geometry` | [GeoJSON](./types.md#geojson)! |  |
| `customFields` | [JSON](../common.md#json)! |  |
| `containsPoints` | [[PointContainmentResult](./types.md#pointcontainmentresult)!]! |  |

</details>

### geoObjectDelete

Deletes a geo object.

```graphql
geoObjectDelete(
  input: GeoObjectDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectDeleteInput](./types.md#geoobjectdeleteinput)! | The input fields for deleting the geo object. |

**Input types:**

<details>

<summary><code>GeoObjectDeleteInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### geoObjectTypeCreate

Creates a new geo object type.

```graphql
geoObjectTypeCreate(
  input: GeoObjectTypeCreateInput!
): GeoObjectTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectTypeCreateInput](../catalogs/entity-types/types.md#geoobjecttypecreateinput)! | The input fields for creating the geo object type. |

**Input types:**

<details>

<summary><code>GeoObjectTypeCreateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code](../common.md#code)! | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>GeoObjectTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)! | The created or updated geo object type. |

</details>

<details>

<summary><code>GeoObjectType (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

</details>

### geoObjectTypeUpdate

Updates a geo object type.

```graphql
geoObjectTypeUpdate(
  input: GeoObjectTypeUpdateInput!
): GeoObjectTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectTypeUpdateInput](../catalogs/entity-types/types.md#geoobjecttypeupdateinput)! | The input fields for updating the geo object type. |

**Input types:**

<details>

<summary><code>GeoObjectTypeUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>GeoObjectTypePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)! | The created or updated geo object type. |

</details>

<details>

<summary><code>GeoObjectType (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

</details>

### geoObjectTypeDelete

Deletes a geo object type.

```graphql
geoObjectTypeDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../catalogs/README.md#catalogitemdeleteinput)! | The input fields for deleting the geo object type. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>
