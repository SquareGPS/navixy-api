---
description: >-
  JSON type mapping, timestamp formatting, binary encoding, and value
  constraints used in NGP messages.
---

# Data types and encoding standards

Navixy Generic Protocol messages use standard JSON with a defined set of field types. This page specifies how each type maps to JSON, how timestamps must be formatted, and how binary payloads should be encoded before transmission. Knowing these constraints helps you construct valid messages and avoid silent discard due to type mismatches or encoding errors.

## Data types

| **Type**  | **JSON** | **Description**                                    | **Examples**                                               | **Limitations**                                        |
| --------- | -------- | -------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------ |
| Integer   | Number   | Whole numeric values, no decimals                  | Bitmasks, counters, impulse counts, passenger counts, RPM  | Signed or unsigned, 1–8 bytes                          |
| Float     | Number   | Numeric values with decimal precision              | Coordinates, speed, altitude, mileage, voltage             | IEEE 754 signed float, up to 8 bytes                   |
| String    | String   | UTF-8 encoded text                                 | Driver name, registration plate, driver ID                 | Up to 10 KB                                            |
| Boolean   | Boolean  | `true` or `false`                                  | Ignition state, door state, presence of movement           | `true` or `false` only                                 |
| Timestamp | String   | ISO 8601 date-time in UTC                          | Message time, GNSS fix time                                | Must be valid ISO 8601 UTC                             |
| Blob      | String   | Binary data, Base64-encoded                        | Photos, raw sensor data, BLE payloads, audio               | Up to 1 MB encoded                                     |
| Mixed     | Any      | Value of any JSON type                             | Custom attributes where type varies by attribute           | Follows the type constraints of the specific attribute |
| Array     | Array    | Ordered list of objects of the same structure      | `mobile_cells`, `wifi_points`                              | No size limit                                          |
| Object    | Object   | Named set of attributes grouped under a single key | `location`, individual mobile cell, individual Wi-Fi point | No size limit                                          |

## Timestamps

All timestamps must use **ISO 8601 UTC** format.

```
"message_time": "2024-09-02T23:59:59Z"
```

The trailing `Z` indicates UTC. Timezone offsets are not supported. Always convert to UTC before sending.

## Binary data

For raw payloads such as sensor data, tachograph logs, images, or audio, binary content must be **Base64-encoded** and sent as a string value.

```json
{
  "my_sensor_data": "SGVsbG8gd29ybGQh",
  "tachograph_log": "U29tZSB0YWNoZW9nIGxvZw==",
  "photo": "/9j/4AAQSkZJRgABAQEAYABgAAD...",
  "audio": "UklGRjIAAABXRUJQVlA4WAoAAAAQAAAA..."
}
```

{% hint style="warning" %}
NGP is not optimized for large binary payloads. The 1 MB limit per encoded blob applies per attribute. Avoid sending multiple large blobs in a single message.
{% endhint %}

Continue reading to learn about [Message structure and attributes](message-structure-and-attributes.md) in Navixy Generic Protocol.
