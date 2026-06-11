# Expression syntax reference

This reference documents the complete syntax of the Navixy IoT Logic Expression Language, including literals, operators, functions, and data types. For conceptual information about how expressions work within IoT Logic, see the [Expression language overview](./).

## Basic syntax elements

The expression language uses JEXL (Java Expression Language) as its foundation, with IoT-specific enhancements for device data processing.

### Literals

| Literal Type            | Syntax                                                | Example                                 |
| ----------------------- | ----------------------------------------------------- | --------------------------------------- |
| Integer                 | Digits 0-9                                            | `42`                                    |
| Float                   | Digits with decimal point, optional `f` or `F` suffix | `3.14`, `42.0f`                         |
| Long                    | Digits with `l` or `L` suffix                         | `42L`                                   |
| Double                  | Digits with decimal point and `d` or `D` suffix       | `42.0d`                                 |
| Hexadecimal             | `0x` or `0X` prefix, then hex digits                  | `0xFF`, `0x1A2B`                        |
| Octal                   | `0` prefix, then octal digits                         | `010`                                   |
| Scientific notation     | Standard scientific notation with `e` or `E`          | `1.5e-10`                               |
| String (double quotes)  | Text enclosed in double quotes                        | `"Hello world"`                         |
| String (single quotes)  | Text enclosed in single quotes                        | `'Hello world'`                         |
| String escape sequences | Backslash escape character                            | `"Line 1\nLine 2"`, `"Quote: \"text\""` |
| Boolean                 | Keywords `true` or `false`                            | `true`, `false`                         |
| Null                    | Keyword `null`                                        | `null`                                  |

#### Identifiers and attribute names

Attribute names must exactly match names from device telemetry. To make sure you use correct names, you can:

