# Architecture

```
src/aion2_menu        -> bootstrap / entry
src/aion2_core        -> cheat features, memory, overlay, offsets
src/aion2_infra       -> config loading, offset updater
src/aion2_utils       -> logging, math helpers
```

## Threads
1. **Main thread** — argument parsing, bootstrap, waits on overlay stop event.
2. **Overlay thread** — pumps features (`tick()` on enabled features) and redraws.
3. **Hotkey thread** — managed by `keyboard` for global hotkey handling.

## Feature lifecycle
Every feature extends `BaseFeature` and is auto-discovered by `FeatureRegistry.discover`.
On toggle, `on_enable` / `on_disable` hooks fire. `tick()` is called per overlay frame
only when `enabled` is True.

## Offsets
Offsets are not hardcoded. `OffsetTable.load()` reads `offsets/global_offsets.json` keyed by
build string. After a game patch, run `tools/offset_scanner.py` to regenerate a
`local_offsets.json` and set `offsets.path` in your `config/local.yaml`.