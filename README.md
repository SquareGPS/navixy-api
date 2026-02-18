# Overview

**Navixy Repository API** is a programming interface for managing the organizational structure and business entities of the Navixy platform. It provides a flexible way to define what you track (assets), what tracks them (devices), where things matter (geographic objects), when things happen (schedules), and who can access what (permissions).

**Navixy Repository is based on GraphQL.** Unlike REST APIs where you call multiple endpoints to gather related data, GraphQL allows you to request the exact fields you need in a single query. You describe the shape of the data you want, and the API returns it in that shape.

For a quick primer on GraphQL concepts, see [GraphQL basics](graphql-basics.md).

## Purpose and capabilities

**Navixy Repository API** enables you to:

* Manage **organizations** in a multi-tenant hierarchy (dealers, sub-organizations)
* Create and configure **asset types** with custom properties (vehicles, equipment, staff)
* Create **assets** and organize them into **groups**
* Register **devices** (GPS trackers, sensors) with hardware identifiers and assign them to **inventories**
* Define **geo objects** (geofences, points of interest, routes) with GeoJSON geometry
* Create **schedules** for work hours, maintenance windows, and time-based rules
* Configure **custom fields** to extend any entity with organization-specific data
* Set up **roles and permissions** to control access at the organization, entity type, or individual record level
* Subscribe to **real-time events** when entities are created, updated, or deleted

## Key concepts

<figure><img src=".gitbook/assets/diagram-logo-final (1).webp" alt=""><figcaption></figcaption></figure>

The API is organized around these core resources:

<table><thead><tr><th width="138.5999755859375">Term</th><th>Definition</th></tr></thead><tbody><tr><td><strong>Organization</strong></td><td>A tenant in the system hierarchy. Organizations own all other resources and can have parent-child relationships.</td></tr><tr><td><strong>Asset</strong></td><td>A business object you're tracking: a vehicle, piece of equipment, employee, or any other entity.</td></tr><tr><td><strong>Asset type</strong></td><td>Defines the structure of property fields and display configuration for assets. Examples: "Boats", "Cargo", "Warehouse Operators". Supports full customization.</td></tr><tr><td><strong>Asset group</strong></td><td>A custom collection of assets organized by business logic (fleets, departments, shifts). Groups have types that can restrict which asset types they contain.</td></tr><tr><td><strong>Device</strong></td><td>Physical tracking hardware (GPS tracker, sensor, beacon). Devices have types, models, statuses, and hardware identifiers (IMEI, serial number).</td></tr><tr><td><strong>Inventory</strong></td><td>A logical grouping of devices for stock management (warehouse, vehicle stock, field inventory). Devices are assigned to inventories before being deployed to assets.</td></tr><tr><td><strong>Geo object</strong></td><td>A location-based entity: geofence, point of interest, or route. Geometry is stored as GeoJSON in the <code>geojson</code> custom field.</td></tr></tbody></table>

## Integration with Navixy ecosystem

**Navixy Repository API** works alongside other APIs, including [Navixy API](https://app.gitbook.com/o/YVLWhgAwCZPoU5vlRsCs/s/6dtcPLayxXVB2qaaiuIL/), which handles tracking, GPS device configuration, and reporting, and [IoT Logic API](https://app.gitbook.com/o/YVLWhgAwCZPoU5vlRsCs/s/tx3J5BxnWyPV0nP2xr0z/), a data flow manager that processes and optimizes data flows between IoT devices and destination systems.

\[Integration specifics go here]

## Navigation

The **Navixy Repository API documentation** is organized into two complementary sections designed to help you understand concepts and implement solutions.

### Section content

These articles provide essential background knowledge and guidelines:

* [**GraphQL basics**](graphql-basics.md): A brief introduction to GraphQL for developers familiar with REST APIs.
* [**Getting started**](getting-started.md): A step-by-step tutorial that walks you through authentication and your first queries.
* [**Authentication**](authentication.md): How to obtain and use access tokens.
* Error handling:
* Pagination and Filtering and sorting:
* [**Optimistic locking**](optimistic-locking.md): Description of the optimistic locking feature.
* Directives:
* [**Guides**](guides/): In-depth guides exploring the most common use cases.

### Core API reference

The API reference provides complete technical specifications for GraphQL types and operations, grouped by categories:

* **Common resources:**
* **Organizations:**
* **Actors:**
* **Devices:**
* **Assets:**
* **Geo objects:**
* **Schedules:**
* **Access control:**
* **Custom fields:**
* **Audit:**
* **Catalogs:**

{% hint style="warning" %}
The API supports [GraphQL introspection](graphql-basics.md#the-schema) for authenticated users. You can perform it via [Navixy Repository GraphQL Sandbox](https://api.navixy.dev/v4/graphql/sandbox) (currently in query-only demo mode) or with your own tools.
{% endhint %}
