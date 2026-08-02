import sys

import MetaTrader5 as mt5


TERMINAL_PATH = "/opt/mt5/terminal64.exe"


def main() -> int:
    print(f"MetaTrader5 package version: {getattr(mt5, '__version__', 'unknown')}")
    print(f"Initializing terminal at: {TERMINAL_PATH}")

    if not mt5.initialize(path=TERMINAL_PATH):
        print(f"initialize() failed: {mt5.last_error()}", file=sys.stderr)
        return 1

    version = mt5.version()
    print(f"Connected to terminal, version={version}")
    mt5.shutdown()
    print("shutdown() completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
