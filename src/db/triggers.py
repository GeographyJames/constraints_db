from sqlalchemy import DDL, Connection
from .sqlalchemy_config import engine, credentials_from_ini
import pathlib
from typing import List
from .initialisation import Table





def create_triggers(conn: Connection, tables: List[Table]) -> None:
    """Function to create database triggers to update database tables with
    current time and database user when updating a table row."""
    for table in tables:
        func = DDL(
            f"CREATE OR REPLACE FUNCTION "
            f"{table.schema}.{table.name}_update() "
            "RETURNS trigger as $$ "
            "BEGIN "
            "NEW.last_update := current_timestamp; "
            "NEW.last_update_by := current_user; "
            "RETURN NEW; "
            "END; "
            "$$ LANGUAGE plpgsql;"
        )

        trigger = DDL(
            f"CREATE OR REPLACE TRIGGER "
            f"{table.name}_update BEFORE UPDATE ON "
            f"{table.schema}.{table.name} "
            f"FOR EACH ROW EXECUTE FUNCTION "
            f"{table.name}_update();"
        )
        conn.execute(func)
        conn.execute(trigger)


if __name__ == "__main__":
    from .initialisation import tables
    with engine(credentials_from_ini(
            pathlib.Path("db_credentials.ini")), echo=True).begin() as conn:
        create_triggers(conn, tables)
