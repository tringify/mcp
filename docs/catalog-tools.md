# MCP tool inventory

Every store-data tool below uses its corresponding Store API operation. The MCP supplies the connected user and store; tool arguments cannot choose another identity or store.

Path and query parameters are named arguments alongside body fields. `variantId` is exposed as `variant_id`. File tools use `library: media|site_assets` in place of API `type` or `file_type`, and `media_type` for the API `media` filter. Attribute lists accept `summary: true`. Content translation writes accept an optional `idempotency_key`.

App-owned product purchase-requirement endpoints require an installed app identity and are not exposed through user connections. Normal resource webhooks apply; webhook subscription management is not included.

## Products

| Tool | Store API operation | Required access |
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

| Tool | Store API operation | Required access |
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

| Tool | Store API operation | Required access |
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

| Tool | Store API operation | Required access |
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

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_attribute_option_translation` | `GET /api/2025-01/attribute-options/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_attribute_option_translation` | `PUT /api/2025-01/attribute-options/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_attribute_option_translations` | `GET /api/2025-01/attribute-options/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_attribute_option_translations` | `PUT /api/2025-01/attribute-options/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Metafield definitions

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_catalog_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | `store:products:read` |

## Tags

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_tags` | `GET /api/2025-01/tags` | `store:products:read` |
| `get_tag` | `GET /api/2025-01/tags/{id}` | `store:products:read` |
| `create_tag` | `POST /api/2025-01/tags` | `store:products:write` |
| `update_tag` | `PUT /api/2025-01/tags/{id}` | `store:products:write` |
| `delete_tag` | `DELETE /api/2025-01/tags/{id}` | `store:products:write` |
| `get_tag_translation` | `GET /api/2025-01/tags/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_tag_translation` | `PUT /api/2025-01/tags/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_tag_translations` | `GET /api/2025-01/tags/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_tag_translations` | `PUT /api/2025-01/tags/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Brands

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_brands` | `GET /api/2025-01/brands` | `store:products:read` |
| `get_brand` | `GET /api/2025-01/brands/{id}` | `store:products:read` |
| `get_brand_metafield_translation` | `GET /api/2025-01/brands/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_brand_metafield_translation` | `PUT /api/2025-01/brands/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `create_brand` | `POST /api/2025-01/brands` | `store:products:write` |
| `update_brand` | `PUT /api/2025-01/brands/{id}` | `store:products:write` |
| `delete_brand` | `DELETE /api/2025-01/brands/{id}` | `store:products:write` |
| `get_brand_translation` | `GET /api/2025-01/brands/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_brand_translation` | `PUT /api/2025-01/brands/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_brand_translations` | `GET /api/2025-01/brands/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_brand_translations` | `PUT /api/2025-01/brands/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Vendors

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_vendors` | `GET /api/2025-01/vendors` | `store:products:read` |
| `get_vendor` | `GET /api/2025-01/vendors/{id}` | `store:products:read` |
| `get_vendor_metafield_translation` | `GET /api/2025-01/vendors/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_vendor_metafield_translation` | `PUT /api/2025-01/vendors/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `create_vendor` | `POST /api/2025-01/vendors` | `store:products:write` |
| `update_vendor` | `PUT /api/2025-01/vendors/{id}` | `store:products:write` |
| `delete_vendor` | `DELETE /api/2025-01/vendors/{id}` | `store:products:write` |
| `get_vendor_translation` | `GET /api/2025-01/vendors/{id}/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_vendor_translation` | `PUT /api/2025-01/vendors/{id}/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |
| `get_vendor_translations` | `GET /api/2025-01/vendors/translations/{locale}` | `store:products:read`, `store:settings.languages:read` |
| `set_vendor_translations` | `PUT /api/2025-01/vendors/translations/{locale}` | `store:products:write`, `store:settings.languages:write` |

