---
description: Send device telemetry to Navixy using NGP, an open JSON telematics protocol. Start with the quick-start, then see transport, encoding, and message format.
---

# Navixy Generic Protocol

The Navixy Generic Protocol (NGP) is an open protocol freely available for manufacturers of GPS trackers and IoT devices. It defines a compact, JSON-based message format for transmitting telematics data (location, sensor readings, events, and custom attributes) over HTTP/HTTPS or MQTT.

## Protocol purpose

NGP is designed to be the single, standardized data format between devices and the Navixy platform. Its straightforward message structure makes it easy to implement on new hardware and extend with device-specific fields, while the platform handles decoding, validation, and routing.

Typical senders include: GPS trackers, IoT sensors, telematics terminals, and gateways that aggregate data from multiple sub-devices.

![NGP-purpose.jpg](<../../.gitbook/assets/NGP-purpose (1).jpg>)

## Protocol versions

| Date | Version | Status | Notes |
|------|---------|--------|-------|
| 2024-09-03 | **1.0** | Stable | Base version |
| 2024-10-25 | **1.1a** | On demand | Structured custom attributes with metadata — requires separate arrangement with Navixy |
| 2026-03-12 | **1.2** | Current | Adds `source_type` and `precision` to the `location` object — **use for all new integrations** |

## Quick start

{% stepper %}
{% step %}
## Choose your transport

NGP supports HTTP/HTTPS and MQTT. See [Transport layer](transport-layer.md) for endpoints, connection parameters, and working code examples for both.
{% endstep %}

{% step %}
## Build your message

Every NGP message is a JSON object requiring two mandatory fields: `device_id` and `message_time`. See [Message structure and attributes](message-structure-and-attributes.md) for the complete field reference and minimum valid message examples.
{% endstep %}

{% step %}
## Declare your version

Include `"version": "1.2"` in your message to enable all current fields. Omitting the field defaults to 1.0 behavior. The availability column in the attribute table shows which fields require a version declaration.
{% endstep %}
{% endstepper %}

## Reference

- [Transport layer](transport-layer.md) — HTTP/HTTPS and MQTT connection parameters, endpoints, and code examples
- [Data types and encoding standards](data-types-and-encoding-standards.md) — JSON type mapping, timestamps, and binary encoding
- [Message structure and attributes](message-structure-and-attributes.md) — complete attribute reference with availability tags
- [Predefined event identifiers](predefined-event-identifiers.md) — standard `event_id` values for common device events
- [NGP Mapper skill](ngp-mapper-skill.md) — AI-assisted field mapping from any device format to NGP

## Implementing NGP

Mapping an existing device or data source to NGP typically means working through the field reference, identifying transforms for unit conversions and enum remappings, and handling edge cases such as LBS-only positioning or bitmask extraction. The [NGP Mapper skill](ngp-mapper-skill.md) handles this process automatically.

You provide a sample message from your source system (a raw JSON export, a proprietary tracker payload, a Wialon record, or any structured format) and the skill produces a complete field mapping table with every required transform, a ready-to-send NGP JSON example built from your real values, exact transport parameters for HTTP or MQTT in your target region, and notes on fields with no direct NGP equivalent and how to handle them.

The result is a self-contained specification you can hand to a developer or use to implement the converter yourself, without having to read through the entire reference first.

{% hint style="info" %}
The NGP Mapper skill runs inside your AI assistant and requires no additional tools or accounts. [Download the skill file and see how to use it](ngp-mapper-skill.md).
{% endhint %}
