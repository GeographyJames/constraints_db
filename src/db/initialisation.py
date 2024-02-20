from .sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
from sqlalchemy import Connection, text

files_to_load = [Path("development_constraints.sql")]


def initialise_db_entries(conn: Connection):
    for path in files_to_load:
        with open(Path("src/db/sql") / path, encoding="utf-8") as f:
            conn.execute(text(f.read()))


if __name__ == "__main__":
    with engine(credentials_from_ini(Path("db_credentials.ini")),
                echo=True).begin() as conn:
        initialise_db_entries(conn)
