---
description: >-
  Create, update, query, and delete JSCalendar-aligned schedules compatible with
  RFC 5545 (iCalendar).
---

# Managing schedules

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

Schedules in Navixy Repository API define time-based rules for your fleet operations, maintenance windows, work hours, restrictions, and more.

The schedule data structure follows a [JSCalendar (RFC 8984)](https://www.rfc-editor.org/rfc/rfc8984.html) profile designed to round-trip to [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545) (iCalendar). If you've worked with iCalendar concepts like RRULE, EXDATE, and VTIMEZONE before, the underlying model will be familiar — the field names and JSON structure come from JSCalendar, while the recurrence semantics follow iCalendar rules.

This guide walks you through creating, configuring, updating, and deleting schedules.

## Before you start

To work with a schedule, you need your organization's ID. Use the [me](../actors/#me) query to find it through your membership:

```graphql
query GetMyOrganization {
  me {
    ... on User {
      memberships {
        nodes {
          organization {
            id
            title
          }
        }
      }
    }
  }
}
```

You'll receive a response:

```json
{
  "data": {
    "me": {
      "memberships": {
        "nodes": [
          {
            "organization": {
              "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
              "title": "TransLog GmbH"
            }
          }
        ]
      }
    }   
  }
}
```

Use the `id` of the organization you want to work with for all subsequent schedule operations.

## Understanding schedule data

A schedule consists of metadata (title and organization) and calendar data stored in the `scheduleData` field, which accepts a value of [ScheduleData](../schedules.md#scheduledata), a structured JSON object validated on every write.

### Top-level fields

The JSON structure follows the RFC 5545 conventions:

<table><thead><tr><th width="115.60003662109375">Field</th><th width="89.20001220703125" data-type="checkbox">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>timezone</code></td><td>true</td><td>IANA timezone identifier (e.g., <code>Europe/Berlin</code>, <code>America/New_York</code>, <code>UTC</code>). Defines how the API interprets all date-time values in timed events.</td></tr><tr><td><code>events</code></td><td>true</td><td>Non-empty array of time slots, each with a start time, end time or duration, and an optional recurrence rule</td></tr><tr><td><code>active</code></td><td>false</td><td>Boolean. When <code>false</code>, the schedule is disabled without deleting it. Defaults to <code>true</code>.</td></tr><tr><td><code>description</code></td><td>false</td><td>Free-text description. The schedule's display name is the entity <code>title</code>, not this field.</td></tr></tbody></table>

### How timezone works

All date-time values in events (`start`, `end`, `excludedDates`, `additionalDates`, and `recurrenceRule.until`) are local time with no UTC offset or `Z` suffix. The `timeZone` field tells the API how to interpret them.

For example, for `"timeZone": "Europe/Berlin"`:

* `"start": "2025-01-06T06:00:00"` means 6:00 AM Berlin time.
* The API handles DST transitions automatically, so a recurring event at `06:00:00` stays at 6 AM local time year-round.

All-day events (where `showWithoutTime: true`) use date strings instead of date-times (`2025-06-10`, not `2025-06-10T00:00:00`) and are timezone-independent.

### Event fields

Each event in the `events` array can include:

<table><thead><tr><th width="112.79998779296875">Field</th><th width="112">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>start</code></td><td>Yes</td><td>Start date-time for timed events (<code>2025-01-06T06:00:00</code>) or date for all-day events (<code>2025-01-06</code>). Seconds required. No fractional seconds. No offset or <code>Z</code>.</td></tr><tr><td><code>end</code></td><td>Conditional</td><td>End date-time (or date for all-day). Mutually exclusive with <code>duration</code>. A timed event needs exactly one of <code>end</code> or <code>duration</code>. An all-day event may omit both.</td></tr><tr><td><code>duration</code></td><td>Conditional</td><td>Duration in ISO 8601 format (e.g., <code>PT9H</code>, <code>PT30M</code>, <code>P1D</code>). Mutually exclusive with <code>end</code>. Must be positive. For all-day events, must be whole days (e.g., <code>P1D</code>, <code>P2W</code>) with no time component. Preferred over <code>end</code> for recurring events because it stays stable across DST transitions.</td></tr><tr><td><code>showWithoutTime</code></td><td>No</td><td>When <code>true</code>, the event is all-day: <code>start</code> and <code>end</code> are dates, and the event ignores <code>timeZone</code>. All-day recurrence rules must not use <code>byHour</code>, <code>byMinute</code>, or <code>bySecond</code>.</td></tr><tr><td><code>recurrenceRule</code></td><td>No</td><td>Recurrence rule defining the repeat pattern. Absent means a single occurrence at <code>start</code>.</td></tr><tr><td><code>excludedDates</code></td><td>No</td><td>Array of local date-times to exclude from recurrence (iCalendar EXDATE). Values must exactly match generated occurrence date-times, including the time component.</td></tr><tr><td><code>additionalDates</code></td><td>No</td><td>Array of local date-times to add as one-off occurrences (iCalendar RDATE).</td></tr><tr><td><code>uid</code></td><td>No</td><td>Stable string identifier for the slot. Useful when tracking individual events across updates.</td></tr><tr><td><code>title</code></td><td>No</td><td>Display label for this event slot (maps to VEVENT SUMMARY).</td></tr></tbody></table>

### Recurrence rule fields

The `rrule` property supports these fields:

<table><thead><tr><th width="118.4000244140625">Field</th><th width="129">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>frequency</code></td><td>String</td><td><strong>Required.</strong> One of: <code>secondly</code>, <code>minutely</code>, <code>hourly</code>, <code>daily</code>, <code>weekly</code>, <code>monthly</code>, <code>yearly</code>. Lowercase.</td></tr><tr><td><code>interval</code></td><td>Integer</td><td>Repeat every N periods. Must be ≥ 1. Defaults to 1.</td></tr><tr><td><code>count</code></td><td>Integer</td><td>Stop after N occurrences. Mutually exclusive with <code>until</code>.</td></tr><tr><td><code>until</code></td><td>String</td><td>Stop after this local date-time. Must be ≥ <code>start</code>. Mutually exclusive with <code>count</code>.</td></tr><tr><td><code>byDay</code></td><td>Object[]</td><td>Days of the week. Each entry is <code>{ "day": "&#x3C;mo|tu|we|th|fr|sa|su>", "nthOfPeriod": &#x3C;integer> }</code>. The optional <code>nthOfPeriod</code> sets an ordinal (e.g., <code>{ "day": "mo", "nthOfPeriod": 1 }</code> = first Monday of the period) and is only valid for <code>monthly</code> or <code>yearly</code> frequency.</td></tr><tr><td><code>byMonth</code></td><td>Integer[]</td><td>Months: 1–12.</td></tr><tr><td><code>byMonthDay</code></td><td>Integer[]</td><td>Days of the month: 1–31, or -31 to -1 from the end (-1 = last day).</td></tr><tr><td><code>byYearDay</code></td><td>Integer[]</td><td>Days of the year: 1–366, or -366 to -1 from the end.</td></tr><tr><td><code>byWeekNo</code></td><td>Integer[]</td><td>Weeks of the year: 1–53, or -53 to -1. Valid only with <code>yearly</code> frequency.</td></tr><tr><td><code>byHour</code></td><td>Integer[]</td><td>Hours: 0–23. Must not be used on all-day events.</td></tr><tr><td><code>byMinute</code></td><td>Integer[]</td><td>Minutes: 0–59. Must not be used on all-day events.</td></tr><tr><td><code>bySecond</code></td><td>Integer[]</td><td>Seconds: 0–60 (60 is valid for leap seconds). Must not be used on all-day events.</td></tr><tr><td><code>firstDayOfWeek</code></td><td>String</td><td>First day of the week for week calculations. One of <code>mo</code>–<code>su</code>. Defaults to <code>mo</code>. (iCalendar WKST.)</td></tr></tbody></table>

### Validation

`scheduleData` is validated on every write against the following rules:&#x20;

* required fields
* mutual exclusions (`end`/`duration`, `count`/`until`)
* date-time format (local time only, no offset or `Z`)
* recurrence constraints (`byWeekNo` only with `yearly`, ordinal `byDay` only with `monthly`/`yearly`, no `byHour`/`byMinute`/`bySecond` on all-day events)
* field types

Non-conforming input is rejected with a [validation error](../error-handling.md#validation-error-400) that includes a field-specific message. Reads are tolerant of legacy data, so existing schedules created before validation was introduced remain readable.

## Example scenario: Fleet maintenance schedule

TransLog GmbH needs to schedule weekly maintenance for their vehicle fleet. The maintenance provider works every Monday from 6:00 to 10:00 (Europe/Berlin timezone). Over time, requirements will change: holidays need to be excluded, the contract has an end date, and the maintenance window gets split to accommodate a break.

{% stepper %}
{% step %}
#### **Create the schedule**

Start with a weekly recurring event. The `scheduleData` field requires a `timeZone` and at least one event with a `start` and either `end` or `duration`.

{% hint style="info" %}
`version` is optional in all mutations — omitting it applies the update unconditionally without conflict detection. Include it whenever you want to guard against overwriting concurrent changes. See [Optimistic locking](../optimistic-locking.md) for details. This example uses it throughout.
{% endhint %}

Run this mutation:

```graphql
mutation CreateMaintenanceSchedule {
  scheduleCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    title: "Weekly fleet maintenance"
    scheduleData: {
      timeZone: "Europe/Berlin"
      events: [
        {
          start: "2025-01-06T06:00:00"
          duration: "PT4H"
          recurrenceRule: {
            frequency: "weekly"
            byDay: [{ day: "mo" }]
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

* `timeZone` is `Europe/Berlin`. All date-times in this schedule are Berlin local time: no `Z`, no offset.
* `start: "2025-01-06T06:00:00"` is a Monday, which matches the `byDay: [{ day: "mo" }]` rule. Always align `start` with your recurrence pattern to ensure predictable behavior.
* `duration: "PT4H"` defines a 4-hour window (06:00–10:00). Using `duration` instead of `end` keeps the window stable across DST transitions.
* `frequency: "weekly"` with `byDay: [{ day: "mo" }]` means the event repeats every Monday.

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
#### **Verify the schedule**

Query the schedule to confirm it was created correctly:

```graphql
query GetMaintenanceSchedule {
  schedule(id: "019a6b2f-793e-807b-8001-555345529b44") {
    id
    version
    title
    scheduleData
  }
}
```

The `scheduleData` field returns the full JSON structure you provided. Use it to verify the configuration before making further changes.
{% endstep %}

{% step %}
#### **Exclude holidays**

The maintenance provider doesn't work on public holidays. Several holidays in the year fall on Mondays. Add these as exception dates using `exdate`. This requires updating the schedule with `scheduleUpdate`.

{% hint style="danger" %}
When updating `scheduleData`, you must provide the complete value, as the API replaces the entire field. Include all existing configuration alongside your changes.
{% endhint %}

`excludedDates` values must exactly match the date-time of generated occurrences. Because the event starts at `06:00:00`, each excluded date uses the same time component.&#x20;

Run this mutation:

```graphql
mutation AddHolidayExceptions {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 1
    scheduleData: {
      timeZone: "Europe/Berlin"
      events: [
        {
          start: "2025-01-06T06:00:00"
          duration: "PT4H"
          recurrenceRule: {
            frequency: "weekly"
            byDay: [{ day: "mo" }]
          }
          excludedDates: [
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

{% hint style="info" %}
For all-day events (`showWithoutTime: true`), use date-only values in `excludedDates`, for example, `"2025-04-21"` instead of `"2025-04-21T06:00:00"`.
{% endhint %}

The response shows the incremented version:

```json
{
  "data": {
    "scheduleUpdate": {
      "schedule": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 2,
        "scheduleData": { "..." : "..." }
      }
    }
  }
}
```
{% endstep %}

{% step %}
#### **Set an end date**

The maintenance contract runs through December 31, 2025. Add an `until` date to the recurrence rule so the schedule stops repeating after that date.

```graphql
mutation SetContractEndDate {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 2
    scheduleData: {
      timeZone: "Europe/Berlin"
      events: [
        {
          start: "2025-01-06T06:00:00"
          duration: "PT4H"
          recurrenceRule: {
            frequency: "weekly"
            byDay: [{ day: "mo" }]
            until: "2025-12-31T23:59:59"
          }
          excludedDates: [
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

`until` is inclusive — the last occurrence can fall on this date. It must be ≥ `start` and cannot be combined with `count`. The schedule's version is now 3.
{% endstep %}

{% step %}
#### **Split the schedule into two windows**

The maintenance team requests a break from 8:00 to 8:30. Replace the single 4-hour event with two events: 6:00–8:00 and 8:30–10:00.

Each event needs its own `excludedDates` array with times matching that event's `start`. Run this mutation:

```graphql
mutation SplitMaintenanceWindow {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 3
    scheduleData: {
      timeZone: "Europe/Berlin"
      events: [
        {
          start: "2025-01-06T06:00:00"
          duration: "PT2H"
          recurrenceRule: {
            frequency: "weekly"
            byDay: [{ day: "mo" }]
            until: "2025-12-31T23:59:59"
          }
          excludedDates: [
            "2025-04-21T06:00:00",
            "2025-05-05T06:00:00",
            "2025-06-09T06:00:00",
            "2025-10-06T06:00:00"
          ]
        },
        {
          start: "2025-01-06T08:30:00"
          duration: "PT1H30M"
          recurrenceRule: {
            frequency: "weekly"
            byDay: [{ day: "mo" }]
            until: "2025-12-31T23:59:59"
          }
          excludedDates: [
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

The schedule's version is now 4.
{% endstep %}

{% step %}
#### **Delete the schedule**

When the contract ends and you no longer need the schedule, run this mutation to delete it:

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

Response:

```json
{
  "data": {
    "scheduleDelete": {
      "deletedId": "019a6b2f-793e-807b-8001-555345529b44"
    }
  }
}
```

Including `version` ensures you don't accidentally delete a schedule that someone else has modified. If the version doesn't match, you'll receive a [conflict error](../error-handling.md#version-conflict-409). See [Optimistic locking](../optimistic-locking.md) for details on when to omit it.
{% endstep %}
{% endstepper %}

## Listing schedules

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

## Handling version conflicts

If you include `version` in your mutation and the entity has been modified since you last fetched it, the API returns a [conflict error](../error-handling.md#version-conflict-409):

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

The snippets below show the `recurrenceRule` object in isolation. In practice, each belongs inside an event in the `events` array alongside `start` and `end` or `duration`.

#### Single-parameter patterns

**Every weekday (standard work hours):**

```json
{
  "frequency": "weekly",
  "byDay": [
    { "day": "mo" }, { "day": "tu" }, { "day": "we" },
    { "day": "th" }, { "day": "fr" }
  ]
}
```

**Every other week on Monday (bi-weekly team meetings):**

```json
{
  "frequency": "weekly",
  "interval": 2,
  "byDay": [{ "day": "mo" }]
}
```

**First and fifteenth of each month (payroll processing):**

```json
{
  "frequency": "monthly",
  "byMonthDay": [1, 15]
}
```

**Last day of each month (monthly reports deadline):**

```json
{
  "frequency": "monthly",
  "byMonthDay": [-1]
}
```

**First Monday of each month (monthly fleet review):**

```json
{
  "frequency": "monthly",
  "byDay": [{ "day": "mo", "nthOfPeriod": 1 }]
}
```

#### Multi-parameter patterns

**Every hour during weekday business hours (hourly check-ins):**

```json
{
  "frequency": "hourly",
  "byDay": [
    { "day": "mo" }, { "day": "tu" }, { "day": "we" },
    { "day": "th" }, { "day": "fr" }
  ],
  "byHour": [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
}
```

{% hint style="info" %}
`byHour`, `byMinute`, and `bySecond` are only valid alongside `hourly`, `minutely`, `secondly`, or `daily` frequency, not `weekly`, `monthly`, or `yearly`. For patterns like "weekdays at 7:30 AM," use two separate events (one per time slot) rather than a single recurrence rule.
{% endhint %}

**Every Monday in January, April, July, and October (quarterly inspections):**

```json
{
  "frequency": "yearly",
  "byMonth": [1, 4, 7, 10],
  "byDay": [{ "day": "mo" }]
}
```

## Complete examples

### Warehouse work hours

Standard weekday schedule with a lunch break, excluding company holidays:

```json
{
  "timeZone": "Europe/Berlin",
  "events": [
    {
      "start": "2025-01-06T08:00:00",
      "duration": "PT4H",
      "recurrenceRule": {
        "frequency": "weekly",
        "byDay": [
          { "day": "mo" }, { "day": "tu" }, { "day": "we" },
          { "day": "th" }, { "day": "fr" }
        ]
      },
      "excludedDates": [
        "2025-01-01T08:00:00",
        "2025-12-25T08:00:00",
        "2025-12-26T08:00:00"
      ]
    },
    {
      "start": "2025-01-06T13:00:00",
      "duration": "PT4H",
      "recurrenceRule": {
        "frequency": "weekly",
        "byDay": [
          { "day": "mo" }, { "day": "tu" }, { "day": "we" },
          { "day": "th" }, { "day": "fr" }
        ]
      },
      "excludedDates": [
        "2025-01-01T13:00:00",
        "2025-12-25T13:00:00",
        "2025-12-26T13:00:00"
      ]
    }
  ]
}
```

### Refrigerated truck temperature monitoring

Different temperature thresholds for day and night operation:

```json
{
  "timeZone": "Europe/Berlin",
  "events": [
    {
      "start": "2025-01-06T08:00:00",
      "duration": "PT4H",
      "recurrenceRule": {
        "frequency": "weekly",
        "byDay": [
          { "day": "mo" }, { "day": "tu" }, { "day": "we" },
          { "day": "th" }, { "day": "fr" }
        ]
      },
      "excludedDates": [
        "2025-01-01T08:00:00",
        "2025-12-25T08:00:00",
        "2025-12-26T08:00:00"
      ]
    },
    {
      "start": "2025-01-06T13:00:00",
      "duration": "PT4H",
      "recurrenceRule": {
        "frequency": "weekly",
        "byDay": [
          { "day": "mo" }, { "day": "tu" }, { "day": "we" },
          { "day": "th" }, { "day": "fr" }
        ]
      },
      "excludedDates": [
        "2025-01-01T13:00:00",
        "2025-12-25T13:00:00",
        "2025-12-26T13:00:00"
      ]
    }
  ]
}
```

### Equipment rental periods

Non-recurring schedule for specific rental dates:

```json
{
  "timeZone": "America/New_York",
  "events": [
    {
      "start": "2025-02-10",
      "end": "2025-02-15",
      "showWithoutTime": true
    },
    {
      "start": "2025-03-01",
      "end": "2025-03-10",
      "showWithoutTime": true
    }
  ]
}
```

## See also

* [Schedules types and operations](../schedules.md): A complete list of all operations and types related to schedules
