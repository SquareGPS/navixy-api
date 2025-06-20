---
stoplight-id: wup1ss2w62vmw
---

# Admin Panel authentication

The Navixy Admin Panel API provides administrative access to manage the entire Navixy platform, including users, devices, settings, and system-wide configurations. To prevent unauthorized access, Admin Panel authentication uses a simplified but secure session-based model designed specifically for administrative operations.

## Authentication method

The Admin Panel API uses **session hash authentication** as its sole authentication method. This approach is specifically designed for administrative workflows and provides:

- **Secure session duration**: 24-hour session lifespan
- **Administrative privileges**: Access to all account and device management functions
- **Simple integration**: Single authentication step for admin operations

<!-- theme: warning -->
>Admin Panel API sessions are completely separate from platform API sessions. You cannot use an admin panel session hash with the platform API, and vice versa.

## Base URLs

Admin Panel API authentication is accessible through the [`/panel/account` resource](resources/account.md).

Depending on the deployment method (regional web server or on-premise installation), here are the common endpoint paths:

- **European server**: `https://api.eu.navixy.com/v2/panel/account/auth/`
- **American server**: `https://api.us.navixy.com/v2/panel/account/auth/`
- **On-premise installations**: `https://api.your-domain.com/v2/panel/account/auth/`

## Obtaining a session hash

### For web usage

To authenticate with ServerMate, send a POST request to the `/account/auth/` endpoint with your admin panel credentials: numeric Admin Paned ID and password.

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/account/auth/" \
  -H "Content-Type: application/json" \
  -d '{"login": "your_numeric_panel_ID", "password": "your_admin_password"}'
```

**Successful response:**
```json
{
  "success": true,
  "hash": "1dc2b813769d846c2c15030884948117",
  "permissions": {
    "trackers": ["create", "read", "update"],
    "users": ["create", "read", "update", "delete"],
    "accounting": ["generate"]
  }
}
```

The `hash` value is your session token - save it securely for subsequent API calls.

### For on-premise installations

On-premise installations include default administrator credentials for initial setup:

- **Default login**: `admin`
- **Default password**: `admin`

<!-- theme: warning -->
> **Security warning**: Change default credentials immediately after installation in production environments.

```bash
curl -X POST "https://api.your-domain.com/v2/panel/account/auth/" \
  -H "Content-Type: application/json" \
  -d '{"login": "admin", "password": "admin"}'
```

**Response format is identical to the one in the web usage example.**

## Using authentication in API requests

Include your session hash in API requests using one of these methods:

#### 1. As request header (recommended)

Include the hash in the `Authorization` header:

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/user/list/" \
  -H "Authorization: NVX 1dc2b813769d846c2c15030884948117" \
  -H "Content-Type: application/json" \
  -d '{"limit": 10}'
```

#### 2. In request body 

Include the `hash` parameter in your JSON request body:

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/user/list/" \
  -H "Content-Type: application/json" \
  -d '{"hash": "1dc2b813769d846c2c15030884948117", "limit": 10}'
```

#### 3. As query parameter (testing only!)

Append the hash to the URL as a query parameter:

```bash
curl "https://api.eu.navixy.com/v2/panel/user/list/?hash=1dc2b813769d846c2c15030884948117&limit=10"
```

<!-- theme: warning -->
> **Security Warning**: Query parameter method exposes credentials in URLs, server logs, and browser history. Use only for testing, never in production.

## Session management

#### Session lifespan

Admin Panel API sessions have a **24-hour lifespan** from creation, regardless of activity. This duration accommodates longer administrative workflows and batch operations.

#### Session expiration

When your session expires, API calls will return:

```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "User not found or session ended"
  }
}
```

To resolve expired sessions, simply obtain a new hash using the `/account/auth/` endpoint.

> Unlike platform API sessions, admin panel sessions cannot be renewed. When a session expires after 24 hours, you must authenticate again to obtain a new session hash.

#### Ending sessions

For security purposes, you can explicitly terminate a session before it expires:

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/account/logout" \
  -H "Content-Type: application/json" \
  -d '{"hash": "1dc2b813769d846c2c15030884948117"}'
```

**Response:**
```json
{
  "success": true
}
```

This immediately invalidates the session hash, making it unusable for further API calls.

This is useful for applications that need to verify capabilities before attempting operations.

## Admin Panel permissions

Every Admin Panel API call requires specific permissions. The system compares your account's permissions against the required permissions for each operation.

#### Permission structure

Permissions are defined as category-operation pairs:

```json
{
  "trackers": ["create", "read", "update"],
  "users": ["create", "read", "update", "delete"],
  "accounting": ["generate"]
}
```

#### Available permission categories

