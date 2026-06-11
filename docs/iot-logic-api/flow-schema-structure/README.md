---
stoplight-id: cr4zu3e4l42hj
---

# Flow object structure

1. **Basic Properties**:
   * `id`: Unique identifier for the flow
   * `title`: Name of the flow for display purposes
   * `enabled`: Toggle to activate or deactivate the flow
2. **Nodes**: The building blocks of the flow, each with a specific purpose:
   * **Data Source Nodes** (`type: "data_source"`): Define the input sources for data
   * **Initiate Attributes Nodes** (`type: "initiate_attributes"`): Process and transform data
   * **Output Endpoint Nodes** (`type: "output_endpoint"`): Define where processed data is sent
3. **Edges**: Connect nodes together to define the flow of data

## Node Types in Detail

### Data Source Node

* Acts as the entry point for data from devices
* Contains a list of source device IDs to monitor
* Example use: Collect data from vehicle trackers, temperature sensors, etc.

### Initiate Attributes Node

* Processes data by creating or modifying attributes
* Uses expressions to transform raw data into meaningful metrics
* Can reference other attributes in calculations
* Example use: Convert analog signals to meaningful metrics (fuel level, temperature)

### Output Endpoint Node

* Defines the destination for processed data
* Two main types:
  * **Navixy Output**: Sends data to the Navixy platform
  * **MQTT Client Output**: Sends data to external MQTT brokers

## Examples

[Flow object model](general-json-schema-example.md#flow-object-model)

[Configured schema example](general-json-schema-example.md#example-schema)

## Customization for Manufacturers

This template can be customized for different manufacturers by:

1. **Adjusting attribute calculations** to match the specific sensor outputs and units of a particular manufacturer's devices
2. **Adding manufacturer-specific attributes** that may be unique to certain vehicles or devices
3. **Configuring appropriate endpoints** based on the manufacturer's preferred data handling systems

For example, if adapting for a specific truck manufacturer, you might:

* Adjust fuel calculations based on their specific tank sizes and sensor characteristics
* Add attributes for manufacturer-specific features (e.g., DEF levels, regeneration status)
* Configure outputs to integrate with their fleet management systems
