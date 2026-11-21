"""Thin wrapper over pymem for the Aion 2 client."""
from __future__ import annotations

from dataclasses import dataclass

import pymem
from pymem.process import module_from_name

from aion2_utils.logging import get_logger

log = get_logger("memory")


@dataclass
class Vec3:
    x: float
    y: float
    z: float


class AionProcess:
    def __init__(self, pm: pymem.Pymem, base: int) -> None:
        self._pm = pm
        self.base = base

    @classmethod
    def attach(cls, binary: str) -> "AionProcess":
        pm = pymem.Pymem(binary)
        mod = module_from_name(pm.process_handle, binary)
        log.info("attached to %s base=0x%x", binary, mod.lpBaseOfDll)
        return cls(pm, mod.lpBaseOfDll)

    def read_vec3(self, addr: int) -> Vec3:
        x, y, z = self._pm.read_float(addr), self._pm.read_float(addr + 4), self._pm.read_float(addr + 8)
        return Vec3(x, y, z)

    def write_vec3(self, addr: int, x: float, y: float, z: float) -> None:
        self._pm.write_float(addr, x)
        self._pm.write_float(addr + 4, y)
        self._pm.write_float(addr + 8, z)

    def write_angles(self, yaw: float, pitch: float, smoothing: float = 1.0) -> None:
        # Placeholder: real impl writes into the camera struct.
        _ = (yaw, pitch, smoothing)

    def read_entity_list(self, addr: int):
        return []

    def world_to_screen(self, pos: Vec3, view_matrix: int):
        return pos