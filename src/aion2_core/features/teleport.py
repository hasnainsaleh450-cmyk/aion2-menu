"""Waypoint teleport using the movement-write primitive."""
from __future__ import annotations

from dataclasses import dataclass

from aion2_core.features.base_feature import BaseFeature


@dataclass
class Waypoint:
    name: str
    x: float
    y: float
    z: float


class Teleport(BaseFeature):
    slug = "teleport"
    display_name = "Teleport"
    default_bind = "F3"

    def __init__(self) -> None:
        super().__init__()
        self.waypoints: list[Waypoint] = []

    def jump(self, index: int) -> None:
        if self.process is None or not (0 <= index < len(self.waypoints)):
            return
        wp = self.waypoints[index]
        self.process.write_vec3(self.offsets.resolve("local_pos"), wp.x, wp.y, wp.z)

    def tick(self) -> None:
        # All mutation happens through explicit jump() calls from the overlay menu.
        pass

    def save_current(self, name: str) -> None:
        if self.process is None:
            return
        pos = self.process.read_vec3(self.offsets.resolve("local_pos"))
        self.waypoints.append(Waypoint(name, pos.x, pos.y, pos.z))