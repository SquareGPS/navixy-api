# Creating a custom asset

An asset represents a trackable unit with a clear business purpose. While assets are stored in the system independently, using them involves assigning them activated GPS devices — or, in the API terms, **inventory items**. Multiple items can be assigned to a single asset.

Each asset belongs to a specific type that defines its structure and allows to add user-defined properties called **custom fields**. Those asset types act as templates that determine what information can be stored for each category of asset.

In this guide, you will learn how to create and configure a custom asset.

{% hint style="info" %}
For more information on API calls, including parameter descriptions and request and response schemas, click their names.
{% endhint %}

#### Step 1. Create an asset type

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
          "label": "Section #1",
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

Two categories are available: `business` for moving assets and `geo` for stationary.

The request body contains the following parameters:

* `settings` defines the structure of sections and fields belonging to your asset type.
* `layout` describes how the asset form is split into logical sections, and the order of fields within each section.
* `fields` is used to add custom information to assets, allowing for enhanced customization and data management.

As response, you will receive the ID of the newly created asset type:

```json
{
  "id": 123
}
```

#### Step 2. Create an asset

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

Now that you have an asset, you need to assign a device to it. This is done by adding an `asset_id` parameter to the inventory item representing the device. You can assign several devices to one asset — or, in the API's terms, add the same `asset_id` to several inventory items.

If your device is already activated (the inventory item already exists), send the following request:

[**POST inventory\_item/master/update**](broken-reference)

```json
{
  "inventory_id": 123,
  "device_id": "string",
  "phone": "12345678910",
  "label": "Ford",
  "model": "Focus",
  "asset_id": 345
}
```

If you haven't created an inventory item yet, you can add the `asset_id` parameter to the creation request:

[**POST inventory\_item/master/create**](broken-reference)

```
​{​
  "inventory_id": 12,
  "device_id": "123456789012345",
  "phone": "+12345678901",
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