- **accounting**: `generate`
- **activation_code**: `create`, `read`, `update`
- **base**: `get_dealer_info`
- **email_gateways**: `create`, `delete`, `read`, `send_email`, `update`
- **notification_settings**: `read`, `update`
- **password**: `update`
- **service_settings**: `read`, `update`
- **sms**: `create`
- **subpaas**: `create`, `delete`, `read`, `update`
- **tariffs**: `create`, `read`, `update`
- **trackers**: `corrupt`, `create`, `delete`, `global`, `read`, `report`, `update`
- **tracker_bundles**: `read`, `update`
- **transactions**: `create`, `read`, `update`
- **users**: `corrupt`, `create`, `read`, `update`, `delete`
- **user_sessions**: `create`

#### Permission denied response

When you lack required permissions:

```json
{
  "success": false,
  "status": {
    "code": 13,
    "description": "Operation not permitted"
  }
}
```

### Checking current permissions

You can verify the permissions of your current session using the `get_permissions` request:

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/account/get_permissions" \
  -H "Content-Type: application/json" \
  -d '{"hash": "1dc2b813769d846c2c15030884948117"}'
```

**Response:**
```json
{
  "success": true,
  "permissions": {
    "base": ["get_dealer_info"],
    "trackers": ["create", "read", "update", "delete"],
    "users": ["create", "read", "update", "delete"],
    "tariffs": ["create", "read", "update"]
  }
}
```

## Error handling

Understanding admin panel authentication errors helps implement proper error handling:

#### Common authentication errors

- **Code 3: Wrong hash** - Your API key or session hash is invalid or has been revoked
- **Code 4: User or API key not found or session ended** - User or session hash don't exist or expired
- **Code 7: Invalid parameters** - Inserted request parameters are incorrect

#### Error handling best practices

1. **Check the `success` field** before processing response data
2. **Implement automatic re-authentication** for expired sessions (code 4)
3. **Handle account blocking** appropriately (code 11) - may require manual intervention
4. **Log permission errors** for administrative review (code 13)
5. **Never use `description` field programmatically** - it may change

## Complete authentication example

Here's a step-by-step workflow for Admin Panel authentication on the example of a regional server.

**Step 1: Authenticate and get session hash**

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/account/auth/" \
  -H "Content-Type: application/json" \
  -d '{"login": "your_numeric_panel_ID", "password": "secure_password"}'
```

Response example: 
```json
{
  "success": true,
  "hash": "1dc2b813769d846c2c15030884948117",
  "permissions": {
    "trackers": ["create", "read", "update"],
    "users": ["create", "read", "update", "delete"],
    "accounting": ["generate"]
  }
}
```

Copy the hash value (`1dc2b813769d846c2c15030884948117` in this example) for use in subsequent requests.

**Step 2: Use the hash to authenticate further API calls**

Now you can use this hash to authenticate any Admin Panel API request. For example, let's list all user accounts existing under a certain Admin Panel:

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/user/list/" \
  -H "Content-Type: application/json" \
  -d '{"hash": "1dc2b813769d846c2c15030884948117"}'
```

> Remember: Your session hash remains valid for 24 hours and can be reused for all admin panel operations during this time.

## Technical service accounts

For secure credential sharing and automated integrations, Navixy supports technical service accounts with limited administrative privileges.

#### Creating technical accounts

Technical accounts must be created by the Navixy support team:

1. **Contact Navixy support** with your request
2. **Provide the email address** for the technical account
3. **Receive login credentials** from the support team
4. **Use these credentials** for API authentication

#### Technical account permissions

Technical accounts have a predefined set of permissions that differ from full administrative accounts:

| Permission type | Technical accounts | Full admin accounts |
|:----------------|:-------------------|:--------------------|
| User management | Can add and modify users | Can add, modify, and delete users |
| Tracker management | Can add, clone, and modify trackers | Can add, clone, modify, and remove trackers |
| Data plan management | Can change tracker data plans | Can change tracker data plans |
| Air console access | Can analyze incoming data | Can analyze incoming data and send commands |
| Plan management | Cannot add, change, or delete plans | Can manage all plans |
| Platform settings | Cannot modify platform settings | Can modify platform settings |

#### Using technical accounts

Authentication with technical accounts follows the same process:

```bash
curl -X POST "https://api.eu.navixy.com/v2/panel/account/auth/" \
  -H "Content-Type: application/json" \
  -d '{"login": "your_numeric_panel_ID", "password": "technical_password"}'
```

## Authentication best practices

Follow these guidelines for secure and effective admin panel authentication:

#### Security practices

1. **Change default credentials immediately** on on-premise installations
2. **Use HTTPS exclusively** for all admin panel API communications
3. **Store session hashes securely**, never in client-side code or logs
4. **Implement session expiration handling** in your applications
5. **Use technical accounts** for automated processes instead of personal credentials
7. **Rotate credentials regularly** especially for technical accounts
8. **Explicitly logout sessions** when no longer needed for enhanced security

#### Integration practices

1. **Implement proper error handling** for all authentication scenarios
2. **Cache session hashes** to avoid unnecessary authentication calls
3. **Plan for 24-hour session lifecycle** in your application architecture
5. **Test authentication flows** in development environments first
6. **Document which technical accounts** are used by which integrations
8. **Support JSON format** for all API requests consistently
