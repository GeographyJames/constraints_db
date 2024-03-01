from .sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
from sqlalchemy import text, Connection, select
from sqlalchemy.orm import Session
from .models import (ConstraintLayer,
                     create_constraint_layer_table,
                     create_prtitioned_tables)
from slugify import slugify
import attrs
from .enums import GeomType


@attrs.define
class Table:
    schema: str
    name: str


tables = [
    Table("public", "constraint_categories"),
    Table("public", "priority_levels"),
    Table("public", "data_publishers"),
    Table("public", "data_licenses"),
    Table("public", "administrative_areas"),
    Table("public", "development_constraints"),
    Table("public", "constraint_objects"),
    Table("public", "constraint_layers"),
]

files_to_load = [Path("priority_levels.sql"),
                 Path("constraint_categories.sql"),
                 Path("data_licenses.sql"),
                 Path("data_publishers.sql"),
                 Path("development_constraints.sql"),
                 Path("administrative_areas.sql"),
                 Path("constraint_layers.sql")
                 ]


def grant_select(conn: Connection, tables: list[Table]) -> None:
    for table in tables:
        conn.execute(text(
            f"GRANT SELECT ON {table.schema}.{table.name} TO PUBLIC;"
        ))


def initialise_db_entries(conn: Connection, files_to_load: list[Path]) -> None:
    """This will execute a list of .sql files."""
    for path in files_to_load:
        with open(Path("src/db/sql") / path, encoding="utf-8") as f:
            conn.execute(text(f.read()))


"""
def set_constraint_layer_names(conn: Connection,
                               layer_ids: None | list[int] = None,
                               all: bool = False) -> None:
    session = Session(engine)
    if all:
        layer_ids = [row.id for row in conn.scalars(
            select(ConstraintLayer.id))]
    if not layer_ids:
        raise Exception("No ids provided")
    for id in layer_ids:
        layer = session.scalar(
            select(ConstraintLayer).where(ConstraintLayer.id == id))
        if layer:
            area = layer.administrative_area.abbreviation
            name = layer.development_constraint.name
            layer_name = slugify(f"{area}_{name}").replace("-", "_").lower()
            layer.name = layer_name
    session.commit()
"""


def set_table_identity_sequence(conn: Connection, tables: list[Table]) -> None:
    for table in tables:
        conn.execute(text(
            f"SELECT setval(pg_get_serial_sequence( "
            f"'{table.schema}.{table.name}', 'id'), "
            f"coalesce(MAX(id), 1)) from {table.schema}.{table.name}"
        ))


def initialise_constraints_tables(conn: Connection) -> None:
    conn.execute(text(
        "CREATE SCHEMA IF NOT EXISTS constraints; "
        "GRANT USAGE ON SCHEMA constraints TO PUBLIC;"
    ))
    for layer in conn.execute(select(ConstraintLayer.name,
                                     ConstraintLayer.id)):
        print(layer.name, layer.id)
        stmts = create_constraint_layer_table(
            layer.name, GeomType.MULTIPOLYGON, layer.id)
        for stmt in stmts:
            conn.execute(text(stmt))


if __name__ == "__main__":
    eng = engine(credentials_from_ini(Path("db_credentials.ini")), echo=True)

    with eng.connect() as conn:
        create_prtitioned_tables(conn)
        grant_select(conn, tables)
        initialise_db_entries(conn, files_to_load)
        # set_constraint_layer_names(conn, all=True)
        set_table_identity_sequence(conn, tables)
        initialise_constraints_tables(conn)
        conn.commit()
