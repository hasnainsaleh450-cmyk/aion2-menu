"""Loads game offsets from a versioned JSON table."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from aion2_utils.logging import get_logger

log = get_logger("offsets")


@dataclass
class OffsetTable:
    build: str
    values: dict[str, int]

    @classmethod
    def load(cls, path: Path, build: str) -> "OffsetTable":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        build_data = data.get(build) or data.get("default", {})
        if not build_data:
            raise ValueError(f"no offsets for build {build} in {path}")
        log.info("loaded %d offsets for build %s", len(build_data), build)
        return cls(build=build, values={k: int(v) for k, v in build_data.items()})

    def resolve(self, name: str) -> int:
        if name not in self.values:
            raise KeyError(f"offset '{name}' missing for build {self.build}")
        return self.values[name]