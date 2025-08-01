# Flexible resource management patterns

The Navixy Repository API uses a consistent pattern across all resources that support flexible creation and progressive enhancement. This pattern applies to:

* **Inventory Items** (master and slave)
* **Assets**
* **Asset Links**
* **Inventories**

### Core pattern: Progressive resource development

#### 1. Minimal creation

Start with just the required fields (often only a `label`):

```bash
curl -X POST {BASE_URL}/{resource}/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Quick identifier"
  }'
```

**Benefits:**

* Rapid prototyping
* Bulk imports without full details
* Placeholder creation for future configuration

#### 2. Progressive enhancement

Add details as they become available through updates:

```bash
curl -X POST {BASE_URL}/{resource}/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "label": "Updated label",
    "additional_field": "value",
    "relationship_id": 456
  }'
```

**Benefits:**

* Flexible workflows
* No need to have all information upfront
* Adapt to changing requirements

#### 3. Adding relationships

Connect resources when relationships become clear:

For direct relationships (update):

```bash
curl -X POST {BASE_URL}/{resource}/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "related_resource_id": 789
  }'
```

For many-to-many relationships (dedicated endpoints):

```bash
curl -X POST {BASE_URL}/{resource}/set \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "resource_id": 123,
    "related_id": 789
  }'
```

**Benefits:**

* Pre-provision resources
* Maintain spare pools
* Flexible reassignment

### Resource-specific applications

#### Inventory Items (Master)

**Minimal → Configured → Assigned → Activated**

Stage 1: Minimal

```bash
curl -X POST {BASE_URL}/inventory_item/master/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "GPS Unit Batch 2024-01"
  }'
```

Stage 2: Add technical details

```bash
curl -X POST {BASE_URL}/inventory_item/master/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "label": "GPS Unit 001",
    "device_id": "123456789",
    "model": "telfmb125",
    "inventory_id": 45
  }'
```

Stage 3: Assign to asset

```bash
curl -X POST {BASE_URL}/inventory_item/master/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 123,
    "label": "GPS Unit 001",
    "asset_id": 789
  }'
```

Stage 4: Activate

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

#### Inventory Items (Slave)

**Minimal → Configured → Paired**

Stage 1: Create unpaired sensors

```bash
curl -X POST {BASE_URL}/inventory_item/slave/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Temperature Sensor Batch 2024"
  }'
```

Stage 2: Add details

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

Stage 3: Pair when deployed

```bash
curl -X POST {BASE_URL}/inventory_item/slave/pair \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 456,
    "master_id": 123
  }'
```

#### Assets

**Minimal → Detailed → Device-Enabled**

Stage 1: Create asset

```bash
curl -X POST {BASE_URL}/asset/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "type_id": 12,
    "label": "Fleet Vehicle",
    "fields": {}
  }'
```

Stage 2: Add custom field data

```bash
curl -X POST {BASE_URL}/asset/update \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 789,
    "label": "Fleet Vehicle #123",
    "fields": {
      "55": {"type": "text", "value": "Toyota Camry"},
      "56": {"type": "text", "value": "2024"}
    }
  }'
```

Stage 3: Devices automatically link to this asset via asset\_id in inventory item create/update

#### Asset Links

**Empty → Populated → Reorganized**

Stage 1: Create empty link

```bash
curl -X POST {BASE_URL}/asset_link/create \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Morning Shift",
    "asset_ids": []
  }'
```

Stage 2: Add assets progressively

```bash
curl -X POST {BASE_URL}/asset_link/set \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 999,
    "asset_id": 789
  }'
```

Stage 3: Reorganize as needed

```bash
curl -X POST {BASE_URL}/asset_link/remove \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "link_id": 999,
    "asset_id": 789
  }'
```

### Common Workflows

#### Workflow 1: Bulk Import

For migrating from other systems:

1. Create all resources with minimal info
2. Run update passes to add details
3. Establish relationships in final pass
4. Activate devices when ready

#### Workflow 2: Just-in-Time Configuration

For dynamic operations:

1. Create resources as needed
2. Configure when deployed
3. Update relationships in real-time
4. Maintain history through relationship changes

#### Workflow 3: Pre-Provisioning

For enterprise deployments:

1. Bulk create future resources
2. Organize into logical groups
3. Configure as equipment arrives
4. Deploy with full configuration

#### Workflow 4: Spare Parts Management

For maintaining reserves:

1. Create items without assignments
2. Keep in "unassigned" state
3. Quick assignment when needed
4. Return to pool when finished

### State Tracking

Resources progress through implicit states based on field population:

| State          | Inventory Item                               | Asset                | Asset Link      |
| -------------- | -------------------------------------------- | -------------------- | --------------- |
| **Minimal**    | Has label only                               | Has type and label   | Has label only  |
| **Configured** | Has device details                           | Has custom fields    | Has description |
| **Assigned**   | Has inventory\_id                            | Has linked devices   | Has asset\_ids  |
| **Connected**  | Has asset\_id (master) or master\_id (slave) | Part of asset links  | Fully populated |
| **Active**     | Successfully activated                       | Devices transmitting | In use          |
| **Archived**   | Soft-deleted                                 | Removed              | Deleted         |

### Best Practices

#### 1. Start Simple

* Create with minimal required fields
* Add complexity only when needed
* Use labels that help identify resources during configuration

#### 2. Use Consistent Patterns

* Apply the same workflow across resource types
* Maintain naming conventions
* Document your organization's patterns

#### 3. Plan for Change

* Design for reassignment
* Keep audit trails through updates
* Use descriptive labels that survive changes

#### 4. Optimize for Your Use Case

* **High Volume**: Use minimal creation for speed
* **High Complexity**: Use full creation for completeness
* **Dynamic Operations**: Use progressive enhancement

### Validation Rules

While fields are optional, certain operations have requirements:

| Operation         | Required Fields                              |
| ----------------- | -------------------------------------------- |
| Device Activation | `device_id`, `model`, `activation_method_id` |
| Slave Pairing     | Valid `master_id`                            |
| Asset Creation    | Valid `type_id`                              |
| Link Population   | Valid `asset_ids`                            |

### FAQ

**Q: Why are so many fields optional?** A: To support diverse workflows from quick prototyping to complex enterprise deployments. This flexibility allows you to work with incomplete data and enhance it over time.

**Q: Can resources exist without relationships?** A: Yes. Items without inventories, slaves without masters, and assets without devices are all valid states that support pre-provisioning and spare management.

**Q: How do I ensure data quality with optional fields?** A: Implement validation at the business logic layer. The API provides flexibility; your application provides constraints based on your specific needs.

**Q: What happens to relationships when resources are deleted?** A: Relationships are automatically cleaned up. Deleted assets are removed from links, deleted masters unpair their slaves, etc.
