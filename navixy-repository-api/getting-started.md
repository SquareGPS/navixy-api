# Getting started

This guide will walk you through the basic steps to start using Navixy Repository API. You'll learn how to authenticate, activate a GPS device, create an asset, and organize assets with asset links.

### Prerequisites

Before you begin, ensure you have:

* Valid Navixy Repository API credentials (`client_id` and `client_secret`)
* Your organization ID (`orgId`) from your JWT token
* A GPS device ready for activation (we'll use a Teltonika FMC130 tracker in this example)

### Step 1. Authentication

The Navixy Repository API uses OAuth 2.0 for authentication. Choose the appropriate flow based on your application type.

#### For Server-to-Server applications

Use the Client Credentials flow for backend applications:

```bash
curl -X POST {AUTH_BASE_URL}/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "<YOUR_CLIENT_ID>",
    "client_secret": "<YOUR_CLIENT_SECRET>"
  }'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "read write"
}
```

#### For frontend applications

Use the Authorization Code flow with user interaction:

1. **Redirect users to authorization endpoint:**

```bash
curl -X GET "{AUTH_BASE_URL}/authorize" \
  --data-urlencode 'client_id=<YOUR_CLIENT_ID>' \
  --data-urlencode 'response_type=code' \
  --data-urlencode 'redirect_uri=https://<YOUR_APP_CALLBACK_URL>' \
  --data-urlencode 'scope=read write' \
  --data-urlencode 'state=<YOUR_SECURE_RANDOM>'
```

2. **Exchange authorization code for access token:**

```bash
curl -X POST {AUTH_BASE_URL}/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "client_id": "<YOUR_CLIENT_ID>",
    "client_secret": "<YOUR_CLIENT_SECRET>",
    "code": "<YOUR_AUTHORIZATION_CODE>",
    "redirect_uri": "https://<YOUR_APP_CALLBACK_URL>"
  }'
```

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

#### 2. 1. Create an inventory

To create an inventory that will hold your device, send the following request:

[**POST /inventory/create**](broken-reference)

```bash
{​
  "label": "Florida",
  "description": "Florida branch office"​
​}
```

**Response:**

```json
{
  "id": 12
}
```

Note the inventory ID (`12`) for the next step.

#### 2.2. Create and activate a master device

Master devices can transmit GPS data independently.

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

#### 2.3. Activate the device

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

***

### Step 3. Create an asset and assign your device

Assets represent the real-world objects you want to track, such as vehicles and equipment. Each asset belongs to an asset type that defines its structure and available custom fields.

#### 3.1. Create an asset type

First, create an asset type for your fleet. In our example, we'll use marine vessels:

```bash
curl -X POST {BASE_URL}/v0/asset_type/create?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Marine vessels",
    "category": "business",
    "settings": {
      "layout": {
        "sections": [
          {
            "label": "Vessel details",
            "fields": [
              "label",
              "registration_number",
              "captain_name",
              "vessel_year"
            ]
          }
        ]
      }
    },
    "fields": [
      {
        "type": "text",
        "label": "Registration number",
        "required": true,
        "description": "Vessel registration or hull identification number"
      },
      {
        "type": "text",
        "label": "Captain name",
        "required": false,
        "description": "Primary captain assigned to the vessel"
      },
      {
        "type": "decimal",
        "label": "Year of manufacture",
        "required": false,
        "description": "Year the vessel was manufactured"
      }
    ]
  }'
```

**Response:**

```json
{
  "id": 456
}
```

#### 3.2 Create an asset

Create a specific asset:

```bash
curl -X POST {BASE_URL}/v0/asset/create?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "type_id": 456,
    "label": "Fishing Boat Neptune",
    "fields": {
      "registration_number": {
        "type": "text",
        "value": "FL-1234-AB"
      },
      "captain_name": {
        "type": "text",
        "value": "Captain Morgan"
      },
      "vessel_year": {
        "type": "decimal",
        "value": 2021
      }
    }
  }'
```

**Response:**

```json
{
  "id": 789
}
```

#### 3.3. Assign your device to the asset

Connect your GPS device to the asset by updating the inventory item:

```bash
curl -X POST {BASE_URL}/v0/inventory_item/master/update?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "inventory_id": 12,
    "label": "Teltonika FMC130 - Vessel 001",
    "asset_id": 789
  }'
```

**Response:** `204 No Content` (Success)

### Step 4. Organize assets with asset links

Asset links help you group related assets together for better organization and management.

#### 4.1. Create an asset link

Let's create a group for delivery vehicles:

```bash
curl -X POST {BASE_URL}/v0/asset_link/create?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Fishing fleet",
    "asset_ids": [789]
  }'
```

**Response:**

```json
{
  "id": 999
}
```

#### Add more assets to the link

As you create more vehicle assets, you can add them to this group:

```bash
curl -X POST {BASE_URL}/v0/asset_link/set?orgId=<YOUR_ORG_ID> \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 999,
    "asset_id": <NEW_ASSET_ID>
  }'
```

### Verification and next steps

#### Verify your setup

Let's confirm everything is working by listing your assets:

```bash
curl -X GET "{BASE_URL}/v0/asset/list?orgId=<YOUR_ORG_ID>&q=&limit=10&offset=0&sort=label" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

You should see your "Fishing Boat Neptune" asset in the response.

{% hint style="success" %}
#### What you've accomplished

* &#x20;**Authenticated** with the Navixy Repository API
* **Activated a GPS device** that can now transmit location data
* **Created an asset type** with custom fields for marine vessel management
* **Created an asset** representing your fishing boat
* **Assigned the GPS device** to track your asset
* **Organized assets** using asset links for better management
{% endhint %}

#### Next steps

Now that you have the basics set up, you can:

* [Add more devices by creating additional inventory items](getting-started.md#id-2.3.-activate-the-device)
* [Create custom asset types for different categories of assets](getting-started.md#id-3.1.-create-an-asset-type)
* [Create more assets and assign them to devices](getting-started.md#id-3.2-create-an-asset)
* [Group assets by location, department, or function via asset links](getting-started.md#step-4.-organize-assets-with-asset-links)
