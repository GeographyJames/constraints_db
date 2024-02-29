from .sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
from sqlalchemy import Connection, text
from typing import List


def initialise_db(conn: Connection) -> None:
    pass


def initialise_db_entries(conn: Connection, files_to_load: List[Path]) -> None:
    """This will execute a list of .sql files."""
    for path in files_to_load:
        with open(Path("src/db/sql") / path, encoding="utf-8") as f:
            conn.execute(text(f.read()))


if __name__ == "__main__":
    files_to_load = [
                     Path("priority_levels.sql"),
                     Path("constraint_categories.sql"),
                     Path("data_licenses.sql"),
                     Path("data_publishers.sql"),
                     Path("development_constraints.sql"),
                     Path("administrative_areas.sql"),
                     Path("constraint_layers.sql")
                     ]

    with engine(credentials_from_ini(Path("db_credentials.ini")),
                echo=True).begin() as conn:
        initialise_db_entries(conn, files_to_load)
