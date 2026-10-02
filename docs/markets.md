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

Duties use destination, origin and HS-code rules. Read a complete rule before editing, including all origin and HS rates. A de-minimis threshold is in the rule's saved destination currency; equality is not exempt. Review whether duties are collected at checkout or paid on delivery. Taxes and duties are calculated from the merchant's saved configuration.

## Shipping and payments

Save Advanced shipping mode before managing zones or methods. Fetch the complete method and preserve its weight unit and tier meaning when replacing it. `item` selects an item-count tier; `per_item` multiplies one charge by shippable quantity. Weight boundaries use the saved g/kg/lb/oz unit. Checkout offers methods only from the matched shipping zone. If its active methods cannot supply a rate, a broader zone is not tried.

COD's market-wide switch applies in Simple and Advanced modes. Development and transfer stores take test payments only, so COD cannot be enabled there. Save Advanced mode before managing COD zones. Preserve `unavailable_display` and `unavailable_message` when replacing COD settings. Product rules do not override a disabled market/zone or order-value restrictions.

Markets manage already-connected payment-provider availability and provider-specific merchandise discounts. They do not create a provider connection or return its credentials. Read the returned discount catalog before authoring. Scheduling, minimum-spend conditions, caps and fee-tax fields are not supported for online-payment discounts.

## Discounts and checkout

Discount types have different required fields and targeting rules. Read discount limits and complete definitions, including related products/variants, gift products, bundle components and tiers. Whole-product and exact-variant targets are distinct. Tiered discounts use only the highest reached base-currency tier. Buy X Get Y/bundles reserve their claimed units; stacked savings use remaining values and cannot make merchandise negative.

Checkout limits compare merchandise after product/order discounts and exclude shipping, tax, duties and fees. Checkout percentage fees use that same merchandise basis; fixed per-item fees multiply merchandise quantity. Required and optional fees differ. Reordering fees requires every current fee ID exactly once.

## Confirmation and bulk results

Show the returned impact before resending a delete or destructive configuration change with `confirmed` and the server's `confirmation_token`. Keep the target and selection unchanged. Do not confirm automatically. Protected/default records and dependencies can still block a confirmed request.

Tax-rate saves, tax-class bulk deletion and currency/country assignment batches have their documented atomic behavior. Discount bulk actions commit per item: inspect every result and retry only failed IDs after resolving their cause. Current changes do not rewrite existing order pricing, tax, duty or payment snapshots.
