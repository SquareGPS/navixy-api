# Activating a GPS device

In Navixy Repository API, GPS devices are referred to as **inventory items** and stored in user-created lists called **inventories**. Inventories are collections of devices used to organize and manage equipment more efficiently. They serve as logical groupings that help structure, track, and operate devices. A device cannot exist outside of inventory.

In this guide, you will learn how to add a device to an inventory and activate it. You can activate any device listed on the [supported models](https://www.navixy.com/devices/) page or a smartphone with the X-GPS Tracker app installed.

{% hint style="info" %}
For more information on API calls, including parameter descriptions and request and response schemas, click their names.
{% endhint %}

### Types of GPS devices

Navixy Repository API supports two types of devices:

* Devices capable of transmitting GPS data independently (referred to as **masters**).
* Devices unable to contact GPS servers (referred to as **slaves**). They must be paired with master devices to transmit data to our servers; they cannot be activated independently. BT sensors are a common example of the second type.

### How to activate a GPS device

#### Step 1. Create an inventory

{% openapi-schemas spec="navixy-repo" schemas="Inventory" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

Every inventory item requires an inventory. To create it, send the following request:

&#x20;[**POST /inventory/create**](broken-reference)

Use this request body:

```
{​
  "label": "Dutch",
  "description": "Dutch branch office"​
​}
```

You will receive the ID of the created inventory:

```
{
  "id": 12
}
```

#### Step 2. Create a master inventory item

{% openapi-schemas spec="navixy-repo" schemas="InventoryMasterItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

To create a **master inventory item**, send the following request:

[**POST /inventory\_item/master/create**](broken-reference)

Use this request body:

```json
{
  "inventory_id": 12,
  "model": "navixy_ngp",
  "device_id": "123456789012345",
  "label": "gps_tracker_fmc130_001"
}

```

You will get the ID of the newly created item:

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 123
}
</code></pre>

{% openapi-schemas spec="navixy-repo" schemas="InventorySlaveItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

**Step 3. (Optional) Create a slave inventory item**

To create a **slave inventory item**, send the following request:

[**POST /inventory\_item/slave/create**](broken-reference)

Use this request body:

```json
{
  "inventory_id": 12,
  "label": "gps_tracker_fmc130_001"
}
```

Just like with the master, the response will contain the ID of the created item.

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 556
}
</code></pre>

#### Step 4. (Optional) Pair slave device with master

If you've created a slave device, you need to pair it with a master device. To do this, send the following request:

[**POST /inventory\_item/slave/pair**](broken-reference)

Use this request body:

```json
{
  "id": 556,
  "master_id": 123
}
```

You will receive an empty response body and a `204 No Content` status.

#### Step 5. Activate the master device

To activate a master-type device, whether paired with slave devices or not, the device must be preconfigured and exist in the organization's inventory. Upon activation, the device is assigned to the organization.

Send the following request:

[**POST inventory/item/master/activate**](broken-reference)

```json
{
  "id": 123,
  "device_id": "123456789012345",
  "model": "navixy_ngp"
}
```

You will receive an empty response body and the `204 No Content` status.

{% hint style="success" %}
**Congratulations!**\
\
You've successfully activated your device. Next, you can [assign it to an asset](creating-a-custom-asset.md#step-3.-assign-a-device).
{% endhint %}
