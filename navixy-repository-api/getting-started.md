# Getting started

This guide will walk you through the basic steps to start using Navixy Repository API. You'll learn how to authenticate, activate a GPS device, create an asset, and organize assets with asset links.

### Prerequisites

Before you begin, ensure you have:

* Valid Navixy Repository API credentials (`client_id` and `client_secret`)
* A GPS device ready for activation (we'll use a Teltonika FMC130 tracker in this example)

### Step 1. Authentication

The Navixy Repository API uses OAuth 2.0 for authentication. Depending on your application type, you can choose between Authorization Code for front-end applications and Client Credentials for Server-to-Server. To learn more about the latter, refer to the corresponding section of the [Authentication page](authentication.md#for-server-to-server-communication).

To use Authorization Code flow with user interaction:

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

#### Making authenticated requests

Include the access token in all API requests:

```bash
curl -X GET {BASE_URL}/v0/inventory/list?orgId=1 \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

{% hint style="warning" %}
The API enforces rate limits of 50 requests per second per user and per IP address. Space out your requests accordingly to avoid hitting these limits.
{% endhint %}

For more information about authenticating in Navixy Repository API, see [Authentication](authentication.md).

### Step 2. Activate your GPS device

GPS devices in Navixy Repository API are called **inventory items** and are organized into **inventories**.

{% stepper %}
{% step %}
#### Create an inventory

To create an inventory that will hold your device, send the following request:

#### &#x20;[**POST /inventory/create**](broken-reference)

```bash
curl -X POST {BASE_URL}/v0/asset/create?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '​{
  "label": "Florida",
  "description": "Florida branch office"​
​}'
```

**Response:**

```json
{
  "id": 12
}
```

Note the inventory ID (`12`) for the next step.
{% endstep %}

{% step %}
#### Create and activate a master device

Devices that can transmit GPS data independently are called master devices.

```bash
curl -X POST {BASE_URL}/v0/inventory_item/master/create?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "inventory_id": 12,
    "device_id": "356307042441234",
    "phone": "+1234567890",
    "label": "Teltonika FMC130 - Vessel 001",
    "model": "teltonika_fmc130"
  }'
```

**Key parameters:**

* `device_id`: The device's IMEI number (usually found on a sticker)
* `model`: Device model code ([see supported devices](https://www.navixy.com/devices/))
* `phone`: SIM card number (optional)

**Response:**

```json
{
  "id": 123
}
```
{% endstep %}

{% step %}
#### Activate the device

```bash
curl -X POST {BASE_URL}/v0/inventory_item/master/activate?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "device_id": "356307042441234",
    "model": "teltonika_fmc130"
  }'
```

**Response:** `204 No Content` (Success)
{% endstep %}
{% endstepper %}

### Verification and next steps

#### Verify your setup

Let's confirm everything is working by listing your inventory items:

```bash
curl -X GET "{BASE_URL}/v0/inventory_item/list?orgId=<YOUR_ORG_ID>&q=&limit=10&offset=0&sort=label" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

You should see your device in the response.

{% hint style="success" %}
#### What you've accomplished

* &#x20;**Authenticated** with the Navixy Repository API
* **Created an inventory for your devices**
* **Activated a GPS device** that can now transmit location data
{% endhint %}

#### Next steps

Now that you have the basics set up, you can:

* [Add more devices by creating additional inventory items](getting-started.md#id-2.3.-activate-the-device)
* [Create custom asset types for different categories of assets](getting-started.md#id-3.1.-create-an-asset-type)
* [Create more assets and assign them to devices](getting-started.md#id-3.2-create-an-asset)
* [Group assets by location, department, or function via asset links](getting-started.md#step-4.-organize-assets-with-asset-links)
