#!/usr/bin/env python3
"""Compare email schemas with an export of the hosted connector's tool catalog."""
import argparse
import json
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument('executable_catalog', type=Path)
p.add_argument('--docs-catalog', type=Path)
a = p.parse_args()
def email(path):
    return {t['api_key']: t for t in json.loads(path.read_text()) if t.get('api_key', '').startswith('email_')}
expected = email(a.executable_catalog)
assert expected, 'executable export contains no email tools'
for path in [Path(__file__).resolve().parents[1] / 'docs/tool-catalog.json'] + ([a.docs_catalog] if a.docs_catalog else []):
    actual = email(path)
    assert actual == expected, f'email tool schema/prose drift: {path}'
reply = expected['email_reply_to.update']['input_schema']
assert 'otp_code' in reply.get('required', []), 'reply-to step-up must be required'
assert reply.get('additionalProperties') is False
print(f'{len(expected)} executable email tool contracts match')