## Files

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_file_limits` | `GET /api/2025-01/files/limits` | `store:files:read` (Media) or `store:online_store.site_assets:read` (Site Assets) |
| `get_storage_quota` | `GET /api/2025-01/files/quota` | `store:files:read` (Media) or `store:online_store.site_assets:read` (Site Assets) |
| `list_files` | `GET /api/2025-01/files` | `store:files:read` (Media) or `store:online_store.site_assets:read` (Site Assets) |
| `create_file_uploads` | `POST /api/2025-01/files/upload-intents` | `store:files:write` (Media) or `store:online_store.site_assets:write` (Site Assets) |
| `finalize_file_uploads` | `POST /api/2025-01/files/upload-intents/finalize` | `store:files:write` (Media) or `store:online_store.site_assets:write` (Site Assets) |
| `get_file_upload_status` | `POST /api/2025-01/files/upload-intents/status` | `store:files:write` (Media) or `store:online_store.site_assets:write` (Site Assets) |
| `get_file` | `GET /api/2025-01/files/{id}` | `store:files:read` (Media) or `store:online_store.site_assets:read` (Site Assets) |
| `update_file` | `PUT /api/2025-01/files/{id}` | `store:files:write` (Media) or `store:online_store.site_assets:write` (Site Assets) |
| `delete_file` | `DELETE /api/2025-01/files/{id}` | `store:files:write` (Media) or `store:online_store.site_assets:write` (Site Assets) |

## Languages

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_languages` | `GET /api/2025-01/languages` | `store:settings.languages:read` |
| `set_languages` | `PUT /api/2025-01/languages` | `store:settings.languages:write` |
| `set_default_language` | `PUT /api/2025-01/languages/default` | `store:settings.languages:write` |
| `delete_language_translations` | `DELETE /api/2025-01/languages/{locale}/translations` | `store:settings.languages:write` |
| `list_available_languages` | `GET /api/2025-01/reference/languages` | Connection only (`connection:read`) |

## Currencies

Currency writes follow the Store API rules: the base currency cannot be changed or rounded, automatic-rate mode manages rates and enabled state, and data removal is a two-step confirmation.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_currencies` | `GET /api/2025-01/currencies` | `store:settings.currencies:read` |
| `list_enabled_currencies` | `GET /api/2025-01/currencies/enabled` | `store:settings.currencies:read` |
| `get_base_currency` | `GET /api/2025-01/currencies/base` | `store:settings.currencies:read` |
| `list_exchange_rates` | `GET /api/2025-01/currencies/exchange-rates` | `store:settings.currencies:read` |
| `get_exchange_rate` | `GET /api/2025-01/currencies/exchange-rates/{code}` | `store:settings.currencies:read` |
| `get_currency` | `GET /api/2025-01/currencies/{id}` | `store:settings.currencies:read` |
| `create_currency` | `POST /api/2025-01/currencies` | `store:settings.currencies:write` |
| `update_currency` | `PUT /api/2025-01/currencies/{id}` | `store:settings.currencies:write` |
| `delete_currency` | `DELETE /api/2025-01/currencies/{id}` | `store:settings.currencies:write` |
| `bulk_remove_currency_data` | `POST /api/2025-01/currencies/bulk-remove-data` | `store:settings.currencies:write` |
| `remove_currency_data` | `POST /api/2025-01/currencies/{id}/remove-data` | `store:settings.currencies:write` |
| `set_currency_rounding` | `PUT /api/2025-01/currencies/{id}/rounding` | `store:settings.currencies:write` |
| `set_multi_currency` | `PUT /api/2025-01/currencies/multi-currency` | `store:settings.currencies:write` |
| `set_auto_exchange_rates` | `PUT /api/2025-01/currencies/auto-rates` | `store:settings.currencies:write` |

## Reference data

These read-only lookups need only the connection; they return platform-wide reference data, not store data.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_store_api_scopes` | `GET /api/2025-01/scopes` | Connection only (`connection:read`) |
| `list_countries` | `GET /api/2025-01/reference/countries` | Connection only (`connection:read`) |
| `list_subdivisions` | `GET /api/2025-01/reference/subdivisions/{countryCode}` | Connection only (`connection:read`) |
| `list_timezones` | `GET /api/2025-01/reference/timezones` | Connection only (`connection:read`) |
| `list_available_currencies` | `GET /api/2025-01/reference/currencies` | Connection only (`connection:read`) |
| `list_phone_country_codes` | `GET /api/2025-01/reference/phone-codes` | Connection only (`connection:read`) |
| `get_number_format_defaults` | `GET /api/2025-01/reference/number-format-defaults/{countryCode}` | Connection only (`connection:read`) |
| `list_address_formats` | `GET /api/2025-01/reference/address-format` | Connection only (`connection:read`) |
| `get_address_format` | `GET /api/2025-01/reference/address-format/{countryCode}` | Connection only (`connection:read`) |

