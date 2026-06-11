---
stoplight-id: n6jl7wc7cska8
---

# Technical reference

API environments

The Navixy IoT Logic API is available on multiple regional platforms to optimize performance and comply with data residency requirements.

### Base URLs

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

## Authentication

Authentication for the Navixy IoT Logic API uses API keys or user session hashes. For detailed information about authentication methods, obtaining API keys, and best practices, please refer to the [Authentication](../authentication.md) documentation.

## API rate limiting

To ensure system stability for all customers, the platform limits API requests to 50 requests per second per user and per IP address (for applications serving multiple users). These limits are applied based on user session hash and API keys.

{% hint style="info" %}
When a rate limit is exceeded, the API returns a 429 Too Many Requests status code with a specific error message
{% endhint %}

To avoid rate limiting issues:

1. Implement exponential backoff for retries
2. Batch operations where possible
3. Cache frequently accessed data
4. Distribute non-urgent requests over time

## Request formats

### HTTP methods

| Method | Usage                                  | Examples                                        |
| ------ | -------------------------------------- | ----------------------------------------------- |
| `GET`  | Retrieving information                 | Flow listing, flow details                      |
| `POST` | Creating, updating, deleting resources | Creating, updating and deleting flows and nodes |

{% hint style="warning" %}
Some read operations use POST requests with a request body instead of GET with query parameters. Always check the endpoint documentation for the correct method.
{% endhint %}

### Content type

All requests and responses use JSON format:

```
Content-Type: application/json
```

All request bodies must be valid JSON objects. The API will return a 400 Bad Request response for malformed JSON.

### Date and time formats

All timestamps in the API use ISO 8601 format in UTC timezone:

```
YYYY-MM-DDThh:mm:ssZ
```

Example: `2025-04-08T14:30:00Z` represents April 8, 2025, at 2:30 PM UTC.

## Response structure

All API responses follow a consistent JSON format.

### Success responses

Success responses always include a `success: true` field and may include additional data:

```json
{
  "success": true,
  "value": {
    // Requested data or resource
  }
}
```

For list operations:

```json
{
  "success": true,
  "list": [
    // Array of requested items
  ]
}
```

### Error responses

Error responses include `success: false` and a `status` object with details, for example:

```json
{
  "success": false,
  "status": {
    "code": 292,
    "description": "IoT Flow Invalid"
  },
  "errors": [
    {
      "node_ids": [2],
      "message": "Node #2 is missing, but has a link from edge"
    },
    {
      "node_ids": [1],
      "message": "Data source node \"New Data Source\" (#1) must be at the start of flow"
    }
  ]
}
```

**Response Fields:**

* `success`: Always `false` for error responses
* `status.code`: Internal error code (see tables below)
* `status.description`: Human-readable error category
* `errors`: Array of detailed validation errors (present only for HTTP 400 responses)
  * `node_ids`: Array of affected node IDs (optional)
  * `message`: Human-readable error description

### Common error codes

<table><thead><tr><th width="132.45458984375">HTTP status</th><th width="132.2728271484375">Internal code</th><th>Description</th><th>Context</th></tr></thead><tbody><tr><td>400</td><td>292</td><td>IoT Flow Invalid</td><td>Flow validation failed</td></tr><tr><td>400</td><td>293</td><td>IoT Endpoint Invalid</td><td>Endpoint validation failed</td></tr><tr><td>400</td><td>294</td><td>IoT Node Invalid</td><td>Node validation failed</td></tr><tr><td>401</td><td>14</td><td>Invalid session</td><td>Authentication required or session expired</td></tr><tr><td>403</td><td>7</td><td>Access denied</td><td>Insufficient permissions</td></tr><tr><td>404</td><td>201</td><td>Not found</td><td>Requested resource doesn't exist</td></tr><tr><td>500</td><td>1</td><td>Database error</td><td>Internal server error</td></tr></tbody></table>

### Validation errors (HTTP 400)

All validation errors return HTTP status 400 and include a detailed `errors` array. The following table lists all possible validation error messages:

