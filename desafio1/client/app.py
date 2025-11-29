import os
import time
from datetime import UTC, datetime

import requests


URL_ALVO = os.environ.get("TARGET_URL", "http://server:8080/")
INTERVALO_SEGUNDOS = float(os.environ.get("INTERVAL_SECONDS", "5"))


def main():
    while True:
        try:
            response = requests.get(URL_ALVO, timeout=5)
            response.raise_for_status()
            now = datetime.now(UTC).isoformat().replace("+00:00", "Z")
            print(f"[{now}] OK: {response.text}")
        except Exception as exc:  # noqa: BLE001
            now = datetime.now(UTC).isoformat().replace("+00:00", "Z")
            print(f"[{now}] ERROR: {exc}")
        time.sleep(INTERVALO_SEGUNDOS)


if __name__ == "__main__":
    main()