## Pages

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_page_limits` | `GET /api/2025-01/pages/limits` | `store:pages:read` |
| `list_pages` | `GET /api/2025-01/pages` | `store:pages:read` |
| `search_pages` | `GET /api/2025-01/pages/search` | `store:pages:read` |
| `get_page` | `GET /api/2025-01/pages/{id}` | `store:pages:read` |
| `list_page_metafields` | `GET /api/2025-01/pages/{id}/metafields` | `store:pages:read` |
| `set_page_metafield` | `PUT /api/2025-01/pages/{id}/metafields` | `store:pages:write` |
| `get_page_metafield_translation` | `GET /api/2025-01/pages/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:pages:read`, `store:settings.languages:read` |
| `set_page_metafield_translation` | `PUT /api/2025-01/pages/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:pages:write`, `store:settings.languages:write` |
| `create_page` | `POST /api/2025-01/pages` | `store:pages:write` |
| `update_page` | `PUT /api/2025-01/pages/{id}` | `store:pages:write` |
| `delete_page` | `DELETE /api/2025-01/pages/{id}` | `store:pages:write` |
| `bulk_delete_pages` | `POST /api/2025-01/pages/bulk-delete` | `store:pages:write` |
| `get_page_translation` | `GET /api/2025-01/pages/{id}/translations/{locale}` | `store:pages:read`, `store:settings.languages:read` |
| `set_page_translation` | `PUT /api/2025-01/pages/{id}/translations/{locale}` | `store:pages:write`, `store:settings.languages:write` |
| `get_page_translations` | `GET /api/2025-01/pages/translations/{locale}` | `store:pages:read`, `store:settings.languages:read` |
| `set_page_translations` | `PUT /api/2025-01/pages/translations/{locale}` | `store:pages:write`, `store:settings.languages:write` |
| `list_page_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | `store:pages:read` |

## Policies

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_policy_limits` | `GET /api/2025-01/policies/limits` | `store:pages:read` |
| `list_policies` | `GET /api/2025-01/policies` | `store:pages:read` |
| `get_policy` | `GET /api/2025-01/policies/{type}` | `store:pages:read` |
| `update_policy` | `PUT /api/2025-01/policies/{type}` | `store:pages:write` |
| `get_policy_translation` | `GET /api/2025-01/policies/{id}/translations/{locale}` | `store:pages:read`, `store:settings.languages:read` |
| `set_policy_translation` | `PUT /api/2025-01/policies/{id}/translations/{locale}` | `store:pages:write`, `store:settings.languages:write` |
| `get_policy_translations` | `GET /api/2025-01/policies/translations/{locale}` | `store:pages:read`, `store:settings.languages:read` |
| `set_policy_translations` | `PUT /api/2025-01/policies/translations/{locale}` | `store:pages:write`, `store:settings.languages:write` |

## Blog Posts

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_blog_post_limits` | `GET /api/2025-01/blog/posts/limits` | `store:blog:read` |
| `list_blog_posts` | `GET /api/2025-01/blog/posts` | `store:blog:read` |
| `search_blog_posts` | `GET /api/2025-01/blog/posts/search` | `store:blog:read` |
| `get_blog_post` | `GET /api/2025-01/blog/posts/{id}` | `store:blog:read` |
| `list_blog_post_metafields` | `GET /api/2025-01/blog/posts/{id}/metafields` | `store:blog:read` |
| `set_blog_post_metafield` | `PUT /api/2025-01/blog/posts/{id}/metafields` | `store:blog:write` |
| `get_blog_post_metafield_translation` | `GET /api/2025-01/blog/posts/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_post_metafield_translation` | `PUT /api/2025-01/blog/posts/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |
| `create_blog_post` | `POST /api/2025-01/blog/posts` | `store:blog:write` |
| `update_blog_post` | `PUT /api/2025-01/blog/posts/{id}` | `store:blog:write` |
| `delete_blog_post` | `DELETE /api/2025-01/blog/posts/{id}` | `store:blog:write` |
| `bulk_delete_blog_posts` | `POST /api/2025-01/blog/posts/bulk-delete` | `store:blog:write` |
| `bulk_update_blog_post_status` | `POST /api/2025-01/blog/posts/bulk-update-status` | `store:blog:write` |
| `bulk_assign_blog_post_categories` | `POST /api/2025-01/blog/posts/bulk-assign-categories` | `store:blog:write` |
| `bulk_assign_blog_post_tags` | `POST /api/2025-01/blog/posts/bulk-assign-tags` | `store:blog:write` |
| `bulk_remove_blog_post_categories` | `POST /api/2025-01/blog/posts/bulk-remove-categories` | `store:blog:write` |
| `bulk_remove_blog_post_tags` | `POST /api/2025-01/blog/posts/bulk-remove-tags` | `store:blog:write` |
| `get_blog_post_translation` | `GET /api/2025-01/blog/posts/{id}/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_post_translation` | `PUT /api/2025-01/blog/posts/{id}/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |
| `get_blog_post_translations` | `GET /api/2025-01/blog/posts/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_post_translations` | `PUT /api/2025-01/blog/posts/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |

## Blog Tags

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_blog_tag_limits` | `GET /api/2025-01/blog/tags/limits` | `store:blog:read` |
| `list_blog_tags` | `GET /api/2025-01/blog/tags` | `store:blog:read` |
| `get_blog_tag` | `GET /api/2025-01/blog/tags/{id}` | `store:blog:read` |
| `create_blog_tag` | `POST /api/2025-01/blog/tags` | `store:blog:write` |
| `update_blog_tag` | `PUT /api/2025-01/blog/tags/{id}` | `store:blog:write` |
| `delete_blog_tag` | `DELETE /api/2025-01/blog/tags/{id}` | `store:blog:write` |
| `bulk_delete_blog_tags` | `POST /api/2025-01/blog/tags/bulk-delete` | `store:blog:write` |
| `get_blog_tag_translation` | `GET /api/2025-01/blog/tags/{id}/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_tag_translation` | `PUT /api/2025-01/blog/tags/{id}/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |
| `get_blog_tag_translations` | `GET /api/2025-01/blog/tags/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_tag_translations` | `PUT /api/2025-01/blog/tags/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |

