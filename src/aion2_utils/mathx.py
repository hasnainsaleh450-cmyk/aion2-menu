"""Small vector math helpers used by aimbot / ESP."""
from __future__ import annotations

import math


def distance2(a: tuple[float, float], b: tuple[float, float]) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def clamp_angle(deg: float) -> float:
    return max(-180.0, min(180.0, deg))


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def yaw_pitch_to_forward(yaw: float, pitch: float) -> tuple[float, float, float]:
    yr, pr = math.radians(yaw), math.radians(pitch)
    return math.cos(yr) * math.cos(pr), math.sin(yr) * math.cos(pr), math.sin(pr)