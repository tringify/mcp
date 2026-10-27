# Changelog

## Translation outcomes, argument errors, CSV import tools — 28 October 2026

- Every `set_<resource>_translations` tool and `set_theme_text_translations` return a top-level `code` and `message` with the unchanged per-row `results`: `TRANSLATIONS_SAVED` (every row saved), `TRANSLATIONS_PARTIALLY_SAVED` (`success: true`; the message counts saved and failed rows and names the failure reasons, e.g. "2 saved, 1 failed. No source text found for the requested fields (description).") or `TRANSLATIONS_NOT_SAVED` (`success: false`, HTTP 422; `error.details` carries `totals` and `results`).
- A call with an unexpected property, a missing required one or a wrongly typed value returns `CONNECTOR_TOOL_ARGUMENTS_INVALID`; its message and `error.details.properties` list the tool's allowed and required properties, and those of each object or list of objects (`translations[]`).
- The CSV import and export tools are listed in the catalog (`list_import_types` … `cancel_export`). `finalize_import_upload` and `get_import_upload_status` take `type` and `intent_ids` only: the upload keeps the `resource` given to `create_import_upload`.
- A translation CSV import or export started while another one runs is refused with `TRANSLATION_CSV_JOB_IN_PROGRESS`, which now says the limit is one job per store and names the running job ("One translation CSV job runs per store at a time; a Brands export is running.").
- `get_import` of an attributes import counts attributes in `total_rows`/`processed_rows` and the file's option rows in `job.option_rows` (`total`, `processed`).

## Metafield definition names, the Metafield block, definition management — 28 October 2026

- Added `get_metafield_definition_translation`, `get_metafield_definition_translations` (up to 100 definitions in one language) and `set_metafield_definition_translations` (up to 100 rows `{id, locale, fields: {name}}` for any enabled non-default languages, per-row results, `totals` and the `TRANSLATIONS_SAVED` / `TRANSLATIONS_PARTIALLY_SAVED` / `TRANSLATIONS_NOT_SAVED` outcome). A definition's name is the label shoppers see next to its value. Names of app-owned definitions the merchant cannot edit return `TRANSLATION_FIELD_NOT_TRANSLATABLE`. Name translations send no webhooks, like choice labels.
- `add_block` places the platform Metafield block (`theme:metafield`) in any slot that accepts app blocks or theme blocks: settings `owner` (`product`, `collection`, `category`, `vendor`, `brand`, `page`, `blog_post` or `store`), `field_<owner>` (`namespace.key` of a storefront-visible definition), `label` (empty shows the definition name in the shopper's language) and `show_label`. `list_section_types` lists it under `theme_blocks` with `platform: true`.
- A store connection creates, updates and deletes the merchant's own metafield definitions with `create_metafield_definition`, `update_metafield_definition` and `delete_metafield_definition` (never an app's definitions or an `app:` namespace). The Store API itself has no definition create, update or delete endpoints; the docs now say so for every token. Behaviour is unchanged.

## Low-stock thresholds without a product update — 28 October 2026

- New `set_product_threshold` and `set_product_variant_threshold` set or clear one low-stock threshold of a simple product or a variant: at a location (`location_id`) or overall across all locations (omit `location_id`). `low_stock_threshold` is required; null clears it and 0 is valid. They need no `expected_revision` and change nothing else on the product. A changed location threshold sends `inventory_levels/update` (reason `threshold_updated`); a changed overall threshold sends `products/update` or `variants/update` with `changed_fields` `["overall_low_stock_threshold"]`. Inventory groups keep `set_inventory_group_threshold`.
- `update_product` states that each `variants` entry takes `overall_low_stock_threshold` (number sets, null disables, omitted keeps; tracked variants only); `create_product` says it can be changed later.
- `list_inventory_low_stocks` says which staff members get low-stock notifications is each staff member's own preference in Store Admin or the Tringify app and is not available to tools; apps use the `inventory/low_stock` webhook.
- `get_inventory_limits` returns the same paging and sorting keys in every section (`list_page_size`, `list_max_limit`, `page_size_options`, `search_max_length`, `sort_columns`, `default_sort`, `default_sort_direction`); `transfers.status_actions` gives each action's label and confirmation text in the request language.

## Timestamps in store time, metafield write rules, variant order — 27 October 2026

