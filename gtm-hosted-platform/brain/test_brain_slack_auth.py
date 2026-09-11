#!/usr/bin/env python3
"""Tests for the brain's Slack identity auth door on /mcp. Run: python3 test_brain_slack_auth.py

Pins the contract added 2026-09-11 so Slackbot's MCP client (auth_type slack_identity_auth)
can reach the brain without a static key, while the key path stays exactly as it was:
  1. a request Slack signed over the raw body passes as actor "slackbot",
  2. a bad signature, a tampered body, or a stale/future/garbage timestamp is rejected,
  3. with no SLACK_SIGNING_SECRET the signature is never consulted: key-only, unchanged,
  4. no keys and no secret is still the open "dev" mode.

Same stubbed web layer as test_brain_state.py; everything under test is the pure
verify_slack_signature / resolve_actor pair the middleware calls.
"""
import hashlib
import hmac
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from test_brain_state import _stub_web_layer  # noqa: E402  (also imports app once)
_stub_web_layer()
import app as brain  # noqa: E402

SECRET = "8f742231b10e8888abcd99yyyzzz85a5"
NOW = 1_757_600_000  # fixed clock so the window tests are deterministic
KEYS = {"KEY1": "slack", "KEY2": "claude"}
BODY = b'{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{"_meta":{"slack":{"user_id":"U1"}}}}'


def signed(body=BODY, ts=NOW, secret=SECRET, sig=None):
    base = b"v0:" + str(ts).encode() + b":" + body
    digest = "v0=" + hmac.new(secret.encode(), base, hashlib.sha256).hexdigest()
    return {"X-Slack-Request-Timestamp": str(ts), "X-Slack-Signature": sig or digest}


def run():
    checks = []

    def check(name, cond):
        checks.append((name, bool(cond)))

    r = brain.resolve_actor

    # 1. valid signature passes
    check("valid Slack signature passes as slackbot / slack_identity",
          r(signed(), BODY, KEYS, SECRET, now=NOW) == ("slackbot", "slack_identity"))
    check("valid signature passes even when no API keys are configured",
          r(signed(), BODY, {}, SECRET, now=NOW) == ("slackbot", "slack_identity"))
    check("header names are matched case-insensitively",
          r({k.lower(): v for k, v in signed().items()}, BODY, KEYS, SECRET, now=NOW)
          == ("slackbot", "slack_identity"))
    check("timestamp 4 minutes old is inside the 5 minute window",
          r(signed(ts=NOW - 240), BODY, KEYS, SECRET, now=NOW) == ("slackbot", "slack_identity"))

    # 2. rejections
    check("bad signature is rejected (401)",
          r(signed(sig="v0=" + "0" * 64), BODY, KEYS, SECRET, now=NOW) is None)
    check("signature made with a different secret is rejected",
          r(signed(secret="wrong"), BODY, KEYS, SECRET, now=NOW) is None)
    check("tampered body is rejected (signature covers the raw body)",
          r(signed(), BODY + b" ", KEYS, SECRET, now=NOW) is None)
    check("stale timestamp (10 minutes old) is rejected",
          r(signed(ts=NOW - 600), BODY, KEYS, SECRET, now=NOW) is None)
    check("future timestamp beyond the window is rejected",
          r(signed(ts=NOW + 600), BODY, KEYS, SECRET, now=NOW) is None)
    check("non-integer timestamp is rejected",
          r({"X-Slack-Request-Timestamp": "soon", "X-Slack-Signature": "v0=abc"},
            BODY, KEYS, SECRET, now=NOW) is None)
    check("signature header without a timestamp is rejected",
          r({"X-Slack-Signature": signed()["X-Slack-Signature"]}, BODY, KEYS, SECRET, now=NOW)
          is None)
    check("no headers at all with keys configured is rejected",
          r({}, b"", KEYS, SECRET, now=NOW) is None)
    check("a rejected Slack signature does not fall through to an unrelated key",
          r({**signed(sig="v0=" + "0" * 64), "X-API-Key": "nope"}, BODY, KEYS, SECRET, now=NOW)
          is None)

    # 3. missing secret falls back to key-only
    check("no secret: a valid-looking signature alone is rejected",
          r(signed(), BODY, KEYS, "", now=NOW) is None)
    check("no secret: a valid API key still passes with its label",
          r({"X-API-Key": "KEY2"}, b"", KEYS, "", now=NOW) == ("claude", "api_key"))
    check("no secret: bearer form of the key still passes",
          r({"Authorization": "Bearer KEY1"}, b"", KEYS, "", now=NOW) == ("slack", "api_key"))
    check("no secret: verify_slack_signature itself returns False",
          brain.verify_slack_signature(signed(), BODY, "", now=NOW) is False)

    # 4. open dev mode unchanged
    check("no keys and no secret is still open dev mode",
          r({}, b"", {}, "", now=NOW) == ("dev", "open"))

    # key path with secret set (both doors open at once)
    check("with a secret set, a valid API key and no signature still passes",
          r({"X-API-Key": "KEY1"}, b"", KEYS, SECRET, now=NOW) == ("slack", "api_key"))
    check("with a secret set, a bad key and no signature is rejected",
          r({"X-API-Key": "bad"}, b"", KEYS, SECRET, now=NOW) is None)

    passed = sum(1 for _, c in checks if c)
    for name, cond in checks:
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    print("-" * 62)
    print(f"{passed}/{len(checks)} passed")
    return passed == len(checks)


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
