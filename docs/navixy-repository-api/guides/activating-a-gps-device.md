# Activating a GPS device

In Navixy Repository API, GPS devices are referred to as **inventory items** and stored in user-created lists called **inventories**. Inventories are collections of devices used to organize and manage equipment more efficiently. They serve as logical groupings that help structure, track, and operate devices. A device cannot exist outside of inventory.

In this guide, you will learn how to add a device to an inventory and activate it. You can activate any device listed on the [supported models](https://www.navixy.com/devices/) page or a smartphone with the [X-GPS Tracker](https://docs.navixy.com/user-guide/x-gps-tracker) app installed.

### Types of GPS devices

Navixy Repository API supports two types of devices:

* Devices capable of transmitting GPS data independently (referred to as **masters**).
* Devices unable to contact GPS servers (referred to as **slaves**). They must be paired with master devices to transmit data to our servers; they cannot be activated independently. BT sensors are a common example of the second type.

### How to activate a GPS device

{% hint style="warning" %}
Note that {BASE\_URL} in sample requests is a placeholder for the URL you'll be using, which depends on your geographical location and the current version of the API. To learn the specific server URLs, see [API environments](../technical-reference.md#api-environments).
{% endhint %}

#### Prerequisites

A GPS device ready for activation.

#### Step 1. Fetch device model specification

Navixy Repository API supports [a wide variety of GPS devices](https://www.navixy.com/devices/), each with its own unique set of parameters for activation and communication. To work with any GPS device, you first need its specific parameters. You can view all specifications for all device models by making this request:

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/model/list" method="get" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

Of course, you probably already know your model and want to fetch its specific parameters. That can be achieved by adding a query. For example, let's say your GPS device is Teltonika FM4200. Use this request:

{% code overflow="wrap" %}
```bash
curl -X GET "{BASE_URL}/inventory_item/master/model/list?q=Teltonika%20FM4200" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```
{% endcode %}

You'll get a response that looks like this:

{% code overflow="wrap" fullWidth="false" %}
```json
{
    "data": [
        {
            "code": "telfm4200",
            "vendor": "Teltonika Telematics",
            "name": "Teltonika FM4200",
            "device_id_pattern": "[0-9]{15,16}",
            "communication": {
                "port": 47776,
                "protocols": {}
            },
            "base_activation_fields": [],
            "activation_methods": [
                {
                    "id": 28,
                    "title": "By tracker phone number",
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
                            "pattern": "^[^\\p{Cntrl}\\uD800-\\uDFFF\\uE000-\\uF8FF]+$"
                        },
                        {
                            "field": "phone",
                            "title": "Phone number",
                            "optional": false,
                            "pattern": "^[0-9]{8,20}$"
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
                            "pattern": "^[^\\p{Cntrl}\\uD800-\\uDFFF\\uE000-\\uF8FF]+$"
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

Remember the following parameters for the next steps:

* `code`: The unique identifier for the model (e.g., `telfm4200`).
* `activation_methods`: An array of supported activation methods. Note the `id` of the method you plan to use (e.g., `44`).
* `method_fields`: A list of field keys required for your chosen activation method (e.g., `apn_name`, `phone`).

#### Step 2. Create an inventory

{% openapi-schemas spec="navixy-repo" schemas="Inventory" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

Every inventory item requires an inventory. To create it, send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/inventory/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

Use this request body:

```bash
curl -X POST {BASE_URL}/inventory/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Paris Depot",
    "description": "Paris Vehicle Depot"
  }'
```

You will receive the ID of the created inventory:

```json
{
  "id": 24
}
```

#### Step 3. Create a master inventory item

{% openapi-schemas spec="navixy-repo" schemas="InventoryMasterItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

```bash
curl -X POST {BASE_URL}/inventory_item/master/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "GPS tracker for Delivery Van 1"
  }'
```

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

You have two approaches to create a **master inventory item**:

**Option A: Create with minimal information.** If you choose Option A, you'll need to update the item with device details before activation.

```bash
curl -X POST {BASE_URL}/inventory_item/master/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "GPS tracker for Delivery Van 1"
  }'
```

**Option B:** **Create with full device details**

<pre class="language-bash"><code class="lang-bash"><strong>curl -X POST {BASE_URL}/inventory_item/master/create \
</strong>  -H "Authorization: Bearer &#x3C;ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
      "inventory_id": 24,
      "model": "telfm4200",
      "device_id": "123456789012345",
      "label": "GPS tracker for Delivery Van 1",
}'
</code></pre>

**Key parameters:**

* `device_id`: The unique identifier of the device, typically its IMEI.
* `model`: Navixy's internal code of your device model that you learned in [Step 1](activating-a-gps-device.md#step-1.-learn-your-devices-parameters).

You will get the ID of the newly created item:

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 34
}
</code></pre>

#### Step 4. Activate the GPS device

To activate a device connected to a master-type inventory item, it must be preconfigured and exist in the organization's inventory. Upon activation, the device is assigned to the organization.

Send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/activate" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

<pre class="language-json"><code class="lang-json">curl -X POST {BASE_URL}/inventory_item/master/activate \
  -H "Authorization: Bearer &#x3C;ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
      "id": 34,
      "device_id": "123456789012345",
      "model": "telfm4200",
      "activation_method_id": 44,
      "fields": {
        "phone": "15551234567",
        "activation_code": "54321"​
        }
<strong>    }'
</strong></code></pre>

These are the key parameters you've learned in [Step 1](activating-a-gps-device.md#step-1.-learn-your-devices-parameters):

* `activation_method_id`: A unique identifier of one of the authentication methods supported by the model.
* `fields` : Combined set of field values needed for model activation, including:
  * Model-specific parameters
  * Activation method-specific parameters

You will receive an empty response body with the `204 No Content` status.

**Step 5. (Optional) Create and pair slave devices**

A slave device doesn't transmit GPS data unless paired with a master device. Many slave devices are sensors connected via Bluetooth.

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

To create a slave inventory item, use this request body:

<pre class="language-bash"><code class="lang-bash">curl -X POST {BASE_URL}/inventory_item/slave/create \
  -H "Authorization: Bearer &#x3C;ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
  "inventory_id": 24,
  "label": "BT sensor 1"
<strong>  }'
</strong></code></pre>

Just like with the master, the response will contain the ID of the created item.

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 556
}
</code></pre>

Now that you've created a slave device, you need to pair it with a master device. To do this, send the following request:

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/pair" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

Use this request body:

```bash
curl -X POST {BASE_URL}/inventory_item/slave/pair \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 556,
    "master_id": 34
  }'
```

You will receive an empty response body and a `204 No Content` status.

Alternatively, you can create and pair the slave device with a single request:

<pre class="language-bash"><code class="lang-bash">curl -X POST {BASE_URL}/inventory_item/slave/create \
  -H "Authorization: Bearer &#x3C;ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
  "inventory_id": 24,
  "label": "BT sensor 1",
  "master_id": 34
<strong>}'
</strong></code></pre>

The response will be the same as with an ordinary creation request (the `id` of the created item).



{% hint style="success" %}
**Congratulations!**\
You've successfully activated your device. Next, you can [assign it to an asset](creating-a-custom-asset.md#step-3.-assign-a-device).
{% endhint %}
