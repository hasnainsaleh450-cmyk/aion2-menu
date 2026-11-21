# Security Policy

This repository is a hobbyist Aion 2 cheat menu intended for offline / private-server
use and reverse-engineering education. Running it against live retail servers will
almost certainly result in a ban and may violate the Aion 2 ToS. You are responsible
for how you use it.

## Reporting a vulnerability
If you find a crash, memory-corruption bug, or an anti-cheat detection vector that
can be responsibly disclosed, open a private security advisory on GitHub or email
`security@aion2-menu.dev`. Do not file public issues for detection bypasses.

## Scope
- In scope: the Python overlay, the memory driver, offset tables.
- Out of scope: third-party DLLs, game client issues, retail-server anti-cheat internals.

## Builds
Only run binaries built from source at a tagged release. The maintainers will never
distribute a compiled `aion2-menu.exe` via random file hosts.