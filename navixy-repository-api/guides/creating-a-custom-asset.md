# Creating a custom asset

An asset represents a trackable unit with a clear business purpose. While assets are stored in the system independently, using them involves assigning them activated GPS devices — or, in the API terms, **inventory items**. Multiple items can be assigned to a single asset.

Each asset belongs to a specific type that defines its structure and allows you to add user-defined properties called **custom fields**. Those asset types act as templates that determine what information can be stored for each category of asset.

In this guide, you will learn how to create and configure a custom asset.

{% hint style="info" %}
For more information on API calls, including parameter descriptions and request and response schemas, click their names.
{% endhint %}



### How to create a custom asset

#### Step 1. Create an asset type

{% openapi-schemas spec="navixy-repo" schemas="AssetType" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

To create a new asset type, send the following request:

[**POST asset\_type/create**](broken-reference)

```json
{
  "label": "Boats",
  "category": "business",
  "settings": {
    "layout": {
      "sections": [
        {
          "label": "Section 1",
          "fields": [
            "label",
            "Text field",
            "131212",
            "description"
          ]
        }
      ]
    }
  },
  "fields": [
    {
      "type": "text",
      "label": "Text field",
      "required": true
    },
    {
      "type": "decimal",
      "label": "Number field",
      "required": false
    }
  ]
}
```

The request body contains the following parameters: `category`, `settings,` and `fields`.

The available categories are `business` for moving assets and `geo` for stationary.

**`settings`** defines the structure of sections and fields belonging to your asset type. This object contains a `layout` property that describes how the asset form is split into logical sections and the order of fields within each section. The layout consists of sections, where each section has:

* `label`: Section name
* `fields`: List of field keys to be displayed in the specified order within the section

**`fields`** is an array of custom field objects used to add custom information to assets, allowing for enhanced customization and data management. Each custom field includes:

* `type`: Field type (text, decimal, geojson)
* `label`: Field's name
* `required`: Whether the field is mandatory
* `description`: Optional description

After sending the request, you will receive a response with the ID of the newly created asset type:

```json
{
  "id": 123
}
```

#### Step 2. Create an asset

{% openapi-schemas spec="navixy-repo" schemas="Asset" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

To create an asset, send the following request:

[**POST asset/create**](broken-reference)

```json
{
    "type_id": 123
    "label": "Aspen V6 GTX",
    "fields": {
      "field1" : {
        "type": "text",
        "value":  "I love text!"
    }
  }
}
```

You will receive the ID of the newly created asset:

```json
{
  "id": 123
}
```

#### Step 3. Assign a device

{% openapi-schemas spec="navixy-repo" schemas="InventoryMasterItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

Now that you have an asset, you need to assign a device to it. This is done by adding an `asset_id` parameter to the master-type inventory item representing the device. You can assign several devices to one asset — or, in the API's terms, add the same `asset_id` to several inventory items.

If your device is already activated (the inventory item already exists), send the following request:

[**POST inventory\_item/master/update**](broken-reference)

```json
{
  "id": 123,
  "inventory_id": 12,
  "label": "GPS tracker FMC130-001",
  "asset_id": 21
}
```

If you haven't created an inventory item yet, you can add the `asset_id` parameter to the creation request:

[**POST inventory\_item/master/create**](broken-reference)

```
​{​
  "inventory_id": 12,
  "device_id": "123456789012345",
  "label": "GPS tracker FMC130-001",
  "model": "navixy_ngp",
  "asset_id": 21​
​}
```

{% hint style="success" %}
**Congratulations!**\
\
You've successfully created a custom asset. Next, you can assign it to a linked group.
{% endhint %}