<table><thead><tr><th width="173.5455322265625">Category</th><th>Error Message</th><th>Description</th></tr></thead><tbody><tr><td><strong>Flow Structure</strong></td><td><code>Node #${node_id} is missing, but has a link from edge</code></td><td>Referenced node doesn't exist in the flow</td></tr><tr><td></td><td><code>Data source node "${title}" (#${node_id}) must be at the start of flow</code></td><td>Data source node has incoming connections</td></tr><tr><td></td><td><code>Output endpoint node #${node_id} must be at the end of flow</code></td><td>Output endpoint node has outgoing connections</td></tr><tr><td></td><td><code>A flow starting from data source node #${node_id} must have an output endpoint node</code></td><td>Flow path or <strong>one of its branches</strong> doesn't terminate with an output endpoint, usually when one of the Logic node branches isn't connected to an Output Endpoint</td></tr><tr><td><strong>Graph topology</strong></td><td><code>The flow's graph cannot contain cycles</code></td><td>Circular references detected in flow</td></tr><tr><td></td><td><code>The flow's graph can't contain self-loops</code></td><td>Node connects to itself</td></tr><tr><td></td><td><code>Node #${node_id} is involved in the message processing twice</code></td><td>Node is reachable through multiple paths</td></tr><tr><td><strong>Connections</strong></td><td><code>Nodes #${node_id1} and #${node_id2} have a duplicate connection</code></td><td>Multiple edges exist between the same nodes</td></tr><tr><td></td><td><code>Logic node #${node_id} does not contain at least one relationship</code></td><td>Logic node has no outgoing connections</td></tr><tr><td></td><td><code>Logic node #${node_id} contains invalid link types, only Then or Else is allowed</code></td><td>Logic node has non-conditional connection types</td></tr><tr><td><strong>Node content</strong></td><td><code>Node #${node_id} has incorrect content</code></td><td>Node configuration data is invalid</td></tr><tr><td></td><td><code>Duplicate Switch Output #${output_number} action in Nodes: #${node_id1}, #${node_id2}</code></td><td>Same output number controlled by multiple action nodes</td></tr><tr><td><strong>Resource limits</strong></td><td><code>The total number of attributes in a flow must not exceed ${max_amount}</code></td><td>Flow contains too many attributes (limit: 200)</td></tr><tr><td></td><td><code>The node identifier must be unique within the flow: non-unique ID is #${node_id}</code></td><td>Multiple nodes have the same ID</td></tr><tr><td><strong>Output nodes</strong></td><td><code>Nodes #${node_id1} and #${node_id2} are duplicated as output nodes</code></td><td>Multiple output endpoints in the same processing subgraph</td></tr><tr><td><strong>JEXL expressions</strong></td><td><code>The formula is invalid: [1:${column} parsing error in '${text}']</code></td><td>Expression has syntax error (missing parentheses, incomplete operator, etc.</td></tr><tr><td></td><td><code>The formula is invalid: [1:${column} JEXL error : no such function namespace ${namespace}]</code></td><td>Function namespace does not exist, only <code>util:</code> namespace is supported</td></tr><tr><td></td><td><code>The formula is invalid: [1:${column} unsolvable function/method '${method}(${args})']</code></td><td>Method does not exist in the specified namespace</td></tr><tr><td></td><td><code>The formula is invalid: [1:${column} JEXL error : ${function}]</code></td><td>Expression is syntactically valid but fails during execution (invalid parameters, type mismatches, etc.)</td></tr></tbody></table>

{% hint style="info" %}
Variables in error messages (e.g., `${node_id}`, `${title}`) are replaced with actual values in API responses.
{% endhint %}

## Flow architecture

Flows in Navixy IoT Logic follow a directed graph architecture with specific requirements and constraints.

### Basic requirements

| Requirement          | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| Input nodes          | Every flow must have at least one data source node              |
| Output nodes         | Every flow must have at least one output endpoint node          |
| Node IDs             | Each node has a unique ID within its flow (not globally unique) |
| Connections          | Edges define directional data flow between nodes                |
| Multiple connections | Nodes can have multiple incoming and outgoing connections       |
| No cycles            | Circular references are not supported                           |

### Flow validation

When creating or updating flows, the API performs several validation checks:

1. Node IDs must be unique within a flow
2. Each edge must reference valid node IDs
3. The flow must be acyclic (no circular references)
4. All nodes must be reachable from data sources
5. All required fields must be present for each node type

### Flow states

| State            | Description   | Effect                               |
| ---------------- | ------------- | ------------------------------------ |
| `enabled: true`  | Active flow   | The flow processes data in real-time |
| `enabled: false` | Inactive flow | Data is not processed by this flow   |

Individual nodes can also be enabled or disabled, allowing for partial flow activation.

### Node positioning

The `view` property in nodes is used for visual representation in UI tools:

```json
"view": {
  "position": {
    "x": 150,
    "y": 50
  }
}
```

While optional for API functionality, including this data helps maintain visual layout when editing flows later.

## Node reference

