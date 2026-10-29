# Store MCP tool catalog

This catalog lists the hosted connector’s supported tools and their native Store API operations. Tool input schemas provide the current field names and types. Access is checked against the connected user and store on every call.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_product_limits` | `GET /api/2025-01/products/limits` | store:products:read |
| `list_products` | `GET /api/2025-01/products` | store:products:read |
| `get_product` | `GET /api/2025-01/products/{id}` | store:products:read |
| `get_product_quantity_pricing` | `GET /api/2025-01/products/{id}/quantity-pricing` | store:products:read |
| `list_product_variants` | `GET /api/2025-01/products/{id}/variants` | store:products:read |
| `list_variants` | `GET /api/2025-01/variants` | store:products:read |
| `get_product_variant` | `GET /api/2025-01/products/{id}/variants/{variantId}` | store:products:read |
| `create_product` | `POST /api/2025-01/products` | store:products:write |
| `update_product` | `PUT /api/2025-01/products/{id}` | store:products:write |
| `duplicate_product` | `POST /api/2025-01/products/{id}/duplicate` | store:products:write |
| `delete_product` | `DELETE /api/2025-01/products/{id}` | store:products:write |
| `list_product_metafields` | `GET /api/2025-01/products/{id}/metafields` | store:products:read |
| `set_product_metafield` | `PUT /api/2025-01/products/{id}/metafields` | store:products:write |
| `delete_product_metafield` | `DELETE /api/2025-01/products/{id}/metafields/{namespace}/{key}` | store:products:write |
| `get_product_metafield_translation` | `GET /api/2025-01/products/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_metafield_translation` | `PUT /api/2025-01/products/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `list_product_variant_metafields` | `GET /api/2025-01/products/{id}/variants/{variantId}/metafields` | store:products:read |
| `set_product_variant_metafield` | `PUT /api/2025-01/products/{id}/variants/{variantId}/metafields` | store:products:write |
| `delete_product_variant_metafield` | `DELETE /api/2025-01/products/{id}/variants/{variantId}/metafields/{namespace}/{key}` | store:products:write |
| `get_product_variant_metafield_translation` | `GET /api/2025-01/products/{id}/variants/{variantId}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_variant_metafield_translation` | `PUT /api/2025-01/products/{id}/variants/{variantId}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `bulk_update_product_status` | `POST /api/2025-01/products/bulk-status` | store:products:write |
| `bulk_update_product_tags` | `POST /api/2025-01/products/bulk-tags` | store:products:write |
| `bulk_update_product_categories` | `POST /api/2025-01/products/bulk-categories` | store:products:write |
| `bulk_update_product_channels` | `POST /api/2025-01/products/bulk-channels` | store:products:write |
| `bulk_set_product_vendor` | `POST /api/2025-01/products/bulk-vendor` | store:products:write |
| `bulk_set_product_brand` | `POST /api/2025-01/products/bulk-brand` | store:products:write |
| `bulk_delete_products` | `POST /api/2025-01/products/bulk-delete` | store:products:write |
| `bulk_delete_product_variants` | `POST /api/2025-01/products/variants/bulk-delete` | store:products:write |
| `get_product_translation` | `GET /api/2025-01/products/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_translation` | `PUT /api/2025-01/products/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_product_translations` | `GET /api/2025-01/products/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_translations` | `PUT /api/2025-01/products/translations` | store:products:write, store:settings.languages:write |
| `get_product_variant_translation` | `GET /api/2025-01/products/{id}/variants/{variantId}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_variant_translation` | `PUT /api/2025-01/products/{id}/variants/{variantId}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_collection_limits` | `GET /api/2025-01/collections/limits` | store:products:read |
| `list_collections` | `GET /api/2025-01/collections` | store:products:read |
| `search_collections` | `GET /api/2025-01/collections/search` | store:products:read |
| `get_collection` | `GET /api/2025-01/collections/{id}` | store:products:read |
| `list_collection_metafields` | `GET /api/2025-01/collections/{id}/metafields` | store:products:read |
| `set_collection_metafield` | `PUT /api/2025-01/collections/{id}/metafields` | store:products:write |
| `delete_collection_metafield` | `DELETE /api/2025-01/collections/{id}/metafields/{namespace}/{key}` | store:products:write |
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
| `set_collection_translations` | `PUT /api/2025-01/collections/translations` | store:products:write, store:settings.languages:write |
| `get_category_limits` | `GET /api/2025-01/categories/limits` | store:products:read |
| `list_categories` | `GET /api/2025-01/categories` | store:products:read |
| `search_categories` | `GET /api/2025-01/categories/search` | store:products:read |
| `get_category` | `GET /api/2025-01/categories/{id}` | store:products:read |
| `list_category_metafields` | `GET /api/2025-01/categories/{id}/metafields` | store:products:read |
| `set_category_metafield` | `PUT /api/2025-01/categories/{id}/metafields` | store:products:write |
| `delete_category_metafield` | `DELETE /api/2025-01/categories/{id}/metafields/{namespace}/{key}` | store:products:write |
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
| `set_category_translations` | `PUT /api/2025-01/categories/translations` | store:products:write, store:settings.languages:write |
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
| `set_attribute_translations` | `PUT /api/2025-01/attributes/translations` | store:products:write, store:settings.languages:write |
| `get_attribute_option_translation` | `GET /api/2025-01/attribute-options/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_attribute_option_translation` | `PUT /api/2025-01/attribute-options/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_attribute_option_translations` | `GET /api/2025-01/attribute-options/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_attribute_option_translations` | `PUT /api/2025-01/attribute-options/translations` | store:products:write, store:settings.languages:write |
| `get_page_limits` | `GET /api/2025-01/pages/limits` | store:pages:read |
| `list_pages` | `GET /api/2025-01/pages` | store:pages:read |
| `search_pages` | `GET /api/2025-01/pages/search` | store:pages:read |
| `get_page` | `GET /api/2025-01/pages/{id}` | store:pages:read |
| `list_page_metafields` | `GET /api/2025-01/pages/{id}/metafields` | store:pages:read |
| `set_page_metafield` | `PUT /api/2025-01/pages/{id}/metafields` | store:pages:write |
| `delete_page_metafield` | `DELETE /api/2025-01/pages/{id}/metafields/{namespace}/{key}` | store:pages:write |
| `get_page_metafield_translation` | `GET /api/2025-01/pages/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_page_metafield_translation` | `PUT /api/2025-01/pages/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `create_page` | `POST /api/2025-01/pages` | store:pages:write |
| `update_page` | `PUT /api/2025-01/pages/{id}` | store:pages:write |
| `delete_page` | `DELETE /api/2025-01/pages/{id}` | store:pages:write |
| `bulk_delete_pages` | `POST /api/2025-01/pages/bulk-delete` | store:pages:write |
| `get_page_translation` | `GET /api/2025-01/pages/{id}/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_page_translation` | `PUT /api/2025-01/pages/{id}/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `get_page_translations` | `GET /api/2025-01/pages/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_page_translations` | `PUT /api/2025-01/pages/translations` | store:pages:write, store:settings.languages:write |
| `get_policy_limits` | `GET /api/2025-01/policies/limits` | store:pages:read |
| `list_policies` | `GET /api/2025-01/policies` | store:pages:read |
| `get_policy` | `GET /api/2025-01/policies/{type}` | store:pages:read |
| `update_policy` | `PUT /api/2025-01/policies/{type}` | store:pages:write |
| `get_policy_translation` | `GET /api/2025-01/policies/{id}/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_policy_translation` | `PUT /api/2025-01/policies/{id}/translations/{locale}` | store:pages:write, store:settings.languages:write |
| `get_policy_translations` | `GET /api/2025-01/policies/translations/{locale}` | store:pages:read, store:settings.languages:read |
| `set_policy_translations` | `PUT /api/2025-01/policies/translations` | store:pages:write, store:settings.languages:write |
| `get_blog_post_limits` | `GET /api/2025-01/blog/posts/limits` | store:blog:read |
| `list_blog_posts` | `GET /api/2025-01/blog/posts` | store:blog:read |
| `search_blog_posts` | `GET /api/2025-01/blog/posts/search` | store:blog:read |
| `get_blog_post` | `GET /api/2025-01/blog/posts/{id}` | store:blog:read |
| `list_blog_post_metafields` | `GET /api/2025-01/blog/posts/{id}/metafields` | store:blog:read |
| `set_blog_post_metafield` | `PUT /api/2025-01/blog/posts/{id}/metafields` | store:blog:write |
| `delete_blog_post_metafield` | `DELETE /api/2025-01/blog/posts/{id}/metafields/{namespace}/{key}` | store:blog:write |
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
| `set_blog_post_translations` | `PUT /api/2025-01/blog/posts/translations` | store:blog:write, store:settings.languages:write |
| `get_blog_category_limits` | `GET /api/2025-01/blog/categories/limits` | store:blog:read |
| `list_blog_categories` | `GET /api/2025-01/blog/categories` | store:blog:read |
| `get_blog_category` | `GET /api/2025-01/blog/categories/{id}` | store:blog:read |
| `list_blog_category_metafields` | `GET /api/2025-01/blog/categories/{id}/metafields` | store:blog:read |
| `set_blog_category_metafield` | `PUT /api/2025-01/blog/categories/{id}/metafields` | store:blog:write |
| `delete_blog_category_metafield` | `DELETE /api/2025-01/blog/categories/{id}/metafields/{namespace}/{key}` | store:blog:write |
| `get_blog_category_metafield_translation` | `GET /api/2025-01/blog/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_category_metafield_translation` | `PUT /api/2025-01/blog/categories/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `create_blog_category` | `POST /api/2025-01/blog/categories` | store:blog:write |
| `update_blog_category` | `PUT /api/2025-01/blog/categories/{id}` | store:blog:write |
| `delete_blog_category` | `DELETE /api/2025-01/blog/categories/{id}` | store:blog:write |
| `bulk_delete_blog_categories` | `POST /api/2025-01/blog/categories/bulk-delete` | store:blog:write |
| `get_blog_category_translation` | `GET /api/2025-01/blog/categories/{id}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_category_translation` | `PUT /api/2025-01/blog/categories/{id}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_category_translations` | `GET /api/2025-01/blog/categories/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_category_translations` | `PUT /api/2025-01/blog/categories/translations` | store:blog:write, store:settings.languages:write |
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
| `set_blog_tag_translations` | `PUT /api/2025-01/blog/tags/translations` | store:blog:write, store:settings.languages:write |
| `get_blog_author_limits` | `GET /api/2025-01/blog/authors/limits` | store:blog:read |
| `list_blog_authors` | `GET /api/2025-01/blog/authors` | store:blog:read |
| `search_blog_authors` | `GET /api/2025-01/blog/authors/search` | store:blog:read |
| `get_blog_author` | `GET /api/2025-01/blog/authors/{id}` | store:blog:read |
| `create_blog_author` | `POST /api/2025-01/blog/authors` | store:blog:write |
| `update_blog_author` | `PUT /api/2025-01/blog/authors/{id}` | store:blog:write |
| `delete_blog_author` | `DELETE /api/2025-01/blog/authors/{id}` | store:blog:write |
| `bulk_delete_blog_authors` | `POST /api/2025-01/blog/authors/bulk-delete` | store:blog:write |
| `get_blog_author_translation` | `GET /api/2025-01/blog/authors/{id}/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_author_translation` | `PUT /api/2025-01/blog/authors/{id}/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_author_translations` | `GET /api/2025-01/blog/authors/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_author_translations` | `PUT /api/2025-01/blog/authors/translations` | store:blog:write, store:settings.languages:write |
| `get_blog_comment_limits` | `GET /api/2025-01/blog/comments/limits` | store:blog:read |
| `list_blog_comments` | `GET /api/2025-01/blog/comments` | store:blog:read |
| `get_blog_comment_counts` | `GET /api/2025-01/blog/comments/counts` | store:blog:read |
| `get_blog_comment` | `GET /api/2025-01/blog/comments/{id}` | store:blog:read |
| `update_blog_comment` | `PUT /api/2025-01/blog/comments/{id}` | store:blog:write |
| `bulk_update_blog_comment_status` | `POST /api/2025-01/blog/comments/bulk-update-status` | store:blog:write |
| `delete_blog_comment` | `DELETE /api/2025-01/blog/comments/{id}` | store:blog:write |
| `bulk_delete_blog_comments` | `POST /api/2025-01/blog/comments/bulk-delete` | store:blog:write |
| `get_menu_limits` | `GET /api/2025-01/menus/limits` | store:menus:read |
| `list_menus` | `GET /api/2025-01/menus` | store:menus:read |
| `get_menu` | `GET /api/2025-01/menus/{menuId}` | store:menus:read |
| `list_menu_items` | `GET /api/2025-01/menus/{menuId}/items` | store:menus:read |
| `search_menu_items` | `GET /api/2025-01/menus/{menuId}/items/search` | store:menus:read |
| `create_menu` | `POST /api/2025-01/menus` | store:menus:write |
| `update_menu` | `PUT /api/2025-01/menus/{menuId}` | store:menus:write |
| `save_menu` | `PUT /api/2025-01/menus/{menuId}/save` | store:menus:write |
| `create_menu_item` | `POST /api/2025-01/menus/{menuId}/items` | store:menus:write |
| `update_menu_item` | `PUT /api/2025-01/menus/{menuId}/items/{itemId}` | store:menus:write |
| `delete_menu_item` | `DELETE /api/2025-01/menus/{menuId}/items/{itemId}` | store:menus:write |
| `delete_menu` | `DELETE /api/2025-01/menus/{menuId}` | store:menus:write |
| `get_menu_item_translation` | `GET /api/2025-01/menus/items/{itemId}/translations/{locale}` | store:menus:read, store:settings.languages:read |
| `set_menu_item_translation` | `PUT /api/2025-01/menus/items/{itemId}/translations/{locale}` | store:menus:write, store:settings.languages:write |
| `get_menu_item_translations` | `GET /api/2025-01/menus/items/translations/{locale}` | store:menus:read, store:settings.languages:read |
| `set_menu_item_translations` | `PUT /api/2025-01/menus/items/translations` | store:menus:write, store:settings.languages:write |
| `get_tag_limits` | `GET /api/2025-01/tags/limits` | store:products:read |
| `list_tags` | `GET /api/2025-01/tags` | store:products:read |
| `search_tags` | `GET /api/2025-01/tags/search` | store:products:read |
| `get_tag` | `GET /api/2025-01/tags/{id}` | store:products:read |
| `create_tag` | `POST /api/2025-01/tags` | store:products:write |
| `bulk_create_tags` | `POST /api/2025-01/tags/bulk-create` | store:products:write |
| `update_tag` | `PUT /api/2025-01/tags/{id}` | store:products:write |
| `delete_tag` | `DELETE /api/2025-01/tags/{id}` | store:products:write |
| `bulk_delete_tags` | `POST /api/2025-01/tags/bulk-delete` | store:products:write |
| `get_tag_translation` | `GET /api/2025-01/tags/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_tag_translation` | `PUT /api/2025-01/tags/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_tag_translations` | `GET /api/2025-01/tags/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_tag_translations` | `PUT /api/2025-01/tags/translations` | store:products:write, store:settings.languages:write |
| `get_brand_limits` | `GET /api/2025-01/brands/limits` | store:products:read |
| `list_brands` | `GET /api/2025-01/brands` | store:products:read |
| `search_brands` | `GET /api/2025-01/brands/search` | store:products:read |
| `get_brand` | `GET /api/2025-01/brands/{id}` | store:products:read |
| `list_brand_metafields` | `GET /api/2025-01/brands/{id}/metafields` | store:products:read |
| `set_brand_metafield` | `PUT /api/2025-01/brands/{id}/metafields` | store:products:write |
| `delete_brand_metafield` | `DELETE /api/2025-01/brands/{id}/metafields/{namespace}/{key}` | store:products:write |
| `get_brand_metafield_translation` | `GET /api/2025-01/brands/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_brand_metafield_translation` | `PUT /api/2025-01/brands/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `create_brand` | `POST /api/2025-01/brands` | store:products:write |
| `update_brand` | `PUT /api/2025-01/brands/{id}` | store:products:write |
| `delete_brand` | `DELETE /api/2025-01/brands/{id}` | store:products:write |
| `get_brand_translation` | `GET /api/2025-01/brands/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_brand_translation` | `PUT /api/2025-01/brands/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_brand_translations` | `GET /api/2025-01/brands/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_brand_translations` | `PUT /api/2025-01/brands/translations` | store:products:write, store:settings.languages:write |
| `get_vendor_limits` | `GET /api/2025-01/vendors/limits` | store:products:read |
| `list_vendors` | `GET /api/2025-01/vendors` | store:products:read |
| `search_vendors` | `GET /api/2025-01/vendors/search` | store:products:read |
| `get_vendor` | `GET /api/2025-01/vendors/{id}` | store:products:read |
| `list_vendor_metafields` | `GET /api/2025-01/vendors/{id}/metafields` | store:products:read |
| `set_vendor_metafield` | `PUT /api/2025-01/vendors/{id}/metafields` | store:products:write |
| `delete_vendor_metafield` | `DELETE /api/2025-01/vendors/{id}/metafields/{namespace}/{key}` | store:products:write |
| `get_vendor_metafield_translation` | `GET /api/2025-01/vendors/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_vendor_metafield_translation` | `PUT /api/2025-01/vendors/{id}/metafields/{namespace}/{key}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `create_vendor` | `POST /api/2025-01/vendors` | store:products:write |
| `update_vendor` | `PUT /api/2025-01/vendors/{id}` | store:products:write |
| `delete_vendor` | `DELETE /api/2025-01/vendors/{id}` | store:products:write |
| `get_vendor_translation` | `GET /api/2025-01/vendors/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_vendor_translation` | `PUT /api/2025-01/vendors/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_vendor_translations` | `GET /api/2025-01/vendors/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_vendor_translations` | `PUT /api/2025-01/vendors/translations` | store:products:write, store:settings.languages:write |
| `get_file_limits` | `GET /api/2025-01/files/limits` | store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `get_storage_quota` | `GET /api/2025-01/files/quota` | store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `list_files` | `GET /api/2025-01/files` | store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `create_file_uploads` | `POST /api/2025-01/files/upload-intents` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `finalize_file_uploads` | `POST /api/2025-01/files/upload-intents/finalize` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `get_file_upload_status` | `POST /api/2025-01/files/upload-intents/status` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `get_file` | `GET /api/2025-01/files/{id}` | store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `request_file_preview` | `POST /api/2025-01/files/{id}/preview` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `update_file` | `PUT /api/2025-01/files/{id}` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `delete_file` | `DELETE /api/2025-01/files/{id}` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `estimate_image_generation` | `POST /api/2025-01/files/generate/estimate` | store:ai.image_generation:write |
| `generate_image` | `POST /api/2025-01/files/generate` | store:ai.image_generation:write, and store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `estimate_alt_text_job` | `GET /api/2025-01/files/alt-text-jobs/estimate` | store:ai.image_generation:write, and store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `create_alt_text_job` | `POST /api/2025-01/files/alt-text-jobs` | store:ai.image_generation:write, and store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `get_alt_text_job` | `GET /api/2025-01/files/alt-text-jobs/{id}` | store:ai.image_generation:write, and store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `cancel_alt_text_job` | `POST /api/2025-01/files/alt-text-jobs/{id}/cancel` | store:ai.image_generation:write, and store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `get_order` | `GET /api/2025-01/orders/{id}` | store:orders:read |
| `list_order_edits` | `GET /api/2025-01/orders/{id}/edits` | store:orders:read |
| `get_order_edit_options` | `GET /api/2025-01/orders/{id}/edit-options` | store:orders:read |
| `list_order_edit_shipping_options` | `POST /api/2025-01/orders/{id}/edit-shipping-options` | store:orders:write |
| `preview_order_edit` | `POST /api/2025-01/orders/{id}/edits/preview` | store:orders:write |
| `apply_order_edit` | `POST /api/2025-01/orders/{id}/edits` | store:orders:write |
| `get_blog_settings` | `GET /api/2025-01/blog/settings` | store:blog:read |
| `update_blog_settings` | `PUT /api/2025-01/blog/settings` | store:blog:write |
| `get_blog_list_seo` | `GET /api/2025-01/blog/list-seo` | store:blog:read |
| `update_blog_list_seo` | `PUT /api/2025-01/blog/list-seo` | store:blog:write |
| `get_blog_list_seo_translation` | `GET /api/2025-01/blog/list-seo/translations/{locale}` | store:blog:read, store:settings.languages:read |
| `set_blog_list_seo_translation` | `PUT /api/2025-01/blog/list-seo/translations/{locale}` | store:blog:write, store:settings.languages:write |
| `get_blog_list_seo_country` | `GET /api/2025-01/blog/list-seo/countries/{countryCode}/{locale}` | store:blog:read |
| `update_blog_list_seo_country` | `PUT /api/2025-01/blog/list-seo/countries/{countryCode}/{locale}` | store:blog:write |
| `delete_blog_list_seo_country` | `DELETE /api/2025-01/blog/list-seo/countries/{countryCode}/{locale}` | store:blog:write |
| `get_list_page_seo` | `GET /api/2025-01/list-page-seo/{pageType}` | store:products:read |
| `update_list_page_seo` | `PUT /api/2025-01/list-page-seo/{pageType}` | store:products:write |
| `get_list_page_seo_translation` | `GET /api/2025-01/list-page-seo/{pageType}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_list_page_seo_translation` | `PUT /api/2025-01/list-page-seo/{pageType}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_list_page_seo_translations` | `GET /api/2025-01/list-page-seo/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_list_page_seo_translations` | `PUT /api/2025-01/list-page-seo/translations` | store:products:write, store:settings.languages:write |
| `get_list_page_seo_country` | `GET /api/2025-01/list-page-seo/{pageType}/countries/{countryCode}/{locale}` | store:products:read |
| `update_list_page_seo_country` | `PUT /api/2025-01/list-page-seo/{pageType}/countries/{countryCode}/{locale}` | store:products:write |
| `delete_list_page_seo_country` | `DELETE /api/2025-01/list-page-seo/{pageType}/countries/{countryCode}/{locale}` | store:products:write |
| `list_languages` | `GET /api/2025-01/languages` | store:settings.languages:read |
| `set_languages` | `PUT /api/2025-01/languages` | store:settings.languages:write |
| `set_default_language` | `PUT /api/2025-01/languages/default` | store:settings.languages:write |
| `replace_only_language` | `PUT /api/2025-01/languages/replace-only` | store:settings.languages:write |
| `get_language_readiness` | `GET /api/2025-01/languages/{locale}/readiness` | store:settings.languages:read, store:online_store.storefronts:read |
| `delete_language_translations` | `DELETE /api/2025-01/languages/{locale}/translations` | store:settings.languages:write |
| `list_available_languages` | `GET /api/2025-01/reference/languages` | Valid Store connection; no resource scope |
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
| `set_automatic_currency_enabled` | `POST /api/2025-01/currencies/enable` | store:settings.currencies:write |
| `bulk_set_automatic_currencies_enabled` | `POST /api/2025-01/currencies/bulk-enable` | store:settings.currencies:write |
| `bulk_create_currencies` | `POST /api/2025-01/currencies/bulk-create` | store:settings.currencies:write |
| `bulk_delete_currencies` | `POST /api/2025-01/currencies/bulk-delete` | store:settings.currencies:write |
| `bulk_update_currency_rates` | `POST /api/2025-01/currencies/bulk-update-rate` | store:settings.currencies:write |
| `bulk_update_currencies` | `POST /api/2025-01/currencies/bulk-update` | store:settings.currencies:write |
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
| `get_dns_operation` | `GET /api/2025-01/dns-zones/{zoneId}/operations/{operationId}` | store:settings.domains:read |
| `create_dns_record` | `POST /api/2025-01/dns-zones/{zoneId}/records` | store:settings.domains:write |
| `update_dns_record` | `PUT /api/2025-01/dns-zones/{zoneId}/records/{recordId}` | store:settings.domains:write |
| `delete_dns_record` | `DELETE /api/2025-01/dns-zones/{zoneId}/records/{recordId}` | store:settings.domains:write |
| `list_assignable_domains` | `GET /api/2025-01/domains/assignable` | store:settings.domains:write |
| `assign_storefront_domain` | `PUT /api/2025-01/domains/{domainId}/storefront` | store:settings.domains:write |
| `set_country_domain` | `PUT /api/2025-01/domains/{domainId}/country` | store:settings.domains:write |
| `clear_country_domain` | `DELETE /api/2025-01/domains/{domainId}/country` | store:settings.domains:write |
| `set_primary_domain` | `PUT /api/2025-01/domains/{domainId}/primary` | store:settings.domains:write |
| `clear_primary_domain` | `DELETE /api/2025-01/storefronts/{storefrontId}/primary-domain` | store:settings.domains:write |
| `create_domain` | `POST /api/2025-01/domains` | store:settings.domains:write |
| `verify_domain` | `POST /api/2025-01/domains/{domainId}/verify` | store:settings.domains:write |
| `check_domain_removal` | `GET /api/2025-01/domains/{domainId}/removal-check` | store:settings.domains:write |
| `delete_domain` | `DELETE /api/2025-01/domains/{domainId}` | store:settings.domains:write |
| `connect_domain` | `POST /api/2025-01/domains/connection` | store:settings.domains:write |
| `create_dns_zone` | `POST /api/2025-01/dns-zones` | store:settings.domains:write |
| `refresh_dns_zone` | `POST /api/2025-01/dns-zones/{zoneId}/refresh` | store:settings.domains:write |
| `scan_dns_zone` | `POST /api/2025-01/dns-zones/{zoneId}/scan` | store:settings.domains:write |
| `cancel_scan_dns_zone` | `POST /api/2025-01/dns-zones/{zoneId}/cancel-scan` | store:settings.domains:write |
| `retry_dns_zone` | `POST /api/2025-01/dns-zones/{zoneId}/retry` | store:settings.domains:write |
| `bulk_delete_dns_records` | `POST /api/2025-01/dns-zones/{zoneId}/records/bulk-delete` | store:settings.domains:write |
| `preview_dns_import` | `POST /api/2025-01/dns-zones/{zoneId}/import/preview` | store:settings.domains:write |
| `import_dns_records` | `POST /api/2025-01/dns-zones/{zoneId}/import` | store:settings.domains:write |
| `export_dns_records` | `POST /api/2025-01/dns-zones/{zoneId}/export` | store:settings.domains:write |
| `list_dns_jobs` | `GET /api/2025-01/dns/jobs` | store:settings.domains:read |
| `get_dns_job_limits` | `GET /api/2025-01/dns/jobs/limits` | store:settings.domains:read |
| `list_dns_job_errors` | `GET /api/2025-01/dns/jobs/{jobId}/errors` | store:settings.domains:read |
| `get_dns_export_download` | `GET /api/2025-01/dns/jobs/{jobId}/download` | store:settings.domains:read |
| `cancel_dns_job` | `POST /api/2025-01/dns/jobs/{jobId}/cancel` | store:settings.domains:write |
| `list_email_senders` | `GET /api/2025-01/email/senders` | store:settings.email:read |
| `list_email_domains` | `GET /api/2025-01/email/domains` | store:settings.email:read |
| `list_email_domain_candidates` | `GET /api/2025-01/email/domains/candidates` | store:settings.email:read |
| `get_email_reply_to` | `GET /api/2025-01/email/reply-to` | store:settings.email:read |
| `update_email_reply_to` | `PUT /api/2025-01/email/reply-to` | store:settings.email:write |
| `get_email_suppression` | `GET /api/2025-01/email/suppressions` | store:settings.email:read |
| `create_email_sender` | `POST /api/2025-01/email/senders` | store:settings.email:write |
| `delete_email_sender` | `DELETE /api/2025-01/email/senders/{addressId}` | store:settings.email:write |
| `set_default_email_sender` | `PUT /api/2025-01/email/senders/{addressId}/default` | store:settings.email:write |
| `create_email_domain` | `POST /api/2025-01/email/domains` | store:settings.email:write |
| `verify_email_domain` | `POST /api/2025-01/email/domains/{domainId}/verify` | store:settings.email:write |
| `restart_email_domain` | `POST /api/2025-01/email/domains/{domainId}/restart` | store:settings.email:write |
| `delete_email_domain` | `DELETE /api/2025-01/email/domains/{domainId}` | store:settings.email:write |
| `set_email_mail_from` | `PUT /api/2025-01/email/domains/{domainId}/mail-from` | store:settings.email:write |
| `get_email_overview` | `GET /api/2025-01/email/overview` | store:settings.email:read |
| `get_email_domain` | `GET /api/2025-01/email/domains/{domainId}` | store:settings.email:read |
| `check_email_domain_removal` | `GET /api/2025-01/email/domains/{domainId}/removal-check` | store:settings.email:read |
| `check_email_sender_removal` | `GET /api/2025-01/email/senders/{addressId}/removal-check` | store:settings.email:read |
| `list_email_history` | `GET /api/2025-01/email/history` | store:settings.email:read |
| `get_email_statistics` | `GET /api/2025-01/email/statistics` | store:settings.email:read |
| `list_email_suppressions` | `GET /api/2025-01/email/suppression-history` | store:settings.email:read |
| `lift_email_suppression` | `POST /api/2025-01/email/suppressions/lift` | store:settings.email:write |
| `request_verification_code` | `POST /api/2025-01/verification-codes` | store:settings.domains:write or store:settings.email:write (the one of the requested action) |
| `list_store_api_scopes` | `GET /api/2025-01/scopes` | Valid Store connection; no resource scope |
| `list_countries` | `GET /api/2025-01/reference/countries` | Valid Store connection; no resource scope |
| `list_subdivisions` | `GET /api/2025-01/reference/subdivisions/{countryCode}` | Valid Store connection; no resource scope |
| `list_timezones` | `GET /api/2025-01/reference/timezones` | Valid Store connection; no resource scope |
| `list_available_currencies` | `GET /api/2025-01/reference/currencies` | Valid Store connection; no resource scope |
| `list_phone_country_codes` | `GET /api/2025-01/reference/phone-codes` | Valid Store connection; no resource scope |
| `get_number_format_defaults` | `GET /api/2025-01/reference/number-format-defaults/{countryCode}` | Valid Store connection; no resource scope |
| `list_address_formats` | `GET /api/2025-01/reference/address-format` | Valid Store connection; no resource scope |
| `get_address_format` | `GET /api/2025-01/reference/address-format/{countryCode}` | Valid Store connection; no resource scope |
| `list_catalog_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | store:products:read |
| `list_page_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | store:pages:read |
| `list_blog_metafield_definitions` | `GET /api/2025-01/metafield-definitions` | store:blog:read |
| `create_order` | `POST /api/2025-01/orders` | store:orders:write |
| `get_customer_limits` | `GET /api/2025-01/customers/limits` | store:customers:read |
| `list_customers` | `GET /api/2025-01/customers` | store:customers:read |
| `get_customer` | `GET /api/2025-01/customers/{id}` | store:customers:read |
| `create_customer` | `POST /api/2025-01/customers` | store:customers:write |
| `update_customer` | `PUT /api/2025-01/customers/{id}` | store:customers:write |

