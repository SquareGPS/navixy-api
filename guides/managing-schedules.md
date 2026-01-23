---
description: Create, update, query, and delete RFC 5545–compatible schedules.
---

# Managing schedules

Schedules in Navixy Repository API represent [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545) (iCalendar)-compliant calendar events that support recurrence rules, exceptions, and multiple time slots.

This guide walks you through creating, updating, and deleting schedules with Navixy Repository API.

## Before you start

To work with a schedule, you need two IDs:

* **Organization ID**: the [organization ](../api-reference/objects.md#organization)that owns the schedule
* **Schedule type ID**: the schedule's [classification type](../api-reference/objects.md#scheduletype)

### Getting your organization ID

If you know which organization you're working with, you can query it directly. To list all organizations you have access to, use this query:

```graphql
query ListOrganizations {
  organizations(first: 10) {
    nodes {
      id
      title
    }
  }
}
```

### Getting schedule type IDs

Schedule types are [catalog items](../api-reference/objects.md#catalog-items) that classify schedules (e.g., "Maintenance", "Work hours", "Restrictions"). Query the types available to your organization:

```graphql
query ListScheduleTypes {
  scheduleTypes(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      code
      title
    }
  }
}
```

Example response:

```json
{
  "data": {
    "scheduleTypes": {
      "nodes": [
        {
          "id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
          "code": "MAINTENANCE",
          "title": "Maintenance"
        },
        {
          "id": "b1ffc99-9c0b-4ef8-bb6d-6bb9bd380a22",
          "code": "WORK_HOURS",
          "title": "Work hours"
        }
      ]
    }
  }
}
```

If no schedule types exist, you can create one using the [scheduleTypeCreate ](../api-reference/mutations.md#scheduletypecreate)mutation.

## Understanding schedule data

A schedule consists of metadata (title, type, organization) and calendar data stored in the `scheduleData` field, which accepts a value of [ScheduleData](../api-reference/scalars.md#scheduledata), a custom scalar containing a JSON value. The JSON structure follows the RFC 5545 conventions:

<table><thead><tr><th width="164.4000244140625">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>timezone</code></td><td>IANA timezone identifier (e.g., <code>Europe/Berlin</code>, <code>America/New_York</code>, <code>UTC</code>)</td></tr><tr><td><code>events</code></td><td>Array of time slots, each with start/end times and optional recurrence rules</td></tr></tbody></table>

Each event in the `events` array can include:

<table><thead><tr><th width="137.79998779296875">Field</th><th width="171.4000244140625">iCalendar equivalent</th><th>Description</th></tr></thead><tbody><tr><td><code>dtstart</code></td><td>DTSTART</td><td><strong>Required.</strong> Start time in ISO 8601 UTC format</td></tr><tr><td><code>dtend</code></td><td>DTEND</td><td>End time (mutually exclusive with <code>duration</code>)</td></tr><tr><td><code>duration</code></td><td>DURATION</td><td>Duration in ISO 8601 format, e.g., <code>PT3H</code> (mutually exclusive with <code>dtend</code>)</td></tr><tr><td><code>allDay</code></td><td>VALUE=DATE</td><td>When <code>true</code>, the event spans entire days</td></tr><tr><td><code>rrule</code></td><td>RRULE</td><td>Recurrence rule object defining repeat patterns</td></tr><tr><td><code>exdate</code></td><td>EXDATE</td><td>Array of dates to exclude from recurrence</td></tr><tr><td><code>rdate</code></td><td>RDATE</td><td>Array of additional dates to include</td></tr></tbody></table>

The `rrule` property supports these fields:

<table><thead><tr><th width="153">Field</th><th width="153.79998779296875">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>freq</code></td><td>String</td><td><strong>Required.</strong> <code>SECONDLY</code>, <code>MINUTELY</code>, <code>HOURLY</code>, <code>DAILY</code>, <code>WEEKLY</code>, <code>MONTHLY</code>, or <code>YEARLY</code></td></tr><tr><td><code>interval</code></td><td>Integer</td><td>Repeat every N periods (default: 1)</td></tr><tr><td><code>count</code></td><td>Integer</td><td>Stop after N occurrences</td></tr><tr><td><code>until</code></td><td>DateTime</td><td>Stop after this date (mutually exclusive with <code>count</code>)</td></tr><tr><td><code>byday</code></td><td>String[]</td><td>Days of week: <code>MO</code>, <code>TU</code>, <code>WE</code>, <code>TH</code>, <code>FR</code>, <code>SA</code>, <code>SU</code></td></tr><tr><td><code>bymonthday</code></td><td>Integer[]</td><td>Days of month: 1–31, or -31 to -1 for days from end (-1 = last day)</td></tr><tr><td><code>byyearday</code></td><td>Integer[]</td><td>Days of year: 1–366, or -366 to -1 for days from end (-1 = last day)</td></tr><tr><td><code>byweekno</code></td><td>Integer[]</td><td>Weeks of year: 1–53, or -53 to -1 (-1 = last week)</td></tr><tr><td><code>bymonth</code></td><td>Integer[]</td><td>Months: 1–12</td></tr><tr><td><code>byhour</code></td><td>Integer[]</td><td>Hours: 0–23</td></tr><tr><td><code>byminute</code></td><td>Integer[]</td><td>Minutes: 0–59</td></tr><tr><td><code>bysecond</code></td><td>Integer[]</td><td>Seconds: 0–60</td></tr><tr><td><code>wkst</code></td><td>String</td><td>Week start day: <code>MO</code> or <code>SU</code> (default: <code>MO</code>)</td></tr></tbody></table>

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
          dtstart: "2025-01-06T05:00:00Z"
          dtend: "2025-01-06T09:00:00Z"
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

* Times are in UTC. The `dtstart` of `05:00:00Z` equals 06:00 in Europe/Berlin (UTC+1 in winter). The `timezone` field tells consuming applications how to interpret and display these times.
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

<pre class="language-graphql"><code class="lang-graphql"><strong>mutation AddHolidayExceptions {
</strong>  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 1
    scheduleData: {
      timezone: "Europe/Berlin"
      events: [
        {
          dtstart: "2025-01-06T05:00:00Z"
          dtend: "2025-01-06T09:00:00Z"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
          }
          exdate: [
            "2025-04-21T05:00:00Z",
            "2025-05-05T05:00:00Z",
            "2025-06-09T05:00:00Z",
            "2025-10-06T05:00:00Z"
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
</code></pre>

The `exdate` times must match the event's `dtstart` time (05:00:00Z) for the exclusions to work correctly.

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
          dtstart: "2025-01-06T05:00:00Z"
          dtend: "2025-01-06T09:00:00Z"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
            until: "2025-12-31T23:59:59Z"
          }
          exdate: [
            "2025-04-21T05:00:00Z",
            "2025-05-05T05:00:00Z",
            "2025-06-09T05:00:00Z",
            "2025-10-06T05:00:00Z"
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

The schedule's version is now 3.
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
          dtstart: "2025-01-06T05:00:00Z"
          dtend: "2025-01-06T07:00:00Z"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
            until: "2025-12-31T23:59:59Z"
          }
          exdate: [
            "2025-04-21T05:00:00Z",
            "2025-05-05T05:00:00Z",
            "2025-06-09T05:00:00Z",
            "2025-10-06T05:00:00Z"
          ]
        },
        {
          dtstart: "2025-01-06T07:30:00Z"
          dtend: "2025-01-06T09:00:00Z"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO"]
            until: "2025-12-31T23:59:59Z"
          }
          exdate: [
            "2025-04-21T07:30:00Z",
            "2025-05-05T07:30:00Z",
            "2025-06-09T07:30:00Z",
            "2025-10-06T07:30:00Z"
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

The `version` parameter ensures you don't accidentally delete a schedule that someone else has modified. If the version doesn't match, you'll receive a conflict error.
{% endstep %}
{% endstepper %}

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

## Common patterns

**Every weekday:**

```json
{ "freq": "WEEKLY", "byday": ["MO", "TU", "WE", "TH", "FR"] }
```

**Every other week on Monday:**

```json
{ "freq": "WEEKLY", "interval": 2, "byday": ["MO"] }
```

**First and fifteenth of each month:**

```json
{ "freq": "MONTHLY", "bymonthday": [1, 15] }
```

**Last day of each month:**

```json
{ "freq": "MONTHLY", "bymonthday": [-1] }
```

**Every day at specific hours:**

```json
{ "freq": "DAILY", "byhour": [9, 14, 18] }
```

## Next steps

* TBD
