from aion2_core.features.feature_registry import FeatureRegistry


def test_discover_finds_builtin_features():
    reg = FeatureRegistry()
    reg.discover("aion2_core.features")
    slugs = {f.slug for f in reg}
    assert "aimbot" in slugs
    assert "esp" in slugs
    assert len(reg) >= 3


def test_toggle_flips_state():
    reg = FeatureRegistry()
    reg.discover("aion2_core.features")
    assert reg.toggles()["aimbot"] is False
    assert reg.toggle("aimbot") is True
    assert reg.toggles()["aimbot"] is True