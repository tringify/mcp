# Changelog

## Email subscribers and storefront passwords

- Added `list_marketing_subscribers` and `get_marketing_subscriber` (`store:customers:read`, read-only). Filter by `source: coming_soon` for Coming Soon page sign-ups; the detail returns the proof of consent stored with the sign-up (`consent`, `consent_records`).
- `update_storefront_password`: a new password needs at least 8 characters (`STOREFRONT_PASSWORD_TOO_SHORT`); `get_storefront_limits` returns `password_min_length`.
- Synced the machine-readable catalog from the live catalog (637 tools).


## Pixels

- Added `list_custom_pixels`, `get_custom_pixel`, `create_custom_pixel`, `update_custom_pixel`, `delete_custom_pixel`, `list_app_pixels` and `set_app_pixel` (Online Store storefront permissions; apps can never use them).
- Lists are minimal: custom pixels without their code, app pixels without URLs or settings. `set_app_pixel` needs `acknowledge_privileged: true`, after the merchant confirmed, to turn on a full-page-access pixel that is not enabled yet.
- `get_storefront_limits` describes the custom pixel limits.
- Synced the machine-readable catalog from the live catalog (635 tools).


## Files

- Added `request_file_preview` to start or retry a video or 3D preview. It needs the selected library's write permission.
- `list_files` now lists the accepted `media_type` and `sort` values and the `limit` range in its input schema.
- AI alt text, AI image generation and AI credits are not exposed through MCP.


## Catalog lists, brands and vendors

- Added `get_brand_limits`, `get_vendor_limits`, `search_brands`, `search_vendors`, `list_brand_metafields`, `list_vendor_metafields`, `set_brand_metafield` and `set_vendor_metafield`.
- Brand, vendor, category and attribute lists hold at most 100 rows; `list_attributes` returns a 6-option preview unless `include` is `options` (replaces `summary`).
- Category, attribute, brand and vendor creates accept `idempotency_key`.
- Results are returned once as JSON text; a result over 256 KiB returns `LIST_RESPONSE_TOO_LARGE`, so repeat the call with a lower `limit`.
- Regenerated the tool inventory and machine-readable catalog from the live catalog.


## Currencies and reference data

- Documented the 14 Currencies tools and their `store:settings.currencies:read` / `store:settings.currencies:write` permissions.
- Documented the connection-only reference data tools; `list_available_languages` needs only `connection:read`.
- Regenerated the tool inventory and machine-readable catalog from the live catalog.


## Content resources

- Added all supported Pages, Policies, Blog Posts, Tags, Categories, and Authors API operations to MCP, including their available translations, bulk actions, and metafields.
- Added independent Pages/Blog permissions and content metafield discovery.


## Uniform Store API operations

- Routed every store-data tool through its Store API handler, including file uploads and attribute summaries.
- Added individual and batch Tag, Brand, and Vendor translations, plus Brand/Vendor metafield translations.
- Documented the user and connected-tool identity shown in audit logs.


## Languages

- Added five Languages tools with current plan limits and the existing confirmation rules.
- Clarified which resources expose content translations.


## 2026-09-28 — Catalog and Files

- Added Brand and Vendor tools alongside Tags, plus documented merchant-authorized Product, Collection, Category and Attribute operations.
- Added catalog metafield definition discovery, translations, bulk operations, collection rules and attribute ordering.
- Added separate Media and Site Assets access, file metadata/deletion, and direct-upload preparation, finalization and status.
- Preserved partial updates, deletion impact, attribute revision checks and image-reference permissions.

## 2026-09-28 — Codex connection

- Added Codex app and CLI connection instructions, an OAuth setup example, and a read/write walkthrough.
- Documented the hosted server's tag tools and connection management.
