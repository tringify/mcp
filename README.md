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

The server returns the tools allowed by your connection and current store permissions.

| Tool | Action | Required scope |
| --- | --- | --- |
| `list_tags` | Search and page through tags | `store:products:read` |
| `get_tag` | Read one tag | `store:products:read` |
| `create_tag` | Create a tag | `store:products:write` |
| `update_tag` | Change supplied fields on a tag | `store:products:write` |
| `delete_tag` | Delete a tag, with impact confirmation when required | `store:products:write` |

`connection:read` permits the connection itself. It does not grant access to store data. Read and write permissions are separate. The [reference](https://dev-docs.tringify.com/apps/connectors/oauth) describes tool arguments, pagination, errors, and deletion confirmation.

## Manage or remove the connection

Open [Connected tools](https://accounts.tringify.com/manage/connected-tools) in Tringify Accounts to review or disconnect access. Store owners can also disconnect their team's connections for that store. Removing a team member or their permissions changes what the connection can do.

To remove the local Codex entry as well:

```sh
codex mcp remove tringify
```

Remove access in Tringify Accounts first. Removing a local configuration entry should not be treated as proof of server-side revocation. To connect to another store, disconnect and authorize a new connection for that store.

## Troubleshooting

- **Authentication does not finish:** complete the browser flow on the computer running Codex. Use the exact server URL above, without a trailing slash. If the approval expired, start a new sign-in.
- **No tools appear:** approve product read or write access as needed. A connection with only `connection:read` has no tag tools. Reconnect after changing approved scopes; refresh cannot add permissions. Reload the connection or start a new conversation after setup.
- **A tool returns insufficient access:** check both the connection's approved scopes and your current store permissions. A tool listed earlier can become unavailable if your access changes.
- **Sign-in is required again:** reconnect through Codex. Disconnecting a tool, removed membership, expired access, and token rotation failures can require a fresh sign-in.
- **The store is not listed:** use the Tringify account with access to that store and check whether the store and subscription are active.

When reporting a problem, include the Codex version, the failing step, and the returned error code. Never include access tokens, refresh tokens, authorization codes, cookies, or private callback URLs containing codes.

## Reference and updates

- [Tringify MCP and OAuth](https://dev-docs.tringify.com/apps/connectors/oauth)
- [Codex MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Changelog](CHANGELOG.md)

This repository contains connection instructions and configuration examples. The service runs at the hosted URL above.
