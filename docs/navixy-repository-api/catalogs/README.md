---
description: >-
  Explains catalogs as Navixy Repository API reference data, including the
  CatalogItem interface, item origins, display metadata, and hierarchical items.
---

# Catalogs

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

Catalogs are the reference data system of Navixy Repository API. They provide structured, reusable lookup values (such as asset types or geo object types) that classify and annotate entities throughout the API. Rather than allowing freeform text, catalogs enforce standardized values, keeping data consistent, supporting filtering and reporting, and enabling localized display names.

&#x20;Catalogs can be system (predefined) and user-created.

## Why use catalogs?

Without a shared reference system, properties like vehicle color, fuel type, or device status end up stored as freeform strings formatted in different ways by different users, in different languages, with inconsistent casing. Filtering for "all red vehicles" becomes unreliable when the value might be `red`, `Red`, or `rouge`. Creating a dedicated entity type for each such property solves the consistency problem, but requires separate backend and frontend work for every new property, making the resulting schema hard to manage.

Catalogs solve both problems at once. All reference data, whether platform-defined or organization-specific, shares a single interface, a single set of queries, and predictable behavior. Adding a new lookup type doesn't require a new API entity: it's a new catalog, handled the same way as every other.

## The CatalogItem interface

Every catalog entry, regardless of its type, implements the [CatalogItem](catalog-items.md#catalogitem) interface. This common structure means you work with catalog items the same way across the entire API.

<table><thead><tr><th width="129.88897705078125">Field</th><th width="166.55560302734375">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td><code>ID!</code></td><td>A globally unique identifier.</td></tr><tr><td><code>version</code></td><td><code>Int!</code></td><td>The version number for <a href="../optimistic-locking.md">optimistic locking</a>.</td></tr><tr><td><code>title</code></td><td><code>String!</code></td><td>The human-readable display name. Can be localized.</td></tr><tr><td><code>code</code></td><td><a href="../common.md#code">Code</a>!</td><td>A machine-readable identifier, unique within the catalog scope.</td></tr><tr><td><code>order</code></td><td><code>Int!</code></td><td>The display order within the same level or category.</td></tr><tr><td><code>catalog</code></td><td><a href="catalog-items.md#catalog-2">Catalog</a>!</td><td>The catalog this item belongs to.</td></tr><tr><td><code>organization</code></td><td><a href="../organizations/#organization-2">Organization</a></td><td>The organization that owns this item. <code>null</code> for system items.</td></tr><tr><td><code>meta</code></td><td><a href="catalog-items.md#catalogitemmeta">CatalogItemMeta</a>!</td><td>Metadata, including origin, display properties, and deletion eligibility.</td></tr></tbody></table>

The `code` field uses the [Code](../common.md#code) scalar, a case-insensitive alphanumeric identifier. System-defined items follow `UPPER_SNAKE_CASE` (e.g., `DEVICE_TYPE`, `ACTIVE`), while user-created items can use format. System item codes are stable across the platform (hardcoded and unchanging), making them safe to use as enum-like constants in business logic. Codes for user-created items are unique within the catalog and organization.

### Catalogs are catalog items

The [Catalog](catalog-items.md#catalog-2) type itself implements `CatalogItem`. A catalog is a named container that groups related items and is associated with a system module (such as `repo`, `fleet_management`, or `iot`). This self-referential design means the API's meta-catalog, "the catalog of catalogs," is itself a catalog item.

### Item origins

The `CatalogItemMeta.origin` field indicates how an item was created and determines whether it can be modified.

<table><thead><tr><th width="249.55560302734375">Origin</th><th>Description</th></tr></thead><tbody><tr><td><code>SYSTEM</code></td><td>Predefined by the platform. Immutable and available to all organizations.</td></tr><tr><td><code>ORGANIZATION</code></td><td>Created by the current organization.</td></tr><tr><td><code>PARENT_ORGANIZATION</code></td><td>Inherited from a parent organization in the dealer hierarchy.</td></tr></tbody></table>

System items cannot be deleted or modified. The `meta.canBeDeleted` field reflects whether a given item is eligible for deletion, returning `false` for system-managed items and for any item referenced by other entities.

Note that origin applies at the **item** level, not the catalog level. Some system catalogs, such as [AssetType](../assets/types.md#assettype), accept organization-created items alongside platform-defined ones. In those cases, the catalog itself has `SYSTEM` origin, while the items your organization adds have `ORGANIZATION` origin.

### **User-created catalogs**

Organizations can also create entirely custom catalogs for domain-specific lookup data that the platform doesn't provide — for example, fuel types, concrete grades, or cargo classifications. Items in a user-created catalog belong exclusively to the organization that created them. Use [catalogCreate](catalog-items.md#catalogcreate) to create a catalog, then [userCatalogItemCreate](../actors/users.md#usercatalogitemcreate) to populate it with items.

### Display properties

All catalog items carry optional display metadata in [CatalogItemMeta](catalog-items.md#catalogitemmeta) that controls how they appear in client UI.

<table><thead><tr><th width="183.22216796875">Field</th><th width="166.4444580078125">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>description</code></td><td><code>String</code></td><td>A description of the item. Can be localized.</td></tr><tr><td><code>hidden</code></td><td><code>Boolean!</code></td><td>Whether the item is hidden from regular UI lists.</td></tr></tbody></table>

### Hierarchical catalog items

Some catalog types support parent-child relationships via the [HierarchicalCatalogItem](catalog-items.md#hierarchicalcatalogitem) interface, which adds a `parent` field pointing to the item's parent in the hierarchy. This allows building tree-structured lookup tables, such as a multi-level classification scheme for assets or devices. The specific type that implements this interface is [UserCatalogItem](../actors/users.md#usercatalogitem), which also exposes a paginated `children` field for traversing the tree downward.

## See also

[Catalog items](catalog-items.md): Core queries and mutations for managing catalogs and their items, including `catalogCreate`, `userCatalogItemCreate`, the `CatalogItem` interface, `CatalogItemMeta`, and shared input/output types.

[Tags](tags.md): Tag management for flexible, cross-entity labeling. Tags extend `CatalogItem` with an optional `entityTypes` constraint that limits which entity types a tag can be applied to.

[System catalogs](system.md): System-defined catalog types that cannot be modified: `Module`, `EntityType`, and `Country`.

[Catalog reference](catalog-reference.md): A cross-reference of the remaining (non-tag and non-system) catalog types organized by their parent entity (devices, assets, geo objects, schedules, and others).