## Product filters

Filter definitions are capped at 50 per store, including built-in and disabled filters. Source discovery pages accept at most 100 rows. Update requires the definition revision; reorder requires the complete list revision and every definition ID. Only labels are translatable; source values retain their filter tokens. Built-in filters keep a platform label, provided in every storefront language, until the merchant renames them; translation reads return `label.origin` (`merchant` or `platform`), and clearing a translation restores the platform label. Translation tools require both Products and Languages access.

| Tool | Store API operation | OAuth scopes |
| --- | --- | --- |
| `get_product_filter_contract` | `GET /api/2025-01/product-filters/contract` | store:products:read |
| `list_product_filter_sources` | `GET /api/2025-01/product-filters/sources` | store:products:read |
| `list_product_filters` | `GET /api/2025-01/product-filters` | store:products:read |
| `create_product_filter` | `POST /api/2025-01/product-filters` | store:products:write |
| `reorder_product_filters` | `PUT /api/2025-01/product-filters/reorder` | store:products:write |
| `update_product_filter` | `PUT /api/2025-01/product-filters/{id}` | store:products:write |
| `delete_product_filter` | `DELETE /api/2025-01/product-filters/{id}` | store:products:write |
| `get_product_filter_translation` | `GET /api/2025-01/product-filters/{id}/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_filter_translation` | `PUT /api/2025-01/product-filters/{id}/translations/{locale}` | store:products:write, store:settings.languages:write |
| `get_product_filter_translations` | `GET /api/2025-01/product-filters/translations/{locale}` | store:products:read, store:settings.languages:read |
| `set_product_filter_translations` | `PUT /api/2025-01/product-filters/translations` | store:products:write, store:settings.languages:write |

