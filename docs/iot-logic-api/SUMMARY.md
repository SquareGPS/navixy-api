# Table of contents

* [Navixy IoT Logic API](README.md)
* [Authentication](authentication.md)
* [Technical reference](technical-details/README.md)
  * [Nodes](technical-details/nodes.md)
* [Flow object structure](flow-schema-structure/README.md)
  * [JSON-schema template](flow-schema-structure/general-json-schema-example.md)
* [Guides](navixy-iot-guide/README.md)
  * [Sending device data to an external system](navixy-iot-guide/scenario1.md)
  * [Managing your flows and endpoints](navixy-iot-guide/scenario2.md)
  * [Advanced configurations](navixy-iot-guide/advanced-configurations.md)
  * [Adding calculated attributes to Navixy UI](navixy-iot-guide/adding-calculated-attributes-to-navixy-ui.md)
  * [AI flow generation guide](navixy-iot-guide/ai-flow-generation-guide.md)
* [Websocket access to Data Stream Analyzer](Websocket-access-for-DSA.md)

## RESOURCES

* [API reference](resources/api-reference/README.md)
  * ```yaml
    props:
      models: true
    type: builtin:openapi
    dependencies:
      spec:
        ref:
          kind: openapi
          spec: iot-logic
    ```

## TECHNOLOGIES

* [Navixy Generic Protocol](Technologies/navixy-generic-protocol/navixy-generic-protocol.md)
  * [Transport layer](Technologies/navixy-generic-protocol/transport-layer.md)
  * [Data types and encoding standards](Technologies/navixy-generic-protocol/data-types-and-encoding-standards.md)
  * [Message structure and attributes](Technologies/navixy-generic-protocol/message-structure-and-attributes.md)
  * [Predefined event identifiers](Technologies/navixy-generic-protocol/predefined-event-identifiers.md)
  * [NGP Mapper skill](Technologies/navixy-generic-protocol/ngp-mapper-skill.md)
* [Navixy IoT Logic Expression Language](technologies/navixy-iot-logic-expression-language/README.md)
  * [Expression syntax reference](technologies/navixy-iot-logic-expression-language/expression-syntax-reference.md)
