# Technical reference

### API environments

The Navixy IoT Logic API is available on multiple regional platforms to optimize performance and comply with data residency requirements.

#### Base URLs

| Region   | Base URL                    | Data Location         |
| -------- | --------------------------- | --------------------- |
| Europe   | `https://api.eu.navixy.com` | European data centers |
| Americas | `https://api.us.navixy.com` | US-based data centers |

#### Environment selection

Choose the environment that:

1. Is geographically closest to your operations (to minimize latency)
2. Complies with your data residency requirements
3. Matches your existing Navixy platform subscription

Both environments offer identical API functionality, but may differ in:

* Response times based on your geographic location
* Data storage location (important for compliance with regulations like GDPR)
* Maintenance windows and update schedules

### Methods

The API follows the **OpenAPI** **standard** with full CRUD for each object type:

| Object          | Main Methods                                    |
| --------------- | ----------------------------------------------- |
| entity          | create, read, update, delete, list              |
| entity\_type    | create, read, update, delete, list              |
| entity\_group   | create, read, update, delete, list, set, remove |
| inventory       | create, read, update, delete, list              |
| inventory\_item | create, read, update, list, activate, pair      |

### Call patterns

#### Request format

**GET requests**

* Use for **read-only operations** that do not change data.
* Pass parameters in the **URL query string**.

**Example:**

```
GET https://api.example.com/v1/data/search?objectId=123&type=location
```

**POST requests**

Use `POST` requests with a **JSON body** when you need to:

* Create, update, or delete data
* Fetch data with complex filter parameters
* Perform bulk operations
* Send parameters as a **JSON object** in the request body with `Content-Type: application/json`.

**Example:**

```json
{
  "id": 123,
  "data": {
    "key": "value"
  }
}
```

#### Response format

All API responses follow a consistent JSON format:

* **HTTP status codes** indicate success or failure
* **Success responses** include the requested data or confirmation
* **Error responses** provide detailed error information in the JSON body
* **List responses** include pagination metadata when applicable

**Example of a paginated response:**

```json
{
  "data": [
    {
      "key1": "value",
      "key2": "value"
    }
  ],
  "has_more": true
}
```

### Errors

We use conventional HTTP status codes to indicate the success or failure of a request.

* **2xx** – Request was successful.
* **4xx** – Request failed due to client error (e.g., validation error, missing parameter).
* **5xx** – An internal server error occurred (these are rare and typically indicate an issue on our side).

#### Error response format

When a request fails (typically with a 4xx or 5xx status), the response body contains a structured error object that helps both users and developers understand and resolve the issue.

```json
{
  "code": "invalid_argument",
  "message": "One or more parameters are invalid.",
  "correlation_id": "1a2b3c4d-5678-90ab-cdef-1234567890ab",
  "errors": [
    {
      "parameter": "email",
      "code": "invalid_format",
      "message": "The email address format is invalid."
    },
    {
      "parameter": "password",
      "code": "too_short",
      "message": "Password must be at least 8 characters long"
    }
  ]
}
```

### Pagination, search, filtering, and sorting

List endpoints in this API support fetching paginated data with flexible filtering and sorting options. You can use both GET and POST methods depending on the complexity of the query.

#### Pagination basics

All list endpoints return results in a paginated format:

```json
{
  "data": [ ... ],
  "has_more": true
}
```

* **data** – array of objects. A list of items returned for the current page, based on the provided query parameters.
* **has\_more** – boolean. Indicates whether more items are available beyond the current page. When `false`, the current result set is the final one, and no additional data can be retrieved using the same query parameters.

#### Query parameters

| **Name** | **Type** | **Nullable** | **Important** | **Description**                                                                                                                           |
| -------- | -------- | ------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| q        | string   | yes          | yes           | A search query string                                                                                                                     |
| limit    | int      | yes          | no            | Maximum number of items to return (default: 100, max: 1000).                                                                              |
| offset   | int      | yes          | no            | The index of the first item to return (default: 0).                                                                                       |
| sort     | string   | yes          | no            | Sort expression. Supports one or more fields, optionally prefixed with `-` to indicate descending order. For example, `title,-created_at` |

