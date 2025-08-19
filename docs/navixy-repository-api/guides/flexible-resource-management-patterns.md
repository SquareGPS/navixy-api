---
hidden: true
---

# Flexible resource management patterns

Navixy Repository API uses a consistent pattern across all resources that support flexible creation and progressive enhancement. This pattern applies to:

* **Inventories**
* **Inventory items** (master and slave)
* **Assets**
* **Asset links**

### Core pattern: progressive resource development

#### 1. Minimal creation

Start with just the required fields (often only a `label`).\
Example: Create an inventory item.

```bash
curl -X POST {BASE_URL}/inventory_item/master/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Fleet Tracker Unit 001"
  }'
```

**Advantages:**

* Rapid prototyping
* Manual import operations without full details
* Placeholder creation for future configuration

#### 2. Progressive enhancement

Add details as they become available through updates.\
Example: Adding device details to a master item:

```bash
curl -X POST {BASE_URL}/inventory_item/master/update \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
 "id": 456,
 "device_id": "359632104567890",
 "model": "telfmb125",
 "inventory_id": 123
 }'
```

**Advantages:**

* Flexible workflows
* No need to enter all information upfront
* Adapt to changing requirements

#### 3. Adding relationships

Create resources now and connect them later when relationships become clear. This pattern supports real-world scenarios where you don't have all the information upfront.

**Direct relationships** (parameters belonging to the resource):

Example: To assign a GPS tracker to a vehicle, use this request:

```bash
curl -X POST {BASE_URL}/inventory_item/master/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 456,
    "asset_id": 789
  }'
```

Other direct relationships:

* **Slave → Master**: Set `master_id` on the slave item
* **Item → Inventory**: Set `inventory_id` on item
* **Asset → Devices**: Devices reference assets via `asset_id`

**Many-to-many relationships** (dedicated endpoints):

Example: To add a vehicle to a delivery route via asset link, use this request:

```bash
curl -X POST {BASE_URL}/asset_link/set \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 999,
    "asset_id": 789
  }'
```

**Advantages:**

* Pre-provision resources
* Maintain spare pools
* Flexible reassignment

### Resource-specific applications

#### Inventory items (master)

**Minimal → Configured → Assigned → Activated**

Step 1. Add only the required information

```bash
curl -X POST {BASE_URL}/inventory_item/master/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "GPS Unit 001"
  }'
```

Step 2. Add technical details

```bash
curl -X POST {BASE_URL}/inventory_item/master/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 556,
    "device_id": "123456789",
    "model": "telfmb125",
    "inventory_id": 45
  }'
```

Step 3. Assign to an asset

```bash
curl -X POST {BASE_URL}/inventory_item/master/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 556,
    "asset_id": 789
  }'
```

Step 3. Activate

```bash
curl -X POST {BASE_URL}/inventory_item/master/activate \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "activation_method_id": 1,
    "fields": {...}
  }'
```

#### Inventory items (slave)

**Minimal → Configured → Paired**

Step 1. Create unpaired sensors

```bash
curl -X POST {BASE_URL}/inventory_item/slave/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Temperature Sensor Batch 2024"
  }'
```

Step 2. Add details

```bash
curl -X POST {BASE_URL}/inventory_item/slave/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 456,
    "label": "Temp Sensor 001",
    "inventory_id": 45
  }'
```

Step 3. Pair when deployed

```bash
curl -X POST {BASE_URL}/inventory_item/slave/pair \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 456,
    "master_id": 556
  }'
```

#### Assets

**Minimal → Detailed → Device-Enabled**

Step 1. Create an asset based on an existing asset type:

```bash
curl -X POST {BASE_URL}/asset/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "type_id": 45,
    "label": "Fleet Vehicle 1",
    "fields": {}
  }'
```

Step 2. Add custom field data

```bash
curl -X POST {BASE_URL}/asset/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 789,
    "label": "Fleet Vehicle 1",
    "fields": {
      "55": {"type": "text", "value": "Toyota Camry"},
      "56": {"type": "integer", "value": 2024}
    }
  }'
```

Step 3. Link devices to this asset

```bash
curl -X POST {BASE_URL}/inventory_item/master/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "label": "Vehicle Tracker",
    "asset_id": 789
  }'
```

#### Asset links

**Empty → Populated → Reorganized**

Step 1. Create an empty asset link

```bash
curl -X POST {BASE_URL}/asset_link/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Morning Shift",
    "asset_ids": []
  }'
```

Step 2. Add assets

```bash
curl -X POST {BASE_URL}/asset_link/set \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 999,
    "asset_id": 789
  }'
```

Step 3. Reorganize as needed

```bash
curl -X POST {BASE_URL}/asset_link/remove \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 999,
    "asset_id": 789
  }'
```

### Common workflows

#### Workflow 1: Bulk import

For migrating from other systems:

1. Create all resources with minimal info
2. Run update passes to add details
3. Establish relationships in the final pass
4. Activate devices when ready

#### Workflow 2: Just-in-time configuration

For dynamic operations:

1. Create resources as needed
2. Configure when deployed
3. Update relationships in real-time
4. Maintain history through relationship changes

#### Workflow 3: Pre-provisioning

For enterprise deployments:

1. Bulk create future resources
2. Organize into logical groups
3. Configure as equipment arrives
4. Deploy with full configuration

#### Workflow 4: Spare parts management

For maintaining reserves:

1. Create items without assignments
2. Keep in "unassigned" state
3. Quick assignment when needed
4. Return to the pool when finished

### Best practices

#### 1. Start simple

* Create with minimal required fields
* Add complexity only when needed
* Use labels that help identify resources during configuration

#### 2. Use consistent patterns

* Apply the same workflow across resource types
* Maintain naming conventions
* Document your organization's patterns

#### 3. Plan for change

* Design for reassignment
* Keep audit trails through updates
* Use descriptive labels that survive changes

#### 4. Optimize for your use case

* **High volume**: Use minimal creation for speed
* **High complexity**: Use full creation for completeness
* **Dynamic operations**: Use progressive enhancement