## Reviews

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_review_limits` | `GET /api/2025-01/reviews/limits` | store:reviews:read |
| `list_reviews` | `GET /api/2025-01/reviews` | store:reviews:read |
| `get_review` | `GET /api/2025-01/reviews/{id}` | store:reviews:read |
| `moderate_review` | `PUT /api/2025-01/reviews/{id}` | store:reviews:write |
| `respond_review` | `PUT /api/2025-01/reviews/{id}/response` | store:reviews:write |
| `delete_review_response` | `DELETE /api/2025-01/reviews/{id}/response` | store:reviews:write |
| `delete_review` | `DELETE /api/2025-01/reviews/{id}` | store:reviews:write |
| `bulk_moderate_reviews` | `POST /api/2025-01/reviews/bulk-moderate` | store:reviews:write |
| `bulk_delete_reviews` | `POST /api/2025-01/reviews/bulk-delete` | store:reviews:write |
| `get_review_bulk_operation` | `GET /api/2025-01/reviews/bulk-operations/{operationId}` | store:reviews:write |
| `acknowledge_review_bulk_operation` | `POST /api/2025-01/reviews/bulk-operations/{operationId}/acknowledge` | store:reviews:write |
| `get_review_settings` | `GET /api/2025-01/reviews/settings` | store:reviews:read |
| `update_review_settings` | `PUT /api/2025-01/reviews/settings` | store:reviews:write |

## Customers, customer tags and customer groups

`list_marketing_subscribers` filters by `status` (`active`, `pending_confirmation`, `unsubscribed`), `source` (`coming_soon` for sign-ups from a storefront's Coming Soon page) or `search`. `get_marketing_subscriber` returns `consent`, the latest proof stored with a sign-up (the consent wording the visitor agreed to, its `text_version`, language, time, IP address, user agent and page), or `null` when the sign-up carried none, and `consent_records` (up to 20, newest first). Times are RFC 3339 in the store's timezone. IP address and user agent are personal data: keep them only as long as the proof is needed.

`delete_marketing_subscriber` permanently deletes a subscriber and its proof of consent (`store:customers:write`). Every first call returns `CONFIRMATION_REQUIRED` with `error.details.warnings`, `error.details.impact` (`email`, `status`, `consent_records`, `customer_id`, `customer_stops_email_marketing`) and a single-use `confirmation_token`. Show the warnings to the merchant and repeat with `confirmed: true` and the token only after they approve. A linked active customer stops receiving marketing emails, the proof can no longer be shown, and the address can be added again only with new consent.

Email subscriber lifecycle webhooks are `subscribers/create`, `subscribers/update` and `subscribers/delete` (app scope `read_customers`). Their `subscriber` payload is the GET resource, including `channel: email`, status, source, and consent proof (`text_version`, `captured_at`, `source_page`, `locale`). Creation includes pending confirmation; confirmation, unsubscribe and resubscription are updates. Delete carries the resource before deletion. Use `get_webhook_topic_schema` to inspect fields and projections.


| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_customer_metafields` | `GET /api/2025-01/customers/{id}/metafields` | store:customers:read |
| `set_customer_metafield` | `PUT /api/2025-01/customers/{id}/metafields` | store:customers:write |
| `delete_customer_metafield` | `DELETE /api/2025-01/customers/{id}/metafields/{namespace}/{key}` | store:customers:write |
| `delete_customer` | `DELETE /api/2025-01/customers/{id}` | store:customers:write |
| `get_customer_store_credit_limits` | `GET /api/2025-01/customers/store-credit/limits` | store:customers:read |
| `get_customer_store_credit_settings` | `GET /api/2025-01/customers/store-credit/settings` | store:customers:read |
| `get_customer_store_credit` | `GET /api/2025-01/customers/{id}/store-credit` | store:customers:read |
| `list_customer_store_credit_ledger` | `GET /api/2025-01/customers/{id}/store-credit/ledger` | store:customers:read |
| `grant_customer_store_credit` | `POST /api/2025-01/customers/{id}/store-credit-grants` | store:customers:write |
| `revoke_customer_store_credit` | `POST /api/2025-01/customers/{id}/store-credit-revocations` | store:customers:write |
| `get_text_marketing_consent` | `GET /api/2025-01/text-marketing-consents` | store:customers:read |
| `set_text_marketing_consent` | `PUT /api/2025-01/text-marketing-consents` | store:customers:write |
| `list_marketing_subscribers` | `GET /api/2025-01/marketing-subscribers` | store:customers:read |
| `get_marketing_subscriber` | `GET /api/2025-01/marketing-subscribers/{subscriberId}` | store:customers:read |
| `delete_marketing_subscriber` | `DELETE /api/2025-01/marketing-subscribers/{subscriberId}` | store:customers:write |
| `get_customer_tag_limits` | `GET /api/2025-01/customer-tags/limits` | store:customers:read |
| `list_customer_tags` | `GET /api/2025-01/customer-tags` | store:customers:read |
| `get_customer_tag` | `GET /api/2025-01/customer-tags/{id}` | store:customers:read |
| `create_customer_tag` | `POST /api/2025-01/customer-tags` | store:customers:write |
| `bulk_create_customer_tags` | `POST /api/2025-01/customer-tags/bulk-create` | store:customers:write |
| `update_customer_tag` | `PUT /api/2025-01/customer-tags/{id}` | store:customers:write |
| `delete_customer_tag` | `DELETE /api/2025-01/customer-tags/{id}` | store:customers:write |
| `bulk_delete_customer_tags` | `POST /api/2025-01/customer-tags/bulk-delete` | store:customers:write |
| `get_customer_group_limits` | `GET /api/2025-01/customer-groups/limits` | store:customers:read |
| `get_customer_group_purchase_rule_readiness` | `GET /api/2025-01/customer-groups/purchase-rule-readiness` | store:customers:read |
| `list_customer_groups` | `GET /api/2025-01/customer-groups` | store:customers:read |
| `get_customer_group` | `GET /api/2025-01/customer-groups/{id}` | store:customers:read |
| `create_customer_group` | `POST /api/2025-01/customer-groups` | store:customers:write |
| `update_customer_group` | `PUT /api/2025-01/customer-groups/{id}` | store:customers:write |
| `delete_customer_group` | `DELETE /api/2025-01/customer-groups/{id}` | store:customers:write |
| `preview_customer_group_rules` | `POST /api/2025-01/customer-groups/preview-rules` | store:customers:read |
| `list_customer_group_members` | `GET /api/2025-01/customer-groups/{id}/members` | store:customers:read |
| `list_customer_group_candidates` | `GET /api/2025-01/customer-groups/{id}/candidate-members` | store:customers:read |
| `get_customer_group_membership_snapshot` | `GET /api/2025-01/customer-groups/{id}/membership-snapshot` | store:customers:read |
| `list_customer_group_membership_changes` | `GET /api/2025-01/customer-groups/{id}/membership-changes` | store:customers:read |
| `add_customer_group_members` | `POST /api/2025-01/customer-groups/{id}/members` | store:customers:write |
| `remove_customer_group_members` | `POST /api/2025-01/customer-groups/{id}/members/remove` | store:customers:write |

