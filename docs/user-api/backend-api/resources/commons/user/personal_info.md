---
title: User personal info
description: Contains user personal info update API call. 
---

# User personal info

Contains user personal info update API call.


## API actions

API path: `/user/personal_info`.

### `update`

Updates user personal info.

Require a plugin with **id=45**.

#### Parameters

* `legal_type` – string. Either "legal_entity", "sole_trader" or "individual".
* `first_name` – string. Contact person first name.
* `middle_name` – string. Contact person middle name.
* `last_name` – string. Contact person last name.
* `phone` – string. 0-15 digits. Optional. Contact phone. Not changes if not passed.
* `post_country` – string. Optional. Country part of user's post address.
* `post_index` – string. Optional. Index part of user's post address.
* `post_region` – string. Optional. Region part of user's post address.
* `post_city` – string. Optional. City from post address.
* `post_street_address` – string. Optional. User's post address,

and for `legal_entity` or `sole_trader`:

* `iec` – string. Industrial Enterprises Classifier aka "KPP". Used in Russia. For `legal_entity` only.
* `legal_name` – string. User legal (juridical) name. For `legal_entity` only.
* `okpo_code` - string, optional, 8 or 10 characters maximum. All-Russian Classifier of Enterprises and Organizations. Used in Russia.
* `registered_country` – string. Country part of user's registered address.
* `registered_index` – string. Index part of user's registered address.
* `registered_region` – string. Region part of user's registered address.
* `registered_city` – string. City from registered address.
* `registered_street_address` – string. User's registered address.
* `state_reg_num` - string, optional, 15 characters maximum. State registration number. E.g. EIN in the USA, OGRN in Russia.
* `tin` – string. Taxpayer identification number.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/personal_info/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "first_name": "Charles", "middle_name": "Henry", "last_name": "Pearson", "legal_type": "legal_entity", "phone": "491761234567", "post_country": "Germany", "post_index": "61169", "post_region": "Hessen", "post_city": "Wiesbaden", "post_street_address": "Marienplatz 2", "registered_country": "Germany", "registered_index": "61169", "registered_region": "Hessen", "registered_city": "Wiesbaden", "registered_street_address": "Marienplatz 2", "state_reg_num": "12-3456789", "tin": "1131145180", "legal_name": "E. Biasi GmbH", "iec": "", "okpo_code": ""}'

    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 222 - Plugin not found – when plugin **45** not available for user.
