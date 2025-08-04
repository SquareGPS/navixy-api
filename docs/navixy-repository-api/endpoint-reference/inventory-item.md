# Inventory item

Inventory items are individual devices or components that belong to an inventory. Each item represents a physical unit, such as a tracker or accessory, used to manage and operate an organization's equipment.

### Master items

#### Master item object

{% openapi-schemas spec="navixy-repo" schemas="InventoryMasterItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

#### Master item endpoints

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/list" method="get" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/list" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/read" method="get" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/update" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/model/list" method="get" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/activate" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/master/archive" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

### Slave item

#### Slave item object

{% openapi-schemas spec="navixy-repo" schemas="InventorySlaveItem" grouped="true" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-schemas %}

#### Slave item endpoints

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/list" method="get" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/list" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/create" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/read" method="get" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/update" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/delete" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="navixy-repo" path="/v0/inventory_item/slave/pair" method="post" %}
[OpenAPI navixy-repo](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/navixy-repo/docs/navixy-repository-api/resources/navixy-repo-api-specification.yaml)
{% endopenapi-operation %}