## Inventory, inventory groups and locations

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_inventory_limits` | `GET /api/2025-01/inventory/limits` | store:inventory:read |
| `list_inventory_levels` | `GET /api/2025-01/inventory/levels` | store:inventory:read |
| `list_inventory_movements` | `GET /api/2025-01/inventory/movements` | store:inventory:read |
| `list_inventory_low_stocks` | `GET /api/2025-01/inventory/low-stock` | store:inventory:read |
| `list_inventory_commitments` | `GET /api/2025-01/inventory/commitments` | store:inventory:read |
| `list_inventory_commitment_activitys` | `GET /api/2025-01/inventory/commitment-activity` | store:inventory:read |
| `create_inventory_sync_jobs_upload_intents` | `POST /api/2025-01/inventory/sync-jobs/upload-intents` | store:inventory:write |
| `finalize_inventory_sync_jobs_upload_intents` | `POST /api/2025-01/inventory/sync-jobs/upload-intents/finalize` | store:inventory:write |
| `status_inventory_sync_jobs_upload_intents` | `POST /api/2025-01/inventory/sync-jobs/upload-intents/status` | store:inventory:write |
| `create_inventory_sync_jobs` | `POST /api/2025-01/inventory/sync-jobs` | store:inventory:write |
| `get_inventory_sync_jobs` | `GET /api/2025-01/inventory/sync-jobs/{jobId}` | store:inventory:read |
| `create_inventory_adjustments` | `POST /api/2025-01/inventory/adjustments` | store:inventory:write |
| `set_product_threshold` | `POST /api/2025-01/products/{id}/set-threshold` | store:inventory:write |
| `set_product_variant_threshold` | `POST /api/2025-01/products/{id}/variants/{variantId}/set-threshold` | store:inventory:write |
| `list_inventory_transfers` | `GET /api/2025-01/transfers` | store:inventory:read |
| `get_inventory_transfer` | `GET /api/2025-01/transfers/{transferId}` | store:inventory:read |
| `create_inventory_transfer` | `POST /api/2025-01/transfers` | store:inventory:write |
| `update_inventory_transfer_status` | `PUT /api/2025-01/transfers/{transferId}/status` | store:inventory:write |
| `bulk_inventory_transfer_status` | `POST /api/2025-01/transfers/bulk-status` | store:inventory:write |
| `receive_inventory_transfer` | `POST /api/2025-01/transfers/{transferId}/receive` | store:inventory:write |
| `delete_inventory_transfer` | `DELETE /api/2025-01/transfers/{transferId}` | store:inventory:write |
| `bulk_inventory_transfer_delete` | `POST /api/2025-01/transfers/bulk-delete` | store:inventory:write |
| `list_inventory_restock_requests` | `GET /api/2025-01/inventory/restock-requests` | store:inventory:read |
| `get_inventory_restock_request_limits` | `GET /api/2025-01/inventory/restock-requests/limits` | store:inventory:read |
| `stats_inventory_restock_request` | `GET /api/2025-01/inventory/restock-requests/stats` | store:inventory:read |
| `notify_inventory_restock_request` | `POST /api/2025-01/inventory/restock-requests/notify` | store:inventory:write |
| `get_inventory_restock_alert_settings` | `GET /api/2025-01/inventory/restock-alert-settings` | store:inventory:read |
| `update_inventory_restock_alert_settings` | `PUT /api/2025-01/inventory/restock-alert-settings` | store:inventory:write |
| `get_inventory_group_limits` | `GET /api/2025-01/inventory-groups/limits` | store:inventory:read |
| `list_inventory_groups` | `GET /api/2025-01/inventory-groups` | store:inventory:read |
| `get_inventory_group` | `GET /api/2025-01/inventory-groups/{groupId}` | store:inventory:read |
| `list_inventory_group_products` | `GET /api/2025-01/inventory-groups/{groupId}/products` | store:inventory:read, store:products:read |
| `list_inventory_group_variants` | `GET /api/2025-01/inventory-groups/{groupId}/variants` | store:inventory:read, store:products:read |
| `create_inventory_group` | `POST /api/2025-01/inventory-groups` | store:inventory:write |
| `update_inventory_group` | `PUT /api/2025-01/inventory-groups/{groupId}` | store:inventory:write |
| `delete_inventory_group` | `DELETE /api/2025-01/inventory-groups/{groupId}` | store:inventory:write |
| `bulk_delete_inventory_groups` | `POST /api/2025-01/inventory-groups/bulk-delete` | store:inventory:write |
| `set_inventory_group_quantity` | `POST /api/2025-01/inventory-groups/{groupId}/set-quantity` | store:inventory:write |
| `adjust_inventory_group_quantity` | `POST /api/2025-01/inventory-groups/{groupId}/adjust` | store:inventory:write |
| `set_inventory_group_threshold` | `POST /api/2025-01/inventory-groups/{groupId}/set-threshold` | store:inventory:write |
| `list_inventory_group_movements` | `GET /api/2025-01/inventory-groups/{groupId}/movements` | store:inventory:read |
| `list_inventory_group_commitments` | `GET /api/2025-01/inventory-groups/{groupId}/commitments` | store:inventory:read |
| `list_inventory_group_commitment_activitys` | `GET /api/2025-01/inventory-groups/{groupId}/commitment-activity` | store:inventory:read |
| `list_inventory_group_stocks` | `GET /api/2025-01/inventory-groups/{groupId}/stock` | store:inventory:read |
| `bulk_add_inventory_group_stocks` | `POST /api/2025-01/inventory-groups/{groupId}/stock/bulk` | store:inventory:write |
| `bulk_mutate_inventory_group_stock` | `POST /api/2025-01/inventory-groups/{groupId}/stock/bulk-mutate` | store:inventory:write |
| `delete_inventory_group_stock` | `DELETE /api/2025-01/inventory-groups/{groupId}/stock/{locationId}` | store:inventory:write |
| `get_location_limits` | `GET /api/2025-01/locations/limits` | store:locations:read |
| `list_locations` | `GET /api/2025-01/locations` | store:locations:read |
| `get_location` | `GET /api/2025-01/locations/{id}` | store:locations:read |
| `impact_location` | `GET /api/2025-01/locations/{id}/impact` | store:locations:read |
| `create_location` | `POST /api/2025-01/locations` | store:locations:write |
| `update_location` | `PUT /api/2025-01/locations/{id}` | store:locations:write |
| `delete_location` | `DELETE /api/2025-01/locations/{id}` | store:locations:write |
| `get_location_translation` | `GET /api/2025-01/locations/{id}/translations/{locale}` | store:locations:read, store:settings.languages:read |
| `set_location_translation` | `PUT /api/2025-01/locations/{id}/translations/{locale}` | store:locations:write, store:settings.languages:write |
| `get_location_translations` | `GET /api/2025-01/locations/translations/{locale}` | store:locations:read, store:settings.languages:read |
| `set_location_translations` | `PUT /api/2025-01/locations/translations` | store:locations:write, store:settings.languages:write |
| `reorder_locations` | `POST /api/2025-01/locations/reorder` | store:locations:write |

## Domains and DNS

The domain tools do everything Store Admin › Settings › Domains does, for the merchant's own connection only; installed apps can never hold domain access. Reads need `store:settings.domains:read`, every change `store:settings.domains:write`, and each change runs as the connected member with that member's permissions.

Every domain returned by `get_domain`, `list_domains`, `create_domain` and `verify_domain` carries what to show and do at any stage of its life, the same values Store Admin and the mobile app render, in the request language:

- `badge` (`label`, `tone`) and `role_label`: how the domain reads in a list.
- `setup`: the step-by-step setup state (nameservers to set or records to add, what public DNS shows now, the last and next automatic check).
- `next_action`: the single next step, with `label`, `message`, `after` (when looking again makes sense) and the `tool` and `arguments` to call. Absent when nothing is left to do.
- `issue`: what is wrong after setup (HTTPS blocked by a CAA record or another Cloudflare account, certificate timed out, DNS records changed, disconnected, primary address handed to another domain), with `title`, `message`, `fix`, `since` and, for a DNS warning, the `deadline`.
- `actions`: what the domain allows now (check, assign_storefront, unassign, set_primary, clear_primary, set_country, clear_country, manage_dns, remove).

Walk the merchant through a domain like this; the [Connect a domain walkthrough](https://developers.tringify.com/apps/connectors/connect-a-domain) has a full example.

1. **Add.** Call `connect_domain` with `action: discover`. Show each of its `options` (`label`, `description`, and `unavailable_reason` when it doesn't suit the address) and let the merchant choose; `chosen` is the recommendation. Call `create_domain` with the chosen `dns_management`. `DOMAIN_LIMIT_REACHED`, `DOMAIN_INVALID_FORMAT` and `DOMAIN_CLAIM_REQUIRED` (another store's unfinished claim: publish the TXT record its message names, then add again) are refusals to relay as given.
2. **Set up.** Show `next_action.message` (and `setup.nameservers` or `setup.records`). When the merchant says they made the change, call `verify_domain`; it never fails a domain while DNS is still updating. Tringify keeps checking in the background, so don't loop: look again with `get_domain` after `next_action.after`. If `connect_domain` (`action: apply`) returns `apply_url`, give it to the merchant to open in their browser; never open or fetch it yourself.
3. **HTTPS.** After ownership is verified the certificate is issued, usually within minutes. If `issue` appears (for example `certificate_caa`), relay its `message` and `fix`.
4. **Assign.** When `next_action.key` is `assign_storefront`, call `list_storefronts`, let the merchant choose and call `assign_storefront_domain`. `set_primary_domain` (confirm first, then a verification code), `set_country_domain` and `clear_country_domain` follow.
5. **Health.** Connected domains are re-checked every 6 hours. A DNS warning (`issue.key` `dns_warning`) says what public DNS shows, the fix and the deadline; after the fix, `verify_domain` re-checks at once. A primary domain that stopped working hands the primary address over (`issue.key` `primary_fallback`); once it reconnects, `next_action` offers `set_primary_domain` again.
6. **Hosted DNS.** `create_dns_zone` lets Tringify host a root domain's DNS. A zone's `view` has `state_label`, `tone`, `working` (read again after `poll_after_ms`) and `operation` (the one change to show: queued, applied, failed or cancelled). Queued DNS work answers HTTP 202: poll `get_dns_operation` with the returned `operation_id`, or follow import and export jobs with `list_dns_jobs`. `refresh_dns_zone`, `scan_dns_zone`, `cancel_scan_dns_zone` and `retry_dns_zone` change no records. Preview an import with `preview_dns_import`; get an export file with `get_dns_export_download` (the link works for 5 minutes).
7. **Remove.** Call `check_domain_removal` and show its `confirm` sentence and every `impacts[].message` (hosted DNS and its records, sending domains, sender addresses, the new default sender, that the domain is free for any store afterwards). After the merchant approves, call its `next_action` (`request_verification_code` with the given arguments), ask the merchant for the emailed code and call `delete_domain` with `otp_code`. A domain that can't be removed yet is refused with `details.next_action`: `DOMAIN_ASSIGNED_TO_STOREFRONT` (unassign first, which needs its own `unassign_domain` code) or `DOMAIN_DNS_NAMESERVERS_IN_USE` (the message lists the Tringify nameservers to change at the registrar; check again once public DNS shows the change).

Removing a domain, setting up hosted DNS, creating, updating, deleting, bulk deleting or importing records, unassigning a domain, and setting or clearing the primary domain need `otp_code`: a verification code bound to the action and target the tool names (see Verification codes). Adding, checking, assigning, country domains, refreshing, scanning, retrying, exporting and reading need no code.

## Email settings

The email settings tools do everything Store Admin › Settings › Email does, for the merchant's own connection only; installed apps can never hold email access. Reads need `store:settings.email:read`, every change `store:settings.email:write`. Every response carries the text Store Admin and the mobile app show, in the request language; show it as given and never work out labels, eligibility or next steps yourself. No response names the sending provider.

- `get_email_overview`: how the store sends now (`badge`), the four `steps` in order (sending domain, sender address, default sender, reply-to), `next_action` (the single next step with the `tool` and `arguments` to call) and `health` (bounce rate, spam complaint rate, addresses Tringify no longer emails, and `issues` with cause and fix).
- `get_email_domain` / `list_email_domains`: each sending domain with `badge`, `actions`, `setup` (`path` `tringify_dns` or `your_dns`, the five steps, the six `records` with what public DNS shows, `last_checked`, `next_check`, `next_check_at`, `poll_after_ms`), `next_action` and `issue`. The records are on the domain; `get_email_domain_records` was removed.
- `check_email_domain_removal` / `check_email_sender_removal`: the removal's `confirm` sentence, `impacts`, `verification` and `next_action`.

Walk the merchant through email like this; the [Set up email walkthrough](https://developers.tringify.com/apps/connectors/set-up-email) has a full example.

1. **Read.** Call `get_email_overview` and show its badge, steps and `next_action.message`. Then call `next_action.tool` with `next_action.arguments` once the merchant agrees.
2. **Sending domain.** `list_email_domain_candidates`, then `create_email_domain`. When `setup.path` is `tringify_dns`, Tringify writes all six records itself (3 DKIM CNAME, MX and TXT on `bounce.<domain>`, DMARC TXT): there is nothing for the merchant to add. Otherwise show each record's `label`, `type`, `host`, `value` and `status_text`.
3. **Don't loop.** Call `verify_email_domain` once when the merchant says they added the records; it runs the next step at once, returns the domain and never fails while DNS is still updating. Tringify keeps checking in the background, so otherwise look again with `get_email_domain` after `next_action.after` (or `setup.poll_after_ms` while verifying). Never call `verify_email_domain` repeatedly.
4. **Sender, default, reply-to.** Follow `next_action`: `create_email_sender` once the domain is ready, `set_default_email_sender`, then `update_email_reply_to` (the merchant confirms it from that inbox).
5. **Health.** Relay `health.issues[]` and each domain's `issue` (`title`, `message`, `fix`). Missing DMARC or bounce records never stop sending; they are shown as something to fix.
6. **Remove.** Call `check_email_domain_removal` or `check_email_sender_removal`, show `confirm` and every `impacts[].message` (senders removed, the Tringify address taking over as default sender, marketing paused, DNS records Tringify deletes). After the merchant approves, call its `next_action` (`request_verification_code`), ask for the emailed code and call `delete_email_domain` or `delete_email_sender` with `otp_code`. Removing the default sender is allowed.

Adding or removing a sending domain, restarting verification, changing MAIL FROM, adding or removing a sender, choosing the default sender and changing reply-to need `otp_code` (see Verification codes); a missing or wrong code is refused with `details.next_action`, the `request_verification_code` call to make.

## Verification codes

Removing a domain, setting up hosted DNS, DNS record changes, unassigning a domain, setting or clearing the primary domain, and sending-domain, sender, reply-to and MAIL FROM changes need the same verification code Store Admin asks for. Each of those tools names the exact `action`, `target_type` and `target_id` in its description.

1. Get the merchant's approval for the change.
2. Call `request_verification_code` with that `action`, `target_type` and `target_id`. Tringify emails the code to the connected merchant. The result has `sent_to` (masked), `expires_at` and `resend_available_at`; it never contains the code.
3. Tell the merchant where the code went and ask them for it. Never guess, reuse or invent a code.
4. Call the tool with `otp_code` before `expires_at`.

A code works once, only for the action and target it was requested for. A missing code is refused with `DANGEROUS_CODE_REQUIRED` (`DOMAIN_REMOVAL_OTP_REQUIRED` for `delete_domain`) and a wrong, expired or mismatched one with `DANGEROUS_CODE_INVALID` (`DOMAIN_REMOVAL_OTP_INVALID`); both carry `details.next_action`, the exact `request_verification_code` call to make. Request a new one, after `resend_available_at` for the same action and target. Requests are limited per merchant and per store. The tool is listed while the connection holds `store:settings.domains:write` or `store:settings.email:write`; each call needs the one of its action. Connected tools get the code by email only; passkey confirmation is for Store Admin. Every request is recorded in the store's activity log.

## Online Store: storefronts

Storefront tools read each storefront with its `go_live` verdict and `cache` state, and change page titles, the share image, status, password protection and languages. Page SEO for the home, shop and search pages (source, translations, country rows) and title pattern and share image overrides per language or language and country use the same storefront permissions; translations also need the Languages permission and assigning an image needs Site Assets read. A title saved on a page, translation or country row is final; a title pattern shapes generated titles only and replaces the automatic store-name suffix. Page SEO updates are patches: `null` or `*_is_default: true` returns a field, robots included, to its default, and reads report `*_default` and `*_is_default` for each field. In an override, `null` uses the next broader setting (language, then the storefront's pattern and the store's share image). `update_storefront_mode` sets `live`, `maintenance` or `coming_soon`. Taking a live storefront offline returns `CONFIRMATION_REQUIRED` with warnings and a single-use `confirmation_token` bound to that storefront and mode; show the change, obtain approval, then repeat the same mode with `confirmed: true` and the token. Going live is refused with `STOREFRONT_NOT_READY_TO_GO_LIVE` and its `blockers` until the store is ready, and a status changed in the meantime returns `STOREFRONT_MODE_CONFLICT`. `update_storefront_password` takes effect at once with no confirmation: a password hides a live storefront from shoppers immediately. A new password needs at least 8 characters (`password_min_length` from `get_storefront_limits`) and at most 72 UTF-8 bytes; a shorter one returns `STOREFRONT_PASSWORD_TOO_SHORT`, and a password set before the minimum keeps working until changed. Order, payment, unsubscribe, text opt-out and privacy-request links keep working while a password is on, and connected product feeds stay public. `clear_storefront_cache` clears every storefront of the store and is allowed once every 12 hours per store; an earlier attempt returns `STOREFRONT_CACHE_CLEAR_TOO_SOON` with `next_available_at`.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_storefront_limits` | `GET /api/2025-01/storefronts/limits` | store:online_store.storefronts:read |
| `list_storefronts` | `GET /api/2025-01/storefronts` | store:online_store.storefronts:read |
| `get_storefront` | `GET /api/2025-01/storefronts/{storefrontId}` | store:online_store.storefronts:read |
| `update_storefront_mode` | `PUT /api/2025-01/storefronts/{storefrontId}/mode` | store:online_store.storefronts:write |
| `update_storefront_seo` | `PUT /api/2025-01/storefronts/{storefrontId}/seo` | store:online_store.storefronts:write |
| `list_storefront_seo_overrides` | `GET /api/2025-01/storefronts/{storefrontId}/seo/overrides` | store:online_store.storefronts:read |
| `set_storefront_seo_override` | `PUT /api/2025-01/storefronts/{storefrontId}/seo/overrides/{locale}` | store:online_store.storefronts:write |
| `delete_storefront_seo_override` | `DELETE /api/2025-01/storefronts/{storefrontId}/seo/overrides/{locale}` | store:online_store.storefronts:write |
| `get_storefront_page_seo` | `GET /api/2025-01/storefronts/{storefrontId}/page-seo/{pageType}` | store:online_store.storefronts:read |
| `update_storefront_page_seo` | `PUT /api/2025-01/storefronts/{storefrontId}/page-seo/{pageType}` | store:online_store.storefronts:write |
| `get_storefront_page_seo_translation` | `GET /api/2025-01/storefronts/{storefrontId}/page-seo/{pageType}/translations/{locale}` | store:online_store.storefronts:read, store:settings.languages:read |
| `set_storefront_page_seo_translation` | `PUT /api/2025-01/storefronts/{storefrontId}/page-seo/{pageType}/translations/{locale}` | store:online_store.storefronts:write, store:settings.languages:write |
| `get_storefront_page_seo_translations` | `GET /api/2025-01/storefronts/{storefrontId}/page-seo/translations/{locale}` | store:online_store.storefronts:read, store:settings.languages:read |
| `set_storefront_page_seo_translations` | `PUT /api/2025-01/storefronts/{storefrontId}/page-seo/translations` | store:online_store.storefronts:write, store:settings.languages:write |
| `get_storefront_page_seo_country` | `GET /api/2025-01/storefronts/{storefrontId}/page-seo/{pageType}/countries/{countryCode}/{locale}` | store:online_store.storefronts:read |
| `update_storefront_page_seo_country` | `PUT /api/2025-01/storefronts/{storefrontId}/page-seo/{pageType}/countries/{countryCode}/{locale}` | store:online_store.storefronts:write |
| `delete_storefront_page_seo_country` | `DELETE /api/2025-01/storefronts/{storefrontId}/page-seo/{pageType}/countries/{countryCode}/{locale}` | store:online_store.storefronts:write |
| `update_storefront_password` | `PUT /api/2025-01/storefronts/{storefrontId}/password` | store:online_store.storefronts:write |
| `get_storefront_languages` | `GET /api/2025-01/storefronts/{storefrontId}/languages` | store:online_store.storefronts:read |
| `set_storefront_languages` | `PUT /api/2025-01/storefronts/{storefrontId}/languages` | store:online_store.storefronts:write |
| `set_storefront_primary_language` | `PUT /api/2025-01/storefronts/{storefrontId}/languages/primary` | store:online_store.storefronts:write |
| `list_country_urls` | `GET /api/2025-01/storefronts/{storefrontId}/country-urls` | store:online_store.storefronts:read |
| `clear_storefront_cache` | `POST /api/2025-01/storefront-cache/clear` | store:online_store.storefronts:write |

