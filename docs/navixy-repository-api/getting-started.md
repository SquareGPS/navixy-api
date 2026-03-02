---
description: old version
---

# Getting started

Start using Navixy Repository API with a minimal end-to-end workflow. You’ll authenticate via OAuth 2.0 Authorization Code flow (OpenID Connect). You’ll then create an inventory, add a GPS device as an inventory item, and activate it.

### Prerequisites

Before you begin, ensure you have:

* Valid Navixy Repository API credentials (`client_id` and `client_secret`).
* A registered Callback URL (Redirect URI) for the OAuth2 redirect.
* Your API base URL (`{BASE_URL}`) for REST endpoints. See [API environments](/broken/pages/UpKpxPxvOOMJckvsSJ9N#api-environments).
* Your authentication base URL (`{AUTH_BASE_URL}`) for OAuth2 endpoints. See [Authentication environments](authentication.md#authentication-urls).
* A secure method to generate and validate the `state` parameter for Cross-Site Request Forgery (CSRF) protection.
* A GPS device ready for activation that belongs to the list of [supported devices](https://www.navixy.com/devices/).

### API endpoints used in this guide

You’ll call these Navixy Repository API endpoints:

* OAuth2 authorization: `{AUTH_BASE_URL}/realms/users/protocol/openid-connect/auth`
* OAuth2 token exchange: `{AUTH_BASE_URL}/realms/users/protocol/openid-connect/token`
* Inventory and device activation:
  * `{BASE_URL}/inventory/create`
  * `{BASE_URL}/inventory_item/master/model/list`
  * `{BASE_URL}/inventory_item/master/create`
  * `{BASE_URL}/inventory_item/master/activate`
  * `{BASE_URL}/inventory_item/master/list`

### Step 1. OAuth2 authentication (Authorization Code flow)

Navixy Repository API supports the OAuth2 Authorization Code Flow. To acquire an access token, follow these steps:

{% stepper %}
{% step %}
**Redirect users to the OAuth2 authorization endpoint**

```bash
curl -L \
  --request GET \
  --url "{AUTH_BASE_URL}/realms/users/protocol/openid-connect/auth" \
  --data-urlencode 'client_id=<YOUR_CLIENT_ID>' \
  --data-urlencode 'response_type=code' \
  --data-urlencode 'redirect_uri=https://<YOUR_APP_CALLBACK_URL>' \
  --data-urlencode 'scope=<REQUESTED_SCOPE_ONE> <REQUESTED_SCOPE_TWO>' \
  --data-urlencode 'state=<YOUR_SECURE_RANDOM>'
```
{% endstep %}

{% step %}
**Exchange authorization code for access token**

**Request:**

```bash
curl -L \
  --request POST \
  --url '{AUTH_BASE_URL}/realms/users/protocol/openid-connect/token' \
  --header 'Content-Type: application/json' \
  --data '{
    "grant_type": "authorization_code",
    "client_id": "<YOUR_CLIENT_ID>",
    "client_secret": "<YOUR_CLIENT_SECRET>",
    "code": "<YOUR_AUTHORIZATION_CODE>",
    "redirect_uri": "https://<YOUR_APP_CALLBACK_URL>"
  }'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ...signature",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "8xLOxBtZp8",
  "scope": "<REQUESTED_SCOPE_ONE> <REQUESTED_SCOPE_TWO>",
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.e...signature"
}
```
{% endstep %}
{% endstepper %}

#### How to make authenticated requests

Include the Bearer access token in every API request:

```bash
curl -L \
  --request GET \
  --url '{BASE_URL}/inventory/list' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>'
```

For more information about authenticating in Navixy Repository API, see [Authentication](authentication.md).

### Step 2. Activate a GPS tracking device (inventory item)

GPS devices in Navixy Repository API are called **inventory items** and are organized into **inventories**.\
For a more in-depth explanation of activating a GPS device and working with inventories, see [Activating a GPS device](guides/activating-a-device.md).

{% stepper %}
{% step %}
**Fetch device model specification**

Navixy Repository API supports [a wide variety of GPS devices](https://www.navixy.com/devices/), each with its own unique set of parameters for activation and communication. To work with any GPS device, you first need its specific parameters. You can retrieve the complete profile for any supported model by querying the [**/inventory\_item/master/model/list**](/broken/pages/DyP1yBfCuntDOIbPhXf1#get-v0-inventory_item-master-model-list) endpoint.

For example, to get the specifications for a Teltonika FMC234, use the following request:

{% code overflow="wrap" %}
```bash
curl -L \
  --request GET \
  --url "{BASE_URL}/inventory_item/master/model/list?q=Teltonika%20FMC234" \
  --header 'Authorization: Bearer <ACCESS_TOKEN>'
```
{% endcode %}

From the response, you will need to save the following critical parameters for future requests:

* `code`: The unique identifier for the model (e.g., `telfmc234`).
* `activation_methods`: An array of supported activation methods. Note the `id` of the method you plan to use (e.g., `1`).
* `method_fields`: A list of fields required for the chosen activation method (e.g., `iccid`).

```
{
    "data": [
        {
            "code": "telfmc234",
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
curl -L \
  --request POST \
  --url '{BASE_URL}/inventory/create' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "label": "Florida",
    "description": "Florida branch office"
  }'
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

Now, create a master device as an item in your inventory. You will need `inventory_id` and the model `code` you've fetched previously, as well as `device_id` , which is typically its IMEI (pattern: `^[0-9a-zA-Z\\-]{1,64}$`).

```bash
curl -L \
  --request POST \
  --url '{BASE_URL}/inventory_item/master/create' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "inventory_id": 12,
    "device_id": "356307042441234",
    "label": "Vessel 001",
    "model": "telfmc234"
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
curl -L \
  --request POST \
  --url '{BASE_URL}/inventory_item/master/activate' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "id": 123,
    "device_id": "356307042441234",
    "model": "telfmc234",
    "activation_method_id": 1,
    "fields": {
      "iccid": "8912345678901234567"
    }
  }'
```

A successful activation will return a `204 No Content` response.
{% endstep %}
{% endstepper %}

### Verification and next steps

Let's confirm everything works by listing your inventory items:

```bash
curl -L \
  --request GET \
  --url "{BASE_URL}/inventory_item/master/list" \
  --header 'Authorization: Bearer <ACCESS_TOKEN>'
```

You should see your device in the response.

{% hint style="success" %}
**What you've accomplished:**

* Authenticated with the Navixy Repository API
* Fetched the specification for your device model
* Created an inventory for your devices
* Created an inventory item representing your device
* Activated the device that can now [transmit location data](guides/activating-a-device.md#how-to-use-the-data-transmitted-by-the-device)
{% endhint %}

#### Next steps

Now that you have the basics set up, you can:

* [Add and activate more devices by creating additional inventory items](guides/activating-a-device.md)
* Create new inventories to store your devices
* Create custom asset types for different categories of assets
* Create assets (objects representing real-world business units) and assign devices to them
* [Group assets by location, department, or function](guides/organizing-assets-into-groups.md)
