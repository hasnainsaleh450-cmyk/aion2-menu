from pathlib import Path

import pytest

from aion2_core.offsets.offset_table import OffsetTable
from aion2_utils.mathx import clamp_angle, distance2

ROOT = Path(__file__).resolve().parents[1]


def test_loads_known_build():
    tbl = OffsetTable.load(ROOT / "offsets/global_offsets.json", build="1.9.4.7")
    assert tbl.resolve("local_pos") > 0


def test_missing_offset_raises():
    tbl = OffsetTable.load(ROOT / "offsets/global_offsets.json", build="1.9.4.7")
    with pytest.raises(KeyError):
        tbl.resolve("nonexistent_offset")


def test_math_helpers():
    assert clamp_angle(200) == 180
    assert clamp_angle(-200) == -180
    assert distance2((0, 0), (3, 4)) == 25