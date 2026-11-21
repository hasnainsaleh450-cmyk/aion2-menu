"""Pulls the latest offset table for a given Aion 2 build."""
from __future__ import annotations

from pathlib import Path

import requests

DEFAULT_REMOTE = "https://raw.githubusercontent.com/aion2-menu/offsets/main/global_offsets.json"


def update(target: Path, build: str, remote: str = DEFAULT_REMOTE) -> bool:
    resp = requests.get(remote, timeout=8)
    resp.raise_for_status()
    payload = resp.json()
    if build not in payload:
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(resp.text, encoding="utf-8")
    return True