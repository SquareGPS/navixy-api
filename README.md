# Overview

**Navixy Repository API** is a programming interface for managing the organizational structure and business entities of the Navixy platform. It provides a flexible way to define what you track (assets), what tracks them (devices), where things matter (geographic objects), when things happen (schedules), and who can access what (permissions).

**Navixy Repository is based on GraphQL.** Unlike REST APIs where you call multiple endpoints to gather related data, GraphQL allows you to request the exact fields you need in a single query. You describe the shape of the data you want, and the API returns it in that shape.

For a quick primer on GraphQL concepts, see [GraphQL basics](graphql-basics.md).

## Purpose and capabilities

**Navixy Repository API** enables you to:

* Manage **organizations** in a multi-tenant hierarchy (dealers, sub-organizations)
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

<table><thead><tr><th width="138.5999755859375">Term</th><th>Definition</th></tr></thead><tbody><tr><td><strong>Organization</strong></td><td>A tenant in the system hierarchy. Organizations own all other resources and can have parent-child relationships.</td></tr><tr><td><strong>Asset</strong></td><td>A business object you're tracking: a vehicle, piece of equipment, employee, or any other entity. Assets can be grouped together or assigned one or several GPS devices.</td></tr><tr><td><strong>Device</strong></td><td>Physical tracking hardware (GPS tracker, sensor, beacon). Devices have types, models, statuses, and hardware identifiers (IMEI, serial number).</td></tr><tr><td><strong>Geo object</strong></td><td>A location-based entity: geofence, point of interest, or route. Geometry is stored as GeoJSON in the <code>geojson</code> custom field.</td></tr><tr><td><strong>Catalog</strong></td><td>Configurable lookup table for entity types, statuses, and other classification systems.</td></tr></tbody></table>

## Navigation

The **Navixy Repository API documentation** is organized into two complementary sections designed to help you understand concepts and implement solutions.

### Section content

These articles provide essential background knowledge and guidelines:

* [**GraphQL basics**](graphql-basics.md): A brief introduction to GraphQL for developers familiar with REST APIs.
* [**GraphQL tips and patterns**](graphql-basics/graphql-tips-and-patterns.md): Practical suggestions for improving your GraphQL experience.
* [**Getting started**](getting-started.md): A step-by-step tutorial that walks you through authentication and your first queries.
* [**Authentication**](authentication.md): How to obtain and use access tokens.
* [**Error handling**](error-handling.md)**:** Error structure, codes, and common error scenarios.
* [**Pagination** ](pagination.md)and [**Filtering and sorting**](filtering-and-sorting.md): Instruments for efficient navigating through pages of data and narrowing down results by criteria and order.
* [**Optimistic locking**](optimistic-locking.md): How the API handles concurrent updates to prevent conflicting changes from overwriting each other.
* [**Guides**](guides/): In-depth guides exploring the most common use cases.

### Core API reference

The API reference provides complete technical specifications for all GraphQL types and operations, grouped by category:

* [**Common resources**](common.md)
* [**Directives**](core-api-reference/directives.md)
* [**Organizations**](organizations/)
* [**Actors**](actors/)
* [**Devices**](devices/)
* [**Assets**](assets/)
* [**Geo objects**](geo-objects/)
* [**Schedules**](schedules/)
* [**Access control**](access-control/)
* [**Custom fields**](custom-fields.md)
* [**Audit**](audit.md)
* [**Catalogs**](catalogs/)

{% hint style="warning" %}
The API supports [GraphQL introspection](graphql-basics.md#the-schema) for authenticated users. You can perform it via [Navixy Repository GraphQL Sandbox](https://api.navixy.dev/v4/graphql/sandbox) (currently in query-only demo mode) or with your own tools.
{% endhint %}
