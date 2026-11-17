#!/usr/bin/env python3
"""Bring docs/tool-catalog.json and docs/catalog-tools.md in line with an export
of the hosted connector's tool catalog.

    scripts/sync-catalog.py export.json

The JSON file becomes the export. In the inventory, each tool's row gets the
export's operation (the access column is written by hand and kept) and rows of
tools missing from the export are dropped. Tools without a row are printed as
table rows to add to the section each belongs to, and the script then exits
with status 1. Prints what changed.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/tool-catalog.json"
INVENTORY = ROOT / "docs/catalog-tools.md"
HEADER = "| Tool | Store API operation | Required access |\n| --- | --- | --- |\n"
ROW = re.compile(r"^\| `([^`]+)` \| `[^`]*` \| (.*) \|$")


def row(tool):
    return "| `%s` | `%s %s` | %s |" % (tool["name"], tool["api_method"], tool["api_path"], ", ".join(tool["scopes"]))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    export_text = Path(sys.argv[1]).read_text()
    tools = json.loads(export_text)
    if not isinstance(tools, list) or len(tools) < 100:
        sys.exit("the export does not look like the tool catalog")
    by_name = {t["name"]: t for t in tools}
    if len(by_name) != len(tools):
        sys.exit("the export names a tool twice")

    lines = INVENTORY.read_text().rstrip("\n").split("\n")
    out, seen, updated, dropped = [], set(), 0, []
    for line in lines:
        m = ROW.match(line)
        if not m:
            out.append(line)
            continue
        name = m.group(1)
        if name not in by_name:
            dropped.append(name)
            continue
        seen.add(name)
        tool = by_name[name]
        new = "| `%s` | `%s %s` | %s |" % (name, tool["api_method"], tool["api_path"], m.group(2))
        updated += new != line
        out.append(new)
    added = [t["name"] for t in tools if t["name"] not in seen]
    INVENTORY.write_text("\n".join(out) + "\n")
    changed_json = CATALOG.read_text() != export_text
    CATALOG.write_text(export_text)
    print("tools %d; catalog json %s; inventory rows updated %d, missing %d, dropped %d" % (
        len(tools), "changed" if changed_json else "unchanged", updated, len(added), len(dropped)))
    for n in dropped:
        print("dropped", n)
    if added:
        print("\nadd these rows to the section each tool belongs to in %s:\n" % INVENTORY.relative_to(ROOT))
        print(HEADER, end="")
        for n in added:
            print(row(by_name[n]))
        sys.exit(1)


if __name__ == "__main__":
    main()
