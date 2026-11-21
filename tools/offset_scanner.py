"""Standalone scanner to locate offsets after a game patch."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pymem

from aion2_utils.logging import get_logger

log = get_logger("scanner")


def scan(binary: str, patterns: dict[str, bytes], out: Path, build: str) -> None:
    pm = pymem.Pymem(binary)
    found: dict[str, int] = {}
    for name, pat in patterns.items():
        try:
            addr = pymem.pattern.pattern_scan_module(pm.process_handle, None, pat, return_multiple=False)
            if addr:
                found[name] = addr
                log.info("%s -> 0x%x", name, addr)
        except Exception:
            log.exception("scan failed for %s", name)
    payload = {build: found}
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--binary", default="aion2.bin")
    ap.add_argument("--build", required=True)
    ap.add_argument("--out", default="offsets/local_offsets.json")
    args = ap.parse_args()
    # TODO: pattern dictionary — fill in once a build is reverse-engineered.
    scan(args.binary, {}, Path(args.out), args.build)


if __name__ == "__main__":
    main()