#### Full-text search

To perform a basic full-text search (available for `list` endpoints), use the `q` parameter.

**GET:**

```bash
curl -X GET {BASE_URL}/org/list \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  --data-urlencode 'q=solutions inc'
```

**POST:**

```bash
curl -X POST {BASE_URL}/org/list \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H 'Content-Type: application/json' \
  -d '{"q": "solutions inc"}'
```

#### Advanced filtering

For complex queries beyond basic search, use the `conditions` parameter in POST requests. The filtering system supports logical operators (AND, OR, NOT) and field-level comparisons (equality, range, set membership, etc.) for complex expressions.

**Basic filtering structure**

Filters are defined as condition objects with a `type` field that determines the comparison operation:

```
{
  "conditions": [
    {
      "type": "eq",
      "field": "status",
      "value": "active"
    }
  ]
}
```

### Versioning

We follow industry-standard semantic versioning principles to ensure clear, predictable upgrades and stable integrations.

#### Versioning strategy

To make versioning transparent and intuitive, we include the version directly in the request URL:

```
{base_url}/v{major}/{resource}/{operation}
```

For example:

```
https://api.example.com/v1/org/list
```

The **major version number** is incremented only when we introduce breaking changes, such as:

* Changing the structure or format of responses.
* Renaming or removing existing endpoints or their fields.
* Modifying validation rules in a way that would reject previously valid requests.

#### Version support and deprecation

We guarantee each major API version will be supported for a minimum of X months from the date of release.

When a new major version is released, the following applies:

* The old version remains fully functional during a grace period.
* A deprecation notice is issued at least Y days in advance of shutting down a previous version.
* You will receive detailed migration guidelines, including examples and mappings of old vs. new formats.

We encourage all users to track version deprecations proactively and implement version upgrades on time.

#### Documentation and migration

Every maintained API version is fully documented, with:

* A version-specific reference.
* A changelog outlining all updates.
* Migration instructions to help you move from an older version to the latest one with minimal friction.

To ease migration:

* We recommend using sandbox environments to validate new versions.
* You can run multiple versions in parallel if needed during transitional periods.

For changelogs and migration guides, refer to the API Changelog.

### API automation tools

In the modern development environment, speed and precision matter. Automating your API interactions saves time, reduces errors, and helps you bring value to users faster. Whether you're building full-stack applications, setting up system integrations, or testing individual endpoints, this section introduces key tools that simplify and accelerate your work with the Metadata Repository API.

We support both developers and non-developers by providing industry-standard tools and resources for interacting with the API. More integrations and tools will be added over time to support growing use cases and automation scenarios.

#### OpenAPI definition

Explore the full structure of Navixy Repository API using the OpenAPI definition.

* Use it to generate client SDKs in various programming languages.
* Import the definition into OpenAPI-based API documentation & testing tools.
* Perfect for documentation readers who want to explore and test endpoints without manual setup, if the built-in documentation tools are insufficient for your specific needs

You can download the OpenAPI specification here.

#### Postman

Postman is a powerful API client used for testing and exploring APIs with ease.

* We provide a ready-to-use Postman Collection for the Metadata Repository API.
* Just import it, enter your credentials, and start making requests – no setup required.
* Great for quickly learning the API and trying different operations in a sandbox environment. Should you encounter limitations with the documentation's sandbox capabilities, we recommend exploring advanced Postman features or dedicated development environments for more complex testing scenarios.

Run in Postman

#### Zapier

Zapier is a no-code automation platform that connects Metadata Repository with thousands of third-party apps.

* Set up workflows (called "Zaps") in which triggers in the Metadata Repository automatically result in actions in other systems.
* Ideal for business users and analysts who need automation without writing code. Example: Automatically log tracker activity to a spreadsheet or notify your team in Slack when a specific event occurs.
