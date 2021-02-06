---
title: /equipment
description: /equipment
---

# equipment/

## equipment data structure:

```json
{
  "equip_id": 33, 
  "model_name": "SPT10 SB", 
  "model_code": "pt10", //model code which should be inserted to tracker bundles
  "vendor": "3. NAVIXY S Series (personal)",
  "name": "NAVIXY S10"
}
```
    
## list

Returns list of all equipment which can be assigned to tracker bundles. 

### required permissions:

*   **tracker_bundles**: "read"

### return

```json
{
    "success": true,
    "list" : [ <equipment> , ... ] 
}
```