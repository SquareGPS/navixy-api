# Navixy IoT Logic Expression Language

## Introduction

The Navixy IoT Logic Expression Language enables real-time transformation of raw IoT device data into meaningful business metrics. Built on JEXL (Java Expression Language) with IoT-specific enhancements, it provides a familiar syntax for developers while offering specialized capabilities for telematics and sensor data processing.

The language operates within IoT Logic flows, where expressions power two critical functions: data transformation in Initiate Attribute nodes and conditional routing in Logic nodes. This separation allows you to build sophisticated data processing pipelines through composable, single-purpose expressions rather than complex scripts.

**Core capabilities:**

* **Mathematical transformations:** Unit conversions, statistical calculations, and formula-based metrics using standard arithmetic and mathematical operations.
* **Binary data processing:** Decode complex device protocols, parse BLE sensor data, extract bit-level status flags, and handle proprietary binary formats through specialized utility functions.
* **Conditional logic:** Route data based on real-time conditions using comparison operators, boolean logic, and pattern matching to create intelligent decision points.

For implementation details about using expressions within IoT Logic flows, see the [IoT Logic documentation](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic).

## Where expressions are used

Expressions operate in two specific contexts within IoT Logic flows:

#### Initiate Attribute nodes

Calculate new **attributes** from incoming device data. Each attribute definition includes an expression that transforms raw parameters into derived metrics. The calculated attributes become available to all downstream nodes in the flow.

Example attribute calculation that converts a temperature value from Celsius to Fahrenheit:

```javascript
temperature * 1.8 + 32
```

#### Logic nodes

Evaluate boolean conditions to determine data flow paths. The `condition` field contains an expression that evaluates to true or false, routing data through THEN or ELSE connections based on the result.

Example condition that creates a conditional branch for high-speed, low-fuel scenarios:

```javascript
speed > 80 && fuel_level < 20
```

For comprehensive details on node configuration and flow architecture, see the [Node documentation](../../technical-details/nodes.md).

## Core concepts

### Attribute access

Within IoT Logic, Navixy Expression Language allows calculations on actual data attributes that come from data sources. There are two options to access the readings:

