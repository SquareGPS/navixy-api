# Geo objects — Mutations

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
| `input` | `GeoObjectCreateInput!` | The input fields for creating the geo object. |

**Input types:**

<details>

<summary>GeoObjectCreateInput</summary>

Input for creating a new geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the geo object. |
| `typeId` | `ID!` | The geo object type ID. |
| `title` | `String!` | The geo object display name. |
| `geometry` | `GeoJSON!` | The GeoJSON geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

</details>

<details>

<summary>CustomFieldsPatchInput</summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary>GeoObjectPayload</summary>

The result of a geo object mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](types.md#geoobject)! | The created or updated geo object. |

</details>

<details>

<summary>GeoObject (entity)</summary>

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](types.md#geoobjecttype)! | The geo object type classification. |
| `geometry` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry. This is an alias for the `geojson` custom field. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |
| `containsPoints` | [[PointContainmentResult](types.md#pointcontainmentresult)!]! | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

</details>

---

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
| `input` | `GeoObjectUpdateInput!` | The input fields for updating the geo object. |

**Input types:**

<details>

<summary>GeoObjectUpdateInput</summary>

Input for updating an existing geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `geometry` | `GeoJSON` | The new geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

</details>

<details>

<summary>CustomFieldsPatchInput</summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary>GeoObjectPayload</summary>

The result of a geo object mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](types.md#geoobject)! | The created or updated geo object. |

</details>

<details>

<summary>GeoObject (entity)</summary>

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](types.md#geoobjecttype)! | The geo object type classification. |
| `geometry` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry. This is an alias for the `geojson` custom field. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |
| `containsPoints` | [[PointContainmentResult](types.md#pointcontainmentresult)!]! | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

</details>

---

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
| `input` | `GeoObjectDeleteInput!` | The input fields for deleting the geo object. |

**Input types:**

<details>

<summary>GeoObjectDeleteInput</summary>

Input for deleting a geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

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
| `input` | `GeoObjectTypeCreateInput!` | The input fields for creating the geo object type. |

**Input types:**

<details>

<summary>GeoObjectTypeCreateInput</summary>

Input for creating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>GeoObjectTypePayload</summary>

The result of a geo object type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](types.md#geoobjecttype)! | The created or updated geo object type. |

</details>

<details>

<summary>GeoObjectType (entity)</summary>

A classification type for geographic objects.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

</details>

---

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
| `input` | `GeoObjectTypeUpdateInput!` | The input fields for updating the geo object type. |

**Input types:**

<details>

<summary>GeoObjectTypeUpdateInput</summary>

Input for updating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>GeoObjectTypePayload</summary>

The result of a geo object type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](types.md#geoobjecttype)! | The created or updated geo object type. |

</details>

<details>

<summary>GeoObjectType (entity)</summary>

A classification type for geographic objects.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

</details>

---

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
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the geo object type. |

**Input types:**

<details>

<summary>CatalogItemDeleteInput</summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

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