Nodes are actual building bricks for your IoT Logic data flows. Each node has its destinctive purpose and capabilities. Now the following nodes are available:

* [Data Source node](nodes.md#data-source-node-data_source) - defines where data comes from.
* [Initiate Attribute node](nodes.md#initiate-attribute-node-initiate_attribute) - allows custom calculations to enrich ar standardize data.
* [Logic node](nodes.md#logic-node-logic) - allows validating logical conditins and routing data based on the outcome.
* [Webhook node](nodes.md#webhook-node-webhook) - sends data to external systems via HTTP POST requests.
* [Device action node](nodes.md#device-action-node-action) - enables the automation of sending commands to devices based on the context.
* [Output endpoint node](nodes.md#output-endpoint-node-output_endpoint) - Defines the destination of data running trough the flow.

For detailed Node reference with object schemas and parameters, see [Nodes](nodes.md).

## API rendpoint reference

See OpenAPI specification in [API reference](../resources/api-reference/).

## Best practices

<details>

<summary>Practical tips for IoT Logic implementations</summary>

**Flow design**

1. **Plan your flow design** before implementation
   * Sketch your flow structure including all nodes and connections
   * Identify device sources and required data transformations
   * Determine appropriate output endpoints
2. **Create endpoints first** before referencing them in flows
   * MQTT endpoints must exist before they can be referenced
   * Test endpoint connectivity independently before adding to flows
3. **Use descriptive titles** for both flows and nodes
   * Clear naming helps with maintenance and troubleshooting
   * Include purpose or function in the title
4. **Test incrementally** by adding one component at a time
   * Start with a minimal viable flow and expand
   * Test each node's functionality before adding complexity
5. **Monitor data flow** after implementation
   * Verify data is flowing as expected
   * Check for proper attribute transformation

**Data processing**

6. **Keep expressions simple** where possible
   * Complex expressions are harder to debug and maintain
   * Consider using multiple nodes for complex transformations
7. **Use consistent naming conventions** for attributes
   * Follow a pattern like `category_attribute_unit`
   * For example: `engine_temperature_celsius`
8. **Document complex expressions** with clear comments
   * Keep documentation for non-obvious calculations
   * Include business logic explanations
9. **Consider data volume** when creating flows
   * High-frequency data may impact performance
   * Multiple outputs multiply processing requirements

**Security**

10. **Secure your MQTT connections** with SSL when possible
    * Enable `use_ssl: true` for production environments
    * Use secure ports (typically 8883 for MQTT over SSL)
11. **Rotate credentials** periodically for MQTT endpoints
    * Update credentials every 90 days or after personnel changes
    * Use strong, unique passwords for each endpoint
12. **Use unique client IDs** for each MQTT endpoint
    * Avoid connection conflicts by using distinctive IDs
    * Consider including account ID and purpose in the client ID
13. **Restrict topic access** on your MQTT broker
    * Limit permissions to only necessary topics
    * Use topic structures that enable precise access control

**Maintenance**

14. **Back up your flow configurations**
    * Store JSON responses from successful flow creation
    * Document flow purposes and interconnections
15. **Version your flows** with sequential titles
    * Include version numbers in flow titles
    * Maintain a changelog of modifications
16. **Regularly review active flows**
    * Audit flows to ensure they're still needed
    * Remove or disable unused flows to reduce overhead
17. **Keep a library of common patterns**
    * Reuse successful flow patterns across applications
    * Standardize approaches to similar problems

**Data security considerations**

When working with the Navixy IoT Logic API:

1. **API Keys**: Protect your API keys as they provide full access to your account
2. **MQTT Credentials**: Use strong passwords for MQTT authentication
3. **SSL**: Enable SSL (`use_ssl: true`) for MQTT connections whenever possible
4. **Data Privacy**: Be mindful of what device data you transmit to external systems
5. **Endpoint Security**: Regularly audit your endpoints and disable unused ones

</details>

## Troubleshooting

| Issue                            | Possible Solution                                        |
| -------------------------------- | -------------------------------------------------------- |
| Flow not processing data         | Check that both flow and all nodes have `enabled: true`  |
| MQTT connection failing          | Verify credentials, domain, port, and SSL settings       |
| Data transformations not working | Test expressions in isolation to identify issues         |
| Missing data in output           | Ensure all required attributes are being processed       |
| API errors                       | Double-check JSON syntax and required fields             |
| Flow validation errors           | Ensure node IDs are unique and edges connect valid nodes |
| Unexpected data format           | Verify the calculation expressions in processing nodes   |
| Missing fields in response       | Check if you have all required permissions               |