* Use the [Autofill attribute names](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/flow-management/initiate-attribute-node/managing-attributes#autofill-attribute-names) option
* Lookup attribute names in [Data Stream Analyzer](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/iot-logic/data-stream-analyzer)

## Attribute access

### Short syntax (current values)

Direct attribute references provide the simplest way to access current device data in expressions. This syntax omits the `value()` function, using implicit default parameters for clean, readable formulas.

**Use for:** Simple calculations with current data

**Syntax:** `attribute_name`

**How it works:** Short syntax is a convenient shorthand that automatically uses `value()` function with default parameters:

* `temperature` is equivalent to `value('temperature', 0, 'all')`
* Default index: `0` (current value)
* Default validation: `'all'` (includes null values)

**Examples:**

| Expression                  | Purpose            |
| --------------------------- | ------------------ |
| `temperature * 1.8 + 32`    | Unit conversion    |
| `speed > 80`                | Threshold check    |
| `fuel_level + reserve_tank` | Combine attributes |

### Full syntax (historical and advanced)

The explicit `value()` function unlocks historical data access and precise control over null handling. This syntax is essential for trend analysis, change detection, and any calculation requiring data from previous readings.

**Use for:** Historical data access, trend analysis, null handling control

**Function:** `value(attribute_name, index, validation)`

**How it works:** Full syntax explicitly defines all parameters of the `value()` function, enabling access to historical data and control over null handling.

| Parameter        | Values               | Description                                 |
| ---------------- | -------------------- | ------------------------------------------- |
| `attribute_name` | String               | Attribute name from device                  |
| `index`          | 0-12                 | 0=current, 1=previous, 12=oldest            |
| `validation`     | `'all'` \| `'valid'` | `'all'`=include nulls, `'valid'`=skip nulls |

#### **Parameter behavior explained:**

Given history: `[25.5, null, 24.8, null, 23.2]` (index 0 to 4)

<table><thead><tr><th>Expression</th><th width="87.18182373046875">Index</th><th width="118.6363525390625">Validation</th><th width="91.81817626953125">Result</th><th>Explanation</th></tr></thead><tbody><tr><td><code>value('temp', 1, 'all')</code></td><td>1</td><td>Include nulls</td><td><code>null</code></td><td>Returns value at exact index 1, which is null</td></tr><tr><td><code>value('temp', 1, 'valid')</code></td><td>1</td><td>Skip nulls</td><td><code>24.8</code></td><td>Skips null at index 1, returns first valid value</td></tr><tr><td><code>value('temp', 2, 'all')</code></td><td>2</td><td>Include nulls</td><td><code>24.8</code></td><td>Returns value at exact index 2</td></tr><tr><td><code>value('temp', 2, 'valid')</code></td><td>2</td><td>Skip nulls</td><td><code>23.2</code></td><td>Skips nulls at indices 1 and 3, returns second valid value</td></tr></tbody></table>

#### **When to use each validation mode:**

* `'all'` - For time-based analysis where null indicates missing data at specific time.
* `'valid'` - For trend analysis where you need actual values regardless of gaps. \
  **Important:** Returns the **last non-null value**, which can belong to another (earlier) reading. Consider it carefully when building expressions.

#### **Formula examples:**

{% hint style="info" %}
Note that the examples in the table below showcase also a mix of short and full syntaxes used in the same formulas.
{% endhint %}

<table><thead><tr><th width="134.45458984375">Use case</th><th width="327.72723388671875">Formula</th><th>Calculation</th></tr></thead><tbody><tr><td>Detect temperature change</td><td><code>temperature - value('temperature', 1, 'all')</code></td><td>Difference between current and previous reading, null if previous missing</td></tr><tr><td>Calculate acceleration</td><td><code>speed - value('speed', 1, 'valid')</code></td><td>Difference between current and last valid reading, ignoring gaps</td></tr><tr><td>Detect gradual trends</td><td><code>(temp - value('temp', 2, 'valid')) / 2</code></td><td>Average change per reading over last 2 valid readings</td></tr><tr><td>Sustained speeding alert</td><td><code>speed > 80 &#x26;&#x26; value('speed', 1, 'valid') > 80</code></td><td>True if current AND previous valid reading both exceed 80</td></tr><tr><td>Smooth sensor fluctuations</td><td><code>(value('pressure', 0, 'valid') + value('pressure', 1, 'valid') + value('pressure', 2, 'valid')) / 3</code></td><td>Average of 3 most recent valid pressure readings</td></tr></tbody></table>

## Operators

### Arithmetic operators

| Operator | Operation           | Example             |
| -------- | ------------------- | ------------------- |
| `+`      | Addition            | `temperature + 10`  |
| `-`      | Subtraction         | `fuel_level - 5`    |
| `*`      | Multiplication      | `temperature * 1.8` |
| `/`      | Division            | `distance / time`   |
| `%`      | Modulus (remainder) | `value % 100`       |

### Comparison operators

| Operator | Comparison            | Example            |
| -------- | --------------------- | ------------------ |
| `==`     | Equal                 | `speed == 80`      |
| `!=`     | Not equal             | `status != 0`      |
| `<`      | Less than             | `temperature < 0`  |
| `<=`     | Less than or equal    | `fuel_level <= 10` |
| `>`      | Greater than          | `speed > 80`       |
| `>=`     | Greater than or equal | `voltage >= 12.0`  |

### Logical operators

| Operator | Alternative | Operation   | Example                      |
| -------- | ----------- | ----------- | ---------------------------- |
| `&&`     | `and`       | Logical AND | `speed > 80 && engine_on`    |
| `\|\|`   | `or`        | Logical OR  | `temp < 0 \|\| pressure_low` |
| `!`      | `not`       | Logical NOT | `!door_closed`               |

### Pattern matching operators

<table><thead><tr><th width="138.54547119140625">Operator</th><th>Description</th></tr></thead><tbody><tr><td><code>=~</code></td><td>Checks if the value of the left operand is in the set of the right operand. For strings, checks for regex pattern match</td></tr><tr><td><code>!~</code></td><td>Checks if the value of the left operand is not in the set of the right operand. For strings, checks for regex pattern mismatch</td></tr><tr><td><code>=^</code></td><td>Checks that the left string operand starts with the right string operand</td></tr><tr><td><code>!^</code></td><td>Checks that the left string operand doesn't start with the right string operand</td></tr><tr><td><code>=$</code></td><td>Checks that the left string operand ends with the right string operand</td></tr><tr><td><code>!$</code></td><td>Checks that the left string operand doesn't end with the right string operand</td></tr></tbody></table>

#### Ternary conditional

**Syntax:** `condition ? value_if_true : value_if_false`

**Example:** `speed > 80 ? "Speeding" : "Normal"`

### Operator precedence

Operators are evaluated in order from highest to lowest precedence:

| Precedence  | Operators                            | Description                       |
| ----------- | ------------------------------------ | --------------------------------- |
| 1 (highest) | `( )`                                | Parentheses                       |
| 2           | `!`, `not`, `-` (unary), `+` (unary) | Unary operators                   |
| 3           | `*`, `/`, `%`                        | Multiplication, division, modulus |
| 4           | `+`, `-`                             | Addition, subtraction             |
| 5           | `<`, `<=`, `>`, `>=`                 | Comparison                        |
| 6           | `==`, `!=`                           | Equality                          |
| 7           | `&&`, `and`                          | Logical AND                       |
| 8           | `\|\|`, `or`                         | Logical OR                        |
| 9 (lowest)  | `? :`                                | Ternary conditional               |

{% hint style="info" %}
Use parentheses to override precedence or clarify complex expressions.
{% endhint %}

## Core functions

### Time and data access functions

| Function                                     | Parameters                                                                                                                                                              | Description                                                                           |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `value(attribute_name, index, validation)`   | <p><code>attribute_name</code> (String)</p><p><code>index</code> (Integer, 0-12)</p><p><code>validation</code> (String: <code>'all'</code> or <code>'valid'</code>)</p> | Attribute value at specified historical position                                      |
| `genTime(attribute_name, index, validation)` | <p><code>attribute_name</code> (String</p><p><code>index</code> (Integer, 0-12)</p><p><code>validation</code> (String: <code>'all'</code> or <code>'valid'</code>)</p>  | Device-side generation timestamp (milliseconds) for attribute value. Default: `now()` |
| `srvTime(attribute_name, index, validation)` | <p><code>attribute_name</code> (String</p><p><code>index</code> (Integer, 0-12</p><p><code>validation</code> (String: <code>'all'</code> or <code>'valid'</code>)</p>   | Server-side reception timestamp (milliseconds) for attribute value. Default: `now()`  |

**Usage examples:**

<table><thead><tr><th width="268.54541015625">Use case</th><th>Expression</th></tr></thead><tbody><tr><td>Default timestamp (current time)</td><td><code>"server_time": "now()"</code> or <code>"generation_time": "now()"</code></td></tr><tr><td>Data age</td><td><code>now() - genTime('temperature', 0, 'all')</code></td></tr><tr><td>Transmission delay</td><td><code>srvTime('temperature', 0, 'all') - genTime('temperature', 0, 'all')</code></td></tr><tr><td>Time offset</td><td><code>genTime('temperature', 0, 'valid') + 120000</code></td></tr></tbody></table>

{% hint style="info" %}
For calculated attributes in IoT Logic flows, if `genTime` and `srvTime` are not explicitly specified, both default to `now()` (current timestamp).
{% endhint %}

### Bit-level operations

The `util:` namespace provides specialized functions for binary data processing, data format conversions, and string operations.

#### Bit-level functions

<table><thead><tr><th>Function</th><th>Parameters</th><th width="120.636474609375">Result type</th><th>Description</th></tr></thead><tbody><tr><td><code>util:signed(n, bytesAmount)</code></td><td><p><code>n</code> (Number): unsigned number</p><p><code>bytesAmount</code> (int): bytes (1, 2, 4, 8)</p></td><td>Long</td><td><p>Converts an unsigned integer of <code>bytesAmount</code> bytes to a signed two's-complement value. </p><p><strong>Note</strong>: It does not convert signed to unsigned.</p></td></tr><tr><td><code>util:checkBit(n, bitIndex)</code></td><td><p><code>n</code> (Number): number to check</p><p><code>bitIndex</code> (int): bit position (0=LSB)</p></td><td>Boolean</td><td>Check if bit is set (true) or not (false)</td></tr><tr><td><code>util:bit(n, bitIndex)</code></td><td><p><code>n</code> (Number): number to check</p><p><code>bitIndex</code> (int): bit position (0=LSB)</p></td><td>Integer</td><td>Get bit value (1 or 0)</td></tr><tr><td><code>util:bits(n, firstBitIndex, lastBitIndexInclusive)</code></td><td><p><code>n</code> (Number): source number</p><p><code>firstBitIndex</code> (int): start position</p><p><code>lastBitIndexInclusive</code> (int): end position</p></td><td>Long</td><td>Extract bit range; reverse if <code>lastBitIndexInclusive</code> &#x3C; <code>firstBitIndex</code>. Returns <code>null</code> if indexes are out of bounds.</td></tr><tr><td><code>util:bytes(n, firstByteIndex, lastByteIndexInclusive)</code></td><td><p><code>n</code> (Number): source number</p><p><code>firstByteIndex</code> (int): start position</p><p><code>lastByteIndexInclusive</code> (int): end position</p></td><td>Long</td><td>Extract byte range; byte swap if <code>lastByteIndexInclusive</code> &#x3C; <code>firstByteIndex</code>. Returns <code>null</code> if indexes are out of bounds.</td></tr></tbody></table>

**Examples:**

<table><thead><tr><th width="270.81817626953125">Expression</th><th width="109">Result</th><th>Use case</th></tr></thead><tbody><tr><td><code>util:signed(65535, 2)</code></td><td><code>-1</code></td><td>Convert 0xFFFF to signed 16-bit</td></tr><tr><td><code>util:checkBit(4, 2)</code></td><td><code>true</code></td><td>Check status flag bit</td></tr><tr><td><code>util:bits(1321678, 0, 3)</code></td><td><code>14</code></td><td>Extract 4-bit sensor value</td></tr><tr><td><code>util:bytes(11189196, 1, 0)</code></td><td><code>52411</code></td><td>Little-endian byte swap</td></tr></tbody></table>

#### HEX string operations

Binary data is processed as HEX strings (uppercase) for readability and protocol compatibility.

<table><thead><tr><th>Function</th><th>Parameters</th><th width="120.63641357421875">Result type</th><th>Description</th></tr></thead><tbody><tr><td><code>util:hex(n)</code></td><td><code>n</code> (Number): value to convert</td><td>String</td><td>Convert to HEX string; 16 chars for negative/float, variable for positive int; <code>null</code> if invalid</td></tr><tr><td><code>util:hex(n, bytesAmount)</code></td><td><code>n</code> (Number): value to convert<code>bytesAmount</code> (int): byte length</td><td>String</td><td>Convert to fixed-length HEX (bytesAmount * 2 chars); pad/truncate as needed; <code>null</code> if invalid</td></tr><tr><td><code>util:hexToLong(s)</code></td><td><code>s</code> (String): HEX string</td><td>Long</td><td>Convert HEX string to Long; <code>null</code> if invalid</td></tr><tr><td><code>util:hexToLong(s, firstByteIndex, lastByteIndexInclusive)</code></td><td><p> </p><ul><li><code>s</code> (String): HEX string</li><li><code>firstByteIndex</code> (int): start byte (0=left). <br>Byte 0 is the leftmost (most-significant) byte of the HEX string.</li><li><code>lastByteIndexInclusive</code> (int): end byte</li></ul></td><td>Long</td><td>Extract bytes from HEX string to Long; reverse if <code>lastByteIndexInclusive</code> &#x3C; <code>firstByteIndex</code>; <code>null</code> if invalid</td></tr></tbody></table>

**Examples:**

| Expression                       | Result           | Use case                   |
| -------------------------------- | ---------------- | -------------------------- |
| `util:hex(127)`                  | `"7F"`           | Variable length conversion |
| `util:hex(127, 6)`               | `"00000000007F"` | Fixed-width formatting     |
| `util:hexToLong("FF")`           | `255`            | Parse HEX value            |
| `util:hexToLong("AABBCC", 1, 0)` | `48042`          | Little-endian parsing      |

### Data format conversions

<table><thead><tr><th>Function</th><th>Parameters</th><th width="120.636474609375">Result type</th><th>Description</th></tr></thead><tbody><tr><td><code>util:fromBcd(o)</code></td><td><code>o</code> (Object): BCD number</td><td>Long</td><td>Convert BCD to decimal; <code>null</code> if invalid BCD</td></tr><tr><td><code>util:toBcd(o)</code></td><td><code>o</code> (Object): decimal (0 to 9999999999999999)</td><td>Long</td><td>Convert decimal to BCD; <code>null</code> if out of range</td></tr><tr><td><code>util:toFloat(o)</code></td><td><code>o</code> (Object): Long (IEEE 754 bits) or Double</td><td>Float</td><td>Convert to Float; interpret Long as IEEE 754 bits; <code>null</code> if invalid</td></tr><tr><td><code>util:toDouble(o)</code></td><td><code>o</code> (Object): Long (IEEE 754 bits) or Double</td><td>Double</td><td>Convert to Double; interpret Long as IEEE 754 bits; <code>null</code> if invalid</td></tr></tbody></table>

**Examples:**

| Expression                 | Result          | Use case                |
| -------------------------- | --------------- | ----------------------- |
| `util:fromBcd(0x1234)`     | `1234`          | Decode BCD device ID    |
| `util:toBcd(1234)`         | `0x1234` (4660) | Encode for BCD protocol |
| `util:toFloat(1065353216)` | `1.0`           | Decode IEEE 754 float   |

### String padding functions

<table><thead><tr><th>Function</th><th>Parameters</th><th width="120.63641357421875">Result type</th><th>Description</th></tr></thead><tbody><tr><td><code>util:leftPad(o, length)</code></td><td><p><code>o</code> (Object): value</p><p><code>length</code> (int): target length</p></td><td>String</td><td>Pad left with "0" to length; <code>null</code> if input null</td></tr><tr><td><code>util:leftPad(o, length, padStr)</code></td><td><p><code>o</code> (Object): value</p><p><code>length</code> (int): target length</p><p><code>padStr</code> (String): padding</p></td><td>String</td><td>Pad left with custom string; <code>null</code> if input null</td></tr><tr><td><code>util:rightPad(o, length)</code></td><td><p><code>o</code> (Object): value</p><p><code>length</code> (int): target length</p></td><td>String</td><td>Pad right with "0" to length; <code>null</code> if input null</td></tr><tr><td><code>util:rightPad(o, length, padStr)</code></td><td><p><code>o</code> (Object): value</p><p><code>length</code> (int): target length</p><p><code>padStr</code> (String): padding</p></td><td>String</td><td>Pad right with custom string; <code>null</code> if input null</td></tr></tbody></table>

**Examples:**

| Expression                | Result    |
| ------------------------- | --------- |
| `util:leftPad(123, 5)`    | `"00123"` |
| `util:leftPad(7, 3, "*")` | `"**7"`   |
| `util:rightPad(123, 5)`   | `"12300"` |

### String join functions

Use these functions to combine multiple attribute values into a single string. They are particularly useful when consolidating readings from indexed device attributes, such as BLE sensor slots, where only some values may be present.

<table><thead><tr><th>Function</th><th>Parameters</th><th width="122">Result type</th><th>Description</th></tr></thead><tbody><tr><td><code>util:join(separator, arguments...)</code></td><td><code>separator</code> (String): delimiter<br><code>arguments</code> (Object...): values to join</td><td>String</td><td>Joins all arguments into a single string using the given separator. Null arguments are treated as empty strings</td></tr><tr><td><code>util:joinNonNull(separator, arguments...)</code></td><td><code>separator</code> (String): delimiter<br><code>arguments</code> (Object...): values to join</td><td>String</td><td>Joins non-null arguments into a single string using the given separator. Null arguments are skipped; returns empty string if all arguments are null</td></tr></tbody></table>

**Examples:**

<table><thead><tr><th width="271">Expression</th><th>Result</th><th>Use case</th></tr></thead><tbody><tr><td><code>util:join(', ', 'a', null, 'b')</code></td><td><code>"a, , b"</code></td><td>Preserve empty positions</td></tr><tr><td><code>util:joinNonNull(', ', 'a', null, 'b')</code></td><td><code>"a, b"</code></td><td>Skip absent values</td></tr><tr><td><code>util:joinNonNull(', ', ble_name_1, ble_name_2, ble_name_3)</code></td><td><code>"Sensor A, Sensor B"</code> (if <code>ble_name_3</code> is null)</td><td>Collect active BLE sensor names</td></tr></tbody></table>

## Data types and type handling

### Supported data types

| Data Type  | Description                             | Examples             |
| ---------- | --------------------------------------- | -------------------- |
| Integer    | Whole numbers                           | `42`, `-100`, `0xFF` |
| Long       | Large integers with `L` suffix          | `42L`, `9999999999L` |
| Float      | Floating-point with optional `f` suffix | `3.14`, `42.0f`      |
| Double     | Double-precision floating-point         | `3.14`, `42.0d`      |
| String     | Text enclosed in quotes                 | `"text"`, `'text'`   |
| Boolean    | True or false values                    | `true`, `false`      |
| HEX String | Uppercase hexadecimal representation    | `"FF"`, `"1A2B"`     |
| Null       | Absence of value                        | `null`               |

### Null propagation

**Rule:** Null values propagate through expressions without errors. When any operand is null, the expression typically evaluates to null.

| Expression         | Result  | Notes                  |
| ------------------ | ------- | ---------------------- |
| `null + 5`         | `null`  | Arithmetic with null   |
| `temperature + 10` | `null`  | If temperature is null |
| `null == null`     | `true`  | Null equality          |
| `null != 5`        | `true`  | Null comparison        |
| `null > 0`         | `false` | Null in comparison     |

{% hint style="info" %}
In **Logic** nodes expressions evaluating to null are treated as `false` and route through ELSE path.
{% endhint %}

#### Error conditions resulting in null

| Condition               | Expression example                 | Result                         |
| ----------------------- | ---------------------------------- | ------------------------------ |
| Invalid function input  | `util:hexToLong("invalid")`        | `null`                         |
| Invalid BCD             | `util:fromBcd(0x99A0)`             | `null`                         |
| Missing historical data | `value('temperature', 5, 'valid')` | `null` (if < 5 valid readings) |
| Type mismatch           | `"text" + 123`                     | `null`                         |

{% hint style="danger" %}
Mismatched attribute names prevent calculation execution (no null returned; calculation skipped).
{% endhint %}

## Expression patterns

<table><thead><tr><th width="159">Pattern type</th><th>Expression</th><th>Use case</th></tr></thead><tbody><tr><td><strong>Unit conversion</strong></td><td><code>temperature * 1.8 + 32</code></td><td>Celsius to Fahrenheit</td></tr><tr><td></td><td><code>distance / 1.609</code></td><td>Kilometers to miles</td></tr><tr><td></td><td><code>volume * 0.264172</code></td><td>Liters to gallons</td></tr><tr><td><strong>Change detection</strong></td><td><code>temperature - value('temperature', 1, 'all')</code></td><td>Temperature change</td></tr><tr><td></td><td><code>value('fuel_level', 1, 'valid') - fuel_level</code></td><td>Fuel consumption</td></tr><tr><td></td><td><code>speed - value('speed', 1, 'valid')</code></td><td>Speed change</td></tr><tr><td><strong>Binary parsing</strong></td><td><code>util:signed(util:hexToLong(hex_data, 0, 1), 2) / 10.0</code></td><td>Signed temp from HEX</td></tr><tr><td></td><td><code>util:checkBit(status_flags, 0)</code></td><td>Check status flag</td></tr><tr><td></td><td><code>util:bits(status_word, 4, 7)</code></td><td>Extract sensor value</td></tr><tr><td><strong>Time calculations</strong></td><td><code>now() - genTime('temperature', 0, 'all')</code></td><td>Data age</td></tr><tr><td></td><td><code>srvTime('temp', 0, 'all') - genTime('temp', 0, 'all')</code></td><td>Transmission delay</td></tr><tr><td></td><td><code>genTime('temperature', 0, 'valid') + 120000</code></td><td>Time offset (2 min)</td></tr></tbody></table>

## Quick reference tables

#### Core functions summary

<table><thead><tr><th>Function</th><th width="121.72735595703125">Result type</th><th>Primary use</th></tr></thead><tbody><tr><td><code>value(attr, idx, val)</code></td><td>Any</td><td>Historical attribute value</td></tr><tr><td><code>genTime(attr, idx, val)</code></td><td>Long</td><td>Device generation time (default: <code>now()</code>)</td></tr><tr><td><code>srvTime(attr, idx, val)</code></td><td>Long</td><td>Server reception time (default: <code>now()</code>)</td></tr></tbody></table>

#### Bit operations summary

<table><thead><tr><th>Function</th><th width="120.81817626953125">Result type</th><th>Primary use</th></tr></thead><tbody><tr><td><code>util:signed(n, bytes)</code></td><td>Long</td><td>Convert unsigned to signed</td></tr><tr><td><code>util:checkBit(n, bit)</code></td><td>Boolean</td><td>Check if bit is set</td></tr><tr><td><code>util:bit(n, bit)</code></td><td>Integer</td><td>Get bit value (0/1)</td></tr><tr><td><code>util:bits(n, firstBitIndex, lastBitIndexInclusive)</code></td><td>Long</td><td>Extract bit range</td></tr><tr><td><code>util:bytes(n, firstByteIndex, lastByteIndexInclusive)</code></td><td>Long</td><td>Extract byte range</td></tr></tbody></table>

#### HEX operations summary

<table><thead><tr><th>Function</th><th width="120.81817626953125">Result type</th><th>Primary use</th></tr></thead><tbody><tr><td><code>util:hex(n)</code></td><td>String</td><td>Number to variable-length HEX</td></tr><tr><td><code>util:hex(n, bytes)</code></td><td>String</td><td>Number to fixed-length HEX</td></tr><tr><td><code>util:hexToLong(s)</code></td><td>Long</td><td>HEX string to number</td></tr><tr><td><code>util:hexToLong(s, firstByteIndex, lastByteIndexInclusive)</code></td><td>Long</td><td>Extract bytes from HEX string</td></tr></tbody></table>

#### Data conversion summary

<table><thead><tr><th>Function</th><th width="120.81817626953125">Result type</th><th>Primary use</th></tr></thead><tbody><tr><td><code>util:fromBcd(o)</code></td><td>Long</td><td>BCD to decimal</td></tr><tr><td><code>util:toBcd(o)</code></td><td>Long</td><td>Decimal to BCD</td></tr><tr><td><code>util:toFloat(o)</code></td><td>Float</td><td>IEEE 754 bits to float</td></tr><tr><td><code>util:toDouble(o)</code></td><td>Double</td><td>IEEE 754 bits to double</td></tr></tbody></table>

#### String operations summary

<table><thead><tr><th>Function</th><th width="121.7271728515625">Result type</th><th>Primary use</th></tr></thead><tbody><tr><td><code>util:leftPad(o, len)</code></td><td>String</td><td>Pad left with "0"</td></tr><tr><td><code>util:leftPad(o, len, pad)</code></td><td>String</td><td>Pad left with custom string</td></tr><tr><td><code>util:rightPad(o, len)</code></td><td>String</td><td>Pad right with "0"</td></tr><tr><td><code>util:rightPad(o, len, pad)</code></td><td>String</td><td>Pad right with custom string</td></tr></tbody></table>
