# Aimbot tuning

| Field | Meaning | Safe default |
|-------|---------|--------------|
| `smoothing` | Higher = slower snap, less obvious | 4.0 |
| `fov` | Aimbot cone in world units | 180 |
| `bone` | Target bone (`head`, `chest`) | `head` |

Anything below `smoothing = 2.0` is basically a rage aimbot and will get you banned
on any server with a server-side movement sanity check. Keep it at 4+.