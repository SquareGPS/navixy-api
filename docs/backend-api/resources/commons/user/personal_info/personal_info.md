---
title: /personal_info
description: /personal_info
---

## update(…)

Update user personal info.

Require plugin with **id=45**.

#### parameters:

*   **legal_type** – string. Either “legal\_entity”, “sole\_trader” or “individual”.
*   **first_name** – string. Contact person first name.
*   **middle_name** – string. Contact person middle name.
*   **last_name** – string. Contact person last name.
*   **phone** – string. 0-15 digits. optional. Contact phone. Not changes if not passed.
*   **post_country** – optional. string. Country part of user’s post address.
*   **post_index** – optional. string. Index part of user’s post address.
*   **post_region** – optional. string. Region part of user’s post address.
*   **post_city** – optional. string. City from post address.
*   **post\_street\_address** – optional. string. User’s post address,

and for “legal\_entity” or “sole\_trader”:

*   **iec** – string. Industrial Enterprises Classifier aka “KPP”. Used in Russia. For “legal_entity” only.
*   **legal_name** – string. User legal (juridical) name. For “legal_entity” only.
*   **okpo_code** - string, optional, 8 or 10 characters maximum. All-Russian Classifier of Enterprises and Organizations. Used in Russia.
*   **registered_country** – string. Country part of user’s registered address.
*   **registered_index** – string. Index part of user’s registered address.
*   **registered_region** – string. Region part of user’s registered address.
*   **registered_city** – string. City from registered address.
*   **registered\_street\_address** – string. User’s registered address.
*   **state_reg_num** - string, optional, 15 characters maximum. State registration number. E.g. EIN in USA, OGRN in Russia.
*   **tin** – string. Taxpayer identification number.


#### return:

    { "success": true }


#### errors:

*   222 (Plugin not found) – when plugin 45 not available for user