Publishing a language requires enabling it for the store, adding it to the storefront, and assigning it to countries with one default per country. Unassigned countries serve only storefront primary. Markets provide countries, not language choices. These tools need no domain or email-settings scope.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_storefront_country_languages` | `GET /api/2025-01/storefronts/{storefrontId}/languages/countries` | store:online_store.storefronts:read |
| `set_storefront_country_languages` | `PUT /api/2025-01/storefronts/{storefrontId}/languages/countries` | store:online_store.storefronts:write |
| `assign_country_default_language` | `POST /api/2025-01/storefronts/{storefrontId}/languages/countries/bulk` | store:online_store.storefronts:write |
| `assign_all_country_default_languages` | `POST /api/2025-01/storefronts/{storefrontId}/languages/countries/all` | store:online_store.storefronts:write |
| `get_localization_prompt` | `GET /api/2025-01/storefronts/{storefrontId}/languages/localization-prompt` | store:online_store.storefronts:read |
| `set_localization_prompt` | `PUT /api/2025-01/storefronts/{storefrontId}/languages/localization-prompt` | store:online_store.storefronts:write |

Country mappings use `{ "FR": { "locales": ["en", "fr"], "default_locale": "fr" } }`; `null` removes an override. Bulk and all-country assignment add the chosen default while keeping other explicitly assigned languages. Changes return `CONFIRMATION_REQUIRED`: show `error.details.warnings` and the complete `impact`, then repeat the same request with `confirmed` and `confirmation_token` after approval. Country before/after lists use codes; `language_labels` supplies backend-localized display labels once per storefront. Include old/new defaults, implicit primary inheritance, retired country/language address-unit counts and affected translated slugs. Changed state or an expired token requires a fresh preview. Render backend success wording in the merchant's interface language. Unpublishing keeps translations.

`replace_only_language` is the atomic operation for a store with exactly one enabled language, including a one-language plan. It replaces references across all storefronts without ever enabling two languages, resets old-language translation/search data and cancels translation work. Source text is not translated. Store-default changes publish the resulting primary storefront's `storefront/locales/update`; replace-only publishes it for every storefront, together with store lifecycle events.

`get_language_readiness` scans up to 500 source identities per call and returns cumulative field counts and backend labels. Follow `next_cursor` until `complete=true`; only then consider `ready`. Content changes invalidate the cursor. It covers catalog/content, platform messages and the selected storefront's live theme and gate text; missing translations never block publication. Theme freshness can require review because author dictionaries do not carry source hashes. A missing active theme requires review. Counts do not certify linguistic quality.

Reset/removal preserves translated slug identities before cleanup. Old links redirect with 301 to the same resource's current canonical address, preserving query strings and a still-served country. Unknown routes, deleted resources and ambiguous owners return 404. History cannot restore translations deleted before installation. On a shared host Brazilian Portuguese in the US uses `/pt-BR-us`; `/pt-br` remains Portuguese in Brazil. Catalog/gate fields use exact → parent → source; slugs remain exact-locale only.

## Online Store: pixels

Pixel tools manage a storefront's custom pixels and the merchant's switch for each installed app's pixel, with the storefront permissions. Apps can never use them (their tokens get `STORE_API_PIXELS_ADMIN_TOKEN_REQUIRED`); an app turns only its own pixel on or off, store-wide, through its own API call. Lists are minimal: `list_custom_pixels` leaves the code out (`code_length`; read it with `get_custom_pixel`) and `list_app_pixels` leaves script and frame URLs and settings out. Custom pixel names are 1 to 100 characters and code at most 65536 (Unicode code points); code is JavaScript only, run in a sandboxed frame, and code with a `<script>` tag is refused with `CUSTOM_PIXEL_CODE_INVALID`. `set_app_pixel` records the merchant's choice for one storefront; it wins over the app's store-wide activation, except that an app that switched its pixel off keeps it off. Turning on a pixel with full page access (`privileged: true`) that is not enabled yet needs `acknowledge_privileged: true`, sent only after the merchant confirmed, otherwise `APP_PIXEL_PRIVILEGED_ACK_REQUIRED`; turning one off, or on when it is already enabled, needs none. The switch controls only the pixel in the browser, not the app's server-side events.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_custom_pixels` | `GET /api/2025-01/storefronts/{storefrontId}/custom-pixels` | store:online_store.storefronts:read |
| `get_custom_pixel` | `GET /api/2025-01/storefronts/{storefrontId}/custom-pixels/{pixelId}` | store:online_store.storefronts:read |
| `create_custom_pixel` | `POST /api/2025-01/storefronts/{storefrontId}/custom-pixels` | store:online_store.storefronts:write |
| `update_custom_pixel` | `PUT /api/2025-01/storefronts/{storefrontId}/custom-pixels/{pixelId}` | store:online_store.storefronts:write |
| `delete_custom_pixel` | `DELETE /api/2025-01/storefronts/{storefrontId}/custom-pixels/{pixelId}` | store:online_store.storefronts:write |
| `list_app_pixels` | `GET /api/2025-01/storefronts/{storefrontId}/app-pixels` | store:online_store.storefronts:read |
| `set_app_pixel` | `PUT /api/2025-01/storefronts/{storefrontId}/app-pixels/{appId}/{embedKey}` | store:online_store.storefronts:write |
| `list_store_fonts` | `GET /api/2025-01/fonts` | store:online_store.storefronts:read |
| `create_store_font_upload` | `POST /api/2025-01/fonts/uploads` | store:online_store.storefronts:write |
| `upload_store_font` | `POST /api/2025-01/fonts` | store:online_store.storefronts:write |
| `update_store_font` | `PATCH /api/2025-01/fonts/{fontId}` | store:online_store.storefronts:write |
| `delete_store_font` | `DELETE /api/2025-01/fonts/{fontId}` | store:online_store.storefronts:write |

