---
title: Checkpoints
description: Checkpoints
---

# Task schedule checkpoints

These actions allow manipulating schedule checkpoint entries similarly to regular route checkpoints.

## API actions

API path: `/task/schedule/checkpoint`.


### delete

Delete checkpoint from route and reorder others. 
If route has two checkpoints then use transmute on the other checkpoint, because route must have
at least two checkpoints.

#### parameters

* **checkpoint_id** – **int**. Checkpoint ID.

#### response

```json5
{ "success": true }
```

### transmute

Transmute checkpoint to task and delete its route and other checkpoints in the route.

#### parameters

* **checkpoint_id** – **int**. Checkpoint ID.

#### response

```json5
{ "success": true }
```
