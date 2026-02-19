# Navixy API Resources Map

This document provides a comprehensive map of all API resources available in the Navixy API documentation repository.

**Generated:** 2026-02-19

## Overview

The Navixy API is organized into 5 main categories:
1. **Backend API** - Main user-facing API for GPS/Vehicle telematics
2. **Panel API** - Admin panel API for platform configuration
3. **Eco Fleet API** - Eco Fleet specific operations
4. **Data Warehouse API** - Raw IoT data retrieval
5. **Repository API** - Asset management system

---

## 1. Backend API

**Base Path:** `/v2`

**Base URLs:**
- EU: `https://api.eu.navixy.com/v2`
- US: `https://api.us.navixy.com/v2`
- On-Premise: `https://api.your_domain`

**Authentication:** API Key hash (session hash)

**Rate Limits:** 50 requests per second per user and per IP address

### Tracking Resources

#### `/tracker`
- **Description:** Tracker object structure and API calls to interact with tracking devices
- **Actions:** read, list, corrupt, delete, change_phone, get_diagnostics, get_fuel, get_inputs, batch_get_inputs, get_outputs, batch_get_outputs, output/update, get_last_gps_point, get_readings, get_state, get_states, list_models, tags/set, location_request, register, register_retry, register_quick, replace, replace_quick, replace_retry, send_command, raw_command/send
- **Sub-resources:**
  - `/tracker/group` - assign, create, delete, list, update
  - `/tracker/sensor` - sensor management
    - `/tracker/sensor/input_name` - list
    - `/tracker/sensor/calibration_data` - read, update, upload_omnicomm
  - `/tracker/settings` - read, update
    - `/tracker/settings/tracking` - read, update
    - `/tracker/settings/lbs` - read, update
    - `/tracker/settings/special`
  - `/tracker/rule` - bind, create, delete, list, unbind, update
  - `/tracker/stats/mileage` - read
  - `/tracker/avatar` - upload
  - `/tracker/output` - set_all, set
  - `/tracker/chat` - list, mark_read_all, mark_read, send, broadcast, updated/list, unread/count
  - `/tracker/counter` - read, update, get_counters, value/get, value/list, value/set, data/read

#### `/zone`
- **Description:** Geofence zones for tracking
- **Actions:** batch_convert, create, delete, list, read, search_location, update, upload, download

#### `/track`
- **Description:** Track data retrieval
- **Sub-resources:**
  - `/track/waybill` - download

#### `/route`
- **Description:** Route planning and optimization
- **Sub-resources:**
  - `/route/google` - get
  - `/route/osrm` - get
  - `/route/progorod` - get

#### `/status`
- **Description:** Status management
- **Actions:** create, delete, list, update
- **Sub-resources:**
  - `/status/listing` - create, delete, list, update

#### `/asset/track`
- **Description:** Asset tracking
- **Sub-resources:**
  - `/asset_group` - create, list, set, remove, update, delete

#### `/beacon`
- **Description:** Beacon data

#### `/geocoder`
- **Description:** Geocoding services
- **Actions:** search_address, search_location

#### `/map_layer`
- **Description:** Map layer management
- **Actions:** read, list, upload, update, delete

### Fleet Resources

#### `/vehicle`
- **Description:** Vehicle management
- **Actions:** create, delete, list, read, update, batch_convert
- **Sub-resources:**
  - `/vehicle/service_task` - batch_create, create, delete, download, list, read, set_status, update

#### `/driver/journal`
- **Description:** Driver journal management
- **Sub-resources:**
  - `/driver/journal/entry` - list, create, update, delete, download

### Field Service Resources

#### `/task`
- **Description:** Field service task management
- **Actions:** assign, batch_convert, count, create, delete, list, read, transmute, update
- **Sub-resources:**
  - `/task/form` - read, download
  - `/task/schedule` - create, delete, list, read, update

#### `/employee`
- **Description:** Employee management
- **Actions:** list, create, read, update, delete, batch_convert

#### `/place`
- **Description:** Place/POI management
- **Actions:** read, list, create, search_location, update, delete, batch_convert, upload

#### `/form`
- **Description:** Form management
- **Actions:** read, download
- **Sub-resources:**
  - `/form/template` - list, create, read, update, delete, stats/read

#### `/checkin`
- **Description:** Check-in management
- **Actions:** read, list, delete, create, image/create, form/create, form/file/create

### Common Resources

#### `/user`
- **Description:** User management
- **Actions:** activate, auth, get_info, get_tariff_restrictions, logout, resend_activation
- **Sub-resources:**
  - `/user/password` - change, set
  - `/user/settings` - read, update, file_storage/update
  - `/user/session` - renew
    - `/user/session/push_token` - bind, delete
  - `/user/audit` - checkin

