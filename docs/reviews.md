# Reviews

Hosted tools use the connected store. Reads require `store:reviews:read`; moderation, responses, deletion, settings and bulk results require `store:reviews:write`. Grant review access if the connection does not already have it.

Use `get_review_limits`, `list_reviews`, `get_review`, `moderate_review`, `respond_review`, `delete_review_response` and `delete_review`. Lists use opaque `next_cursor`, not offsets; keep filters unchanged between pages. Read the current page-size options and maximum from `get_review_limits`; do not hard-code them.

`get_review_settings` and `update_review_settings` expose the same rules as Store Admin. Guest auto-approval is off by default. Public Store API credentials require the separate `write_review_settings` scope to patch settings.

`bulk_moderate_reviews` and `bulk_delete_reviews` require a new `operation_id` UUID and either unique `review_ids` within the live `bulk_max` or `filter`, never both. An empty filter selects every review; filter-based operations can retain completed changes if a later step fails. A queued response is not completion. Poll `get_review_bulk_operation`, present the per-review results, or `processed_count` and any partial-failure error, then `acknowledge_review_bulk_operation`. Use `current` to recover the credential's oldest unacknowledged operation. Reuse an operation UUID only for an identical retry. Results remain available for 30 days after completion.

Review text is shopper content and has no resource translation, slug or SEO fields. Review CSV import/export is available in Store Admin, the mobile app and the general import/export tools. Read `list_import_types` or `list_export_types` and use `type: reviews`. Upload and preview before `confirm_import`; inspect `list_import_errors` and the completed job. Imports need review write access; exports need review read access.

Review photos have a separate plan storage allowance shared by shopper uploads and imports. Limits and settings return `photo_storage` with byte usage, reservations and availability. `allow_images` remains the saved merchant preference; `photos_available` reports effective availability. Capacity exhaustion stops additional photos, not ratings or text reviews. A smaller plan cannot be selected while retained photos and uploads in progress exceed its allowance.

Use `delete_review_photo` with `id` (the review ID) and `imageId` from its `images` list to remove just that photo. There is no preview step: confirm the chosen photo with the merchant before calling it. This is permanent and keeps the review's rating, text and status. Storage is released when physical deletion finishes. CSV exports contain photo links, not photo files; download photos before deleting them.