* **Current values:** Reference attributes by name directly in expressions. This provides clean, readable syntax for accessing real-time device data. [Short syntax](expression-syntax-reference.md#short-syntax-current-values) is supported in this case (e.g., `temperature` = `value('temperature', 0, 'all')`).
* **Historical values:** Access previous readings using the `value()` function with parameters for historical depth and validation mode. The system maintains the last 12 values per attribute for trend analysis and change detection. [Full syntax](expression-syntax-reference.md#full-syntax-historical-and-advanced) is needed.

{% hint style="warning" %}
Attribute names in expressions must exactly match device-transmitted names (case-sensitive). Mismatched names prevent calculation execution.
{% endhint %}

For complete syntax details, see [Expression syntax reference](expression-syntax-reference.md).

### Data types and null handling

The expression language handles numbers, strings, booleans, hexadecimal literals, and null values. Null represents missing or undefined data from devices.

{% hint style="info" %}
**Null propagation:** Null values propagate through expressions without causing errors, maintaining processing continuity even with unreliable device connectivity. Calculations involving null return null rather than failing.
{% endhint %}

For detailed type behavior and null handling rules, see [Data types](expression-syntax-reference.md#data-types-and-type-handling) in the Expression syntax reference.

### Binary data processing

Many IoT devices transmit data in compact binary formats to minimize bandwidth and power consumption. The expression language provides specialized `util:` namespace functions to decode these formats without external processing.

<details>

<summary><strong>Common use cases</strong></summary>

#### Extract sensor values from HEX-encoded data

```javascript
util:hexToLong(ble_additional_data_1, 1, 0) / 1000.0
```

**What this expression does:** Extracts a 2-byte sensor value from BLE additional data in HEX format, reverses byte order for little-endian reading, and converts from millivolts to volts.

**Calculation example:** Device sends `ble_additional_data = "FF7A2B"` → Result: `2.991` (volts)

**Formula breakdown:**

* `util:hexToLong` - Converts HEX string bytes to a Long integer
* `ble_additional_data` - Attribute containing HEX string from the device
* `1` - First byte position (starting from left, 0-indexed)
* `0` - Last byte position (reading right-to-left for little-endian byte swap)
* `/ 1000.0` - Division operation to convert millivolts to volts

#### Check device status flags at bit level

```javascript
util:checkBit(status_flags, 2)
```

**What this expression does:** Checks if a specific bit is set in a status byte, useful for reading boolean device states like door open/closed, engine on/off, or sensor active/inactive.

**Calculation example:** Device sends `status_flags = 4` (binary `0100`) → Result: `true` (bit 2 is set)

**Formula breakdown:**

* `util:checkBit` - Returns `true` if the specified bit is set (equals 1), `false` otherwise
* `status_flags` - Attribute containing the device status byte
* `2` - Bit position to check (0 = rightmost/LSB, counting from right to left)

#### Decode BCD-encoded identifiers

```javascript
util:fromBcd(raw_device_id)
```

**What this expression does:** Converts a Binary Coded Decimal (BCD) number to standard decimal format, commonly used for device IDs and timestamps in industrial protocols.

**Calculation example:** Device sends `raw_device_id = 0x1234` → Result: `1234`

**Formula breakdown:**

* `util:fromBcd` - Converts BCD-encoded number to decimal Long integer
* `raw_device_id` - Attribute containing the BCD-encoded identifier from the device

{% hint style="info" %}
In BCD format, each decimal digit (0-9) is represented by 4 bits. For example, BCD `0x1234` represents decimal `1234`.
{% endhint %}

#### Handle signed values from binary protocols

```javascript
util:signed(util:hexToLong(sensor_data, 0, 1), 2)
```

**What this expression does:** Extracts a 2-byte value from HEX data and interprets it as a signed integer, necessary when devices transmit negative values (like temperatures below zero) as unsigned integers.

**Calculation example:** Device sends `sensor_data = "FFFF"` → Result: `-1`

**Formula breakdown:**

* `util:signed` - Converts unsigned number to signed by interpreting the most significant bit as a sign bit
* `util:hexToLong(sensor_data, 0, 1)` - Inner function that extracts bytes 0-1 from HEX string
  * `sensor_data` - Attribute containing HEX string from the device
  * `0` - First byte position
  * `1` - Last byte position (big-endian byte order)
* `2` - Number of bytes to interpret as signed (2 bytes = 16-bit signed integer, range: -32768 to 32767)

</details>

The `util:` namespace includes functions for bit manipulation, byte extraction, format conversion (BCD, IEEE 754), HEX string operations, and string padding.

For complete function reference, see [Bit-level operations](expression-syntax-reference.md#bit-level-operations) in the Expression syntax reference.

## Built-in functions

### Time functions

Access timing information for data processing and latency analysis:

* **Device generation time:** `genTime(attribute, index, validation)` returns when the device generated the value. Useful for detecting sensor delays or calculating time between events.
* **Server reception time:** `srvTime(attribute, index, validation)` returns when the server received the value. Useful for transmission latency analysis.

{% hint style="info" %}
Current timestamp `now()` is default for both `genTime` and `srvTime` and returns time in Unix milliseconds. Use for calculating data age or setting default timestamps.
{% endhint %}

For function signatures and usage examples, see [Core functions](expression-syntax-reference.md#core-functions) in the Expression syntax reference.

### Data access functions

The `value()` function accesses historical attribute values with control over validation mode (include or exclude null values) and historical depth (up to 12 previous readings).

For parameter details and historical data access patterns, see [Full syntax](expression-syntax-reference.md#full-syntax) in the Expression syntax reference.

### Bit-level functions

The `util:` namespace provides functions for binary data processing, bit manipulation, format conversion, and string operations. These handle device protocols and binary data formats common in telematics applications.

{% hint style="danger" %}
When using `'valid'` validation mode, the function returns the last non-null value, which can belong to another (earlier) reading. Consider it carefully when building expressions.
{% endhint %}

For complete utility function catalog, see [Bit-level operations](expression-syntax-reference.md#bit-level-operations) in the Expression syntax reference.

## Operators and expressions

The expression language is based on [JEXL ](https://commons.apache.org/proper/commons-jexl/reference/syntax.html)and supports standard arithmetic, comparison, logical, and conditional operators. Expressions can combine multiple operations with explicit precedence control using parentheses.

Example combining operators:

```javascript
(speed > 80 && fuel_level < 20) || maintenance_due
```

The language supports method chaining for function composition:

```javascript
util:signed(util:hexToLong("FF7A"), 2)
```

For complete operator reference and precedence rules, see [Operators](expression-syntax-reference.md#operators) in the Expression syntax reference.

#### Common expression patterns

Unit conversion:

```javascript
temperature * 1.8 + 32
```

Threshold detection:

```javascript
speed > 80 && fuel_level < 20
```

Trend analysis:

```javascript
temperature - value('temperature', 1, 'all') > 5
```

Status flag extraction:

```javascript
util:checkBit(device_status, 3)
```

## Integration and results

Expression results integrate with the Navixy platform through multiple channels:

[**Data Stream Analyzer**](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/data-stream-analyzer)**:** Monitor expression results in real-time. View calculated attributes, historical values, and expression evaluation results for debugging and validation.

[**Custom sensors**](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/initiate-attribute-node/displaying-new-calculated-attributes-on-the-navixy-platform)**:** Convert calculated attributes into dashboard-visible sensors when connected to Navixy output endpoints.

[**Alert rules**](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/events-and-notifications)**:** Use boolean expression results from Logic nodes to trigger notifications based on real-time conditions.

[**Third-party integration**](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/output-endpoint-node)**:** Forward transformed data to external systems via MQTT output endpoints.

### Additional resources

* [Expression syntax reference](expression-syntax-reference.md)
* [Complete IoT Logic API reference](../../resources/api-reference/)
* [IoT Logic user guide](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic)