## Online Store: preferences, redirects, search, recommendations and messages

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_permalink_limits` | `GET /api/2025-01/preferences/limits` | store:online_store.preferences:read |
| `get_preferences` | `GET /api/2025-01/preferences` | store:online_store.preferences:read |
| `set_favicon` | `PUT /api/2025-01/preferences/favicon` | store:online_store.preferences:write |
| `get_permalinks` | `GET /api/2025-01/preferences/permalinks` | store:online_store.preferences:read |
| `update_permalinks` | `PUT /api/2025-01/preferences/permalinks` | store:online_store.preferences:write |
| `get_age_gate_limits` | `GET /api/2025-01/preferences/age-gate/limits` | store:settings.compliance:read |
| `get_age_gate` | `GET /api/2025-01/preferences/age-gate` | store:settings.compliance:read |
| `update_age_gate` | `PUT /api/2025-01/preferences/age-gate` | store:settings.compliance:write |
| `get_express_checkout` | `GET /api/2025-01/preferences/express-checkout` | store:online_store.preferences:read |
| `update_express_checkout` | `PUT /api/2025-01/preferences/express-checkout` | store:online_store.preferences:write |
| `get_redirect_limits` | `GET /api/2025-01/redirects/limits` | store:online_store.redirects:read |
| `list_redirects` | `GET /api/2025-01/redirects` | store:online_store.redirects:read |
| `get_redirect` | `GET /api/2025-01/redirects/{redirectId}` | store:online_store.redirects:read |
| `create_redirect` | `POST /api/2025-01/redirects` | store:online_store.redirects:write |
| `update_redirect` | `PUT /api/2025-01/redirects/{redirectId}` | store:online_store.redirects:write |
| `delete_redirect` | `DELETE /api/2025-01/redirects/{redirectId}` | store:online_store.redirects:write |
| `bulk_delete_redirects` | `POST /api/2025-01/redirects/bulk-delete` | store:online_store.redirects:write |
| `get_search_settings` | `GET /api/2025-01/search/settings` | store:online_store.search:read |
| `update_search_settings` | `PUT /api/2025-01/search/settings` | store:online_store.search:write |
| `rebuild_search_index` | `POST /api/2025-01/search/reindex` | store:online_store.search:write |
| `get_search_index_job_limits` | `GET /api/2025-01/search/jobs/limits` | store:online_store.search:read |
| `list_search_index_jobs` | `GET /api/2025-01/search/jobs` | store:online_store.search:read |
| `get_active_search_index_job` | `GET /api/2025-01/search/jobs/active` | store:online_store.search:read |
| `get_search_index_job` | `GET /api/2025-01/search/jobs/{job_id}` | store:online_store.search:read |
| `list_search_synonym_languages` | `GET /api/2025-01/search-synonyms/locales` | store:online_store.search:read |
| `get_search_synonym_limits` | `GET /api/2025-01/search-synonyms/limits` | store:online_store.search:read |
| `list_search_synonyms` | `GET /api/2025-01/search-synonyms` | store:online_store.search:read |
| `create_search_synonym` | `POST /api/2025-01/search-synonyms` | store:online_store.search:write |
| `update_search_synonym` | `PUT /api/2025-01/search-synonyms/{synonymId}` | store:online_store.search:write |
| `delete_search_synonym` | `DELETE /api/2025-01/search-synonyms/{synonymId}` | store:online_store.search:write |
| `get_recommendation_limits` | `GET /api/2025-01/recommendations/limits` | store:online_store.recommendations:read |
| `get_recommendation_settings` | `GET /api/2025-01/recommendations/settings` | store:online_store.recommendations:read |
| `update_recommendation_settings` | `PUT /api/2025-01/recommendations/settings` | store:online_store.recommendations:write |
| `get_recommendation_rules` | `GET /api/2025-01/recommendations/rules` | store:online_store.recommendations:read |
| `set_recommendation_rules` | `PUT /api/2025-01/recommendations/rules` | store:online_store.recommendations:write |
| `list_recommendation_pins` | `GET /api/2025-01/recommendations/pins` | store:online_store.recommendations:read |
| `get_recommendation_pins` | `GET /api/2025-01/recommendations/pins/{productId}` | store:online_store.recommendations:read |
| `set_recommendation_pins` | `PUT /api/2025-01/recommendations/pins/{productId}` | store:online_store.recommendations:write |
| `list_recommendation_exclusions` | `GET /api/2025-01/recommendations/exclusions` | store:online_store.recommendations:read |
| `add_recommendation_exclusion` | `POST /api/2025-01/recommendations/exclusions` | store:online_store.recommendations:write |
| `remove_recommendation_exclusion` | `DELETE /api/2025-01/recommendations/exclusions/{productId}` | store:online_store.recommendations:write |
| `list_storefront_messages` | `GET /api/2025-01/storefront-messages` | store:online_store.storefront_messages:read |
| `save_storefront_message` | `PUT /api/2025-01/storefront-messages/overrides` | store:online_store.storefront_messages:write |
| `reset_storefront_message` | `DELETE /api/2025-01/storefront-messages/overrides/{code}` | store:online_store.storefront_messages:write |

## Gift Cards

Gift Cards are bearer cards: anyone with the code can redeem an active card at checkout when Gift Cards are enabled. Checkout does not check whether the shopper matches the recipient email or linked customer. Recipient details control delivery; they do not restrict who can redeem the card. Anyone with the code can use it. Keep the code and the View your gift card link safe. If a code is leaked, disable the card to pause redemption or cancel it to permanently revoke its remaining balance.

`issue_gift_card` sets delivery recipient details, including `recipient_customer_id`; it does not lock redemption to that customer. `get_gift_card` and `list_gift_cards` return recipient details for delivery and masked codes, not exclusive redemption rights. Balance lookups on the storefront require the code.

Read tools need `store:gift_cards:read`; write tools need `store:gift_cards:write` (write access does not include read). Cards are always shown with a masked code (`code_last4`); the full code is returned only by `issue_gift_card` when it creates a card (or repeats the same issue with the same `idempotency_key` within an hour) and by `reveal_gift_card_code`. Call `reveal_gift_card_code` only when the merchant explicitly asks to see a card's code: every call is recorded in the card's history as `code_revealed` with the connected user as `actor_name`, and in the store's audit log. The code is never in webhooks, history or logs. Naming a customer (`recipient_customer_id` on `issue_gift_card`, `customer_id` on `list_gift_card_languages`) also needs `store:customers:read`.

`adjust_gift_card_balance` adds (`direction: "credit"`) or removes (`direction: "debit"`) balance with a required `reason` and `idempotency_key`. Only `active` or `depleted` cards that have not expired can be adjusted (`can_adjust_balance` on every card; otherwise `GIFT_CARD_ADJUSTMENT_UNAVAILABLE`). A debit can't exceed the balance (`GIFT_CARD_ADJUSTMENT_EXCEEDS_BALANCE`), a credit can't take the balance above `balance_max` (`GIFT_CARD_BALANCE_LIMIT_EXCEEDED`), and one adjustment is at most `adjustment_max` from `get_gift_card_limits` (`GIFT_CARD_ADJUSTMENT_LIMIT_EXCEEDED`). Each adjustment is an `adjustment` movement with its `reason` in the card's balance history, a `balance_adjusted` event with `actor_name`, an audit log entry and a `gift_cards/adjust` webhook (an `adjustment` movement with a signed `amount`, `balance_after` and `reason`). Reusing the key with the same details returns the card without a second adjustment.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_gift_card_limits` | `GET /api/2025-01/gift-cards/limits` | store:gift_cards:read |
| `list_gift_card_languages` | `GET /api/2025-01/gift-cards/languages` | store:gift_cards:read (with `customer_id` also store:customers:read) |
| `get_gift_card_settings` | `GET /api/2025-01/gift-cards/settings` | store:gift_cards:read |
| `update_gift_card_settings` | `PUT /api/2025-01/gift-cards/settings` | store:gift_cards:write |
| `list_gift_cards` | `GET /api/2025-01/gift-cards` | store:gift_cards:read |
| `get_gift_card` | `GET /api/2025-01/gift-cards/{id}` | store:gift_cards:read |
| `list_gift_card_history` | `GET /api/2025-01/gift-cards/{id}/history` | store:gift_cards:read |
| `issue_gift_card` | `POST /api/2025-01/gift-cards` | store:gift_cards:write (with `recipient_customer_id` also store:customers:read) |
| `update_gift_card` | `PUT /api/2025-01/gift-cards/{id}` | store:gift_cards:write |
| `set_gift_card_status` | `POST /api/2025-01/gift-cards/{id}/status` | store:gift_cards:write |
| `bulk_set_gift_card_status` | `POST /api/2025-01/gift-cards/bulk-status` | store:gift_cards:write |
| `resend_gift_card` | `POST /api/2025-01/gift-cards/{id}/resend` | store:gift_cards:write |
| `reveal_gift_card_code` | `POST /api/2025-01/gift-cards/{id}/reveal-code` | store:gift_cards:write |
| `adjust_gift_card_balance` | `POST /api/2025-01/gift-cards/{id}/adjustments` | store:gift_cards:write |
| `list_gift_card_products` | `GET /api/2025-01/gift-cards/products` | store:gift_cards:read, store:products:read |
| `create_gift_card_product` | `POST /api/2025-01/gift-cards/products` | store:gift_cards:write, store:products:write |
| `list_order_gift_cards` | `GET /api/2025-01/orders/{id}/gift-cards` | store:orders:read |
| `retry_order_gift_card_issuance` | `POST /api/2025-01/orders/{id}/gift-cards/{intent_id}/retry` | store:orders:write |

