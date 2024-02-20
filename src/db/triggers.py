from sqlalchemy import DDL, Engine
from .sqlalchemy_config import engine, credentials_from_ini
import pathlib
from typing import List
import attrs


@attrs.define
class Table:
    schema: str
    name: str


tables = [Table("public", "development_constraints"),
          Table("public", "constriaint_categories")]


def create_triggers(engine: Engine, tables: List[Table]) -> None:
    """Function to create database triggers to update databas tables with"""
    """current time and database user when updating a table row."""
    with engine.connect() as conn:
        for table in tables:
            func = DDL(
                f"CREATE OR REPLACE FUNCTION {
                    table.schema}.{table.name}_update() "
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
                f"{table}_update BEFORE UPDATE ON {table.schema}.{table.name} "
                f"FOR EACH ROW EXECUTE FUNCTION {
                    table.schema}.{table.name}_update();"
            )
            conn.execute(func)
            conn.execute(trigger)
            conn.commit()


if __name__ == "__main__":
    create_triggers(engine(credentials_from_ini(
        pathlib.Path("db_credentials.ini")), echo=True), tables)