- Every tool now returns timestamps as RFC 3339 in the store's timezone with its offset (for example `2026-10-28T01:16:00+05:30`), never display text. This covers orders (and their items, payments, refunds, fulfillments), discounts, shipping, COD, checkout and duty settings, campaigns and templates, email history, statistics, suppressions, reply-to and domains, inventory low stock, movements and restock requests, DNS jobs, domains, webhook endpoints, deliveries and attempts, and sales channels. `request_verification_code` returns `expires_at` and `resend_available_at` in that form and no longer returns `*_iso` copies.
- The `set_*_metafield` tools state who may write which definitions: an app connection writes its own app's definitions; a merchant connection (connected AI tools, store admin tokens) writes merchant-owned definitions, and app-owned ones whose `merchant_access` is `read_write`. Behaviour is unchanged.
- `create_product` returns each variant's attribute values with `attribute_name`, `attribute_slug` and option label/value, as `list_product_variants` does, and its stored `sort_order`. A variant sent without `sort_order` is stored at its position in `variants` (`update_product`: after the variants the product keeps).

## Translation writes during a translation import — 27 October 2026

- Translation tools no longer wait for a running translation CSV import. Writes of other items, types and languages never wait; a write of an item or a name or slug the import's current batch is writing waits at most 2 seconds and then fails with `TRANSLATION_WRITE_BUSY` (HTTP 503, nothing saved) with `error.details.retry_after_seconds`; send it again after that. Every row or call either saved or reports an error; none times out with an unknown outcome.

## One uniqueness rule for translations; retryable busy rows — 27 October 2026

- Every `set_<resource>_translation` and `set_<resource>_translations` tool states its type's uniqueness rule, the same rule translation CSV preview and import use: per language, a translated category name must be unique among categories with the same parent (like source names; the same name under different parents is fine); slugs, and vendor, brand, blog category and blog tag names, must be unique among the values shown in that language; tag and attribute names among translated names. Of two rows of one call sharing a value, the earlier row keeps it and the later row fails with the duplicate code and `details.existing_id`.
- A row (or a single save) that fails with `TRANSLATION_WRITE_BUSY` (HTTP 503) saved nothing because another change to the same item was saving at the same time; send it again. Several languages of one item in one call no longer collide.

## Translations in one call, compact bulk results — 27 October 2026

- Every `set_<resource>_translations` batch tool (products, collections, categories, attributes, attribute options, tags, brands, vendors, pages, policies, blog posts, categories, tags and authors, menu items, locations, product filters, list-page and storefront page SEO) takes rows `{id, locale, fields}` (`page_type` instead of `id` for page SEO) for any enabled non-default languages in one call, up to 100 rows (one row = one item in one language). The `locale` argument is gone. Each row is saved on its own; the result has `totals` (`rows`, `saved`, `failed`) and one `{id, locale, status}` per row, with the full `error` on failed rows (new code `TRANSLATION_ROW_DUPLICATE` for a second row for the same item and language).
- `finalize_file_uploads` and `get_file_upload_status` return `totals` (`ready`, `in_progress`, `failed`) and per intent only `intent_id`, `status`, `file.id` when ready, `reused` and `error`. Get the file for its URLs.
- Bulk creates (`bulk_create_brands`, `bulk_create_categories`, `bulk_create_tags`, `bulk_create_vendors`, `bulk_create_customer_tags`) return `totals` and `created` as `{id, name}`; `skipped` and `row_errors` are unchanged. Gift Card and transfer bulk status, manual currency bulk create, market currency bulk add, currency data bulk removal, inventory adjustments and fulfillment event batches return `totals` plus id/status rows.

## Email setup steps — 27 October 2026

- Added `get_email_overview`: the store's email setup in order (sending domain, sender address, default sender, reply-to), the single `next_action` with the `tool` and `arguments` to call, and sending health (bounce rate, spam complaint rate, addresses Tringify no longer emails, each problem with its cause and fix).
- Added `get_email_domain`. Every sending domain now carries `badge`, `actions`, `setup` (path, five steps, the six records with what public DNS shows, last and next check, `poll_after_ms`), `next_action` and `issue`. When Tringify hosts the domain's DNS it writes every record itself.
- Removed `get_email_domain_records`: the records are `setup.records` on the domain.
- `verify_email_domain` returns the sending domain (code `EMAIL_LIFE_CHECKED`) and never fails while DNS is still updating. Don't call it in a loop; look again after `next_action.after`.
- Added `check_email_domain_removal` and `check_email_sender_removal`: `confirm`, `impacts`, `verification` and `next_action` (`request_verification_code`). Removing the default sender, or a sending domain that holds it, is allowed; the Tringify address takes over. `EMAIL_ADDRESS_DELETE_DEFAULT` and `EMAIL_DOMAIN_DELETE_WITH_DEFAULT` are gone.
- Removed the sending provider from every email result: `provider`, `sending_provider`, `ses`, `ses_is_verified`, `can_delete`, `permanent`, `dns_records`, `status` and the other raw fields, and the `provider` argument.

## Email times and send history — 27 October 2026