`create_product` with `is_gift_card: true` creates a Gift Card product exactly as `create_gift_card_product` does and also needs `store:gift_cards:write`. `get_product` returns `is_gift_card` and, for a Gift Card product, `gift_card_policy`; editing or deleting a Gift Card product with `update_product` or `delete_product` also needs `store:gift_cards:write`. `list_products` with `is_gift_card: true` returns the same rows as `list_gift_card_products`.

`list_order_gift_cards` lists the Gift Cards an order bought (one row per card, `intent_id`), with `state` and `state_display`, the issued card's `gift_card_id` and `code_last4`, and what refunding it would give back. A unit in `needs_attention` can be retried with `retry_order_gift_card_issuance`, optionally with a new `recipient_email` and/or `recipient_phone`; anything else returns `ORDER_GIFT_CARD_NOT_RETRYABLE`.

Gift Cards are also a CSV type for the [CSV import and export tools](#csv-imports-and-exports): import type `gift_cards` issues one new card per row (codes are generated by Tringify, a preview with no errors is required, there is no undo), export type `gift_cards` lists the store's cards without their codes.

## CSV imports and exports

Translation CSV uses `type: "translations"` and `options: {resource: "message_template" | "email_template" | "order_status" | "file" | "product_media", locale: "fr"}` for these resources, alongside the other types returned by the backend. List the current import/export types and use their permissions and limits. Upload-intent creation keeps `resource` at its existing top level.

- Message Templates: one SMS/WhatsApp message type and channel per row, field `content`.
- Emails: one editor text per row, field `content`; `text_id` is `<template UUID>:<exact text_key>`. Subject, preview line, preheader, reachable visual block texts and code-mode text runs have the same granularity as the editor. Keep the exported keys, source columns and template syntax; edit translated text. Layout stays with the source template.
- Order statuses: one custom status per row, field `name`. System statuses are supplied by Tringify and cannot be translated.
- Files and Product media: field `alt_text`, addressed by library file UUID / product gallery item ID. File alt text also has the existing individual translation tools.

Blank translated cells preserve stored values; `__CLEAR__` clears a translation. Preview counts, row errors, confirmation, job progress and downloads use the ordinary CSV workflow. The standard AI Translator estimate/review/apply flow is available in Store Admin and mobile; there is no public MCP AI job tool or dedicated per-email translation tool. Theme text uses its existing storefront/theme-scoped workflow and CSV format.

Each tool needs the access of the import or export `type` it works on: read for the listing, status and export tools, write for uploading, starting, confirming, discarding, cancelling and undoing an import. `list_import_types` and `list_export_types` list every type with the scopes it needs; a translation type also needs its resource's owner scope. `finalize_import_upload` and `get_import_upload_status` take `type` and `intent_ids` only; the upload keeps the `resource` given to `create_import_upload`.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_import_types` | `GET /api/2025-01/imports/types` | The import or export type's read access |
| `create_import_upload` | `POST /api/2025-01/imports/upload-intents` | The import or export type's write access |
| `finalize_import_upload` | `POST /api/2025-01/imports/upload-intents/finalize` | The import or export type's write access |
| `get_import_upload_status` | `POST /api/2025-01/imports/upload-intents/status` | The import or export type's write access |
| `create_import` | `POST /api/2025-01/imports` | The import or export type's write access |
| `list_imports` | `GET /api/2025-01/imports` | The import or export type's read access |
| `get_import` | `GET /api/2025-01/imports/{importId}` | The import or export type's read access |
| `list_import_errors` | `GET /api/2025-01/imports/{importId}/errors` | The import or export type's read access |
| `confirm_import` | `POST /api/2025-01/imports/{importId}/confirm` | The import or export type's write access |
| `discard_import` | `POST /api/2025-01/imports/{importId}/discard` | The import or export type's write access |
| `cancel_import` | `POST /api/2025-01/imports/{importId}/cancel` | The import or export type's write access |
| `undo_import` | `POST /api/2025-01/imports/{importId}/undo` | The import or export type's write access |
| `list_export_types` | `GET /api/2025-01/exports/types` | The import or export type's read access |
| `create_export` | `POST /api/2025-01/exports` | The import or export type's read access |
| `list_exports` | `GET /api/2025-01/exports` | The import or export type's read access |
| `get_export` | `GET /api/2025-01/exports/{exportId}` | The import or export type's read access |
| `cancel_export` | `POST /api/2025-01/exports/{exportId}/cancel` | The import or export type's read access |

## Other catalog, file and market tools

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `get_product_metafields` | `GET /api/2025-01/products/metafields` | store:products:read |
| `get_product_variant_metafields` | `GET /api/2025-01/products/variants/metafields` | store:products:read |
| `bulk_create_brands` | `POST /api/2025-01/brands/bulk-create` | store:products:write |
| `bulk_delete_brands` | `POST /api/2025-01/brands/bulk-delete` | store:products:write |
| `bulk_create_vendors` | `POST /api/2025-01/vendors/bulk-create` | store:products:write |
| `bulk_delete_vendors` | `POST /api/2025-01/vendors/bulk-delete` | store:products:write |
| `bulk_info_file` | `POST /api/2025-01/files/bulk-info` | store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `get_file_translation` | `GET /api/2025-01/files/{id}/translations/{locale}` | store:files:read (Media) or store:online_store.site_assets:read (Site Assets) |
| `set_file_translation` | `PUT /api/2025-01/files/{id}/translations/{locale}` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `bulk_delete_files` | `POST /api/2025-01/files/bulk-delete` | store:files:write (Media) or store:online_store.site_assets:write (Site Assets) |
| `health_market_duty_country_rule` | `GET /api/2025-01/markets/duty-health` | store:markets:read, store:products:read |

## Message templates

SMS and WhatsApp templates are one row per message type and channel: list them with `list_message_templates` and pass `type` and `channel` (`sms` or `whatsapp`) to the others. Each row carries its `id`, `default_locale` and `translations`, its state in every other store language (`translated`, `outdated` or `not_translated`). The translation tools take that `id`. A translation keeps the original's values and tags exactly (`{{ ... }}`, `{% ... %}`); otherwise it is refused with `MARKETING_TRANSLATION_VARIABLES_MISMATCH` and `details.variables` lists what to keep. Blank text is refused with `MESSAGE_TEMPLATE_CONTENT_REQUIRED`, text over the template limit with `MESSAGE_TEMPLATE_CONTENT_TOO_LONG`; an empty string clears a translation. Translation changes send `message_templates/translations/update`, or `message_templates/translations/delete` when cleared. Source edits use `message_templates/update`.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_message_templates` | `GET /api/2025-01/message-templates` | store:marketing:read |
| `get_message_template` | `GET /api/2025-01/message-templates/{type}` | store:marketing:read |
| `update_message_template` | `PUT /api/2025-01/message-templates/{type}` | store:marketing:write |
| `reset_message_template` | `POST /api/2025-01/message-templates/{type}/reset` | store:marketing:write |
| `get_message_template_translation` | `GET /api/2025-01/message-templates/{id}/translations/{locale}` | store:marketing:read, store:settings.languages:read |
| `set_message_template_translation` | `PUT /api/2025-01/message-templates/{id}/translations/{locale}` | store:marketing:write, store:settings.languages:write |
| `get_message_template_translations` | `GET /api/2025-01/message-templates/translations/{locale}` | store:marketing:read, store:settings.languages:read |
| `set_message_template_translations` | `PUT /api/2025-01/message-templates/translations` | store:marketing:write, store:settings.languages:write |

## Order and store metafield values

Value translations require both owner and Languages access: read for get, write for set or clear, including product and variant values. Store values use `store:settings.metafield_definitions:read/write`; order and order-item values use `store:orders:read/write`. Orders and order items have no value translations. These tools use the existing Store API endpoints and validation, preserve omitted values, and require no confirmation token. Sharing and merchant-access restrictions still apply.

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_order_metafields` | `GET /api/2025-01/orders/{orderId}/metafields` | store:orders:read |
| `set_order_metafield` | `PUT /api/2025-01/orders/{orderId}/metafields` | store:orders:write |
| `delete_order_metafield` | `DELETE /api/2025-01/orders/{orderId}/metafields/{namespace}/{key}` | store:orders:write |
| `set_order_item_metafield` | `PUT /api/2025-01/orders/{orderId}/items/{itemId}/metafields` | store:orders:write |
| `delete_order_item_metafield` | `DELETE /api/2025-01/orders/{orderId}/items/{itemId}/metafields/{namespace}/{key}` | store:orders:write |
| `list_order_item_metafields` | `GET /api/2025-01/orders/{orderId}/items/{itemId}/metafields` | store:orders:read |
| `list_store_metafields` | `GET /api/2025-01/store/metafields` | store:settings.metafield_definitions:read |
| `set_store_metafield` | `PUT /api/2025-01/store/metafields` | store:settings.metafield_definitions:write |
| `delete_store_metafield` | `DELETE /api/2025-01/store/metafields/{namespace}/{key}` | store:settings.metafield_definitions:write |
| `get_store_metafield_translation` | `GET /api/2025-01/store/metafields/{namespace}/{key}/translations/{locale}` | store:settings.metafield_definitions:read, store:settings.languages:read |
| `set_store_metafield_translation` | `PUT /api/2025-01/store/metafields/{namespace}/{key}/translations/{locale}` | store:settings.metafield_definitions:write, store:settings.languages:write |

## Gift Card operations

| Tool | Store API operation | Required access |
| --- | --- | --- |
| `list_gift_card_products` | `GET /api/2025-01/gift-cards/products` | store:gift_cards:read, store:products:read |
| `create_gift_card_product` | `POST /api/2025-01/gift-cards/products` | store:gift_cards:write, store:products:write |
| `get_gift_card_limits` | `GET /api/2025-01/gift-cards/limits` | store:gift_cards:read |
| `list_gift_card_languages` | `GET /api/2025-01/gift-cards/languages` | store:gift_cards:read |
| `get_gift_card_settings` | `GET /api/2025-01/gift-cards/settings` | store:gift_cards:read |
| `update_gift_card_settings` | `PUT /api/2025-01/gift-cards/settings` | store:gift_cards:write |
| `list_gift_cards` | `GET /api/2025-01/gift-cards` | store:gift_cards:read |
| `issue_gift_card` | `POST /api/2025-01/gift-cards` | store:gift_cards:write |
| `get_gift_card` | `GET /api/2025-01/gift-cards/{id}` | store:gift_cards:read |
| `list_gift_card_history` | `GET /api/2025-01/gift-cards/{id}/history` | store:gift_cards:read |
| `update_gift_card` | `PUT /api/2025-01/gift-cards/{id}` | store:gift_cards:write |
| `resend_gift_card` | `POST /api/2025-01/gift-cards/{id}/resend` | store:gift_cards:write |
| `reveal_gift_card_code` | `POST /api/2025-01/gift-cards/{id}/reveal-code` | store:gift_cards:write |
| `set_gift_card_status` | `POST /api/2025-01/gift-cards/{id}/status` | store:gift_cards:write |
| `adjust_gift_card_balance` | `POST /api/2025-01/gift-cards/{id}/adjustments` | store:gift_cards:write |
| `bulk_set_gift_card_status` | `POST /api/2025-01/gift-cards/bulk-status` | store:gift_cards:write |

## Gift Card delivery edits

Read `get_gift_card` before editing or resending. Use `can_edit_delivery` and `edit_delivery_reason_display` for recipient details, message, language and delivery schedule; use `can_edit_expiry` for expiry. Sent, in-flight or used cards lock delivery details. Expired, depleted, cancelled and disabled cards cannot be edited or resent. Use `can_resend` and `resend_reason_display` for Resend, which always uses the saved recipient and language.

`update_gift_card` with a future `delivery_scheduled_at` before expiry creates or moves the waiting send, preferring recipient email, otherwise phone through the store’s configured route. `clear_delivery_schedule` cancels the waiting send and never sends now. `resend_gift_card` takes `id`, `delivery_method` and `idempotency_key`; recipient and language overrides are not accepted. See the [Gift Cards Store API contract](https://dev-docs.tringify.com/store-api/orders/gift-cards) for response flags and refusal codes.

Fake Pay is a simulator and moves no real money. Use `get_order` and the ordinary refund tools to show the platform’s recorded results. The platform reads the app’s live status endpoints; browser returns and provider notifications never establish payment. There are no separate merchant tools for the app’s signed provider operations.