#### `/subuser`
- **Description:** Sub-user management
- **Actions:** delete, list, register, update
- **Sub-resources:**
  - `/subuser/zones` - bind, unbind, list_ids, list
  - `/subuser/tracker` - bind, list, unbind

#### `/tag`
- **Description:** Tag management
- **Actions:** create, delete, list, search, update

#### `/entity`
- **Description:** Entity customization
- **Actions:** list
- **Sub-resources:**
  - `/entity/fields` - read, update

#### `/history`
- **Description:** History data
- **Sub-resources:**
  - `/history/tracker` - list
  - `/history/unread` - list, count

#### `/report`
- **Description:** Report management
- **Sub-resources:**
  - `/report/schedule` - create, delete, list, update

#### `/notification`
- **Description:** Notification management
- **Actions:** list

#### `/plugin`
- **Description:** Registration plugin management
- **Actions:** list

#### `/billing`
- **Description:** Billing operations
- **Sub-resources:**
  - `/subscription` - cancel, list
  - `/bill` - create, list
  - `/tariff` - list

---

## 2. Panel API

**Base Path:** `/v2/panel`

**Authentication:** Panel API Key hash

### Resources

#### `panel/account`
- **Description:** Panel account authentication and permissions
- **Actions:** auth, get_permissions, logout

#### `panel/dealer`
- **Description:** Dealer management
- **Actions:** get_info
- **Sub-resources:**
  - `panel/dealer/settings`
    - `panel/dealer/settings/service`
    - `panel/dealer/settings/notification`

#### `panel/user`
- **Description:** User management in admin panel
- **Actions:** create, read, update, change_password, corrupt, upload, list, export, session/create, transaction/list, transaction/change_balance

#### `panel/subpaas`
- **Description:** Sub-PaaS management
- **Actions:** create, delete, read, update

---

## 3. Eco Fleet API

**Base Path:** `/eco-fleet/v1`

**Authentication:** OAuth 2.0 Bearer token

### Resources

#### `/trackers`
- **Description:** Eco Fleet tracker operations
- **Sub-resources:**
  - `/trackers/$tracker_id/resampling`
  - `/trackers/sensors`
    - `/trackers/sensors/quality` - GET

---

## 4. Data Warehouse API

**Base Path:** `/dwh/v1`

**Authentication:** OAuth 2.0 Bearer token

### Resources

#### `/tracker`
- **Description:** Data warehouse tracker operations
- **Sub-resources:**
  - `/tracker/raw_data` - get_inputs, read

---

## 5. Repository API

**Base Path:** `/repo/v0`

**Base URLs:**
- EU: `https://api.navixy.com/repo/v0`
- US: `https://api.us.navixy.com/repo/v0`

**Auth URLs:**
- EU: `https://keycloak.navixy.com`
- US: `https://keycloak.us.navixy.com`

**Authentication:** OAuth 2.0 Bearer token

### Resources

#### `/asset`
- **Description:** Assets represent individual real-world objects stored in the system
- **Actions:** list, create, read, update, delete

#### `/asset_type`
- **Description:** Model that defines the structure of custom property fields and display configuration for assets
- **Actions:** list, create, read, update, delete

#### `/asset_link`
- **Description:** Collections of assets used to organize and manage equipment
- **Actions:** list, create, read, update, delete, set, remove

#### `/inventory`
- **Description:** Collections of devices used to organize and manage equipment
- **Actions:** list, create, read, update, delete

#### `/inventory_item`
- **Description:** Devices stored in inventories
- **Sub-resources:**
  - `/inventory_item/master` - list, create, read, update, model/list, activate, archive
  - `/inventory_item/slave` - list, create, read, update, delete, pair

---

## Statistics

- **Total API Categories:** 5
- **Total Resources:** 100+
- **Documentation Base:** `docs/`

## Notes

- API calls follow the pattern: `/resource/sub_resource/action`
- Parameters can be passed via HTTP POST `application/json` (recommended), HTTP POST `application/x-www-form-urlencoded`, or HTTP GET (not recommended)
- All responses are in JSON format
- API evolves over time - clients should ignore unsupported JSON fields
- NULL fields are omitted from responses

## Documentation Structure

Each resource documentation typically includes:
- Introduction
- Object structure (if applicable)
- API Actions with:
  - Action description
  - Requirements (permissions)
  - Parameters table
  - Examples (cURL and HTTP GET)
  - Response examples
  - Error codes

For detailed information about each resource, refer to the documentation files in the `docs/` directory.
