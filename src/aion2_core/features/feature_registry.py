"""Registry for all cheat-menu feature modules."""
from __future__ import annotations

import importlib
import pkgutil
from typing import Any

from aion2_core.features.base_feature import BaseFeature
from aion2_utils.logging import get_logger

log = get_logger("registry")


class FeatureRegistry:
    def __init__(self) -> None:
        self._features: dict[str, BaseFeature] = {}

    def discover(self, package: str) -> None:
        pkg = importlib.import_module(package)
        for mod in pkgutil.iter_modules(pkg.__path__):
            if mod.name.startswith("_") or mod.name == "base_feature":
                continue
            module = importlib.import_module(f"{package}.{mod.name}")
            for attr in vars(module).values():
                if isinstance(attr, type) and issubclass(attr, BaseFeature) and attr is not BaseFeature:
                    inst = attr()
                    self._features[inst.slug] = inst
                    log.debug("registered feature %s", inst.slug)

    def inject_context(self, **ctx: Any) -> None:
        for feat in self._features.values():
            feat.bind(**ctx)

    def toggles(self) -> dict[str, bool]:
        return {slug: f.enabled for slug, f in self._features.items()}

    def toggle(self, slug: str) -> bool:
        feat = self._features.get(slug)
        if feat is None:
            raise KeyError(f"unknown feature: {slug}")
        feat.enabled = not feat.enabled
        return feat.enabled

    def __len__(self) -> int:
        return len(self._features)

    def __iter__(self):
        return iter(self._features.values())