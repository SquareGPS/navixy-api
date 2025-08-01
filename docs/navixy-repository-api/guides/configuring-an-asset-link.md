---
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Configuring an asset link

In Navixy Repository API, **asset links** are user-created collections of assets grouped by a certain principle, such as a truck, a trailer, and the equipment it carries, or vehicles parked at a specific site. These links help organize and manage assets that work together or have logical relationships.

An asset link can contain assets of all types. Links automatically manage asset relationships and handle reassignments when assets are moved between groups.

In this guide, you will learn about how asset links are structured, how to create them, and how to assign assets to them.

### How to configure an asset link

{% hint style="warning" %}
Note that {BASE\_URL} in sample requests is a placeholder for the URL you'll be using, which depends on your geographical location. To learn the specific server URLs, see [API environments](../technical-reference.md#api-environments).
{% endhint %}

{% openapi-schemas spec="navixy-repo" schemas="AssetLink" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

#### Prerequisites

An existing asset. Learn how to create it in [Creating a custom asset](creating-a-custom-asset.md).

#### Step 1. Create a new asset link

To create a new asset link, prepare an array of assets (or use an empty array) and send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/asset_link/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

Use this request body:

```json
curl -X POST {BASE_URL}/v0/asset_link/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Boston boats",
    "asset_ids": [
      3
    ]
  }'
```

You will receive a response with the new link ID:

```json
{
  "id": 789
}
```

#### Step 2. Add an asset to an existing link

To add an asset to an existing link, send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/asset_link/set" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

Use this request body:

```json
curl -X POST {BASE_URL}/v0/asset_link/set \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 789,
    "asset_id": 2
  }'
```

You will receive `204 No Content` response, and the asset will be added to the `asset_ids` array.

**Step 3. (Optional) Remove an asset from an asset link**

To remove an asset from an existing link, send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/asset_link/remove" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

Use this request body:

```json
curl -X POST {BASE_URL}/v0/asset_link/remove \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 789,
    "asset_id": 2
  }'
```

You will receive an empty response body and a `204 No Content` status, and the asset will be removed from the `asset_ids` array.

{% hint style="success" %}
**Congratulations!**\
You've successfully created and configured an asset link.
{% endhint %}
