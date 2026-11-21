"""YAML -> typed config objects."""
from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class GameCfg(BaseModel):
    binary: str = "aion2.bin"
    region: str = "eu"


class OffsetCfg(BaseModel):
    path: Path = Path("offsets/global_offsets.json")
    build: str = "1.9.4.7"


class OverlayCfg(BaseModel):
    hotkeys: dict[str, str] = Field(default_factory=lambda: {"aimbot": "F1", "esp": "F2", "teleport": "F3"})
    opacity: float = 0.85


class AppConfig(BaseModel):
    profile: str = "default"
    game: GameCfg = GameCfg()
    offsets: OffsetCfg = OffsetCfg()
    overlay: OverlayCfg = OverlayCfg()


def load_config(path: Path) -> AppConfig:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    return AppConfig.model_validate(raw)