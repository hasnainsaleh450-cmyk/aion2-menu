"""Contract every cheat feature implements."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseFeature(ABC):
    slug: str = ""
    display_name: str = ""
    default_bind: str = ""

    def __init__(self) -> None:
        self.enabled: bool = False
        self._ctx: dict[str, Any] = {}

    def bind(self, **ctx: Any) -> None:
        self._ctx = ctx

    @property
    def process(self):
        return self._ctx.get("process")

    @property
    def offsets(self):
        return self._ctx.get("offsets")

    @property
    def config(self):
        return self._ctx.get("config")

    def enable(self) -> None:
        self.enabled = True
        self.on_enable()

    def disable(self) -> None:
        self.enabled = False
        self.on_disable()

    def on_enable(self) -> None:  # optional override
        pass

    def on_disable(self) -> None:  # optional override
        pass

    @abstractmethod
    def tick(self) -> None:
        """Called each overlay frame while `enabled` is True."""