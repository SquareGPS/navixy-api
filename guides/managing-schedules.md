---
description: Create, update, query, and delete RFC 5545–compatible schedules.
---

# Managing schedules

Schedules in Navixy Repository API represent [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545) (iCalendar)-compliant calendar events that support recurrence rules, exceptions, and multiple time slots. This compliance enables integration with industry-standard calendar systems such as Google Calendar, Outlook, and Apple Calendar, allowing you to import and export scheduling data across platforms.

This guide walks you through creating, updating, and deleting schedules with Navixy Repository API.

## Prerequisites

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

A schedule consists of metadata (title, type, organization) and calendar data stored in the `scheduleData` field. The calendar data follows the RFC 5545 conventions:

<table><thead><tr><th width="164.4000244140625">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>timezone</code></td><td>IANA timezone identifier (e.g., <code>Europe/Berlin</code>, <code>America/New_York</code>, <code>UTC</code>)</td></tr><tr><td><code>events</code></td><td>Array of time slots, each with start/end times and optional recurrence rules</td></tr></tbody></table>

Each event in the `events` array can include:

<table><thead><tr><th width="137.79998779296875">Field</th><th width="171.4000244140625">iCalendar equivalent</th><th>Description</th></tr></thead><tbody><tr><td><code>dtstart</code></td><td>DTSTART</td><td>Start time in ISO 8601 UTC format</td></tr><tr><td><code>dtend</code></td><td>DTEND</td><td>End time (mutually exclusive with <code>duration</code>)</td></tr><tr><td><code>duration</code></td><td>DURATION</td><td>Duration in ISO 8601 format, e.g., <code>PT3H</code> (mutually exclusive with <code>dtend</code>)</td></tr><tr><td><code>allDay</code></td><td>VALUE=DATE</td><td>When <code>true</code>, the event spans entire days</td></tr><tr><td><code>rrule</code></td><td>RRULE</td><td>Recurrence rule object defining repeat patterns</td></tr><tr><td><code>exdate</code></td><td>EXDATE</td><td>Array of dates to exclude from recurrence</td></tr><tr><td><code>rdate</code></td><td>RDATE</td><td>Array of additional dates to include</td></tr></tbody></table>

## Creating a schedule

