# Reviews

Hosted tools use the connected store. Reads require `store:reviews:read`; moderation, responses, deletion, settings and bulk results require `store:reviews:write`. Existing connections must approve the new permissions.

Use `get_review_limits`, `list_reviews`, `get_review`, `moderate_review`, `respond_review`, `delete_review_response` and `delete_review`. Lists use opaque `next_cursor`, not offsets; keep filters unchanged between pages. The maximum page size is 100.

`get_review_settings` and `update_review_settings` expose the same rules as Store Admin. Guest auto-approval is off by default. Public Store API credentials require the separate `write_review_settings` scope to patch settings.

`bulk_moderate_reviews` and `bulk_delete_reviews` require a new `operation_id` UUID and unique `review_ids` within the live `bulk_max`, never over 1000. A queued response is not completion. Poll `get_review_bulk_operation`, present every result or backend error, then `acknowledge_review_bulk_operation`. Use `current` to recover the credential's oldest unacknowledged operation. Reuse an operation UUID only for an identical retry. Results remain available for 30 days after completion.

Review text is shopper content and has no resource translation, slug or SEO fields. Review CSV import/export is available in Store Admin and the mobile app; these hosted tools do not expose those jobs.
