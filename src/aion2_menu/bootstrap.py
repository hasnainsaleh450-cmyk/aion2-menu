"""Wires the cheat menu together: config -> process attach -> feature registry -> overlay."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from aion2_core.features.feature_registry import FeatureRegistry
from aion2_core.memory.process_handle import AionProcess
from aion2_core.overlay.overlay_loop import OverlayLoop
from aion2_core.offsets.offset_table import OffsetTable
from aion2_infra.config_loader import load_config
from aion2_utils.logging import get_logger

log = get_logger("bootstrap")


@dataclass
class Bootstrapper:
    config_path: Path
    overlay: OverlayLoop | None = None

    @classmethod
    def from_default_config(cls) -> "Bootstrapper":
        return cls(config_path=Path("config/default.yaml"))

    def run(self) -> None:
        cfg = load_config(self.config_path)
        log.info("loaded profile=%s game=%s", cfg.profile, cfg.game.binary)

        proc = AionProcess.attach(cfg.game.binary)
        offsets = OffsetTable.load(cfg.offsets.path, build=cfg.offsets.build)

        registry = FeatureRegistry()
        registry.discover(package="aion2_core.features")
        registry.inject_context(process=proc, offsets=offsets, config=cfg)
        log.info("registered %d feature modules", len(registry))

        self.overlay = OverlayLoop(registry=registry, hotkeys=cfg.overlay.hotkeys)
        self.overlay.start()