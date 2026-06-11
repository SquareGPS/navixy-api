---
description: Build IoT Logic flows from the JSON schema template. Includes the full flow object model with property names, types, and constraints for API-based creation.
stoplight-id: h8mpgrged6ndl
---

# JSON-schema template

Here's an example of a JSON structure describing a complete flow.

### Flow object model

{% openapi-schemas spec="iot-logic" schemas="Flow" grouped="true" %}
[OpenAPI iot-logic](https://raw.githubusercontent.com/SquareGPS/iot-logic-api/refs/heads/main/docs/resources/api-reference/IoT_Logic.json)
{% endopenapi-schemas %}

## Example schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Navixy IoT Logic Flow",
  "description": "A schema for defining IoT data flows in the Navixy platform",
  "type": "object",
  "required": [
    "id",
    "title",
    "enabled",
    "nodes",
    "edges"
  ],
  "properties": {
    "id": {
      "type": "integer",
      "description": "Unique identifier for the flow",
      "examples": [543]
    },
    "title": {
      "type": "string",
      "description": "Name of the flow",
      "examples": ["Temperature Monitoring Flow", "Vehicle Tracking Flow"]
    },
    "enabled": {
      "type": "boolean",
      "description": "Whether the flow is active or not",
      "default": true
    },
    "nodes": {
      "type": "array",
      "description": "Collection of nodes in the flowchart",
      "items": {
        "type": "object",
        "oneOf": [
          { "$ref": "#/definitions/dataSourceNode" },
          { "$ref": "#/definitions/initiateAttributesNode" },
          { "$ref": "#/definitions/outputEndpointNode" }
        ]
      }
    },
    "edges": {
      "type": "array",
      "description": "Connections between nodes in the flowchart",
      "items": {
        "$ref": "#/definitions/edge"
      }
    }
  },
  "definitions": {
    "edge": {
      "type": "object",
      "description": "Represents a connection between two nodes",
      "required": ["from", "to"],
      "properties": {
        "from": {
          "type": "integer",
          "description": "ID of the source node",
          "examples": [1]
        },
        "to": {
          "type": "integer",
          "description": "ID of the destination node",
          "examples": [2]
        }
      }
    },
    "nodeView": {
      "type": "object",
      "description": "Visual properties of a node in the flowchart UI",
      "properties": {
        "position": {
          "type": "object",
          "description": "Position of the node's top-left corner in the UI",
          "properties": {
            "x": {
              "type": "integer",
              "description": "X coordinate (horizontal position)",
              "examples": [25]
            },
            "y": {
              "type": "integer",
              "description": "Y coordinate (vertical position)",
              "examples": [25]
            }
          },
          "required": ["x", "y"]
        }
      }
    },
    "dataSourceNode": {
      "type": "object",
      "description": "Input endpoint node that defines the source of data for the flow",
      "required": ["id", "type", "title", "enabled", "data"],
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the node within the flow",
          "examples": [1]
        },
        "type": {
          "type": "string",
          "description": "Type of node, must be 'data_source' for input endpoints",
          "enum": ["data_source"]
        },
        "title": {
          "type": "string",
          "description": "Name of the node",
          "examples": ["GPS Tracker Input", "Sensor Data Input"]
        },
        "enabled": {
          "type": "boolean",
          "description": "Whether the node is active within the flow",
          "default": true
        },
        "data": {
          "type": "object",
          "description": "Configuration data specific to this node type",
          "required": ["source_ids"],
          "properties": {
            "source_ids": {
              "type": "array",
              "description": "Collection of source device IDs to receive data from",
              "items": {
                "type": "integer",
                "description": "ID of a source device",
                "examples": [123458]
              }
            }
          }
        },
        "view": {
          "$ref": "#/definitions/nodeView"
        }
      }
    },
    "initiateAttributesNode": {
      "type": "object",
      "description": "Node that creates or modifies data attributes in the flow",
      "required": ["id", "type", "title", "data"],
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the node within the flow",
          "examples": [2]
        },
        "type": {
          "type": "string",
          "description": "Type of node, must be 'initiate_attributes' for attribute manipulation nodes",
          "enum": ["initiate_attributes"]
        },
        "title": {
          "type": "string",
          "description": "Name of the node",
          "examples": ["Calculate Fuel Consumption", "Convert Temperature Units"]
        },
        "data": {
          "type": "object",
          "description": "Configuration data specific to this node type",
          "required": ["items"],
          "properties": {
            "items": {
              "type": "array",
              "description": "Collection of attribute definitions/transformations",
              "items": {
                "type": "object",
                "required": ["name", "value"],
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the attribute to create or modify",
                    "examples": ["fuel_tank_2", "temperature_celsius"]
                  },
                  "value": {
                    "type": "string",
                    "description": "Expression that defines the attribute value, can reference other attributes or functions",
                    "examples": ["(analog_1 + 100)/2", "temp_f * 5/9 - 32"]
                  },
                  "generation_time": {
                    "type": "string",
                    "description": "Expression for when the data was generated, often uses functions like now()",
                    "examples": ["now()", "timestamp"]
                  },
                  "server_time": {
                    "type": "string",
                    "description": "Expression for when the data was received by the server, often uses functions like now()",
                    "examples": ["now()"]
                  }
                }
              }
            }
          }
        },
        "view": {
          "$ref": "#/definitions/nodeView"
        }
      }
    },
    "outputEndpointNode": {
      "type": "object",
      "description": "Terminating node that defines where the processed data will be sent",
      "required": ["id", "type", "title", "enabled", "data"],
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the node within the flow",
          "examples": [3]
        },
        "type": {
          "type": "string",
          "description": "Type of node, must be 'output_endpoint' for data output nodes",
          "enum": ["output_endpoint"]
        },
        "title": {
          "type": "string",
          "description": "Name of the node",
          "examples": ["Navixy Output", "MQTT Broker Output"]
        },
        "enabled": {
          "type": "boolean",
          "description": "Whether the node is active within the flow",
          "default": true
        },
        "data": {
          "type": "object",
          "description": "Configuration data specific to this node type",
          "oneOf": [
            {
              "$ref": "#/definitions/outputEndpointDataNavixy"
            },
            {
              "$ref": "#/definitions/outputEndpointDataMqtt"
            }
          ]
        },
        "view": {
          "$ref": "#/definitions/nodeView"
        }
      }
    },
    "outputEndpointDataNavixy": {
      "type": "object",
      "description": "Configuration for sending data to the Navixy platform",
      "required": ["output_endpoint_type"],
      "properties": {
        "output_endpoint_type": {
          "type": "string",
          "description": "Type of output endpoint, must be 'output_default' for Navixy platform",
          "enum": ["output_default"]
        }
      }
    },
    "outputEndpointDataMqtt": {
      "type": "object",
      "description": "Configuration for sending data to an MQTT broker",
      "required": ["output_endpoint_type", "output_endpoint_id"],
      "properties": {
        "output_endpoint_type": {
          "type": "string",
          "description": "Type of output endpoint, must be 'output_mqtt_client' for MQTT brokers",
          "enum": ["output_mqtt_client"]
        },
        "output_endpoint_id": {
          "type": "integer",
          "description": "ID of the predefined MQTT endpoint configuration",
          "examples": [44551]
        }
      }
    }
  }
}
```

## Example flow

The example template shows a flow that:

1. Collects data from vehicle tracking devices
2. Processes the data in two parallel paths:
   * Calculating fuel-related metrics (level, consumption, range)
   * Calculating engine metrics (temperature, load, maintenance status)
3. Sends the processed data to:
   * The Navixy platform for tracking and visualization
   * An external MQTT broker for integration with other systems

```json
{
  "id": 1001,
  "title": "Vehicle Telematics Processing Flow",
  "enabled": true,
  "nodes": [
    {
      "id": 1,
      "type": "data_source",
      "title": "Vehicle Tracker Input",
      "enabled": true,
      "data": {
        "source_ids": [
          123458,
          123459,
          123460
        ]
      },
      "view": {
        "position": {
          "x": 50,
          "y": 50
        }
      }
    },
    {
      "id": 2,
      "type": "initiate_attributes",
      "title": "Calculate Fuel Metrics",
      "data": {
        "items": [
          {
            "name": "fuel_level_percent",
            "value": "(analog_1 / 1024) * 100",
            "generation_time": "now()",
            "server_time": "now()"
          },
          {
            "name": "fuel_consumption_rate",
            "value": "analog_2 * 0.25",
            "generation_time": "now()",
            "server_time": "now()"
          },
          {
            "name": "estimated_range_km",
            "value": "fuel_level_percent * 5",
            "generation_time": "now()",
            "server_time": "now()"
          }
        ]
      },
      "view": {
        "position": {
          "x": 250,
          "y": 50
        }
      }
    },
    {
      "id": 3,
      "type": "initiate_attributes",
      "title": "Calculate Engine Metrics",
      "data": {
        "items": [
          {
            "name": "engine_temp_celsius",
            "value": "analog_3 * 0.5 - 40",
            "generation_time": "now()",
            "server_time": "now()"
          },
          {
            "name": "engine_load",
            "value": "(analog_4 / 1024) * 100",
            "generation_time": "now()",
            "server_time": "now()"
          },
          {
            "name": "maintenance_due",
            "value": "mileage > 10000",
            "generation_time": "now()",
            "server_time": "now()"
          }
        ]
      },
      "view": {
        "position": {
          "x": 250,
          "y": 200
        }
      }
    },
    {
      "id": 4,
      "type": "output_endpoint",
      "title": "Navixy Platform Output",
      "enabled": true,
      "data": {
        "output_endpoint_type": "output_default"
      },
      "view": {
        "position": {
          "x": 450,
          "y": 125
        }
      }
    },
    {
      "id": 5,
      "type": "output_endpoint",
      "title": "MQTT Broker Output",
      "enabled": true,
      "data": {
        "output_endpoint_type": "output_mqtt_client",
        "output_endpoint_id": 44551
      },
      "view": {
        "position": {
          "x": 450,
          "y": 250
        }
      }
    }
  ],
  "edges": [
    {
      "from": 1,
      "to": 2
    },
    {
      "from": 1,
      "to": 3
    },
    {
      "from": 2,
      "to": 4
    },
    {
      "from": 3,
      "to": 4
    },
    {
      "from": 3,
      "to": 5
    }
  ]
}
```
