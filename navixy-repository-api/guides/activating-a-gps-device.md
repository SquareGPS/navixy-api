# Activating a GPS device

the In Navixy Repository API, GPS devices are referred to as **inventory items** and stored in user-created lists called **inventories**. Inventories are collections of devices used to organize and manage equipment more efficiently. They serve as logical groupings that help structure, track, and operate devices. A device cannot exist outside of inventory.

In this guide, you will learn how to add a device to an inventory and activate it. You can activate any device listed on the [supported models](https://www.navixy.com/devices/) page or a smartphone with the [X-GPS Tracker](https://docs.navixy.com/user-guide/x-gps-tracker) app installed.

{% hint style="info" %}
For more information on API calls, including parameter descriptions and request and response schemas, click their names.
{% endhint %}

### Types of GPS devices

Navixy Repository API supports two types of devices:

* Devices capable of transmitting GPS data independently (referred to as **masters**).
* Devices unable to contact GPS servers (referred to as **slaves**). They must be paired with master devices to transmit data to our servers; they cannot be activated independently. BT sensors are a common example of the second type.

### How to activate a GPS device

#### Prerequisites

A GPS device ready for activation.

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
  "label": "gps_tracker_fmc130_001",
  "phone": "+1234567890"
}

```

**Key parameters:**

* `device_id`: The device's IMEI number (usually found on a sticker)
* `model`: Device model code ([see supported devices](https://www.navixy.com/devices/))
* `phone`: SIM card number (optional)

You will get the ID of the newly created item:

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 123
}
</code></pre>

{% openapi-schemas spec="navixy-repo" schemas="InventorySlaveItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

#### Step 3. Activate the master device

To activate a master-type device, the device must be preconfigured and exist in the organization's inventory. Upon activation, the device is assigned to the organization.

Send the following request:

[**POST inventory\_item/master/activate**](broken-reference)

```json
{
  "id": 123,
  "device_id": "123456789012345",
  "model": "navixy_ngp",
  "activation_method_id": 1,
  "fields": {​
    "iridium_modem_imei": "123456789012345",
    "activation_code": "123"​
  }
}
```

**Key parameters:**

* `activation_method_id`: Unique identifier of one of the authentication methods supported by the model.
*   `fields` : Combined set of field values needed for model activation, including:

    * Model-specific parameters
    * Activation method-specific parameters

    You will receive an empty response body and the `204 No Content` status



**Step 4. (Optional) Create and pair slave devices**

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

Now that you've created a slave device, you need to pair it with a master device. To do this, send the following request:

[**POST /inventory\_item/slave/pair**](broken-reference)

Use this request body:

```json
{
  "id": 556,
  "master_id": 123
}
```

You will receive an empty response body and a `204 No Content` status.

Alternatively, you can create and pair the slave device with a single request:

```json
{
  "inventory_id": 12,
  "label": "gps_tracker_fmc130_001",
  "master_id": 123
}
```

The response will be the same as with an ordinary creation request.

### Extracting GPS device data

Activating the device registers it with [Navixy API](https://www.navixy.com/docs/navixy-api/) and [IoT Logic](https://www.navixy.com/docs/iot-logic-api) systems. This allows you to:

* Receive the device's telematics data via Navixy API's [Track points](https://www.navixy.com/docs/navixy-api/user-api/backend-api/guides/data-retrieval/get-track-points)
* Enrich the received data with [IoT Logic via Websocket](https://www.navixy.com/docs/iot-logic-api/websocket-access-for-dsa)
* Send the data to an external system via [IoT Logic and MQTT](https://www.navixy.com/docs/iot-logic-api/navixy-iot-guide/scenario1)

{% hint style="success" %}
**Congratulations!**\
\
You've successfully activated your device. Next, you can [assign it to an asset](creating-a-custom-asset.md#step-3.-assign-a-device).
{% endhint %}
