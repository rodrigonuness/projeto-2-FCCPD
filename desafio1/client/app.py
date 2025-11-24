import os
import time
from datetime import UTC, datetime

import requests


TARGET_URL = os.environ.get("TARGET_URL", "http://server:8080/")
INTERVAL = float(os.environ.get("INTERVAL_SECONDS", "5"))


def main():
    while True:
        try:
            response = requests.get(TARGET_URL, timeout=5)
            response.raise_for_status()
            now = datetime.now(UTC).isoformat().replace("+00:00", "Z")
            print(f"[{now}] OK: {response.text}")
        except Exception as exc:  # noqa: BLE001
            now = datetime.now(UTC).isoformat().replace("+00:00", "Z")
            print(f"[{now}] ERROR: {exc}")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
