"""Overlay render loop + hotkey pump."""
from __future__ import annotations

import threading
import time

import keyboard

from aion2_core.features.feature_registry import FeatureRegistry
from aion2_utils.logging import get_logger

log = get_logger("overlay")


class OverlayLoop:
    def __init__(self, registry: FeatureRegistry, hotkeys: dict[str, str]) -> None:
        self.registry = registry
        self.hotkeys = hotkeys
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, name="overlay", daemon=True)

    def start(self) -> None:
        for slug, key in self.hotkeys.items():
            keyboard.add_hotkey(key, self._make_toggle(slug))
        self._thread.start()
        log.info("overlay started with %d hotkeys", len(self.hotkeys))

    def stop(self) -> None:
        self._stop.set()
        self._thread.join(timeout=2.0)

    def _make_toggle(self, slug: str):
        def _toggle() -> None:
            state = self.registry.toggle(slug)
            log.info("feature %s -> %s", slug, state)
        return _toggle

    def _run(self) -> None:
        while not self._stop.is_set():
            for feat in self.registry:
                if feat.enabled:
                    try:
                        feat.tick()
                    except Exception:
                        log.exception("feature %s tick failed", feat.slug)
            time.sleep(1 / 120)