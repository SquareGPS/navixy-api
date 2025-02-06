---
title: User applications
description: Information about embedding custom applications to the UI on user's own
---

# User applications

The User Applications feature enables you to embed third-party applications into the platform entirely on your own, without requiring assistance from developers or support. You can integrate external services directly into the interface or open them in a new tab, using URL parameters, user authentication, and secure session management for seamless interaction.

With full control over configuration, you can customize your workspace to fit your needs without technical expertise. For instructions on how to configure such applications from the platform's UI, see [User applications section in Navixy's User documentation](https://docs.navixy.com/user-guide/user-applications). 

However, if you need to automate application management and integrate external tools programmatically, you can access User applications functionality through API. It has dedicated endpoints to:
- List existing applications in the account
- Create new user applications
- Update existing applications
- Delete existing applications 
- Enable/Disable - control application availability 

For detailed reference see [User application resources](../../backend-api/resources/commons/user/applications.md). 

## How to create a new application

To create a new user application using the user/application/update API, send a POST request with the required parameters.

### Example

 === "cURL"

    ```shell
    curl -X POST "https://api.navixy.com/v2/user/application/create" \
            -H "Content-Type: application/json" \
            -d '{
                "hash": "your_api_hash",
                "application": {
                "id": null,
                "name": "New Application",
                "url": "https://example.com",
                "icon": "https://example.com/icon.png",
                "is_enabled": true
            }
    }'
    ```

### Parameters explained

- `hash` (string, required) – Your API authentication hash.
- `application` (object, required):
  - `id` (integer, optional) – Set to null to create a new application.
  - `name` (string, required) – Name of the application.
  - `url` (string, required) – The URL where the application is hosted.
  - `icon` (string, optional) – URL of the application's icon.
  - `is_enabled` (boolean, required) – Set to true to enable the application right after creation.

### Response 

```json
{
  "success": true,
  "id": 12345
}
```
This confirms that the application has been successfully created with the ID `12345`.