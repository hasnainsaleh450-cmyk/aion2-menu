# Contributing to aion2-menu

Thanks for helping out with the Aion 2 cheat menu.

## Ground rules
- Every feature must be toggleable from the in-game overlay. No silent hooks.
- Memory offsets live under `aion2_core/offsets/` — do not hardcode them in feature modules.
- Feature modules register themselves through `FeatureRegistry`; do not import feature modules directly elsewhere.
- Keep the overlay thread separate from the game-attach thread. Never block either.

## Local dev
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m aion2_menu
```

## Submitting PRs
1. Fork, branch from `main`.
2. Add a stub test under `tests/` for new feature modules.
3. Run `pytest -q` before opening the PR.
4. Attach a screenshot of the overlay if you touched rendering.

## Style
- Black-compatible formatting, 100 cols.
- Type hints on public functions.
- No prints in library code — use the logger from `aion2_utils.logging`.