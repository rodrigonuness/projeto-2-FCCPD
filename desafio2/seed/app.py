import os
import sqlite3
from datetime import UTC, datetime

CAMINHO_BD = os.environ.get("DB_PATH", "/data/desafio2.db")
USUARIOS_EXEMPLO = (
    ("alice", "Alice Costa"),
    ("bruno", "Bruno Lima"),
    ("carla", "Carla Mendes"),
)


def popular_banco() -> None:
    os.makedirs(os.path.dirname(CAMINHO_BD), exist_ok=True)
    connection = sqlite3.connect(CAMINHO_BD)
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
    for username, full_name in USUARIOS_EXEMPLO:
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
    print(f"Seed concluído em {CAMINHO_BD}")


if __name__ == "__main__":
    popular_banco()
