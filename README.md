# Tringify MCP

Connect [Codex](https://developers.openai.com/codex/) to your Tringify store. Sign in with your Tringify account, choose a store, and approve access.

**Server URL:** `https://api.tringify.com/mcp/store`

**Transport:** Streamable HTTP

**Authentication:** OAuth with PKCE

Tringify hosts the server. You do not need to clone this repository, run a server, install a Tringify package, or create an API key.

[Connection guide](https://developers.tringify.com/mcp) · [MCP and OAuth reference](https://dev-docs.tringify.com/apps/connectors/oauth) · [Connected tools](https://accounts.tringify.com/manage/connected-tools)

## Connect in the Codex app

On the computer where you want to use the connection:

1. Open **Settings → MCP servers → Add server**.
2. Name the server **Tringify**, choose **Streamable HTTP**, and enter `https://api.tringify.com/mcp/store`.
3. Save the server, then select **Restart** when prompted.
4. Select **Authenticate** for Tringify. Sign in in the browser, choose your store, review the requested permissions, and approve.
5. Return to Codex and start a new conversation. Type `/mcp` to check the connection.

Complete sign-in on the same computer that started it. The browser returns to a local callback on that computer.

## Connect with the Codex CLI

If the Codex CLI is already installed:

```sh
codex mcp add tringify --url https://api.tringify.com/mcp/store
```

Follow the sign-in prompt if one opens. If the server still needs authentication:

```sh
codex mcp login tringify
```

The app and CLI share MCP configuration on the same Codex host; choose either setup method. Run `codex mcp list` to see configured servers. Listing a configuration does not by itself prove that authentication or a tool call succeeded.

For manual configuration, see [examples/codex-config.toml](examples/codex-config.toml). Merge that entry into your existing configuration; do not replace your whole file. No bearer token or client secret belongs in the example.

## Try a read

Ask Codex:

> Use Tringify to list five tags in my connected store.

Then:

> Get the details of the tag with ID [one of the returned IDs].

Results come from the store selected during approval. Tool arguments cannot switch the connection to a different store.

## Try a small change

Use a development store or a test tag you intend to remove. Request both product read and write access during approval for this walkthrough.

1. Ask: **Create a tag named “MCP connection test” with slug “mcp-connection-test”. If that slug already exists, stop without changing it.** Record the returned ID.
2. Ask: **Rename only the tag you just created to “MCP connection test updated”. Keep its slug unchanged.**
3. Ask: **Get that tag again and show its ID, name, and slug.**
4. Ask: **Delete only the test tag we created, after showing me any deletion impact that Tringify returns.**

If deletion requires confirmation, Tringify returns the impact and a confirmation token. Review the impact before approving the second delete call. Do not ask Codex to remove an existing tag just to make this walkthrough pass.

If a write reports an uncertain result or loses its response, read back the result before attempting it again. Repeating a write is not a substitute for checking whether it completed.

## Available tools

All store-data tools use the corresponding Store API operations. The server returns tools allowed by your approved connection and current permissions. Read and write access are separate.

| Resource | Read tools | Write tools |
| --- | --- | --- |
| Tags | List, get, individual and batch translations | Create, update, delete, individual and batch translations |
| Brands | List, get, individual/batch translations, metafield translations | Create, update, delete, individual/batch translations, metafield translations |
| Vendors | List, get, individual/batch translations, metafield translations | Create, update, delete, individual/batch translations, metafield translations |
| Attributes | Lists, discovery, details, translations | Create, update, delete, bulk delete, reorder attributes/options, translations |
| Products | Lists, details, variants, quantity pricing, metafields, translations | Create, update, duplicate, delete, supported bulk actions, metafields and translations |
| Collections | Lists, search, details, product lists, rules, metafields, translations | Create, update, delete, bulk actions, rules, metafields and translations |
| Categories | Lists, search, details, metafields, translations | Create, update, delete, bulk create/delete, metafields and translations |
| Pages | Limits, list, search, details, translations, metafields | Create, update, delete, bulk delete, translations and metafields |
| Policies | Limits, list, get by type, translations | Update by type, individual and batch translations |
| Blog Posts | Limits, list, search, details, translations, metafields | Create, update, delete, bulk status/category/tag changes, translations and metafields |
| Blog Tags and Categories | Limits, list, details, translations; category metafields | Create, update, delete, bulk delete, translations; category metafields |
| Blog Authors | Limits, list, search, details | Create, update, delete, bulk delete with reassignment when required |
| Markets | All 107 documented JSON operations; live limits, country/currency mappings, tax, discounts, shipping, duties, COD, payments, checkout | Market and specialist configuration, bulk operations, confirmation and fee ordering |
| Languages | `list_languages`, `list_available_languages` | `set_languages`, `set_default_language`, `delete_language_translations` |
| Currencies | `list_currencies`, `list_enabled_currencies`, `get_base_currency`, `get_currency`, `list_exchange_rates`, `get_exchange_rate` | `create_currency`, `update_currency`, `delete_currency`, `remove_currency_data`, `bulk_remove_currency_data`, `set_currency_rounding`, `set_multi_currency`, `set_auto_exchange_rates` |
| Reference data | `list_countries`, `list_subdivisions`, `list_timezones`, `list_available_currencies`, `list_phone_country_codes`, `get_number_format_defaults`, `list_address_formats`, `get_address_format`, `list_store_api_scopes` | — |
| Files | `list_files`, `get_file`, `get_file_limits`, `get_storage_quota` | `update_file`, `delete_file`, `create_file_uploads`, `finalize_file_uploads`, `get_file_upload_status` |

Catalog reads require `store:products:read`; catalog writes require `store:products:write`. Binding new catalog images also requires `store:files:read`. `connection:read` permits the connection itself and grants no store-data access.

For Files, choose `library: "media"` or `library: "site_assets"` on every call. Media requires `store:files:read` or `store:files:write`. Site Assets requires `store:online_store.site_assets:read` or `store:online_store.site_assets:write`. Upload status is a read of an upload operation and, like preparation and finalization, requires that library's **write** permission. A file ID from another library cannot bypass these permissions.

Existing Products permissions cover the catalog tools. Translation operations also require `store:settings.languages:read` or `store:settings.languages:write`, matching the existing Languages permissions. Product operations affecting Gift Card products require `store:gift_cards:write` where the API requires it. Currency tools require `store:settings.currencies:read` or `store:settings.currencies:write`, independently of Products access. Reference data tools and `list_available_languages` need only `connection:read`. Refresh the tool list in your client to discover new tools. To add permissions, use the access-update flow below; refreshing a token cannot enlarge its grant.

Order editing uses `get_order`, `get_order_edit_options`, `list_order_edit_shipping_options`, `preview_order_edit`, `apply_order_edit`, and `list_order_edits`. Reads need `store:orders:read`; previews, delivery quotes and applying need `store:orders:write`. Read current field permissions before editing. Preview item, price, manual discount, contact, address and shipping changes, review the resulting totals and settlement, then apply with the returned `preview_token`, current `order_version` and a stable `idempotency_key`. The server revalidates every write. Existing connections must approve the added Orders access. See the [Orders API reference](https://dev-docs.tringify.com/store-api/orders/orders).

The [complete tool inventory](docs/catalog-tools.md) lists the supported operations and their API counterparts. The [reference](https://dev-docs.tringify.com/apps/connectors/oauth) describes accepted fields, pagination, errors, limits, and confirmation. Products, Collections, Categories, Attributes, Languages, and Currencies cover their documented merchant-authorized API endpoints. App-only purchase requirements remain outside user connections. Brands, Vendors, Tags, and Files support the tools shown above; their remaining API endpoints are not implied.

## Pages, policies, and blogs

Pages and Policies require `store:pages:read` or `store:pages:write`. Blog Posts, Tags, Categories, and Authors require `store:blog:read` or `store:blog:write`. These are separate from Products permissions. Translations also require the corresponding Languages permission; attaching a post featured image or author avatar requires Files read access.

Policies are fixed records: use their type for get/update and their UUID for translations. There are no create or delete policy tools. Deleting an author assigned to posts requires a replacement author. Blog Authors have no translation endpoints.

Use `list_page_metafield_definitions` and `list_blog_metafield_definitions` to discover accessible definitions before setting Page, Blog Post, or Blog Category values. Blog Comments expose single and bulk moderation and permanent deletion. Blog Settings expose comment mode and moderation. Blog index SEO includes source and translations; setting a social image also requires Site Assets read access. Menus have separate `store:menus:read` and `store:menus:write` access, including full and lazy tree reads, item changes, atomic saves and title translations. Send the revision from your menu read with every save; a stale save is refused with `MENU_SAVE_CONFLICT`.

## Markets

Markets require `store:markets:read` and `store:markets:write`, independently of Products and store Currencies. The hosted connector exposes all 107 documented Markets JSON operations, including country/currency assignments, tax classes/zones/rates/price rules, discounts, shipping, duties, COD, connected payment-provider availability/discounts, checkout limits and fees. Update an existing connection's approved access to add Markets, then refresh discovery.

Start with `get_market_limits`, `get_assigned_market_countries`, `list_markets` and `get_market`. Read each specialist's live limits and complete saved definition before changing it. Market PATCH changes supplied fields; specialist PUT requests follow their replacement contract. Amount maps and fields declared as decimal strings retain currency precision. Buy X Get Y `fixed` means an amount off each reward item; a bundle fixed price is the complete set's price.

The [Markets integration guide](docs/markets.md) covers dependencies, calculation behavior, confirmation and bulk results. The same guide is available through MCP `resources/read` at `https://dev-docs.tringify.com/store-api/markets/markets`. CSV tax import/export and its asynchronous jobs are available in Store Admin and mobile.

## Languages and translations

Languages use `store:settings.languages:read` and `store:settings.languages:write`, independently of Products access. `list_available_languages` is universal reference data and needs only the connection.

- `list_available_languages` lists supported locale codes.
- `list_languages` returns enabled languages, the default, and the current plan limit.
- `set_languages` sets the complete enabled list. Always include the default; omitting `locales` leaves the set unchanged.
- `set_default_language` changes the source language after impact confirmation.
- `delete_language_translations` resets one enabled non-default language after impact confirmation, without disabling it.

Removing a language can permanently delete translations and requires confirmation. A language assigned to a storefront is protected until its assignments are removed. Adding a language does not publish it on a storefront or translate content automatically. Review the returned warnings before confirming destructive changes.

Content translation tools are already available for **Products, variant titles, Collections, Categories, Attributes, attribute options, Tags, Brands, Vendors, Pages, Policies, Blog Posts, Blog Tags, Blog Categories, and supported product, variant, category, collection, brand, vendor, page, blog post, and blog category metafields**. Product, collection, category, attribute, option, tag, brand, vendor, page, policy, blog post, blog tag, and blog category translations also have batch tools. Variant titles and metafields use individual tools. **Files translations, AI translation jobs, and translation CSV import/export are not exposed through MCP.**

## Currencies

Currencies use `store:settings.currencies:read` and `store:settings.currencies:write`, independently of Products access.

- The base currency is fixed: it cannot be added, edited, disabled, rounded, or removed. Its `rounding_modes` is empty.
- `update_currency` changes only the fields you send; send at least one. Offer only the currency's own `rounding_modes`.
- In automatic-rate mode, rates and enabled state follow the market (`rate_source: "automatic"`); only rounding can change. Turning automatic rates on requires no additional currencies; turning them off copies the current market rate onto every additional currency.
- `remove_currency_data` and `bulk_remove_currency_data` preview first and need confirmation. `delete_currency` is blocked while live references or active Gift Card balances in that currency remain.

## Work with brands and vendors

Start with reads:

> Use Tringify to list five brands and five vendors in my connected store.

Create and update tools support names, slugs, descriptions, SEO fields, an existing Media image, and a storefront template. Updates change only supplied fields. A slug change creates a redirect unless you explicitly turn that off with `create_redirect: false`. Deletion preserves the related products and can require confirmation of the returned impact.

## Edit attributes

Read an attribute first. An update requires its exact current `revision` as `expected_revision`, its unchanged `sub_type`, and its **complete option set**. Keep the IDs and values of options you want to preserve. Options left out request removal; the service blocks removal while they are in use.

> Get attribute [ID] and show me its current options. Do not change anything yet.

After reviewing the result, describe the change you want. If another edit made the revision stale, read again and review the new state. Do not automatically overwrite it. Existing images on the same options can be preserved without Files read permission; adding or replacing an option image requires that permission.

## Upload a file

Codex needs a way to read the local file and make the upload request from the computer running it. The MCP tools handle upload preparation, validation and the resulting library record.

1. Read `get_file_limits` and `get_storage_quota` for the intended library.
2. Call `create_file_uploads` with that library and the file's exact `original_filename`, `mime_type`, and `size_bytes`. `alt_text` is optional.
3. The result contains `data.intents`. PUT the file bytes to the returned `url`, using its returned `headers`, before `expires_in` elapses. Treat that signed URL as a temporary credential; do not publish it.
4. Call `finalize_file_uploads` with the same library and returned `intent_ids`.
5. Check `get_file_upload_status` while processing. Attach the file only after its status is `ready` and the result includes the validated `file`.

Do not put binary data or base64 into MCP arguments. Starting an upload does not mean it has passed validation. Do not restart an upload just because validation is still processing.

Files can be renamed or have their alt text changed with `update_file`. Clearing a catalog image reference does not delete its library file. `delete_file` checks use and may require impact confirmation; a file required by another record can block deletion.

## Update permissions

Keep your existing MCP server entry and start authorization again:

```sh
codex mcp login tringify
```

Use your configured server name if it differs from `tringify`. On Tringify’s approval screen, select the same store and choose the existing connection. Review the permissions marked **New permission** and any access that will be removed, then select **Update access**. If several connections match, select the one you intend to update; **Create a separate connection** is a separate choice.

Your current connection keeps working until Codex completes the authorization. The connection keeps its ID, its old credentials stop working, and Codex receives replacement credentials. Cancelling or abandoning approval leaves existing access unchanged. Refresh the connection or start a new conversation to load the updated tools.

The tool must request the additional scopes, and your current store role must allow them. An expired or disconnected connection needs a new authorization. **Accounts → Connected Tools → Update access** also explains these steps. You do not need to disconnect first.

## Audit logs

Audited changes identify the user who authorized the connection. The store audit log shows that account’s email in **User**, **API** as the source, and **Connected tool: Codex** when Codex is the client. Other clients show their registered name. A staff member’s connection records that staff member, not the store owner.

File uploads retain the same user and tool attribution. The usual resource audit details apply, such as the affected record and recorded changes. Reading data does not create a mutation audit entry.

## Manage or remove the connection

Open [Connected tools](https://accounts.tringify.com/manage/connected-tools) in Tringify Accounts to review or disconnect access. Store owners can also disconnect their team's connections for that store. Removing a team member or their permissions changes what the connection can do.

To remove the local Codex entry as well:

```sh
codex mcp remove tringify
```

Remove access in Tringify Accounts first. Removing a local configuration entry should not be treated as proof of server-side revocation. To connect to another store, disconnect and authorize a new connection for that store.

## Troubleshooting

- **Authentication does not finish:** complete the browser flow on the computer running Codex. Use the exact server URL above, without a trailing slash. If the approval expired, start a new sign-in.
- **No tools appear:** approve product read or write access as needed. A connection with only `connection:read` has no tag tools. Use Update access to approve missing permissions; refresh cannot add permissions. Reload the connection or start a new conversation after setup.
- **A tool returns insufficient access:** check both the connection's approved scopes and your current store permissions. A tool listed earlier can become unavailable if your access changes.
- **Sign-in is required again:** reconnect through Codex. Disconnecting a tool, removed membership, expired access, and token rotation failures can require a fresh sign-in.
- **The store is not listed:** use the Tringify account with access to that store and check whether the store and subscription are active.

When reporting a problem, include the Codex version, the failing step, and the returned error code. Never include access tokens, refresh tokens, authorization codes, cookies, or private callback URLs containing codes.

## Reference and updates

- [Tringify MCP and OAuth](https://dev-docs.tringify.com/apps/connectors/oauth)
- [Codex MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Changelog](CHANGELOG.md)

This repository contains connection instructions and configuration examples. The service runs at the hosted URL above.
