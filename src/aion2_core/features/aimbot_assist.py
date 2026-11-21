"""Aimbot / snap-target assist for Aion 2."""
from __future__ import annotations

import math

from aion2_core.features.base_feature import BaseFeature


class AimbotAssist(BaseFeature):
    slug = "aimbot"
    display_name = "Aimbot"
    default_bind = "F1"

    def __init__(self) -> None:
        super().__init__()
        self.smoothing = 4.0
        self.bone = "head"
        self.fov = 180

    def tick(self) -> None:
        if not self.enabled or self.process is None:
            return
        target = self._pick_nearest()
        if target is None:
            return
        self._snap_to(target)

    def _pick_nearest(self):
        # Reads entity list from the offset table; returns (screen_pos, dist) or None.
        ents = self.process.read_entity_list(self.offsets.resolve("entity_list"))
        local = self.process.read_vec3(self.offsets.resolve("local_pos"))
        best, best_d = None, math.inf
        for e in ents:
            d = (e.pos.x - local.x) ** 2 + (e.pos.y - local.y) ** 2
            if d < best_d and d < self.fov ** 2:
                best, best_d = e, d
        return best

    def _snap_to(self, entity) -> None:
        delta = (entity.pos - self.process.read_vec3(self.offsets.resolve("cam_pos")))
        yaw = math.degrees(math.atan2(delta.y, delta.x))
        pitch = math.degrees(math.atan2(delta.z, math.hypot(delta.x, delta.y)))
        self.process.write_angles(yaw, pitch, smoothing=self.smoothing)