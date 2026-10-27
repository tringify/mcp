# Changelog

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
