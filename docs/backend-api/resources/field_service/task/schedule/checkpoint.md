---
title: Task schedule checkpoint
description: Task schedule checkpoint
---

# Task schedule checkpoint

API path: `/task/schedule/checkpoint`.


## delete

Delete checkpoint from route and reorder others. 
If route has two checkpoints then use transmute on the other checkpoint, because route must have
at least two checkpoints.

#### parameters

* **checkpoint_id** – **int**. Checkpoint ID.

#### return

```json
{ "success": true }
```

## transmute

Transmute checkpoint to task and delete its route and other checkpoints in the route.

#### parameters

* **checkpoint_id** – **int**. Checkpoint ID.

#### return

```json
{ "success": true }
```
