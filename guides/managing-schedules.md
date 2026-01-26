---
description: Create, update, query, and delete RFC 5545–compatible schedules.
---

# Managing schedules

Schedules in Navixy Repository API define time-based rules for your fleet operations, maintenance windows, work hours, restrictions, and more.

The schedule data structure is semantically compatible with VEVENT and RRULE from [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545) (iCalendar). This means familiar concepts like recurrence rules, exception dates, and timezones work as expected, though the API uses JSON format rather than the iCalendar text format.

This guide walks you through creating, configuring, updating, and deleting schedules.

## Before you start

To work with a schedule, you need your [organization](../api-reference/objects.md#organization)'s ID. Use the [me](../api-reference/queries.md#me) query to find it through your membership:

```graphql
query GetMyOrganization {
  me {
    memberships {
      organization {
        id
        title
      }
    }
  }
}
```

In most cases, you'll have one organization in the response. Use its `id` for schedule operations.

## Understanding schedule data

A schedule consists of metadata (title, type, organization) and calendar data stored in the `scheduleData` field, which accepts a value of [ScheduleData](../api-reference/scalars.md#scheduledata), a custom scalar containing a JSON value.&#x20;

{% hint style="info" %}
The `scheduleData` field is a convenience alias for the `schedule_data` system custom field. You can also access the same data through the `customFields` field if needed. See [Working with custom fields](working-with-custom-fields.md) for details.
{% endhint %}

The JSON structure follows the RFC 5545 conventions:

<table><thead><tr><th width="115.60003662109375">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>timezone</code></td><td>IANA timezone identifier (e.g., <code>Europe/Berlin</code>, <code>America/New_York</code>, <code>UTC</code>). Defines how the system interprets all datetime values in events.</td></tr><tr><td><code>events</code></td><td>Array of time slots, each with start/end times and optional recurrence rules.</td></tr></tbody></table>

### How timezone works

All datetime values in events (`dtstart`, `dtend`, `exdate`, `rdate`, `until`) are interpreted as **local time** in the specified timezone. Do not include the `Z` suffix — these are not UTC values.

For example, with `"timezone": "Europe/Berlin"`:

* `"dtstart": "2025-01-06T06:00:00"` means 6:00 AM Berlin time
* The system handles DST transitions automatically

### Event fields

Each event in the `events` array can include:

<table><thead><tr><th width="95.39990234375">Field</th><th width="128.2000732421875">iCalendar equivalent</th><th>Description</th></tr></thead><tbody><tr><td><code>dtstart</code></td><td>DTSTART</td><td><strong>Required.</strong> Start time. Use ISO 8601 UTC format for regular events (<code>2025-01-06T05:00:00Z</code>). For all-day events, use DATE format without time component (<code>2025-01-06</code>).</td></tr><tr><td><code>dtend</code></td><td>DTEND</td><td>End time. Mutually exclusive with <code>duration</code>. Must match <code>dtstart</code> value type: DATE-TIME for regular events, DATE for all-day events.</td></tr><tr><td><code>duration</code></td><td>DURATION</td><td>Duration in ISO 8601 format. Mutually exclusive with <code>dtend</code>. Examples: <code>PT30M</code> (30 minutes), <code>PT3H</code> (3 hours), <code>P1D</code> (1 day). For all-day events, use day or week format only (<code>P1D</code>, <code>P1W</code>).</td></tr><tr><td><code>allDay</code></td><td>VALUE=DATE</td><td>When <code>true</code>, the event spans entire days. Requires <code>dtstart</code>, <code>dtend</code>, and <code>exdate</code> to use DATE format (no time component).</td></tr><tr><td><code>rrule</code></td><td>RRULE</td><td>Recurrence rule defining repeat patterns. See the <code>rrule</code> reference below.</td></tr><tr><td><code>exdate</code></td><td>EXDATE</td><td>Array of dates to exclude from recurrence. Values must exactly match generated occurrences. Use DATE-TIME format for regular events, DATE format for all-day events.</td></tr><tr><td><code>rdate</code></td><td>RDATE</td><td>Array of additional dates to include in recurrence. Must match <code>dtstart</code> value type: DATE-TIME for regular events, DATE for all-day events.</td></tr></tbody></table>

### Recurrence rule fields

The `rrule` property supports these fields:

<table><thead><tr><th width="153">Field</th><th width="153.79998779296875">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>freq</code></td><td>String</td><td><strong>Required.</strong> <code>SECONDLY</code>, <code>MINUTELY</code>, <code>HOURLY</code>, <code>DAILY</code>, <code>WEEKLY</code>, <code>MONTHLY</code>, or <code>YEARLY</code></td></tr><tr><td><code>interval</code></td><td>Integer</td><td>Repeat every N periods (default: 1)</td></tr><tr><td><code>count</code></td><td>Integer</td><td>Stop after N occurrences. Mutually exclusive with <code>until</code>.</td></tr><tr><td><code>until</code></td><td>DateTime</td><td>Stop after this date. Mutually exclusive with <code>count</code>.</td></tr><tr><td><code>byday</code></td><td>String[]</td><td>Days of week: <code>MO</code>, <code>TU</code>, <code>WE</code>, <code>TH</code>, <code>FR</code>, <code>SA</code>, <code>SU</code></td></tr><tr><td><code>bymonthday</code></td><td>Integer[]</td><td>Days of month: 1–31, or -31 to -1 for days from end (-1 = last day)</td></tr><tr><td><code>byyearday</code></td><td>Integer[]</td><td>Days of year: 1–366, or -366 to -1 for days from end (-1 = last day)</td></tr><tr><td><code>byweekno</code></td><td>Integer[]</td><td>Weeks of year: 1–53, or -53 to -1 (-1 = last week)</td></tr><tr><td><code>bymonth</code></td><td>Integer[]</td><td>Months: 1–12</td></tr><tr><td><code>byhour</code></td><td>Integer[]</td><td>Hours: 0–23</td></tr><tr><td><code>byminute</code></td><td>Integer[]</td><td>Minutes: 0–59</td></tr><tr><td><code>bysecond</code></td><td>Integer[]</td><td>Seconds: 0–60</td></tr><tr><td><code>wkst</code></td><td>String</td><td>Week start day: <code>MO</code> or <code>SU</code>. Default: <code>MO</code></td></tr></tbody></table>

### Validation rules

The API validates schedule data and returns a [validation error](../error-handling.md#validation-error-400) if:

* `dtend` is not later than `dtstart`
* `until` uses a different format than `dtstart` (e.g., DATE vs DATE-TIME)
* Required fields are missing (`dtstart`, `freq` in rrule)

## Example scenario: Fleet maintenance schedule

A logistics company needs to schedule weekly maintenance for their vehicle fleet. The maintenance provider works every Monday from 6:00 to 10:00 (Europe/Berlin timezone). Over time, requirements will change: holidays need to be excluded, the contract has an end date, and the maintenance window gets split to accommodate a break.

{% stepper %}
{% step %}
### Create the schedule

Start with a weekly schedule. The `scheduleData` field accepts a JSON structure with a timezone and an array of events. Each event has a start time, end time (or duration), and an optional recurrence rule.

```graphql
mutation CreateMaintenanceSchedule {
  scheduleCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Weekly fleet maintenance"
    scheduleData: {
      timezone: "Europe/Berlin"
      events: [
        {
          dtstart: "2025-01-06T06:00:00"
          dtend: "2025-01-06T10:00:00"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
          }
        }
      ]
    }
  }) {
    schedule {
      id
      version
      title
    }
  }
}
```

Note the following:

* Times are in the local format without the Z suffix. The `timezone` field (Europe/Berlin) tells the system how to interpret these values — here, 06:00:00 means 6:00 AM Berlin time.
* `rrule.freq: "WEEKLY"` with `byday: ["MO"]` means the event repeats every Monday.
* The `dtstart` date is when the schedule comes into effect. Match it to your recurrence pattern to ensure predictable behavior — in this case, a Monday, since the rule uses `byday: ["MO"]`.

The response confirms creation:

```json
{
  "data": {
    "scheduleCreate": {
      "schedule": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 1,
        "title": "Weekly fleet maintenance"
      }
    }
  }
}
```

Save the `id` and `version` — you'll need them for updating the schedule.
{% endstep %}

{% step %}
### Verify the schedule

Query the schedule to confirm it was created correctly:

```graphql
query GetMaintenanceSchedule {
  schedule(id: "019a6b2f-793e-807b-8001-555345529b44") {
    id
    version
    title
    type {
      code
      title
    }
    scheduleData
  }
}
```

The `scheduleData` field returns the full JSON structure you provided, which you can use to verify the configuration or display it in your application.
{% endstep %}

{% step %}
### Exclude holidays

The maintenance provider doesn't work on public holidays. Several holidays in the year fall on Mondays. Add these as exception dates using `exdate`. This requires updating the schedule with `scheduleUpdate`.

{% hint style="danger" %}
When updating `scheduleData`, you must provide the complete value — the API replaces the entire field. Include all existing configuration plus your changes.
{% endhint %}

```graphql
mutation AddHolidayExceptions {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 1
    scheduleData: {
      timezone: "Europe/Berlin"
      events: [
        {
          dtstart: "2025-01-06T06:00:00"
          dtend: "2025-01-06T10:00:00"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
          }
          exdate: [
            "2025-04-21T06:00:00",
            "2025-05-05T06:00:00",
            "2025-06-09T06:00:00",
            "2025-10-06T06:00:00"
          ]
        }
      ]
    }
  }) {
    schedule {
      id
      version
      scheduleData
    }
  }
}
```

The `exdate` values must exactly match generated occurrences. Since all occurrences inherit the time from `dtstart`, use the same time component (here, `05:00:00Z`) for each excluded date.

{% hint style="info" %}
For all-day events (where `allDay: true`), use date-only values in `exdate` (e.g., `"2025-04-21"`) instead of full datetime values.
{% endhint %}

The response shows the incremented version:

```json
{
  "data": {
    "scheduleUpdate": {
      "schedule": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 2,
        "scheduleData": { ... }
      }
    }
  }
}
```
{% endstep %}

{% step %}
### Set an end date

The maintenance contract runs through December 31, 2025. Add an `until` date to the recurrence rule so the schedule stops repeating after that date.

```graphql
mutation SetContractEndDate {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 2
    scheduleData: {
      timezone: "Europe/Berlin"
      events: [
        {
          dtstart: "2025-01-06T06:00:00"
          dtend: "2025-01-06T10:00:00"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
            until: "2025-12-31T23:59:59"
          }
          exdate: [
            "2025-04-21T06:00:00",
            "2025-05-05T06:00:00",
            "2025-06-09T06:00:00",
            "2025-10-06T06:00:00"
          ]
        }
      ]
    }
  }) {
    schedule {
      id
      version
    }
  }
}
```

The `until` value is inclusive — the last occurrence can happen on this date. The schedule's version is now 3.
{% endstep %}

{% step %}
### Split the schedule into two windows

The maintenance team requests a break from 8:00 to 8:30. Instead of one 4-hour window, you now need two windows: 6:00–8:00 and 8:30–10:00.

Replace the single event with two events, each with its own recurrence rule:

```graphql
mutation SplitMaintenanceWindow {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 3
    scheduleData: {
      timezone: "Europe/Berlin"
      events: [
        {
          dtstart: "2025-01-06T06:00:00"
          dtend: "2025-01-06T08:00:00"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
            until: "2025-12-31T23:59:59"
          }
          exdate: [
            "2025-04-21T06:00:00",
            "2025-05-05T06:00:00",
            "2025-06-09T06:00:00",
            "2025-10-06T06:00:00"
          ]
        },
        {
          dtstart: "2025-01-06T08:30:00"
          dtend: "2025-01-06T10:00:00"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
            until: "2025-12-31T23:59:59"
          }
          exdate: [
            "2025-04-21T08:30:00",
            "2025-05-05T08:30:00",
            "2025-06-09T08:30:00",
            "2025-10-06T08:30:00"
          ]
        }
      ]
    }
  }) {
    schedule {
      id
      version
    }
  }
}
```

Note that each event has its own `exdate` array with times matching that event's `dtstart`.
{% endstep %}

{% step %}
### Delete the schedule

When the contract ends and you no longer need the schedule, delete it:

```graphql
mutation DeleteMaintenanceSchedule {
  scheduleDelete(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 4
  }) {
    deletedId
  }
}
```

The `version` parameter ensures you don't accidentally delete a schedule that someone else has modified. If the version doesn't match, you'll receive a [conflict error](../error-handling.md#version-conflict-409).
{% endstep %}
{% endstepper %}

### Listing schedules

To retrieve all schedules for an organization:

```graphql
query ListSchedules {
  schedules(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      title
      type {
        title
      }
      scheduleData
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

For details on pagination, see [Pagination](../pagination.md).

### Handling version conflicts

If someone else updates the schedule while you're working on it, your mutation will fail with a conflict error:

```json
{
  "errors": [
    {
      "message": "Entity has been modified by another request",
      "extensions": {
        "code": "CONFLICT",
        "status": 409,
        "expectedVersion": 3,
        "currentVersion": 4
      }
    }
  ]
}
```

To resolve this:

1. Query the schedule to get the current version and data
2. Merge your changes with the current state
3. Retry the mutation with the correct version

For more details on version conflicts, see [Optimistic locking](../optimistic-locking.md).

## Common patterns

#### Single-parameter patterns

**Every weekday (standard work hours):**

```json
{ "freq": "WEEKLY", "byday": ["MO", "TU", "WE", "TH", "FR"] }
```

**Every other week on Monday (bi-weekly team meetings):**

```json
{ "freq": "WEEKLY", "interval": 2, "byday": ["MO"] }
```

**First and fifteenth of each month (payroll processing):**

```json
{ "freq": "MONTHLY", "bymonthday": [1, 15] }
```

**Last day of each month (monthly reports deadline):**

```json
{ "freq": "MONTHLY", "bymonthday": [-1] }
```

#### Multi-parameter patterns

**Weekdays at 8:00 AM (daily data export):**

```json
{ "freq": "WEEKLY", "byday": ["MO", "TU", "WE", "TH", "FR"], "byhour": [8] }
```

**Monday, Wednesday, Friday at 7:30 AM (driver briefings):**

```json
{ "freq": "WEEKLY", "byday": ["MO", "WE", "FR"], "byhour": [7], "byminute": [30] }
```

**Every Monday in January, April, July, and October (quarterly inspections):**

```json
{ "freq": "YEARLY", "bymonth": [1, 4, 7, 10], "byday": ["MO"] }
```

**Twice daily on weekdays at 9:00 and 17:00 (shift change checks):**

```json
{ "freq": "WEEKLY", "byday": ["MO", "TU", "WE", "TH", "FR"], "byhour": [9, 17] }
```

## Complete examples

### Warehouse work hours

Standard weekday schedule with a lunch break, excluding company holidays:

```json
{
  "timezone": "Europe/Berlin",
  "events": [
    {
      "dtstart": "2025-01-06T08:00:00",
      "dtend": "2025-01-06T12:00:00",
      "rrule": {
        "freq": "WEEKLY",
        "byday": ["MO", "TU", "WE", "TH", "FR"]
      },
      "exdate": ["2025-01-01T08:00:00", "2025-12-25T08:00:00", "2025-12-26T08:00:00"]
    },
    {
      "dtstart": "2025-01-06T13:00:00",
      "dtend": "2025-01-06T17:00:00",
      "rrule": {
        "freq": "WEEKLY",
        "byday": ["MO", "TU", "WE", "TH", "FR"]
      },
      "exdate": ["2025-01-01T13:00:00", "2025-12-25T13:00:00", "2025-12-26T13:00:00"]
    }
  ]
}
```

### Refrigerated truck temperature monitoring

Different temperature thresholds for day and night operation:

```json
{
  "timezone": "Europe/Moscow",
  "events": [
    {
      "dtstart": "2025-01-06T06:00:00",
      "dtend": "2025-01-06T22:00:00",
      "rrule": {
        "freq": "DAILY"
      }
    },
    {
      "dtstart": "2025-01-06T22:00:00",
      "dtend": "2025-01-07T06:00:00",
      "rrule": {
        "freq": "DAILY"
      }
    }
  ]
}
```

### Equipment rental periods

Non-recurring schedule for specific rental dates:

```json
{
  "timezone": "America/New_York",
  "events": [
    {
      "dtstart": "2025-02-10",
      "dtend": "2025-02-15",
      "allDay": true
    },
    {
      "dtstart": "2025-03-01",
      "dtend": "2025-03-10",
      "allDay": true
    }
  ]
}
```

## Next steps

* TBD
