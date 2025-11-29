import os
import sqlite3
from pprint import pprint

CAMINHO_BD = os.environ.get("DB_PATH", "/data/desafio2.db")


def listar_usuarios() -> None:
    connection = sqlite3.connect(CAMINHO_BD)
    cursor = connection.cursor()
    cursor.execute("SELECT username, full_name, created_at FROM users ORDER BY username")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    if not rows:
        print("Nenhum usuário encontrado. Execute o seed primeiro.")
    else:
        print("Usuários persistidos:")
        pprint(rows)


if __name__ == "__main__":
    listar_usuarios()
