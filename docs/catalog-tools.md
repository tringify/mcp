# Catalog tools

Generated from the hosted MCP tool registry. Refresh the connection’s tool list to discover released additions; new permissions require new approval.

Tool arguments follow the linked Store API contract. Path and query parameters are named arguments alongside body fields; `variantId` is exposed as `variant_id`. Attribute lists additionally accept `summary: true`. Translation writes accept an optional `idempotency_key`.

App-only product purchase-requirement endpoints are excluded: a user connection cannot act as an installed app. MCP mutations keep the existing resource webhook behavior; webhook subscription management is not included.

## Products

| Tool | API operation | Required access |
| --- | --- | --- |
| `get_product_limits` | `GET /api/2025-01/products/limits` | `store:products:read` |
| `list_products` | `GET /api/2025-01/products` | `store:products:read` |
| `get_product` | `GET /api/2025-01/products/{id}` | `store:products:read` |
| `get_product_quantity_pricing` | `GET /api/2025-01/products/{id}/quantity-pricing` | `store:products:read` |
| `list_product_variants` | `GET /api/2025-01/products/{id}/variants` | `store:products:read` |
| `get_product_variant` | `GET /api/2025-01/products/{id}/variants/{variantId}` | `store:products:read` |
| `create_product` | `POST /api/2025-01/products` | `store:products:write` |
| `update_product` | `PUT /api/2025-01/products/{id}` | `store:products:write` |
| `duplicate_product` | `POST /api/2025-01/products/{id}/duplicate` | `store:products:write` |
| `delete_product` | `DELETE /api/2025-01/products/{id}` | `store:products:write` |
| `list_product_metafields` | `GET /api/2025-01/products/{id}/metafields` | `store:products:read` |
| `set_product_metafield` | `PUT /api/2025-01/products/{id}/metafields` | `store:products:write` |
| `get_product_metafield_translation` | `GET /api/2025-01/products/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_product_metafield_translation` | `PUT /api/2025-01/products/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `list_product_variant_metafields` | `GET /api/2025-01/products/{id}/variants/{variantId}/metafields` | `store:products:read` |
| `set_product_variant_metafield` | `PUT /api/2025-01/products/{id}/variants/{variantId}/metafields` | `store:products:write` |
| `get_product_variant_metafield_translation` | `GET /api/2025-01/products/{id}/variants/{variantId}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_product_variant_metafield_translation` | `PUT /api/2025-01/products/{id}/variants/{variantId}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `bulk_update_product_status` | `POST /api/2025-01/products/bulk-status` | `store:products:write` |
| `bulk_update_product_tags` | `POST /api/2025-01/products/bulk-tags` | `store:products:write` |
| `bulk_update_product_categories` | `POST /api/2025-01/products/bulk-categories` | `store:products:write` |
| `bulk_update_product_channels` | `POST /api/2025-01/products/bulk-channels` | `store:products:write` |
| `bulk_set_product_vendor` | `POST /api/2025-01/products/bulk-vendor` | `store:products:write` |
| `bulk_set_product_brand` | `POST /api/2025-01/products/bulk-brand` | `store:products:write` |
| `bulk_delete_products` | `POST /api/2025-01/products/bulk-delete` | `store:products:write` |
| `get_product_translation` | `GET /api/2025-01/products/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_product_translation` | `PUT /api/2025-01/products/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_product_translations` | `GET /api/2025-01/products/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_product_translations` | `PUT /api/2025-01/products/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_product_variant_translation` | `GET /api/2025-01/products/{id}/variants/{variantId}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_product_variant_translation` | `PUT /api/2025-01/products/{id}/variants/{variantId}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Collections

| Tool | API operation | Required access |
| --- | --- | --- |
| `get_collection_limits` | `GET /api/2025-01/collections/limits` | `store:products:read` |
| `list_collections` | `GET /api/2025-01/collections` | `store:products:read` |
| `search_collections` | `GET /api/2025-01/collections/search` | `store:products:read` |
| `get_collection` | `GET /api/2025-01/collections/{id}` | `store:products:read` |
| `list_collection_metafields` | `GET /api/2025-01/collections/{id}/metafields` | `store:products:read` |
| `set_collection_metafield` | `PUT /api/2025-01/collections/{id}/metafields` | `store:products:write` |
| `get_collection_metafield_translation` | `GET /api/2025-01/collections/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_collection_metafield_translation` | `PUT /api/2025-01/collections/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `create_collection` | `POST /api/2025-01/collections` | `store:products:write` |
| `update_collection` | `PUT /api/2025-01/collections/{id}` | `store:products:write` |
| `delete_collection` | `DELETE /api/2025-01/collections/{id}` | `store:products:write` |
| `bulk_delete_collections` | `POST /api/2025-01/collections/bulk-delete` | `store:products:write` |
| `bulk_update_collection_status` | `POST /api/2025-01/collections/bulk-activate` | `store:products:write` |
| `list_collection_products` | `GET /api/2025-01/collections/{id}/products` | `store:products:read` |
| `list_collection_product_details` | `GET /api/2025-01/collections/{id}/products/details` | `store:products:read` |
| `list_collection_rules` | `GET /api/2025-01/collections/{id}/rules` | `store:products:read` |
| `add_collection_rule` | `POST /api/2025-01/collections/{id}/rules` | `store:products:write` |
| `update_collection_rule` | `PUT /api/2025-01/collections/{id}/rules/{rule_id}` | `store:products:write` |
| `delete_collection_rule` | `DELETE /api/2025-01/collections/{id}/rules/{rule_id}` | `store:products:write` |
| `get_collection_translation` | `GET /api/2025-01/collections/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_collection_translation` | `PUT /api/2025-01/collections/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_collection_translations` | `GET /api/2025-01/collections/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_collection_translations` | `PUT /api/2025-01/collections/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Categories

| Tool | API operation | Required access |
| --- | --- | --- |
| `get_category_limits` | `GET /api/2025-01/categories/limits` | `store:products:read` |
| `list_categories` | `GET /api/2025-01/categories` | `store:products:read` |
| `search_categories` | `GET /api/2025-01/categories/search` | `store:products:read` |
| `get_category` | `GET /api/2025-01/categories/{id}` | `store:products:read` |
| `list_category_metafields` | `GET /api/2025-01/categories/{id}/metafields` | `store:products:read` |
| `set_category_metafield` | `PUT /api/2025-01/categories/{id}/metafields` | `store:products:write` |
| `get_category_metafield_translation` | `GET /api/2025-01/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_category_metafield_translation` | `PUT /api/2025-01/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `create_category` | `POST /api/2025-01/categories` | `store:products:write` |
| `bulk_create_categories` | `POST /api/2025-01/categories/bulk-create` | `store:products:write` |
| `update_category` | `PUT /api/2025-01/categories/{id}` | `store:products:write` |
| `delete_category` | `DELETE /api/2025-01/categories/{id}` | `store:products:write` |
| `bulk_delete_categories` | `POST /api/2025-01/categories/bulk-delete` | `store:products:write` |
| `get_category_translation` | `GET /api/2025-01/categories/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_category_translation` | `PUT /api/2025-01/categories/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_category_translations` | `GET /api/2025-01/categories/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_category_translations` | `PUT /api/2025-01/categories/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Attributes

| Tool | API operation | Required access |
| --- | --- | --- |
| `get_attribute_limits` | `GET /api/2025-01/attributes/limits` | `store:products:read` |
| `list_attributes` | `GET /api/2025-01/attributes` | `store:products:read` |
| `search_attributes` | `GET /api/2025-01/attributes/search` | `store:products:read` |
| `get_attribute` | `GET /api/2025-01/attributes/{id}` | `store:products:read` |
| `create_attribute` | `POST /api/2025-01/attributes` | `store:products:write` |
| `update_attribute` | `PUT /api/2025-01/attributes/{id}` | `store:products:write` |
| `delete_attribute` | `DELETE /api/2025-01/attributes/{id}` | `store:products:write` |
| `bulk_delete_attributes` | `POST /api/2025-01/attributes/bulk-delete` | `store:products:write` |
| `reorder_attributes` | `POST /api/2025-01/attributes/reorder` | `store:products:write` |
| `reorder_attribute_options` | `POST /api/2025-01/attributes/{id}/options/reorder` | `store:products:write` |
| `get_attribute_translation` | `GET /api/2025-01/attributes/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_attribute_translation` | `PUT /api/2025-01/attributes/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_attribute_translations` | `GET /api/2025-01/attributes/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_attribute_translations` | `PUT /api/2025-01/attributes/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Attribute options

| Tool | API operation | Required access |
| --- | --- | --- |
| `get_attribute_option_translation` | `GET /api/2025-01/attribute-options/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_attribute_option_translation` | `PUT /api/2025-01/attribute-options/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_attribute_option_translations` | `GET /api/2025-01/attribute-options/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_attribute_option_translations` | `PUT /api/2025-01/attribute-options/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Metafield discovery

| Tool | API operation | Required access |
| --- | --- | --- |
| `list_catalog_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | `store:products:read` |

## Languages

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_languages` | `GET /api/2025-01/languages` | `store:settings.languages:read` |
| `set_languages` | `PUT /api/2025-01/languages` | `store:settings.languages:write` |
| `set_default_language` | `PUT /api/2025-01/languages/default` | `store:settings.languages:write` |
| `delete_language_translations` | `DELETE /api/2025-01/languages/{locale}/translations` | `store:settings.languages:write` |
| `list_available_languages` | `GET /api/2025-01/reference/languages` | `store:settings.languages:read` |
