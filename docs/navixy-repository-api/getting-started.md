# Getting started

This guide will walk you through the basic steps to start using Navixy Repository API. You'll learn how to authenticate, create an inventory and inventory item to store your GPS device, and activate it.

### Prerequisites

Before you begin, ensure you have:

* Valid Navixy Repository API credentials (`client_id` and `client_secret`).
* A registered Callback URL (Redirect URI): The specific URL in your application where users will be redirected after granting consent.
* URLs of API and authentication servers ({BASE\_URL} and {AUTH\_BASE\_URL}), determined depending on your geographical location. For more information about {BASE\_URL}, see [API Environments](technical-reference.md#api-environments). For information about {AUTH\_BASE\_URL}, see [Authentication environments](authentication.md#authentication-urls).
* A secure method to generate and validate the `state` parameter for Cross-Site Request Forgery (CSRF) protection.
* A GPS device ready for activation that belongs to the list of [supported devices](https://www.navixy.com/devices/).

### Step 1. Authentication

Navixy Repository API uses OAuth 2.0 for authentication. Depending on your application type, you can choose between Authorization Code for front-end applications and Client Credentials for Server-to-Server. To learn more about the latter, refer to the corresponding section of the [Authentication article](authentication.md#for-server-to-server-communication).

To use Authorization Code flow:

{% stepper %}
{% step %}
**Redirect users to the authorization endpoint**

```bash
curl -X GET "{AUTH_BASE_URL}/authorize" \
  --data-urlencode 'client_id=<YOUR_CLIENT_ID>' \
  --data-urlencode 'response_type=code' \
  --data-urlencode 'redirect_uri=https://<YOUR_APP_CALLBACK_URL>' \
  --data-urlencode 'scope=read write' \
  --data-urlencode 'state=<YOUR_SECURE_RANDOM>'
```
{% endstep %}

{% step %}
**Exchange authorization code for access token**

<pre class="language-bash"><code class="lang-bash">curl -X POST {AUTH_BASE_URL}/oauth/token \
<strong>  -H "Content-Type: application/json" \
</strong>  -d '{
    "grant_type": "authorization_code",
    "client_id": "&#x3C;YOUR_CLIENT_ID>",
    "client_secret": "&#x3C;YOUR_CLIENT_SECRET>",
    "code": "&#x3C;YOUR_AUTHORIZATION_CODE>",
    "redirect_uri": "https://&#x3C;YOUR_APP_CALLBACK_URL>"
  }'
</code></pre>
{% endstep %}
{% endstepper %}

#### How to make authenticated requests

Include the access token in all API requests:

```bash
curl -X GET {BASE_URL}/v0/inventory/list \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

{% hint style="warning" %}
The API enforces rate limits of 50 requests per second per user and per IP address. Space out your requests accordingly to avoid hitting these limits.
{% endhint %}

For more information about authenticating in Navixy Repository API, see [Authentication](authentication.md).

### Step 2. Activate your GPS device

GPS devices in Navixy Repository API are called **inventory items** and are organized into **inventories**.\
For a more in-depth explanation of activating a GPS device and working with inventories, see [Activating a GPS device](guides/activating-a-gps-device.md).

{% stepper %}
{% step %}
#### Fetch device model specification

Navixy Repository API supports [a wide variety of GPS devices](https://www.navixy.com/devices/), each with its own unique set of parameters for activation and communication. To work with any GPS device, you first need its specific parameters. You can retrieve the complete profile for any supported model by querying the [**/inventory\_item/master/models/list**](broken-reference) endpoint.

For example, to get the specifications for a Teltonika FMC234, use the following request:

**GET /inventory\_item/master/models/list?q=Teltonika%20FMC234**

From the response, you will need to save the following critical parameters for future requests:

* `code`: The unique identifier for the model (e.g., `telfmc234`).
* `activation_methods`: An array of supported activation methods. Note the `id` of the method you plan to use (e.g., `1`).
* `method_fields`: A list of fields required for the chosen activation method (e.g., `iccid`).

```
{
    "data": [
        {
            "code": "telfmu130_fmc130_234",
            "vendor": "Teltonika Telematics",
            "name": "Teltonika FMC234",
            ...,
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
                ...
            ]
        }
    ],
    "has_more": false
}
```
{% endstep %}

{% step %}
**Create an inventory**

Next, create an inventory to house your new device. Inventories are logical containers for organizing your items.

```bash
curl -X POST {BASE_URL}/v0/inventory/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '​{
  "label": "Florida",
  "description": "Florida branch office"​
​}'
```

The API will respond with the new inventory's `id`. Save it for the next step.

```json
{
  "id": 12
}
```
{% endstep %}

{% step %}
**Create a master device**

Devices that can transmit GPS data independently are called master devices. In Navixy Repository API, devices are stored as inventory items.

Now, create a master device as an item in your inventory. You will need `inventory_id` and the model `code` you've fetched previously, as well as `device_id` , which is typically its IMEI.

```bash
curl -X POST {BASE_URL}/v0/inventory_item/master/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "inventory_id": 12,
    "device_id": "356307042441234",
    "label": "Vessel 001",
    "model": "telfmu130_fmc130_234"
  }'
```

Save the returned device `id` for the next and final step.

```json
{
  "id": 123
}
```
{% endstep %}

{% step %}
**Activate the device**

Finally, activate the device using its `id` from the previous step along with the `activation_method_id` and `fields` you saved earlier.

```bash
curl -X POST {BASE_URL}/v0/inventory_item/master/activate \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "device_id": "356307042441234",
    "model": "telfmu130_fmc130_234",
    "activation_method_id": 1,
    "fields": {​
      "iccid": "8912345678901234567"
    }
  }'
```

A successful activation will return a `204 No Content` response.
{% endstep %}
{% endstepper %}

### Verification and next steps

#### Verify your setup

Let's confirm everything works by listing your inventory items:

```bash
curl -X GET "{BASE_URL}/v0/inventory_item/master/list" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

You should see your device in the response.

{% hint style="success" %}
**What you've accomplished:**

* Authenticated with the Navixy Repository API
* Fetched the specification for your device model
* Created an inventory for your devices
* Created an inventory item representing your device
* Activated the device that can now [transmit location data](guides/activating-a-gps-device.md#how-to-use-the-data-transmitted-by-the-device)
{% endhint %}

#### Next steps

Now that you have the basics set up, you can:

* [Add and activate more devices by creating additional inventory items](guides/activating-a-gps-device.md)
* [Create new inventories to store your devices](guides/activating-a-gps-device.md#step-2.-create-an-inventory)
* [Create custom asset types for different categories of assets](guides/creating-a-custom-asset.md#step-1.-create-an-asset-type)
* [Create assets (objects representing real-world business units) and assign devices to them](guides/creating-a-custom-asset.md#step-3.-create-an-asset)
* [Group assets by location, department, or function via asset links](getting-started.md#step-4.-organize-assets-with-asset-links)
