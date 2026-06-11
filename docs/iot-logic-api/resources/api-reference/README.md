# API reference

The IoT Logic API allows you to programmatically manage data flows and endpoints for processing IoT device data. Create flows, configure nodes, and route data between different systems.

{% hint style="info" %}
**BETA Version**\
This API is in early access. Functionality may change in future updates.
{% endhint %}

## Overview

The API is organized around two main resource types:

**Flows** - Manage data processing workflows. Learn more about flow concepts and structure in our [technical overview](../../technical-details/#flow-architecture).

**Endpoints (Nodes)** - Configure input and output endpoints for data routing. Understand different node types and their configuration in the [core concepts documentation](../../technical-details/#node-reference).

{% hint style="info" %}
Looking for node schemas and examples? See [Nodes](../../technical-details/nodes.md) (includes the [Webhook node](../../technical-details/nodes.md#webhook-node-webhook) for HTTP integrations).
{% endhint %}

For a complete walkthrough of creating your first flow, see our [step-by-step tutorial](../../#quick-start-for-iot-logic-api).

### Authentication

All requests require authentication using an API key with `NVX:` prefix in the Authorization header. See the [authentication guide](../../authentication.md) for detailed setup instructions.

### Base URLs

* **European platform**: `https://api.eu.navixy.com/v2`
* **American platform**: `https://api.us.navixy.com/v2`

### OpenAPI spec <a href="#openapi-spec" id="openapi-spec"></a>

Under this section you can find a complete and interactive API reference generated from an up-to-date OpenAPI specification. There you can discover endpoint paths, parameters, object schemas (models), and test API calls right from the documentation.\
You can view the original OpenAPI spec used to generate our API docs [here](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json).

### Quick endpoint reference

The Navixy IoT Logic API provides the following endpoints for managing flows and endpoints:

### Flow management endpoints

<table><thead><tr><th width="229.72723388671875">Endpoint</th><th width="94.18182373046875">Method</th><th width="211.54541015625">Description</th><th>Key Parameters</th></tr></thead><tbody><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/flow#post-iot-logic-flow-create">/iot/logic/flow/create</a></td><td>POST</td><td>Create a new flow</td><td><code>flow</code> object with title, nodes, edges</td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/flow#get-iot-logic-flow-read">/iot/logic/flow/read</a></td><td>GET</td><td>Read an existing flow</td><td><code>flow_id</code></td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/flow#post-iot-logic-flow-update">/iot/logic/flow/update</a></td><td>POST</td><td>Update an existing flow</td><td><code>flow</code> object with id, title, nodes, edges</td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/flow#post-iot-logic-flow-delete">/iot/logic/flow/delete</a></td><td>POST</td><td>Delete a flow</td><td><code>flow_id</code></td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/flow#get-iot-logic-flow-list">/iot/logic/flow/list</a></td><td>GET</td><td>List all flows</td><td>none</td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/flow#get-iot-logic-flow-export">/iot/logic/flow/export</a></td><td>GET</td><td>Export an existing flow</td><td><code>flow_id</code></td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/flow#get-iot-logic-flow-sources-mapping-list">/iot/logic/flow/sources/mapping/list</a></td><td>GET</td><td>List all device-to-flow assignments</td><td>none</td></tr></tbody></table>

### Node management endpoints

<table><thead><tr><th width="229.6363525390625">Endpoint</th><th width="94.27276611328125">Method</th><th width="211.0909423828125">Description</th><th>Key Parameters</th></tr></thead><tbody><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/node#post-iot-logic-flow-endpoint-create">/iot/logic/flow/endpoint/create</a></td><td>POST</td><td>Create a new endpoint</td><td><code>endpoint</code> object with type, title, properties</td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/node#post-iot-logic-flow-endpoint-read">/iot/logic/flow/endpoint/read</a></td><td>POST</td><td>Read an existing endpoint</td><td><code>endpoint_id</code></td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/node#post-iot-logic-flow-endpoint-update">/iot/logic/flow/endpoint/update</a></td><td>POST</td><td>Update an existing endpoint</td><td><code>endpoint</code> object with id and updated fields</td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/node#post-iot-logic-flow-endpoint-delete">/iot/logic/flow/endpoint/delete</a></td><td>POST</td><td>Delete an endpoint</td><td><code>endpoint_id</code></td></tr><tr><td><a href="https://www.navixy.com/docs/iot-logic-api/resources/api-reference/node#post-iot-logic-flow-endpoint-list">/iot/logic/flow/endpoint/list</a></td><td>POST</td><td>List all endpoints</td><td>none</td></tr></tbody></table>

## Support

For questions and support, contact [support@navixy.com](mailto:support@navixy.com).
