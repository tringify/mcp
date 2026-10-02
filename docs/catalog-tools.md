# Store MCP tool catalog

This catalog lists the hosted connector’s supported tools and their native Store API operations. Tool input schemas provide the current field names and types. Access is checked against the connected user and store on every call.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_product_limits` | `GET /api/2025-01/products/limits` | store:products:read |
| `list_products` | `GET /api/2025-01/products` | store:products:read |
| `get_product` | `GET /api/2025-01/products/{id}` | store:products:read |
| `get_product_quantity_pricing` | `GET /api/2025-01/products/{id}/quantity-pricing` | store:products:read |
| `list_product_variants` | `GET /api/2025-01/products/{id}/variants` | store:products:read |
| `get_product_variant` | `GET /api/2025-01/products/{id}/variants/{variantId}` | store:products:read |
| `create_product` | `POST /api/2025-01/products` | store:products:write |
| `update_product` | `PUT /api/2025-01/products/{id}` | store:products:write |
| `duplicate_product` | `POST /api/2025-01/products/{id}/duplicate` | store:products:write |
| `delete_product` | `DELETE /api/2025-01/products/{id}` | store:products:write |
| `list_product_metafields` | `GET /api/2025-01/products/{id}/metafields` | store:products:read |
| `set_product_metafield` | `PUT /api/2025-01/products/{id}/metafields` | store:products:write |
| `get_product_metafield_translation` | `GET /api/2025-01/products/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_metafield_translation` | `PUT /api/2025-01/products/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `list_product_variant_metafields` | `GET /api/2025-01/products/{id}/variants/{variantId}/metafields` | store:products:read |
| `set_product_variant_metafield` | `PUT /api/2025-01/products/{id}/variants/{variantId}/metafields` | store:products:write |
| `get_product_variant_metafield_translation` | `GET /api/2025-01/products/{id}/variants/{variantId}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_variant_metafield_translation` | `PUT /api/2025-01/products/{id}/variants/{variantId}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `bulk_update_product_status` | `POST /api/2025-01/products/bulk-status` | store:products:write |
| `bulk_update_product_tags` | `POST /api/2025-01/products/bulk-tags` | store:products:write |
| `bulk_update_product_categories` | `POST /api/2025-01/products/bulk-categories` | store:products:write |
| `bulk_update_product_channels` | `POST /api/2025-01/products/bulk-channels` | store:products:write |
| `bulk_set_product_vendor` | `POST /api/2025-01/products/bulk-vendor` | store:products:write |
| `bulk_set_product_brand` | `POST /api/2025-01/products/bulk-brand` | store:products:write |
| `bulk_delete_products` | `POST /api/2025-01/products/bulk-delete` | store:products:write |
| `get_product_translation` | `GET /api/2025-01/products/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_translation` | `PUT /api/2025-01/products/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_product_translations` | `GET /api/2025-01/products/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_translations` | `PUT /api/2025-01/products/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_product_variant_translation` | `GET /api/2025-01/products/{id}/variants/{variantId}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_variant_translation` | `PUT /api/2025-01/products/{id}/variants/{variantId}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_collection_limits` | `GET /api/2025-01/collections/limits` | store:products:read |
| `list_collections` | `GET /api/2025-01/collections` | store:products:read |
| `search_collections` | `GET /api/2025-01/collections/search` | store:products:read |
| `get_collection` | `GET /api/2025-01/collections/{id}` | store:products:read |
| `list_collection_metafields` | `GET /api/2025-01/collections/{id}/metafields` | store:products:read |
| `set_collection_metafield` | `PUT /api/2025-01/collections/{id}/metafields` | store:products:write |
| `get_collection_metafield_translation` | `GET /api/2025-01/collections/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_collection_metafield_translation` | `PUT /api/2025-01/collections/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `create_collection` | `POST /api/2025-01/collections` | store:products:write |
| `update_collection` | `PUT /api/2025-01/collections/{id}` | store:products:write |
| `delete_collection` | `DELETE /api/2025-01/collections/{id}` | store:products:write |
| `bulk_delete_collections` | `POST /api/2025-01/collections/bulk-delete` | store:products:write |
| `bulk_update_collection_status` | `POST /api/2025-01/collections/bulk-activate` | store:products:write |
| `list_collection_products` | `GET /api/2025-01/collections/{id}/products` | store:products:read |
| `list_collection_product_details` | `GET /api/2025-01/collections/{id}/products/details` | store:products:read |
| `list_collection_rules` | `GET /api/2025-01/collections/{id}/rules` | store:products:read |
| `add_collection_rule` | `POST /api/2025-01/collections/{id}/rules` | store:products:write |
| `update_collection_rule` | `PUT /api/2025-01/collections/{id}/rules/{rule_id}` | store:products:write |
| `delete_collection_rule` | `DELETE /api/2025-01/collections/{id}/rules/{rule_id}` | store:products:write |
| `get_collection_translation` | `GET /api/2025-01/collections/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_collection_translation` | `PUT /api/2025-01/collections/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_collection_translations` | `GET /api/2025-01/collections/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_collection_translations` | `PUT /api/2025-01/collections/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_category_limits` | `GET /api/2025-01/categories/limits` | store:products:read |
| `list_categories` | `GET /api/2025-01/categories` | store:products:read |
| `search_categories` | `GET /api/2025-01/categories/search` | store:products:read |
| `get_category` | `GET /api/2025-01/categories/{id}` | store:products:read |
| `list_category_metafields` | `GET /api/2025-01/categories/{id}/metafields` | store:products:read |
| `set_category_metafield` | `PUT /api/2025-01/categories/{id}/metafields` | store:products:write |
| `get_category_metafield_translation` | `GET /api/2025-01/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_category_metafield_translation` | `PUT /api/2025-01/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `create_category` | `POST /api/2025-01/categories` | store:products:write |
| `bulk_create_categories` | `POST /api/2025-01/categories/bulk-create` | store:products:write |
| `update_category` | `PUT /api/2025-01/categories/{id}` | store:products:write |
| `delete_category` | `DELETE /api/2025-01/categories/{id}` | store:products:write |
| `bulk_delete_categories` | `POST /api/2025-01/categories/bulk-delete` | store:products:write |
| `get_category_translation` | `GET /api/2025-01/categories/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_category_translation` | `PUT /api/2025-01/categories/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_category_translations` | `GET /api/2025-01/categories/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_category_translations` | `PUT /api/2025-01/categories/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_attribute_limits` | `GET /api/2025-01/attributes/limits` | store:products:read |
| `list_attributes` | `GET /api/2025-01/attributes` | store:products:read |
| `search_attributes` | `GET /api/2025-01/attributes/search` | store:products:read |
| `get_attribute` | `GET /api/2025-01/attributes/{id}` | store:products:read |
| `create_attribute` | `POST /api/2025-01/attributes` | store:products:write |
| `update_attribute` | `PUT /api/2025-01/attributes/{id}` | store:products:write |
| `delete_attribute` | `DELETE /api/2025-01/attributes/{id}` | store:products:write |
| `bulk_delete_attributes` | `POST /api/2025-01/attributes/bulk-delete` | store:products:write |
| `reorder_attributes` | `POST /api/2025-01/attributes/reorder` | store:products:write |
| `reorder_attribute_options` | `POST /api/2025-01/attributes/{id}/options/reorder` | store:products:write |
| `get_attribute_translation` | `GET /api/2025-01/attributes/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_attribute_translation` | `PUT /api/2025-01/attributes/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_attribute_translations` | `GET /api/2025-01/attributes/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_attribute_translations` | `PUT /api/2025-01/attributes/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_attribute_option_translation` | `GET /api/2025-01/attribute-options/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_attribute_option_translation` | `PUT /api/2025-01/attribute-options/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_attribute_option_translations` | `GET /api/2025-01/attribute-options/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_attribute_option_translations` | `PUT /api/2025-01/attribute-options/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_page_limits` | `GET /api/2025-01/pages/limits` | store:pages:read |
| `list_pages` | `GET /api/2025-01/pages` | store:pages:read |
| `search_pages` | `GET /api/2025-01/pages/search` | store:pages:read |
| `get_page` | `GET /api/2025-01/pages/{id}` | store:pages:read |
| `list_page_metafields` | `GET /api/2025-01/pages/{id}/metafields` | store:pages:read |
| `set_page_metafield` | `PUT /api/2025-01/pages/{id}/metafields` | store:pages:write |
| `get_page_metafield_translation` | `GET /api/2025-01/pages/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_page_metafield_translation` | `PUT /api/2025-01/pages/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `create_page` | `POST /api/2025-01/pages` | store:pages:write |
| `update_page` | `PUT /api/2025-01/pages/{id}` | store:pages:write |
| `delete_page` | `DELETE /api/2025-01/pages/{id}` | store:pages:write |
| `bulk_delete_pages` | `POST /api/2025-01/pages/bulk-delete` | store:pages:write |
| `get_page_translation` | `GET /api/2025-01/pages/{id}/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_page_translation` | `PUT /api/2025-01/pages/{id}/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `get_page_translations` | `GET /api/2025-01/pages/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_page_translations` | `PUT /api/2025-01/pages/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `get_policy_limits` | `GET /api/2025-01/policies/limits` | store:pages:read |
| `list_policies` | `GET /api/2025-01/policies` | store:pages:read |
| `get_policy` | `GET /api/2025-01/policies/{type}` | store:pages:read |
| `update_policy` | `PUT /api/2025-01/policies/{type}` | store:pages:write |
| `get_policy_translation` | `GET /api/2025-01/policies/{id}/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_policy_translation` | `PUT /api/2025-01/policies/{id}/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `get_policy_translations` | `GET /api/2025-01/policies/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_policy_translations` | `PUT /api/2025-01/policies/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `get_blog_post_limits` | `GET /api/2025-01/blog/posts/limits` | store:blog:read |
| `list_blog_posts` | `GET /api/2025-01/blog/posts` | store:blog:read |
| `search_blog_posts` | `GET /api/2025-01/blog/posts/search` | store:blog:read |
| `get_blog_post` | `GET /api/2025-01/blog/posts/{id}` | store:blog:read |
| `list_blog_post_metafields` | `GET /api/2025-01/blog/posts/{id}/metafields` | store:blog:read |
| `set_blog_post_metafield` | `PUT /api/2025-01/blog/posts/{id}/metafields` | store:blog:write |
| `get_blog_post_metafield_translation` | `GET /api/2025-01/blog/posts/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_post_metafield_translation` | `PUT /api/2025-01/blog/posts/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `create_blog_post` | `POST /api/2025-01/blog/posts` | store:blog:write |
| `update_blog_post` | `PUT /api/2025-01/blog/posts/{id}` | store:blog:write |
| `delete_blog_post` | `DELETE /api/2025-01/blog/posts/{id}` | store:blog:write |
| `bulk_delete_blog_posts` | `POST /api/2025-01/blog/posts/bulk-delete` | store:blog:write |
| `bulk_update_blog_post_status` | `POST /api/2025-01/blog/posts/bulk-update-status` | store:blog:write |
| `bulk_assign_blog_post_categories` | `POST /api/2025-01/blog/posts/bulk-assign-categories` | store:blog:write |
| `bulk_assign_blog_post_tags` | `POST /api/2025-01/blog/posts/bulk-assign-tags` | store:blog:write |
| `bulk_remove_blog_post_categories` | `POST /api/2025-01/blog/posts/bulk-remove-categories` | store:blog:write |
| `bulk_remove_blog_post_tags` | `POST /api/2025-01/blog/posts/bulk-remove-tags` | store:blog:write |
| `get_blog_post_translation` | `GET /api/2025-01/blog/posts/{id}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_post_translation` | `PUT /api/2025-01/blog/posts/{id}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_post_translations` | `GET /api/2025-01/blog/posts/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_post_translations` | `PUT /api/2025-01/blog/posts/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_category_limits` | `GET /api/2025-01/blog/categories/limits` | store:blog:read |
| `list_blog_categories` | `GET /api/2025-01/blog/categories` | store:blog:read |
| `get_blog_category` | `GET /api/2025-01/blog/categories/{id}` | store:blog:read |
| `list_blog_category_metafields` | `GET /api/2025-01/blog/categories/{id}/metafields` | store:blog:read |
| `set_blog_category_metafield` | `PUT /api/2025-01/blog/categories/{id}/metafields` | store:blog:write |
| `get_blog_category_metafield_translation` | `GET /api/2025-01/blog/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_category_metafield_translation` | `PUT /api/2025-01/blog/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `create_blog_category` | `POST /api/2025-01/blog/categories` | store:blog:write |
| `update_blog_category` | `PUT /api/2025-01/blog/categories/{id}` | store:blog:write |
| `delete_blog_category` | `DELETE /api/2025-01/blog/categories/{id}` | store:blog:write |
| `bulk_delete_blog_categories` | `POST /api/2025-01/blog/categories/bulk-delete` | store:blog:write |
| `get_blog_category_translation` | `GET /api/2025-01/blog/categories/{id}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_category_translation` | `PUT /api/2025-01/blog/categories/{id}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_category_translations` | `GET /api/2025-01/blog/categories/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_category_translations` | `PUT /api/2025-01/blog/categories/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_tag_limits` | `GET /api/2025-01/blog/tags/limits` | store:blog:read |
| `list_blog_tags` | `GET /api/2025-01/blog/tags` | store:blog:read |
| `get_blog_tag` | `GET /api/2025-01/blog/tags/{id}` | store:blog:read |
| `create_blog_tag` | `POST /api/2025-01/blog/tags` | store:blog:write |
| `update_blog_tag` | `PUT /api/2025-01/blog/tags/{id}` | store:blog:write |
| `delete_blog_tag` | `DELETE /api/2025-01/blog/tags/{id}` | store:blog:write |
| `bulk_delete_blog_tags` | `POST /api/2025-01/blog/tags/bulk-delete` | store:blog:write |
| `get_blog_tag_translation` | `GET /api/2025-01/blog/tags/{id}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_tag_translation` | `PUT /api/2025-01/blog/tags/{id}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_tag_translations` | `GET /api/2025-01/blog/tags/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_tag_translations` | `PUT /api/2025-01/blog/tags/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_author_limits` | `GET /api/2025-01/blog/authors/limits` | store:blog:read |
| `list_blog_authors` | `GET /api/2025-01/blog/authors` | store:blog:read |
| `search_blog_authors` | `GET /api/2025-01/blog/authors/search` | store:blog:read |
| `get_blog_author` | `GET /api/2025-01/blog/authors/{id}` | store:blog:read |
| `create_blog_author` | `POST /api/2025-01/blog/authors` | store:blog:write |
| `update_blog_author` | `PUT /api/2025-01/blog/authors/{id}` | store:blog:write |
| `delete_blog_author` | `DELETE /api/2025-01/blog/authors/{id}` | store:blog:write |
| `bulk_delete_blog_authors` | `POST /api/2025-01/blog/authors/bulk-delete` | store:blog:write |
| `list_tags` | `GET /api/2025-01/tags` | store:products:read |
| `get_tag` | `GET /api/2025-01/tags/{id}` | store:products:read |
| `create_tag` | `POST /api/2025-01/tags` | store:products:write |
| `update_tag` | `PUT /api/2025-01/tags/{id}` | store:products:write |
| `delete_tag` | `DELETE /api/2025-01/tags/{id}` | store:products:write |
| `get_tag_translation` | `GET /api/2025-01/tags/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_tag_translation` | `PUT /api/2025-01/tags/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_tag_translations` | `GET /api/2025-01/tags/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_tag_translations` | `PUT /api/2025-01/tags/translations/{locale}` | store:products:write, store:settings.languages:write |
| `list_brands` | `GET /api/2025-01/brands` | store:products:read |
| `get_brand` | `GET /api/2025-01/brands/{id}` | store:products:read |
| `get_brand_metafield_translation` | `GET /api/2025-01/brands/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_brand_metafield_translation` | `PUT /api/2025-01/brands/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `create_brand` | `POST /api/2025-01/brands` | store:products:write |
| `update_brand` | `PUT /api/2025-01/brands/{id}` | store:products:write |
| `delete_brand` | `DELETE /api/2025-01/brands/{id}` | store:products:write |
| `get_brand_translation` | `GET /api/2025-01/brands/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_brand_translation` | `PUT /api/2025-01/brands/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_brand_translations` | `GET /api/2025-01/brands/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_brand_translations` | `PUT /api/2025-01/brands/translations/{locale}` | store:products:write, store:settings.languages:write |
| `list_vendors` | `GET /api/2025-01/vendors` | store:products:read |
| `get_vendor` | `GET /api/2025-01/vendors/{id}` | store:products:read |
| `get_vendor_metafield_translation` | `GET /api/2025-01/vendors/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_vendor_metafield_translation` | `PUT /api/2025-01/vendors/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `create_vendor` | `POST /api/2025-01/vendors` | store:products:write |
| `update_vendor` | `PUT /api/2025-01/vendors/{id}` | store:products:write |
| `delete_vendor` | `DELETE /api/2025-01/vendors/{id}` | store:products:write |
| `get_vendor_translation` | `GET /api/2025-01/vendors/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_vendor_translation` | `PUT /api/2025-01/vendors/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_vendor_translations` | `GET /api/2025-01/vendors/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_vendor_translations` | `PUT /api/2025-01/vendors/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_file_limits` | `GET /api/2025-01/files/limits` | store:files:read (Media), or store:online_store.site_assets:read (Site Assets) |
| `get_storage_quota` | `GET /api/2025-01/files/quota` | store:files:read (Media), or store:online_store.site_assets:read (Site Assets) |
| `list_files` | `GET /api/2025-01/files` | store:files:read (Media), or store:online_store.site_assets:read (Site Assets) |
| `create_file_uploads` | `POST /api/2025-01/files/upload-intents` | store:files:write (Media), or store:online_store.site_assets:write (Site Assets) |
| `finalize_file_uploads` | `POST /api/2025-01/files/upload-intents/finalize` | store:files:write (Media), or store:online_store.site_assets:write (Site Assets) |
| `get_file_upload_status` | `POST /api/2025-01/files/upload-intents/status` | store:files:write (Media), or store:online_store.site_assets:write (Site Assets) |
| `get_file` | `GET /api/2025-01/files/{id}` | store:files:read (Media), or store:online_store.site_assets:read (Site Assets) |
| `update_file` | `PUT /api/2025-01/files/{id}` | store:files:write (Media), or store:online_store.site_assets:write (Site Assets) |
| `delete_file` | `DELETE /api/2025-01/files/{id}` | store:files:write (Media), or store:online_store.site_assets:write (Site Assets) |
| `list_languages` | `GET /api/2025-01/languages` | store:settings.languages:read |
| `set_languages` | `PUT /api/2025-01/languages` | store:settings.languages:write |
| `set_default_language` | `PUT /api/2025-01/languages/default` | store:settings.languages:write |
| `delete_language_translations` | `DELETE /api/2025-01/languages/{locale}/translations` | store:settings.languages:write |
| `list_available_languages` | `GET /api/2025-01/reference/languages` | Valid Store connection |
| `list_currencies` | `GET /api/2025-01/currencies` | store:settings.currencies:read |
| `list_enabled_currencies` | `GET /api/2025-01/currencies/enabled` | store:settings.currencies:read |
| `get_base_currency` | `GET /api/2025-01/currencies/base` | store:settings.currencies:read |
| `list_exchange_rates` | `GET /api/2025-01/currencies/exchange-rates` | store:settings.currencies:read |
| `get_exchange_rate` | `GET /api/2025-01/currencies/exchange-rates/{code}` | store:settings.currencies:read |
| `get_currency` | `GET /api/2025-01/currencies/{id}` | store:settings.currencies:read |
| `create_currency` | `POST /api/2025-01/currencies` | store:settings.currencies:write |
| `update_currency` | `PUT /api/2025-01/currencies/{id}` | store:settings.currencies:write |
| `delete_currency` | `DELETE /api/2025-01/currencies/{id}` | store:settings.currencies:write |
| `bulk_remove_currency_data` | `POST /api/2025-01/currencies/bulk-remove-data` | store:settings.currencies:write |
| `remove_currency_data` | `POST /api/2025-01/currencies/{id}/remove-data` | store:settings.currencies:write |
| `set_currency_rounding` | `PUT /api/2025-01/currencies/{id}/rounding` | store:settings.currencies:write |
| `set_multi_currency` | `PUT /api/2025-01/currencies/multi-currency` | store:settings.currencies:write |
| `set_auto_exchange_rates` | `PUT /api/2025-01/currencies/auto-rates` | store:settings.currencies:write |
| `get_market_limits` | `GET /api/2025-01/markets/limits` | store:markets:read |
| `get_assigned_market_countries` | `GET /api/2025-01/markets/assigned-countries` | store:markets:read |
| `list_markets` | `GET /api/2025-01/markets` | store:markets:read |
| `create_market` | `POST /api/2025-01/markets` | store:markets:write |
| `get_market` | `GET /api/2025-01/markets/{marketId}` | store:markets:read |
| `update_market` | `PATCH /api/2025-01/markets/{marketId}` | store:markets:write |
| `delete_market` | `DELETE /api/2025-01/markets/{marketId}` | store:markets:write |
| `list_market_currencies` | `GET /api/2025-01/markets/{marketId}/currencies` | store:markets:read |
| `add_market_currency` | `POST /api/2025-01/markets/{marketId}/currencies` | store:markets:write |
| `bulk_add_market_currencies` | `POST /api/2025-01/markets/{marketId}/currencies/bulk` | store:markets:write |
| `bulk_remove_market_currencies` | `POST /api/2025-01/markets/{marketId}/currencies/bulk-delete` | store:markets:write |
| `remove_market_currency` | `DELETE /api/2025-01/markets/{marketId}/currencies/{currencyId}` | store:markets:write |
| `list_market_country_currencies` | `GET /api/2025-01/markets/{marketId}/country-currencies` | store:markets:read |
| `get_market_country_currency_limits` | `GET /api/2025-01/markets/{marketId}/country-currencies/limits` | store:markets:read |
| `set_market_country_currencies` | `PUT /api/2025-01/markets/{marketId}/country-currencies` | store:markets:write |
| `bulk_assign_market_country_currencies` | `POST /api/2025-01/markets/{marketId}/country-currencies/bulk-assign` | store:markets:write |
| `assign_all_market_country_currencies` | `POST /api/2025-01/markets/{marketId}/country-currencies/auto-assign` | store:markets:write |
| `list_market_payment_providers` | `GET /api/2025-01/markets/{marketId}/payment-providers` | store:markets:read |
| `update_market_payment_provider` | `PUT /api/2025-01/markets/{marketId}/payment-providers/{bindingId}` | store:markets:write |
| `list_market_payment_adjustments` | `GET /api/2025-01/markets/{marketId}/payment-adjustments` | store:markets:read |
| `list_market_provider_payment_adjustments` | `GET /api/2025-01/markets/{marketId}/payment-providers/{bindingId}/adjustments` | store:markets:read |
| `create_market_payment_adjustment` | `POST /api/2025-01/markets/{marketId}/payment-providers/{bindingId}/adjustments` | store:markets:write |
| `update_market_payment_adjustment` | `PUT /api/2025-01/markets/{marketId}/payment-providers/{bindingId}/adjustments/{ruleId}` | store:markets:write |
| `delete_market_payment_adjustment` | `DELETE /api/2025-01/markets/{marketId}/payment-providers/{bindingId}/adjustments/{ruleId}` | store:markets:write |
| `get_market_tax_class_limits` | `GET /api/2025-01/markets/tax-classes/limits` | store:markets:read |
| `list_market_tax_classes` | `GET /api/2025-01/markets/{marketId}/tax-classes` | store:markets:read |
| `create_market_tax_class` | `POST /api/2025-01/markets/{marketId}/tax-classes` | store:markets:write |
| `get_market_tax_class` | `GET /api/2025-01/markets/{marketId}/tax-classes/{taxClassId}` | store:markets:read |
| `update_market_tax_class` | `PUT /api/2025-01/markets/{marketId}/tax-classes/{taxClassId}` | store:markets:write |
| `bulk_delete_market_tax_classes` | `POST /api/2025-01/markets/{marketId}/tax-classes/bulk-delete` | store:markets:write |
| `delete_market_tax_class` | `DELETE /api/2025-01/markets/{marketId}/tax-classes/{taxClassId}` | store:markets:write |
| `get_market_tax_zone_limits` | `GET /api/2025-01/markets/tax-zones/limits` | store:markets:read |
| `list_market_tax_available_countries` | `GET /api/2025-01/markets/{marketId}/tax-zones/available-countries` | store:markets:read |
| `list_market_tax_zones` | `GET /api/2025-01/markets/{marketId}/tax-zones` | store:markets:read |
| `create_market_tax_zone` | `POST /api/2025-01/markets/{marketId}/tax-zones` | store:markets:write |
| `get_market_tax_zone` | `GET /api/2025-01/markets/{marketId}/tax-zones/{taxZoneId}` | store:markets:read |
| `update_market_tax_zone` | `PUT /api/2025-01/markets/{marketId}/tax-zones/{taxZoneId}` | store:markets:write |
| `delete_market_tax_zone` | `DELETE /api/2025-01/markets/{marketId}/tax-zones/{taxZoneId}` | store:markets:write |
| `get_market_tax_rate_limits` | `GET /api/2025-01/markets/{marketId}/tax-rates/limits` | store:markets:read |
| `search_market_tax_rates` | `GET /api/2025-01/markets/{marketId}/tax-rates/search` | store:markets:read |
| `get_market_tax_rate_coverage_gaps` | `GET /api/2025-01/markets/{marketId}/tax-rates/coverage-gaps` | store:markets:read |
| `create_market_tax_rate` | `POST /api/2025-01/markets/{marketId}/tax-rates` | store:markets:write |
| `save_market_tax_rate` | `PUT /api/2025-01/markets/{marketId}/tax-rates` | store:markets:write |
| `get_market_tax_rate` | `GET /api/2025-01/markets/{marketId}/tax-rates/{taxRateId}` | store:markets:read |
| `update_market_tax_rate` | `PUT /api/2025-01/markets/{marketId}/tax-rates/{taxRateId}` | store:markets:write |
| `delete_market_tax_rate` | `DELETE /api/2025-01/markets/{marketId}/tax-rates/{taxRateId}` | store:markets:write |
| `get_market_tax_price_rule_eligibility` | `GET /api/2025-01/markets/{marketId}/tax-price-rules/eligibility` | store:markets:read |
| `list_market_tax_price_rules` | `GET /api/2025-01/markets/{marketId}/tax-price-rules` | store:markets:read |
| `get_market_tax_price_rule` | `GET /api/2025-01/markets/{marketId}/tax-price-rules/{ruleId}` | store:markets:read |
| `create_market_tax_price_rule` | `POST /api/2025-01/markets/{marketId}/tax-price-rules` | store:markets:write |
| `update_market_tax_price_rule` | `PUT /api/2025-01/markets/{marketId}/tax-price-rules/{ruleId}` | store:markets:write |
| `delete_market_tax_price_rule` | `DELETE /api/2025-01/markets/{marketId}/tax-price-rules/{ruleId}` | store:markets:write |
| `get_market_discount_limits` | `GET /api/2025-01/markets/{marketId}/discounts/limits` | store:markets:read |
| `list_market_discounts` | `GET /api/2025-01/markets/{marketId}/discounts` | store:markets:read |
| `create_market_discount` | `POST /api/2025-01/markets/{marketId}/discounts` | store:markets:write |
| `get_market_discount` | `GET /api/2025-01/markets/{marketId}/discounts/{discountId}` | store:markets:read |
| `update_market_discount` | `PUT /api/2025-01/markets/{marketId}/discounts/{discountId}` | store:markets:write |
| `bulk_market_discount` | `POST /api/2025-01/markets/{marketId}/discounts/bulk` | store:markets:write |
| `delete_market_discount` | `DELETE /api/2025-01/markets/{marketId}/discounts/{discountId}` | store:markets:write |
| `enable_market_discount` | `POST /api/2025-01/markets/{marketId}/discounts/{discountId}/enable` | store:markets:write |
| `disable_market_discount` | `POST /api/2025-01/markets/{marketId}/discounts/{discountId}/disable` | store:markets:write |
| `get_market_discount_settings` | `GET /api/2025-01/markets/{marketId}/discount-settings` | store:markets:read |
| `set_market_discount_settings` | `PUT /api/2025-01/markets/{marketId}/discount-settings` | store:markets:write |
| `get_market_shipping_settings` | `GET /api/2025-01/markets/{marketId}/shipping-settings` | store:markets:read |
| `update_market_shipping_settings` | `PUT /api/2025-01/markets/{marketId}/shipping-settings` | store:markets:write |
| `get_market_shipping_zone_limits` | `GET /api/2025-01/markets/{marketId}/shipping-zones/limits` | store:markets:read |
| `list_market_shipping_available_countries` | `GET /api/2025-01/markets/{marketId}/shipping-zones/available-countries` | store:markets:read |
| `list_market_shipping_zones` | `GET /api/2025-01/markets/{marketId}/shipping-zones` | store:markets:read |
| `create_market_shipping_zone` | `POST /api/2025-01/markets/{marketId}/shipping-zones` | store:markets:write |
| `get_market_shipping_zone` | `GET /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}` | store:markets:read |
| `update_market_shipping_zone` | `PUT /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}` | store:markets:write |
| `delete_market_shipping_zone` | `DELETE /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}` | store:markets:write |
| `get_market_shipping_method_limits` | `GET /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}/methods/limits` | store:markets:read |
| `list_market_shipping_methods` | `GET /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}/methods` | store:markets:read |
| `create_market_shipping_method` | `POST /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}/methods` | store:markets:write |
| `get_market_shipping_method` | `GET /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}/methods/{methodId}` | store:markets:read |
| `update_market_shipping_method` | `PUT /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}/methods/{methodId}` | store:markets:write |
| `delete_market_shipping_method` | `DELETE /api/2025-01/markets/{marketId}/shipping-zones/{zoneId}/methods/{methodId}` | store:markets:write |
| `get_market_duty_country_rule_limits` | `GET /api/2025-01/markets/{marketId}/duty-country-rules/limits` | store:markets:read |
| `list_market_duty_available_countries` | `GET /api/2025-01/markets/{marketId}/duty-country-rules/available-countries` | store:markets:read |
| `list_market_duty_country_rules` | `GET /api/2025-01/markets/{marketId}/duty-country-rules` | store:markets:read |
| `create_market_duty_country_rule` | `POST /api/2025-01/markets/{marketId}/duty-country-rules` | store:markets:write |
| `get_market_duty_rule_by_country` | `GET /api/2025-01/markets/{marketId}/duty-country-rules/by-country/{countryCode}` | store:markets:read |
| `get_market_duty_country_rule` | `GET /api/2025-01/markets/{marketId}/duty-country-rules/{ruleId}` | store:markets:read |
| `update_market_duty_country_rule` | `PUT /api/2025-01/markets/{marketId}/duty-country-rules/{ruleId}` | store:markets:write |
| `delete_market_duty_country_rule` | `DELETE /api/2025-01/markets/{marketId}/duty-country-rules/{ruleId}` | store:markets:write |
| `get_market_cod_settings` | `GET /api/2025-01/markets/{marketId}/cod-settings` | store:markets:read |
| `update_market_cod_settings` | `PUT /api/2025-01/markets/{marketId}/cod-settings` | store:markets:write |
| `get_market_cod_zone_limits` | `GET /api/2025-01/markets/{marketId}/cod-zones/limits` | store:markets:read |
| `list_market_cod_zones` | `GET /api/2025-01/markets/{marketId}/cod-zones` | store:markets:read |
| `create_market_cod_zone` | `POST /api/2025-01/markets/{marketId}/cod-zones` | store:markets:write |
| `get_market_cod_zone` | `GET /api/2025-01/markets/{marketId}/cod-zones/{zoneId}` | store:markets:read |
| `update_market_cod_zone` | `PUT /api/2025-01/markets/{marketId}/cod-zones/{zoneId}` | store:markets:write |
| `delete_market_cod_zone` | `DELETE /api/2025-01/markets/{marketId}/cod-zones/{zoneId}` | store:markets:write |
| `list_market_cod_rules` | `GET /api/2025-01/markets/{marketId}/cod-rules` | store:markets:read |
| `create_market_cod_rule` | `POST /api/2025-01/markets/{marketId}/cod-rules` | store:markets:write |
| `update_market_cod_rule` | `PUT /api/2025-01/markets/{marketId}/cod-rules/{ruleId}` | store:markets:write |
| `delete_market_cod_rule` | `DELETE /api/2025-01/markets/{marketId}/cod-rules/{ruleId}` | store:markets:write |
| `get_market_checkout_settings_limits` | `GET /api/2025-01/markets/{marketId}/checkout-settings/limits` | store:markets:read |
| `get_market_checkout_settings` | `GET /api/2025-01/markets/{marketId}/checkout-settings` | store:markets:read |
| `update_market_checkout_settings` | `PUT /api/2025-01/markets/{marketId}/checkout-settings` | store:markets:write |
| `list_market_checkout_fees` | `GET /api/2025-01/markets/{marketId}/checkout-fees` | store:markets:read |
| `get_market_checkout_fee` | `GET /api/2025-01/markets/{marketId}/checkout-fees/{feeId}` | store:markets:read |
| `create_market_checkout_fee` | `POST /api/2025-01/markets/{marketId}/checkout-fees` | store:markets:write |
| `update_market_checkout_fee` | `PUT /api/2025-01/markets/{marketId}/checkout-fees/{feeId}` | store:markets:write |
| `delete_market_checkout_fee` | `DELETE /api/2025-01/markets/{marketId}/checkout-fees/{feeId}` | store:markets:write |
| `reorder_market_checkout_fees` | `POST /api/2025-01/markets/{marketId}/checkout-fees/reorder` | store:markets:write |
| `list_domains` | `GET /api/2025-01/domains` | store:settings.domains:read |
| `get_domain` | `GET /api/2025-01/domains/{domainId}` | store:settings.domains:read |
| `list_dns_zones` | `GET /api/2025-01/dns-zones` | store:settings.domains:read |
| `get_dns_zone` | `GET /api/2025-01/dns-zones/{zoneId}` | store:settings.domains:read |
| `create_dns_record` | `POST /api/2025-01/dns-zones/{zoneId}/records` | store:settings.domains:write |
| `update_dns_record` | `PUT /api/2025-01/dns-zones/{zoneId}/records/{recordId}` | store:settings.domains:write |
| `delete_dns_record` | `DELETE /api/2025-01/dns-zones/{zoneId}/records/{recordId}` | store:settings.domains:write |
| `list_email_senders` | `GET /api/2025-01/email/senders` | store:settings.email:read |
| `list_email_domains` | `GET /api/2025-01/email/domains` | store:settings.email:read |
| `get_email_reply_to` | `GET /api/2025-01/email/reply-to` | store:settings.email:read |
| `update_email_reply_to` | `PUT /api/2025-01/email/reply-to` | store:settings.email:write |
| `get_email_suppression` | `GET /api/2025-01/email/suppressions` | store:settings.email:read |
| `list_store_api_scopes` | `GET /api/2025-01/scopes` | Valid Store connection |
| `list_countries` | `GET /api/2025-01/reference/countries` | Valid Store connection |
| `list_subdivisions` | `GET /api/2025-01/reference/subdivisions/{countryCode}` | Valid Store connection |
| `list_timezones` | `GET /api/2025-01/reference/timezones` | Valid Store connection |
| `list_available_currencies` | `GET /api/2025-01/reference/currencies` | Valid Store connection |
| `list_phone_country_codes` | `GET /api/2025-01/reference/phone-codes` | Valid Store connection |
| `get_number_format_defaults` | `GET /api/2025-01/reference/number-format-defaults/{countryCode}` | Valid Store connection |
| `list_address_formats` | `GET /api/2025-01/reference/address-format` | Valid Store connection |
| `get_address_format` | `GET /api/2025-01/reference/address-format/{countryCode}` | Valid Store connection |
| `list_catalog_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | store:products:read |
| `list_page_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | store:pages:read |
| `list_blog_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | store:blog:read |
