# Creating a custom asset

An asset represents a trackable unit with a clear business purpose. While assets are stored in the system independently, using them involves assigning them activated GPS devices — or, in the API terms, **inventory items**. Multiple items can be assigned to a single asset.

Each asset belongs to a specific type that defines its structure and allows you to add user-defined properties called **custom fields**. Those asset types act as templates that determine what information can be stored for each category of asset.

In this guide, you will learn how to create and configure a custom asset.

### How to create a custom asset

#### Step 1. Create an asset type

{% openapi-schemas spec="navixy-repo" schemas="AssetType" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

To create a new asset type, send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/asset_type/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

```json
{
  "label": "Commercial Vessels",
  "category": "business",
  "fields": [
    {
      "type": "text",
      "label": "Vessel Name",
      "required": true
    },
    {
      "type": "text",
      "label": "Registration Number",
      "required": true
    },
    {
      "type": "decimal",
      "label": "Engine Power",
      "required": false
    },
    {
      "type": "decimal",
      "label": "Max Passengers",
      "required": false
    }
  ],
  "settings": {
    "layout": {
      "sections": [
        {
          "label": "Vessel Information",
          "fields": [
            "Vessel Name",
            "Registration Number"
          ]
        },
        {
          "label": "Technical Specifications",
          "fields": [
            "Engine Power",
            "Max Passengers"
          ]
        }
      ]
    }
  }
}
```

Aside from the `label` of the asset type, the request body contains the following parameters: `category`, `settings,` and `fields`.

The available categories are `business` for moving assets and `geo` for stationary.

The **`settings`** key defines the structure of sections and fields belonging to your asset type. This object contains a `layout` property that describes how the asset form is split into logical sections and the order of fields within each section. The layout consists of sections, where each section has:

* `label`: Section name
* `fields`: List of fields to be displayed in the specified order inside the section

The **`fields`** key is an array of custom field objects used to add user-created information to assets, allowing for enhanced customization and data management. Each field includes:

* `type`: Field type (text, decimal, geojson)
* `label`: Field name
* `required`: Whether the field is mandatory
* `description`: An optional description

After sending the request, you will receive a response with the ID of the newly created asset type:

```json
{
  "id": 456
}
```

#### Step 2. Fetch custom field IDs

Before creating an asset, we'll need to learn the IDs of the custom fields we've added in Step 1. To do it, send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/asset_type/read" method="get" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

In our case, it will be **POST asset\_type/read?id=456.**

You will receive full information about the asset type, including the `id` of each custom field. Save them for later.

```
{
    "id": 25,
    "label": "Commercial Vessels",
    "category": "business",
    "settings": {
        "layout": {
            "sections": [
                {
                    "label": "Vessel Information",
                    "fields": [
                        "Vessel Name",
                        "Registration Number"
                    ]
                },
                {
                    "label": "Technical Specifications",
                    "fields": [
                        "Engine Power",
                        "Max Passengers"
                    ]
                }
            ]
        }
    },
    "fields": [
        {
            "id": 55,
            "label": "Vessel Name",
            "required": true,
            "description": "",
            "type": "text"
        },
        {
            "id": 56,
            "label": "Registration Number",
            "required": true,
            "description": "",
            "type": "text"
        },
        {
            "id": 57,
            "label": "Engine Power",
            "required": false,
            "description": "",
            "type": "decimal"
        },
        {
            "id": 58,
            "label": "Max Passengers",
            "required": false,
            "description": "",
            "type": "decimal"
        }
    ],
    "created_at": "2025-07-09T11:57:36.003383Z"
}
```

#### Step 3. Create an asset

{% openapi-schemas spec="navixy-repo" schemas="Asset" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

To create an asset, send the following request using the `id` of each custom field from the previous step, or at least those you marked as `required`.

{% openapi-operation spec="navixy-repo" path="/v0/asset/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

```json
{
  "type_id": 456,
  "label": "Sea Explorer",
  "fields": {
    "55": {
      "type": "text",
      "value": "Sea Explorer"
    },
    "56": {
      "type": "text",
      "value": "BOT-2024-001"
    },
    "57": {
      "type": "decimal",
      "value": 350.5
    },
    "58": {
      "type": "decimal",
      "value": 12
    }
  }
}
```

You will receive the ID of the newly created asset:

```json
{
  "id": 789
}
```

#### Step 4. Assign a GPS device

{% openapi-schemas spec="navixy-repo" schemas="InventoryMasterItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

Now that you have an asset, you need to assign a device to it. This is done by adding the `asset_id` parameter to the master-type inventory item representing the device. You can assign several devices to one asset — or, in the API's terms, add the same `asset_id` to several inventory items.

If your device is already activated, send the following request (let's assume your item's `label` is `Sea Explorer GPS Tracker`):

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/update" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

```json
{
  "id": 123,
  "inventory_id": 12,
  "label": "Sea Explorer GPS Tracker",
  "asset_id": 789
}
```

If you haven't created an inventory item yet, you can add the `asset_id` parameter to the creation request:

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

```
​{
  "inventory_id": 12,
  "device_id": "123456789012345",
  "label": "Sea Explorer GPS Tracker",
  "model": "telfmu130_fmc130_234",
  "asset_id": 789
}
```

{% hint style="success" %}
**Congratulations!**\
You've successfully created a custom asset. Next, you can [add it to an asset link](configuring-an-asset-link.md).
{% endhint %}