## Blog Categories

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_blog_category_limits` | `GET /api/2025-01/blog/categories/limits` | `store:blog:read` |
| `list_blog_categories` | `GET /api/2025-01/blog/categories` | `store:blog:read` |
| `get_blog_category` | `GET /api/2025-01/blog/categories/{id}` | `store:blog:read` |
| `list_blog_category_metafields` | `GET /api/2025-01/blog/categories/{id}/metafields` | `store:blog:read` |
| `set_blog_category_metafield` | `PUT /api/2025-01/blog/categories/{id}/metafields` | `store:blog:write` |
| `get_blog_category_metafield_translation` | `GET /api/2025-01/blog/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_category_metafield_translation` | `PUT /api/2025-01/blog/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |
| `create_blog_category` | `POST /api/2025-01/blog/categories` | `store:blog:write` |
| `update_blog_category` | `PUT /api/2025-01/blog/categories/{id}` | `store:blog:write` |
| `delete_blog_category` | `DELETE /api/2025-01/blog/categories/{id}` | `store:blog:write` |
| `bulk_delete_blog_categories` | `POST /api/2025-01/blog/categories/bulk-delete` | `store:blog:write` |
| `get_blog_category_translation` | `GET /api/2025-01/blog/categories/{id}/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_category_translation` | `PUT /api/2025-01/blog/categories/{id}/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |
| `get_blog_category_translations` | `GET /api/2025-01/blog/categories/translations/{locale}` | `store:blog:read`, `store:settings.languages:read` |
| `set_blog_category_translations` | `PUT /api/2025-01/blog/categories/translations/{locale}` | `store:blog:write`, `store:settings.languages:write` |

## Blog Authors

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_blog_author_limits` | `GET /api/2025-01/blog/authors/limits` | `store:blog:read` |
| `list_blog_authors` | `GET /api/2025-01/blog/authors` | `store:blog:read` |
| `search_blog_authors` | `GET /api/2025-01/blog/authors/search` | `store:blog:read` |
| `get_blog_author` | `GET /api/2025-01/blog/authors/{id}` | `store:blog:read` |
| `create_blog_author` | `POST /api/2025-01/blog/authors` | `store:blog:write` |
| `update_blog_author` | `PUT /api/2025-01/blog/authors/{id}` | `store:blog:write` |
| `delete_blog_author` | `DELETE /api/2025-01/blog/authors/{id}` | `store:blog:write` |
| `bulk_delete_blog_authors` | `POST /api/2025-01/blog/authors/bulk-delete` | `store:blog:write` |

## Blog metafield definitions

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_blog_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | `store:blog:read` |
