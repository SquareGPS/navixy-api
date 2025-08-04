# Asset events

Contains methods to get asset events.

## API actions

API path: `/history/asset/`.

### list

Lists less than or equal to `limit` of assets' events sorted by the `time` field.

**Parameters**

| name                | description                                                                                                                                               | type             |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| assets              | Optional. Default: all. List of objects containing identifier and type to define a list of tracker identifiers. Type can be one of `vehicle`, `employee`. | object array     |
| asset\_types        | Optional. Default: all. List of asset types. Type can be one of `vehicle`, `employee`.                                                                    | string array     |
| from                | Start date/time for searching.                                                                                                                            | string date/time |
| to                  | End date/time for searching. Must be after "from" date.                                                                                                   | string date/time |
| events              | Optional. Default: all. List of event types.                                                                                                              | string array     |
| limit               | Optional. Default: history.maxLimit. Max count of entries in result.                                                                                      | int              |
| ascending           | Optional. Default: `true`. If `true`, ordering by time will be ascending, descending otherwise.                                                           | boolean          |
| only\_emergency     | Optional. Default: `false`. If `true`, only emergency events will be included.                                                                            | boolean          |
| only\_unread        | Optional. Default: `false`. If `true`, only unread events will be included.                                                                               | boolean          |
| add\_asset\_label   | Optional. Default: `true`. If `true`, asset label will be added to "message" field.                                                                       | boolean          |
| add\_tracker\_label | Optional. Default: `false`. If `true`, tracker label will be added to "message" field.                                                                    | boolean          |
| add\_tracker\_files | Optional. Default: `false`. If `true`, tracker files info will be included.                                                                               | boolean          |

Available event types can be obtained by `/history/type/list` action.

Default and max limit is 1000. (Note for StandAlone: this value configured by `maxHistoryLimit` config option).

Interval will be restricted by store period interval.

The asset label is calculated as the vehicle label. If there is no vehicle asset, it is calculated as the employee's full name. If both `add_asset_label` and `add_tracker_label` are `true`, the asset label will be added.

**Example**

\=== "cURL"

{% code overflow="wrap" %}
```
curl -X POST '{{ extra.api_example_url }}/history/asset/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "assets": [{"id": 1683258, "type": "employee"}], "from": "2020-12-10 16:44:00", "to": "2020-12-22 16:44:00"}'
```
{% endcode %}

**Response**

```json
{
  "list": [<history_entry>],
  "limit_exceeded": false,
  "success": true
}
```

* `list` - list of zero or more history entry objects described here.
* `limit_exceeded` - boolean. `true` if the requested period exceeds the user's tariff store period.

**Errors**

* 211 – Requested time span is too big - time span between `from` and `to` is more than report.maxTimeSpan days.
* 212 – Requested `limit` is too big - `limit` is more than history.maxLimit.

### count

Count the total and unread number of asset events.

**Parameters**

| name            | description                                                                                                                                               | type             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| assets          | Optional. Default: all. List of objects containing identifier and type to define a list of tracker identifiers. Type can be one of `vehicle`, `employee`. | object array     |
| asset\_types    | Optional. Default: all. List of asset types. Type can be one of `vehicle`, `employee`.                                                                    | string array     |
| from            | Start date/time for searching.                                                                                                                            | string date/time |
| to              | End date/time for searching. Must be after "from" date.                                                                                                   | string date/time |
| events          | Optional. Default: all. List of event types.                                                                                                              | string array     |
| only\_emergency | Optional. Default: `false`. If `true`, only emergency events will be included.                                                                            | boolean          |
| only\_unread    | Optional. Default: `false`. If `true`, only unread events will be included.                                                                               | boolean          |

Available event types can be obtained by `/history/type/list` action.

Interval will be restricted by store period interval.

**Example**

\=== "cURL"

```
curl -X POST '{{ extra.api_example_url }}/history/asset/count' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "assets": [{"id": 1683258, "type": "employee"}], "from": "2020-12-10 16:44:00", "to": "2020-12-22 16:44:00"}'
```

**Response**

```json
{
    "total": 150,
    "total_unread": 10,
    "success": true
}
```

* `total` - int. Number of events satisfied with conditions.
* `total_unread` - int. Number of unread events that satisfy the conditions.

**Errors**

* 211 — Requested time span is too big — the time span between `from` and `to` is more than `report.maxTimeSpan` days.
