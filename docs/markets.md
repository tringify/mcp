# Markets integration

Markets decide which countries a store serves and how it prices and accepts an order there. This guide applies to the hosted Store MCP and the [Markets Store API](https://dev-docs.tringify.com/store-api/markets/markets).

## Access and discovery

Request `store:markets:read` to read Markets and `store:markets:write` to change them. Request both when a workflow needs both. Products or store-currency access does not grant Markets access. Existing connections need an approved access update to add these permissions; refresh does not expand a grant.

The hosted MCP exposes every documented Markets JSON operation: markets, assigned countries, market currencies, country currencies, tax classes/zones/rates/price rules, all six discount types and discount settings, shipping settings/zones/methods, duties, COD settings/zones/product rules, connected payment-provider availability/discounts, checkout limits, and checkout fees/ordering.

Use the tool list and input schemas for exact tool names and fields. Path IDs use names such as `market_id`, `tax_class_id`, `zone_id` and `binding_id`. IDs must belong to the connected store and the indicated parent. Arguments cannot choose another store or actor. CSV tax import/export and its asynchronous jobs are available in Store Admin and mobile.

## Read before changing

1. Read market limits and the assigned/available country list.
2. Read the market, its assigned currencies and country-currency mappings.
3. Read the relevant specialist limits or returned authoring catalog and the complete current definition.
4. Decide the intended change, submit it once and inspect the returned saved state.

The market PATCH changes only supplied fields. Specialist PUT operations follow their documented replacement rules; preserve the complete editable definition where required. A returned error does not authorize another write. After a timeout or uncertain write, read current state before deciding whether a retry is needed.

## Countries and currencies

Every market needs at least one country; a country belongs to only one market. The primary market cannot be deleted or disabled. Removing a country is blocked while a tax, shipping or COD zone still uses it. Resolve the named dependency first.

Create a market in the store base currency. Adding another assigned currency requires the plan and store's multi-currency setting to allow it, and the currency must be enabled for the store. Adding a currency alone does not offer it to shoppers: Pricing assigns one currency to each country.

Before reassigning a country's currency, configure every enabled monetary rule for that currency: checkout limits/fees, COD limits/fees and online-payment discounts. Duty rules retain their explicit currency; the API blocks silently changing it. Currency removal retains the base/last currency and checks country/duty references. Removing a currency deletes its exact shipping overrides. Read live batch limits before adding or removing assignments.

## Exact amounts and percentages

Send currency amount maps, tax rates, duty thresholds and other fields declared as decimal strings with a decimal point and no grouping or currency symbols. Use the currency's accepted amount precision. KRW has no fractional amounts; KWD has three. Follow each field's schema: percentage-discount values, Buy X Get Y values and bundle percentages are numeric fields. A Buy X Get Y `fixed` value is an amount off each reward item in the base currency, capped at its remaining value. A bundle fixed price is the total price of a complete set.

Use the returned limits, rather than copying monetary ceilings or maximum selection counts into an integration. Minimum/maximum order limits need a positive amount for every assigned currency, and each maximum must exceed its minimum. Disabled limits use empty amount maps. Shipping may convert the required base amount when an exact currency override is absent; checkout/COD/payment rules require their documented currency coverage.

## Tax and duties

Tax classes and zones belong to the market. Read rates and coverage gaps before adding rates; subdivision matches precede country matches and the default zone. Rates come from the matched zone; a class does not inherit rates from another zone. Use the atomic rate-save operation when several creates/updates/deletes must succeed together. A batch containing creates is not safe to retry automatically.

Price-based tax rules have a single country/currency eligibility requirement. Check eligibility before authoring, and adjust the rule before expanding that market. Tax-included pricing, tax display mode, tax basis and the default-class setting are independent settings.

Duties use destination, origin and HS-code rules. Read a complete rule before editing, including all origin and HS rates. A de-minimis threshold is in the rule's saved destination currency, compares the goods' value only, and equality is not exempt. `duty_includes_shipping` adds shipping without its included tax to the customs value (on by default for CIF destinations, off for the US, Canada, Australia and New Zealand); a checkout fee with `counts_toward_customs_value` joins it too. COD fees never count.

A checkout fee can apply only to carts holding chosen products or products of chosen collections (`applies_to` with `target_product_ids` as strings or `target_collection_ids`), only from or below a discounted merchandise subtotal (`min_subtotal_*`, `max_subtotal_*`), and a percentage fee can be capped (`percent_cap_*`); each enabled condition needs an amount for every market currency. An optional fee can ask the customer for text (`collect_text`, `text_required`, `text_max_length`, `text_prompts`). Updates replace the whole fee, so resend the conditions you keep. Checkout settings also limit the items per order (`min_quantity`, `max_quantity`, inclusive).

A fixed checkout fee charged per item or a percentage fee shows how it was calculated under its name at checkout (`₹100.00 per item × 3`, `5% of ₹1,000.00`) unless `show_calculation` is false. Word the line per storefront language with `calculation_texts` (`{{amount}}`/`{{quantity}}` per item, `{{rate}}`/`{{base}}` percent); read `checkout_fee_catalog.calculation_defaults` for the default wording first, and leave a language out to keep it. A fixed per-order fee has no line, so send no texts for it.

Each market answers who pays import duties on international shipments with `duty_collection_mode`: `pay_on_delivery` (the customer; any estimate shows below the total), `collect_at_checkout` (the customer at checkout; duty and its import tax are added to the total; needs `duties_enabled`, otherwise `MARKET_DUTY_COLLECT_NEEDS_ESTIMATES`) or `included_in_price` (the merchant; nothing is added and orders record the estimate as `duty_total` plus `duty_tax_estimate`, the merchant's estimated cost). `duties_enabled` only turns estimates from country rules on or off; the answer applies either way. Confirm the answer with the merchant before changing it: estimates come from their own rules, carriers and customs may charge differently (including handling fees), and the merchant is responsible for the choice.

`get_market_customer_notes` and `update_market_customer_notes` read and change the tax, shipping and duty notes a market shows shoppers, per storefront language and variant. Send only the texts to change; `text: null` resets a variant to the platform default and an empty string shows nothing. Only `on_delivery_estimate` may use `{{.amount}}`.

## Shipping and payments

Save Advanced shipping mode before managing zones or methods. Fetch the complete method and preserve its weight unit and tier meaning when replacing it. `item` selects an item-count tier; `per_item` multiplies one charge by shippable quantity. Weight boundaries use the saved g/kg/lb/oz unit. Checkout offers methods only from the matched shipping zone. If its active methods cannot supply a rate, a broader zone is not tried.

COD's market-wide switch applies in Simple and Advanced modes. Development and transfer stores take test payments only, so COD cannot be enabled there. Save Advanced mode before managing COD zones. Preserve `unavailable_display`, `unavailable_message` and `unavailable_message_translations`, and `waiver_notice_enabled`, `waiver_notice_waived` and `waiver_notice_remaining`, when replacing COD settings or a COD zone; both carry all six. With `unavailable_display: show_reason`, checkout lists an order's unavailable COD disabled with the reason in the shopper's language: the translation for that store language, else `unavailable_message` (the store's default language), else Tringify's standard reason in the shopper's language. `{{.amount}}` prints the minimum or maximum order value for COD in the shopper's currency; when a product rule or the destination makes COD unavailable, a reason using it is replaced by the standard reason. Which setting applies: in Simple mode, the market's; in Advanced mode, when a zone matched the shipping address (including the default zone, and including a zone whose `is_enabled` is false), that zone's, for every reason COD is unavailable (zone off, minimum or maximum order value, product rule); in Advanced mode, when no zone matched (none covers the address and there is no default zone), the market's. A zone created without `unavailable_display` uses `hide`.

While COD is available and `waive_fee_over_amounts` has an amount for the checkout currency, checkout shows a fee waiver message on the COD option: "Cash on delivery fee waived." once the discounted merchandise subtotal reaches it, else "Add {{.amount}} more to have the cash on delivery fee waived." (`{{.amount}}` is the waiver amount minus the subtotal, in the checkout currency). Nothing is shown when `waive_fee_enabled` is false, the fee is 0 anyway, or `waiver_notice_enabled` is false (it defaults to `true`). The standard texts exist in every storefront language; `waiver_notice_waived` and `waiver_notice_remaining` override them per store language, the default language included (200 characters; only the remaining text may use `{{.amount}}`, otherwise `COD_WAIVER_NOTICE_PLACEHOLDER_INVALID`; empty texts are dropped). Reads add `waiver_notice_defaults` (`waived`/`remaining` per enabled store language) to show where the merchant wrote nothing. Simple mode uses the market's message settings; Advanced mode uses the matched zone's.

Product rules do not override a disabled market/zone or order-value restrictions.

Markets manage already-connected payment-provider availability and provider-specific merchandise discounts. They do not create a provider connection or return its credentials. Read the returned discount catalog before authoring. Scheduling, minimum-spend conditions, caps and fee-tax fields are not supported for online-payment discounts.

## Discounts and checkout

Discount types have different required fields and targeting rules. Read discount limits and complete definitions, including related products/variants, gift products, bundle components and tiers. Whole-product and exact-variant targets are distinct. Tiered discounts use only the highest reached base-currency tier. Buy X Get Y/bundles reserve their claimed units; stacked savings use remaining values and cannot make merchandise negative.

To list a discount or an online-payment discount under Available offers on product pages, set `show_on_product_page` (discounts for everyone only; a code then becomes public) and optionally `product_page_label`. Read `product_page_max_per_market`, `product_page_max_shown` and `product_page_label_max_length` from the discount limits (the payment adjustment catalog carries the label limit). Tringify words the offer in each shopper's language and currency; themes show it from `product.offers`.

Checkout limits compare merchandise after product/order discounts and exclude shipping, tax, duties and fees. Checkout percentage fees use that same merchandise basis; fixed per-item fees multiply merchandise quantity. Required and optional fees differ. Reordering fees requires every current fee ID exactly once.

## Confirmation and bulk results

Show the returned impact before resending a delete or destructive configuration change with `confirmed` and the server's `confirmation_token`. Keep the target and selection unchanged. Do not confirm automatically. Protected/default records and dependencies can still block a confirmed request.

Tax-rate saves, tax-class bulk deletion and currency/country assignment batches have their documented atomic behavior. Discount bulk actions commit per item: inspect every result and retry only failed IDs after resolving their cause. Current changes do not rewrite existing order pricing, tax, duty or payment snapshots.

Tax IDs and customer exemptions use offline checks only. Tringify checks tax ID formats and check digits only. It does not verify registrations or exemptions with tax authorities. You are responsible for your tax settings and for approving exempt customers.

EU VAT uses each member state's published construction and checksum rules; Canadian BN uses MOD10. Czech nine-digit birth numbers have no checksum, and Latvian personal-number checksums are not publicly specified, so those personal forms receive structural checks only. Checkout ignores saved IDs that fail the matched zone's type, format or custom pattern, without blocking pricing or payment. Shopper-entered IDs travel with quotes and return field errors. Order address edits recalculate the identity type, applied exemption source and GSTIN state mismatch with the tax totals.

Choose a tax ID type that fits at least one country in the zone: eu_vat for EU countries, uk_vat for GB, gstin for IN, abn for AU, gst_hst for CA, ein for US, or custom anywhere. A default zone uses its market's countries. Existing mismatched settings remain unchanged and the API returns tax_exemption.type_mismatch=true; correct the type or countries before saving the zone.

For custom IDs, set a label and optionally a placeholder, example and RE2 pattern (maximum 256 UTF-8 bytes). The pattern must match the entire normalized ID; without a pattern, custom IDs are free text up to 100 characters. Examples must pass validation. Label and placeholder allow 50 characters each; checkout text allows 100. Supply translations for en, de, es, fr and it in tax_exemption.translations. Built-in labels use the checkout text system. The checkout editor preview shows the first exemption-enabled zone's field with an empty value; it shows none when no zone enables it.
