import os
import sqlite3
from datetime import UTC, datetime

DB_PATH = os.environ.get("DB_PATH", "/data/desafio2.db")
SAMPLE_USERS = (
    ("alice", "Alice Costa"),
    ("bruno", "Bruno Lima"),
    ("carla", "Carla Mendes"),
)


def seed_database() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    for username, full_name in SAMPLE_USERS:
        cursor.execute(
            """
            INSERT INTO users (username, full_name, created_at)
            VALUES (?, ?, ?)
            ON CONFLICT(username) DO NOTHING
            """,
            (
                username,
                full_name,
                datetime.now(UTC).isoformat().replace("+00:00", "Z"),
            ),
        )
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Seed concluído em {DB_PATH}")


if __name__ == "__main__":
    seed_database()
