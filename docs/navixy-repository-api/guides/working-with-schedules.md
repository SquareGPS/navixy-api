---
hidden: true
---

# Working with schedules

**Schedules** in Navixy Repository API represent RFC 5545-compliant calendar events that support recurrence rules, exceptions, and metadata. This compliance enables integration with industry-standard calendar systems such as Google Calendar, Outlook, and Apple Calendar, allowing you to import and export scheduling data across platforms. You can define events with repeating patterns, specify exceptions for holidays, and enrich them with custom metadata.

### Understanding schedules and iCalendar

[iCalendar (RFC 5545](https://www.rfc-editor.org/rfc/rfc5545)) is the internet standard for exchanging calendar data. These files typically use the `.ics` extension and the MIME type `text/calendar`. Navixy Repository API uses the following core iCalendar concepts:

* **Recurrence rules (**`rrule`**)**: Define repeating patterns using RFC 5545 syntax, such as daily, weekly, or monthly schedules. For example, `FREQ=WEEKLY;BYDAY=MO,WE,FR` creates a schedule that repeats every Monday, Wednesday, and Friday.
* **Exception dates (**`exdate`**)**: An array of specific date-time strings to exclude from a recurring schedule. This is perfect for handling holidays or one-off cancellations.
* **Duration vs end time**: A schedule can specify either an `end_at` time or a `duration`, but never both. The duration is expressed in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) (e.g., `PT1H30M` for 1 hour and 30 minutes).
* **Timezone support**: All date-time fields must be in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and include a timezone offset (e.g., `2025-01-15T09:00:00-05:00`) or be in UTC (e.g., `2025-01-15T14:00:00Z`).

#### Standard field mappings

<table><thead><tr><th width="164.27276611328125">Navixy field</th><th width="161.72723388671875">iCalendar property</th><th>Description</th></tr></thead><tbody><tr><td><code>start_at</code></td><td>DTSTART</td><td>The event's start time in ISO 8601 format.</td></tr><tr><td><code>end_at</code></td><td>DTEND</td><td>The event's end time. Mutually exclusive with <code>duration</code>.</td></tr><tr><td><code>duration</code></td><td>DURATION</td><td>The event's duration (e.g., <code>PT2H</code>). Mutually exclusive with <code>end_at</code>.</td></tr><tr><td><code>summary</code></td><td>SUMMARY</td><td>A short title for the event.</td></tr><tr><td><code>rrule</code></td><td>RRULE</td><td>The recurrence rule string.</td></tr><tr><td><code>exdate</code></td><td>EXDATE</td><td>An array of ISO 8601 date-time strings to exclude from the recurrence.</td></tr></tbody></table>

### How to work with schedules

{% hint style="warning" %}
Note that {BASE\_URL} in sample requests is a placeholder for the URL you'll be using, which depends on your geographical location and the current version of the API. To learn the specific server URLs, see [API environments](../technical-reference.md#api-environments).
{% endhint %}

#### Step 1. Create a basic schedule

First, create a simple weekly maintenance window that occurs every Monday at 2:00 AM UTC and lasts for four hours. Use this request body:

```bash
curl -L \
  --request POST \
  --url '{BASE_URL}/schedule/create' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "start_at": "2025-01-06T02:00:00Z",
    "duration": "PT4H",
    "summary": "Weekly maintenance window",
    "rrule": "FREQ=WEEKLY;BYDAY=MO"
  }'
```

The response returns the ID of the newly created schedule. You'll need it in the next steps.

```json
{
  "id": 515
}
```

#### Step 2. Add exception dates for holidays

Update the maintenance schedule to exclude holiday weeks when maintenance should not occur:

```bash
curl -L \
  --request POST \
  --url '{BASE_URL}/schedule/update' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "id": 515,
    "exdate": [
      "2025-01-20T02:00:00Z",
      "2025-02-17T02:00:00Z",
      "2025-05-26T02:00:00Z",
      "2025-12-22T02:00:00Z"
    ]
  }'
```

A successful update returns a `204 No Content` response with an empty body.

#### Step 3. Configure external system integration

You can link schedules to external systems using the `external_system`, `external_id`, and `meta` fields. The `meta` field accepts any valid JSON object, allowing you to store rich contextual data.

```bash
curl -L \
  --request POST \
  --url '{BASE_URL}/schedule/update' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "id": 12345,
    "external_system": "maintenance_system",
    "external_id": "WEEKLY-MAINT-001",
    "meta": {
      "type": "system_maintenance",
      "priority": "high",
      "affected_systems": ["database", "api_servers"],
      "notification_list": ["ops@company.com"]
    }
  }'
```

#### Step 4. Extend the schedule with an end date

Finally, update the schedule to make it stop repeating after the end of 2025.

{% hint style="warning" %}
When updating the `rrule` field, you must provide the entire new rule. The API replaces the old value completely. Forgetting to include existing parts like `FREQ=WEEKLY;BYDAY=MO` will break your schedule.
{% endhint %}

```bash
curl -L \
  --request POST \
  --url '{BASE_URL}/schedule/update' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "id": 12345,
    "rrule": "FREQ=WEEKLY;BYDAY=MO;UNTIL=20251231T235959Z"
  }'
```

{% hint style="info" %}
Note the `UNTIL` date format is `20251231T235959Z`. This is the standard iCalendar format, which does not use hyphens or colons.
{% endhint %}

{% hint style="success" %}
**Congratulations!**\
You've successfully created, updated, and enriched a recurring schedule.
{% endhint %}