- `verify_email_domain` returns `next_check_at` as RFC 3339 in the store's timezone with its offset, and `next_check`, the same time as text to show. Sending domains no longer return the raw UTC `ses.last_check_at` and `ses.verified_at`; read the domain's `last_check_at` and `verified_at`.
- Each send in `list_email_history` carries `submission_label`, the text to show for its `submission_state`. Emails sent before submission states were recorded now carry a derived state; `no_provider_record` means no record of the email provider's answer remains.

## Domain lifecycle — 27 October 2026

- Every domain now carries `badge`, `role_label`, `actions`, `next_action` (the single next step with the `tool` and `arguments` to call) and `issue` (HTTPS blocked by a CAA record or another Cloudflare account, certificate timed out, DNS warning with its deadline, disconnected, primary address handed over), the same values Store Admin and the mobile app show.
- `connect_domain` (`action: discover`) explains each way to connect the address (`options`, `chosen`) and returns `domain` (ASCII) and `domain_display` (Unicode); a failed provider lookup is `DOMAIN_DISCOVERY_FAILED`.
- `check_domain_removal` returns `confirm`, `impacts`, `verification` and `next_action` (the `request_verification_code` call); its refusals carry `details.next_action`. Every missing or rejected verification code returns `details.next_action` with the exact `request_verification_code` arguments.
- `verify_domain` on a domain in a DNS warning runs the health re-check at once.
- DNS zones carry `view.state_label`, `tone`, `in_setup`, `working` and `operation`.
- `get_dns_operation` takes `operation_id`, `delete_email_sender` and `set_default_email_sender` take `address_id`, and `get_review_bulk_operation` / `acknowledge_review_bulk_operation` take `operation_id` (were camelCase).
- Catalog table lists the 13 email settings tools it was missing; fixed the note that only some domain tools need a code.

## Domain setup steps — 27 October 2026

- `get_domain`, `list_domains` and `create_domain` return `setup` on each domain: the same step list Store Admin shows (`path`, `state`, `summary`, `current_step`, `steps`, the `nameservers` to set or the `records` to add with what public DNS shows, `last_checked`, `next_check`, `expires`, `actions`). Labels and messages are in the request language.
- `verify_domain` now runs the domain's next setup step at once (code `DOMAIN_SETUP_CHECKED`, or `DOMAIN_VERIFIED` when it connects) and never marks a domain failed while DNS is still updating; `DOMAIN_DNS_TXT_LOOKUP_FAILED` and `DOMAIN_DNS_TXT_MISMATCH` are gone. Tringify keeps checking in the background, so there is no need to call it in a loop.

## Verification codes — 27 October 2026

- Added `request_verification_code`: it emails the merchant the verification code a tool with `otp_code` needs, for the exact `action`, `target_type` and `target_id` that tool names. Until now the code could only be requested in Store Admin.
- Every tool that takes `otp_code` now names those three values and points to `request_verification_code`.
- Synced the machine-readable catalog (715 tools).

## Domain and DNS management — 27 October 2026

- Added 19 domain and DNS tools: `create_domain`, `verify_domain`, `check_domain_removal`, `delete_domain`, `connect_domain`, `create_dns_zone`, `refresh_dns_zone`, `scan_dns_zone`, `cancel_scan_dns_zone`, `retry_dns_zone`, `bulk_delete_dns_records`, `preview_dns_import`, `import_dns_records`, `export_dns_records`, `list_dns_jobs`, `get_dns_job_limits`, `list_dns_job_errors`, `get_dns_export_download` and `cancel_dns_job`, plus `list_email_domain_candidates`. A connection can now do everything Store Admin › Settings › Domains does.
- Removing a domain, setting up hosted DNS and record changes need the merchant's `otp_code`, exactly as in Store Admin. Installed apps still cannot hold domain access.
- Synced the machine-readable catalog (714 tools).

## Metafield value clear tools

- Documented the 13 `delete_<owner>_metafield` tools in the catalog table and README. The variant tool is `delete_product_variant_metafield`, matching `set_product_variant_metafield` (it was briefly listed as `delete_variant_metafield`).

## Metafield follow-up — 26 October 2026

- Added order, order-item, and store metafield list/set tools, plus store translation get/set: eight tools, 660 total.
- Product and variant metafield translations now require owner access and Languages access at the matching read/write level; store translations preserve both permissions too.
- Synced the hosted tool catalog and documented scopes, immediate writes, and translation clearing.

## Deleting email subscribers

- Added `delete_marketing_subscriber` (`store:customers:write`). Every delete asks for confirmation first: it returns the warnings and impact (proof-of-consent records deleted, a linked customer that stops email marketing) and a single-use token for the retry with `confirmed: true`.
- Synced the machine-readable catalog entry (638 tools).


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
