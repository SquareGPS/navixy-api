---
description: >-
  HTTP/HTTPS and MQTT connection parameters, regional endpoints, and code
  examples for sending NGP messages.
---

# Transport layer

NGP supports both **HTTP/HTTPS** and **MQTT** as transport options. Choose based on your device capabilities and infrastructure requirements.

## HTTP/HTTPS

NGP supports **HTTP/HTTPS versions 1.1 and 2.0**. This is the simplest option for devices that already support HTTP.

**Request format:**

| Parameter     | Value              |
| ------------- | ------------------ |
| Method        | `POST`             |
| Content-Type  | `application/json` |
| Body encoding | UTF-8              |
| Body          | Single JSON object |

**Regional endpoints:**

| Region | Endpoint                             |
| ------ | ------------------------------------ |
| EU     | `http://tracker.navixy.com:47642`    |
| US     | `http://tracker.us.navixy.com:47642` |

**Response codes:**

| Code  | Meaning                                                                           |
| ----- | --------------------------------------------------------------------------------- |
| `200` | Message received successfully.                                                    |
| `400` | Invalid request. Malformed JSON or field values are outside allowed ranges.       |
| `403` | Unknown device identifier. Verify that `device_id` is registered on the platform. |
| `500` | Unexpected server error. Contact the platform's technical support.                |

**Example: sending a message via curl:**

```bash
curl --location 'tracker.navixy.com:47642' \
--header 'Content-Type: application/json' \
--data '{
    "message_time": "2024-10-10T06:00:11Z",
    "device_id": "1112312212",
    "location": {
        "latitude": 34.15929687705282,
        "longitude": -118.4614133834839,
        "satellites": 3
    },
    "battery_level": 68
}'
```

## MQTT

NGP uses MQTT as a lightweight, reliable transport over TCP.

**Supported MQTT versions:** 5.0 and 3.1.1

**Quality of Service levels:**

| QoS | Behaviour                                                            |
| --- | -------------------------------------------------------------------- |
| 0   | At most once. Suitable where occasional message loss is acceptable.  |
| 1   | At least once. Use when reliable delivery is required.               |

All message bodies must be UTF-8 encoded JSON containing a single JSON object per message. Responses to messages are not supported. The platform strictly validates incoming messages and silently discards those with invalid JSON or out-of-range attribute values.

**Connection parameters:**

| Parameter | Value                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Host (EU) | `mqtt.eu.navixy.com`                                                    |
| Host (US) | `mqtt.us.navixy.com`                                                    |
| Port      | `1883` (plain TCP) / `8883` (TLS)                                       |
| Username  | `ngp_device`                                                            |
| Password  | Device password configured in the Navixy platform                       |
| Topic     | `ngp/{device_id}` (replace `{device_id}` with your device's identifier) |

**Example: sending a message via Mosquitto client:**

```bash
mosquitto_pub \
  -h mqtt.eu.navixy.com \
  -p 1883 \
  -u ngp_device \
  -P <your_device_password> \
  -t "ngp/1112312212" \
  -m '{
    "message_time": "2024-10-10T06:00:11Z",
    "device_id": "1112312212",
    "location": {
        "latitude": 34.15929687705282,
        "longitude": -118.4614133834839,
        "satellites": 3
    },
    "battery_level": 68
}'
```

Continue reading to learn about [Data types and encoding standards](data-types-and-encoding-standards.md) in Navixy Generic Protocol.
