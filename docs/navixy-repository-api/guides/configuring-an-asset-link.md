# Configuring an asset link

In Navixy Repository API, **asset links** are user-created collections of assets grouped by a certain principle, such as a truck, a trailer, and the equipment it carries, or vehicles parked at a specific site. These links help organize and manage assets that work together or have logical relationships.

An asset link can contain assets of all types. Links automatically manage asset relationships and handle reassignments when assets are moved between groups.

In this guide, you will learn about how asset links are structured, how to create them, and how to assign assets to them.

{% hint style="info" %}
For more information on API calls, including parameter descriptions and request and response schemas, click their names.
{% endhint %}

### How to configure an asset link

{% openapi-schemas spec="navixy-repo" schemas="AssetLink" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

#### Prerequisites

An existing asset. Learn how to create it in [Creating a custom asset](creating-a-custom-asset.md).

#### Step 1. Create a new asset link

To create a new asset link, prepare an array of assets (or use an empty array) and send the following request:

[**POST /asset\_link/create**](broken-reference/)

Use this request body:

```json
{
  "label": "Boston boats",
  "asset_ids": [
    3
  ]
}
```

You will receive a response with the new link ID:

```json
{
  "id": 789
}
```

#### Step 2. Add an asset to an existing link

To add an asset to an existing link, send the following request:

[**POST /asset\_link/set**](broken-reference/)

Use this request body:

```json
{
  "link_id": 789,
  "asset_id": 2
}
```

You will receive `200 OK` response, and the asset will be added to the `asset_ids` array.

**Step 3. (Optional) Remove an asset from an asset link**

To remove an asset from an existing link, send the following request:

[**POST /asset\_link/remove**](broken-reference/)

Use this request body:

```json
{
  "link_id": 789,
  "asset_id": 2
}
```

You will receive an empty response body and a `204 No Content` status, and the asset will be removed from the `asset_ids` array.

{% hint style="success" %}
**Congratulations!**\
You've successfully created and configured an asset link.
{% endhint %}
