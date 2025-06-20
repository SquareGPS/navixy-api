---
title: Getting Started
description: Getting started with Navixy API
---

# Navixy Developer Documentation

[Navixy](https://navixy.com) is a comprehensive GPS/Vehicle telematics platform developed by [SquareGPS](https://squaregps.com). This documentation provides detailed information on integrating third-party solutions with the Navixy platform, including API and technical documentation tailored for developers and partners.

## How to use this documentation

The documentation is organized into sections, each addressing a specific aspect of the Navixy platform:

* [**General**](./): Introduction, Navixy API Sandbox, No-code automation, and contribution guidelines.
* [**Navixy platform API**](https://app.gitbook.com/o/YVLWhgAwCZPoU5vlRsCs/s/wsyU95CoLDheydH0OQPY/): API calls for user interface functionalities like raw device data, tracking, reports, tasks, and much more.
* [**Admin Panel API**](https://app.gitbook.com/s/yXecjDA8Sz658QNg2Ynx/getting-started#introduction): API calls for admin panel functionalities such as platform config and user management.

### Navigation

Navigate the documentation sections using the left sidebar. Use the internal menu on the right for quick navigation within the page.

You can access the related GitHub repository directly via link on the left sidebar.

### Documentation structure

The documentation includes two types of files: Documents, and API calls. Documents are divided into semantic parts, starting with an introduction that summarizes the content.

### API call descriptions

**Resources** sections represent API reference for the related functionality and have a common structure:

* **Introduction** - General information and purpose of the API call.
* **Object structure** - Describes the object structure used in the calls (optional).
* **API Actions** - Base API call and associated actions, including:
  * **Action description** - Purpose of the API action.
  * **Requirements** - Necessary permissions (optional).
  * **Parameters table** - Lists parameters for the API call with descriptions and data types.
  * **Examples** - API call examples with parameters. Includes a copy button for easy use.
  * **Response** - Example of a successful server response with field descriptions.
  * **Errors** - Specific errors related to the API action, plus a general error list.

## API Limits

To ensure system stability for all customers, the platform limits API requests to 50 requests per second per user and per IP address (for applications serving multiple users). These limits are applied based on user session hash and API keys.

## Navixy API Sandbox

Navixy provides a powerful Postman collection, the Navixy API Sandbox, for working with API documentation, exploring, and testing API queries using real or demo data. This collection offers a familiar environment for many developers and simplifies the process of building customized solutions. For detailed information on using Postman with Navixy, please refer to the [Postman Guide](general/api-tools/postman.md).

## Get involved

Help improve the [Navixy developer documentation](general/contribute/) or assist with [language translations](general/contribute/translation.md). Your contributions make the Navixy platform even better for the community.
