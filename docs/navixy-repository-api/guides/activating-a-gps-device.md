# Activating a GPS device

In Navixy Repository API, GPS devices are referred to as **inventory items** and stored in user-created lists called **inventories**. Inventories are collections of devices used to organize and manage equipment more efficiently. They serve as logical groupings that help structure, track, and operate devices. A device cannot exist outside of inventory.

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

#### Step 1. Fetch device model specification

Navixy Repository API supports [a wide variety of GPS devices](https://www.navixy.com/devices/), each with its own unique set of parameters for activation and communication. To work with any GPS device, you first need its specific parameters. You can view all specifications for all device models by making this request:

[**GET /inventory\_item/master/models/list**](broken-reference)

Of course, you probably already know your model and want to fetch its specific parameters. That can be achieved by adding a query. For example, let's say our GPS device is Teltonika GMC4200. We'll use this request:

**GET /inventory\_item/master/models/list?q=Teltonika%20FM4200**

{% code fullWidth="false" %}
```json
{
    "data": [
        {
            "code": "telfm4200",
            "vendor": "Teltonika Telematics",
            "name": "Teltonika FM4200",
            "communication": {
                "port": 47776,
                "protocols": {}
            },
            "base_activation_fields": [],
            "activation_methods": [
                {
                    "id": 1,
                    "title": "SIM card provided with a device",
                    "method_fields": [
                        {
                            "field": "iccid",
                            "title": "ICCID number of SIM-card from the package",
                            "optional": false,
                            "pattern": "89[0-9]{17,18}"
                        }
                    ]
                },
                {
                    "id": 44,
                    "title": "By activation code and tracker phone number",
                    "method_fields": [
                        {
                            "field": "apn_name",
                            "title": "APN",
                            "optional": true,
                            "pattern": "[-a-zA-Z0-9_.@ ]*"
                        },
                        {
                            "field": "apn_user",
                            "title": "Username",
                            "optional": true,
                            "pattern": "[-a-zA-Z0-9_.@ ]*"
                        },
                        {
                            "field": "apn_password",
                            "title": "Password",
                            "optional": true,
                            "pattern":"^[^\p{Cntrl}\uD800-\uDFFF\uE000-\uF8FF]+$"
                        },
                        {
                            "field": "phone",
                            "title": "Phone number",
                            "optional": false,
                            "pattern": "^[0-9]{8,20}$"
                        },
                        {
                            "field": "activation_code",
                            "title": "Activation code",
                            "optional": true,
                            "pattern": "[0-9]{3,20}"
                        }
                    ]
                }
            ]
        }
    ],
    "has_more": false
}
```
{% endcode %}

From the response, the following parameters are required for the next steps:

* `code`: The unique identifier for the model (e.g., `telfm4200`).
* `activation_methods`: An array of supported activation methods. Note the `id` of the method you plan to use (e.g., `44`).
* `method_fields`: A list of field keys required for your chosen activation method (e.g., `apn_name`, `phone`).

#### Step 2. Create an inventory

{% openapi-schemas spec="navixy-repo" schemas="Inventory" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

Every inventory item requires an inventory. To create it, send the following request:

[**POST /inventory/create**](broken-reference/)

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

#### Step 3. Create a master inventory item

{% openapi-schemas spec="navixy-repo" schemas="InventoryMasterItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

To create a **master inventory item**, send the following request:

[**POST /inventory\_item/master/create**](broken-reference/)

Use this request body:

```json
{
  "inventory_id": 12,
  "model": "telfm4200",
  "device_id": "123456789012345",
  "label": "Delivery Van 1",
}
```

**Key parameters:**

* `device_id`: The unique identifier of the device, typically its IMEI.
* `model`: The code of your device model that you learned in [Step 1](activating-a-gps-device.md#step-1.-learn-your-devices-parameters).

You will get the ID of the newly created item:

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 34
}
</code></pre>

{% openapi-schemas spec="navixy-repo" schemas="InventorySlaveItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

#### Step 4. Activate the GPS device

To activate a device connected to a master-type inventory item, it must be preconfigured and exist in the organization's inventory. Upon activation, the device is assigned to the organization.

Send the following request:

[**POST inventory\_item/master/activate**](broken-reference/)

```json
{
  "id": 34,
  "device_id": "123456789012345",
  "model": "telfm4200",
  "activation_method_id": 44,
  "fields": {​
    "apn_name": "broadband",
    "apn_user": "user",
    "apn_password": "SecurePassword123!",
    "phone": "15551234567",
    "activation_code": "54321"​
  }
}
```

These are the key parameters you've learned in [Step 1](activating-a-gps-device.md#step-1.-learn-your-devices-parameters):

* `activation_method_id`: A unique identifier of one of the authentication methods supported by the model.
* `fields` : Combined set of field values needed for model activation, including:
  * Model-specific parameters
  * Activation method-specific parameters

You will receive an empty response body with the `204 No Content` status.

**Step 5. (Optional) Create and pair slave devices**

To create a **slave inventory item**, send the following request:

[**POST /inventory\_item/slave/create**](broken-reference/)

Use this request body:

```json
{
  "inventory_id": 12,
  "label": "BT sensor 1"
}
```

Just like with the master, the response will contain the ID of the created item.

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 556
}
</code></pre>

Now that you've created a slave device, you need to pair it with a master device. To do this, send the following request:

[**POST /inventory\_item/slave/pair**](broken-reference/)

Use this request body:

```json
{
  "id": 556,
  "master_id": 34
}
```

You will receive an empty response body and a `204 No Content` status.

Alternatively, you can create and pair the slave device with a single request:

```json
{
  "inventory_id": 12,
  "label": "BT sensor 1",
  "master_id": 34
}
```

The response will be the same as with an ordinary creation request.

### How to use the data transmitted by the device

Activating the GPS device registers it with other Navixy systems: [Navixy API](https://www.navixy.com/docs/navixy-api/), a telematics platform without business management features, and [IoT Logic](https://www.navixy.com/docs/iot-logic-api), a low-code data processing and enrichment tool.

{% hint style="warning" %}
Please note that Navixy API has a [different authentication system](https://www.navixy.com/docs/navixy-api/user-api/authentication) from Navixy Repository API.
{% endhint %}

Activation allows you to:

* Receive the device's location data via [Navixy API's Track points](https://www.navixy.com/docs/navixy-api/user-api/backend-api/guides/data-retrieval/get-track-points)
* Enrich the received data with [IoT Logic via Websocket](https://www.navixy.com/docs/iot-logic-api/websocket-access-for-dsa)
* Send the data to an external system via [IoT Logic and MQTT](https://www.navixy.com/docs/iot-logic-api/navixy-iot-guide/scenario1)

{% hint style="success" %}
**Congratulations!**\\

\
You've successfully activated your device. Next, you can [assign it to an asset](creating-a-custom-asset.md#step-3.-assign-a-device).
{% endhint %}
