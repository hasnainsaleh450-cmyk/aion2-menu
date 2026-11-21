"""Bootstrap for the Aion 2 cheat menu."""
from __future__ import annotations

import sys

from aion2_menu.bootstrap import Bootstrapper
from aion2_utils.logging import get_logger

log = get_logger("aion2-menu")


def main() -> int:
    log.info("starting aion2-menu %s", __import__("aion2_menu").__version__)
    try:
        boot = Bootstrapper.from_default_config()
        boot.run()
    except KeyboardInterrupt:
        log.info("interrupted by user")
        return 130
    except Exception:
        log.exception("fatal error")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())