Use the [scheduleCreate ](../api-reference/mutations.md#schedulecreate)mutation to create a new schedule. You'll need to provide the organization ID, schedule type ID, title, and schedule data.

### Basic weekly schedule

This sample operation creates a warehouse work schedule that runs Monday through Friday, 9:00 AM to 6:00 PM (Europe/Moscow timezone):

```graphql
mutation CreateWarehouseSchedule {
  scheduleCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Warehouse work hours"
    scheduleData: {
      timezone: "Europe/Moscow"
      events: [
        {
          dtstart: "2025-01-06T06:00:00Z"
          dtend: "2025-01-06T15:00:00Z"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO", "TU", "WE", "TH", "FR"]
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

The response returns the created schedule with its ID and version:

```json
{
  "data": {
    "scheduleCreate": {
      "schedule": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 1,
        "title": "Warehouse work hours"
      }
    }
  }
}
```

Save the `id` and `version` — you'll need them for updates and deletion.

### Schedule with duration instead of end time

For maintenance windows or tasks with fixed duration, use `duration` instead of `dtend`. This example creates a monthly maintenance schedule on the 15th of each month, lasting 3 hours:

```graphql
mutation CreateMaintenanceSchedule {
  scheduleCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Monthly maintenance"
    scheduleData: {
      timezone: "Europe/Moscow"
      events: [
        {
          dtstart: "2025-01-15T11:00:00Z"
          duration: "PT3H"
          rrule: {
            freq: "MONTHLY"
            bymonthday: [15]
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

The duration format follows ISO 8601: `PT3H` means 3 hours, `PT30M` means 30 minutes, `PT1H30M` means 1 hour and 30 minutes.

### Schedule with multiple events

A single schedule can contain multiple events. This is useful for scenarios like refrigerator temperature modes or split shifts:

```graphql
mutation CreateRefrigeratorModes {
  scheduleCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Refrigerator modes"
    scheduleData: {
      timezone: "Europe/Moscow"
      events: [
        {
          dtstart: "2025-01-06T19:00:00Z"
          dtend: "2025-01-07T03:00:00Z"
          rrule: {
            freq: "DAILY"
          }
        },
        {
          dtstart: "2025-01-06T03:00:00Z"
          dtend: "2025-01-06T19:00:00Z"
          rrule: {
            freq: "DAILY"
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

### Non-recurring schedule (fixed date ranges)

For rental periods or one-time events, omit the `rrule` field entirely:

```graphql
mutation CreateRentalSchedule {
  scheduleCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Excavator rental"
    scheduleData: {
      timezone: "Europe/Moscow"
      events: [
        {
          dtstart: "2025-02-10T06:00:00Z"
          dtend: "2025-02-15T15:00:00Z"
        },
        {
          dtstart: "2025-03-01T06:00:00Z"
          dtend: "2025-03-10T15:00:00Z"
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

## Configuring recurrence rules

The `rrule` property defines how events repeat. It follows [RFC 5545 RRULE](https://www.rfc-editor.org/rfc/rfc5545#section-3.3.10) conventions. Common patterns include:

### Daily recurrence

Repeat every day:

```json
{
  "rrule": {
    "freq": "DAILY"
  }
}
```

Repeat every 2 days:

```json
{
  "rrule": {
    "freq": "DAILY",
    "interval": 2
  }
}
```

### Weekly recurrence

Repeat every week on specific days:

```json
{
  "rrule": {
    "freq": "WEEKLY",
    "byday": ["MO", "WE", "FR"]
  }
}
```

Day codes: `MO`, `TU`, `WE`, `TH`, `FR`, `SA`, `SU`

### Monthly recurrence

Repeat on specific days of the month:

```json
{
  "rrule": {
    "freq": "MONTHLY",
    "bymonthday": [1, 15]
  }
}
```

Use `-1` for the last day of the month:

```json
{
  "rrule": {
    "freq": "MONTHLY",
    "bymonthday": [-1]
  }
}
```

### Ending recurrence

By count (stop after N occurrences):

```json
{
  "rrule": {
    "freq": "WEEKLY",
    "byday": ["MO"],
    "count": 10
  }
}
```

By date (stop after a specific date):

```json
{
  "rrule": {
    "freq": "WEEKLY",
    "byday": ["MO"],
    "until": "2025-12-31T23:59:59Z"
  }
}
```

## Adding exception dates

Use `exdate` to exclude specific dates from a recurring schedule. This is useful for holidays or one-off cancellations.

This example creates a weekly Monday maintenance window but excludes holiday Mondays:

```graphql
mutation CreateScheduleWithExceptions {
  scheduleCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Weekly maintenance"
    scheduleData: {
      timezone: "UTC"
      events: [
        {
          dtstart: "2025-01-06T02:00:00Z"
          duration: "PT4H"
          rrule: {
            freq: "WEEKLY",
            byday: ["MO"]
          },
          exdate: [
            "2025-01-20T02:00:00Z",
            "2025-02-17T02:00:00Z",
            "2025-05-26T02:00:00Z",
            "2025-12-22T02:00:00Z"
          ]
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

The times in `exdate` should match the `dtstart` time of the recurring event.

## Updating a schedule

Use the [scheduleUpdate ](../api-reference/mutations.md#scheduleupdate)mutation to modify an existing schedule. Updates require the schedule's current `version` for [optimistic locking](../optimistic-locking.md) — this prevents conflicts when multiple users edit the same schedule.

### Updating the title

```graphql
mutation UpdateScheduleTitle {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 1
    title: "Warehouse hours (updated)"
  }) {
    schedule {
      id
      version
      title
    }
  }
}
```

The response includes the incremented version:

```json
{
  "data": {
    "scheduleUpdate": {
      "schedule": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 2,
        "title": "Warehouse hours (updated)"
      }
    }
  }
}
```

### Updating schedule data

When updating `scheduleData`, you must provide the complete new value — the API replaces the entire field, it doesn't merge with existing data.

\{% hint style="warning" %\} Always include all events and their full configuration when updating `scheduleData`. Omitting an event removes it from the schedule. \{% endhint %\}

```graphql
mutation UpdateScheduleData {
  scheduleUpdate(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 2
    scheduleData: {
      timezone: "Europe/Moscow"
      events: [
        {
          dtstart: "2025-01-06T06:00:00Z"
          dtend: "2025-01-06T15:00:00Z"
          rrule: {
            freq: "WEEKLY"
            byday: ["MO", "TU", "WE", "TH", "FR"]
          },
          exdate: [
            "2025-05-01T06:00:00Z"
          ]
        }
      ]
    }
  }) {
    schedule {
      id
      version
      title
      scheduleData
    }
  }
}
```

### Handling version conflicts

If the schedule has been modified since you fetched it, the API returns a `CONFLICT` error:

```json
{
  "errors": [
    {
      "message": "Entity has been modified by another request",
      "extensions": {
        "code": "CONFLICT",
        "status": 409,
        "expectedVersion": 2,
        "currentVersion": 3
      }
    }
  ]
}
```

To resolve this:

1. Query the schedule to get the current version and data
2. Merge your changes with the current state
3. Retry the mutation with the correct version

## Deleting a schedule

Use the `scheduleDelete` mutation to remove a schedule. Like updates, deletion requires the current version:

```graphql
mutation DeleteSchedule {
  scheduleDelete(input: {
    id: "019a6b2f-793e-807b-8001-555345529b44"
    version: 3
  }) {
    deletedId
  }
}
```

The response confirms the deletion:

```json
{
  "data": {
    "scheduleDelete": {
      "deletedId": "019a6b2f-793e-807b-8001-555345529b44"
    }
  }
}
```

## Querying schedules

### Get a single schedule

```graphql
query GetSchedule {
  node(id: "019a6b2f-793e-807b-8001-555345529b44") {
    ... on Schedule {
      id
      version
      title
      organization {
        id
        title
      }
      type {
        code
        title
      }
      scheduleData
    }
  }
}
```

### List schedules for an organization

```graphql
query ListSchedules {
  schedules(
    filter: { organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7" }
    first: 20
  ) {
    edges {
      node {
        id
        title
        type {
          code
        }
        scheduleData
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

## Common use cases

<table><thead><tr><th width="207.5999755859375">Use case</th><th>Configuration approach</th></tr></thead><tbody><tr><td>Work hours</td><td>Weekly recurrence with <code>byday</code> for weekdays</td></tr><tr><td>Maintenance windows</td><td>Monthly recurrence with <code>bymonthday</code>, use <code>duration</code> for fixed length</td></tr><tr><td>Driver shifts</td><td>Daily recurrence, multiple events for different shifts</td></tr><tr><td>Equipment rental</td><td>Non-recurring events with explicit date ranges</td></tr><tr><td>Holiday calendar</td><td>Non-recurring events, one per holiday</td></tr><tr><td>Night restrictions</td><td>Daily recurrence with overnight time span</td></tr></tbody></table>

## Next steps

* TBD
