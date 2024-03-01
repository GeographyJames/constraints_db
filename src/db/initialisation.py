from .sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
from sqlalchemy import Connection, text, Engine, select
from sqlalchemy.orm import Session
from typing import List
from .models import ConstraintLayer, create_constraint_layer_table
from slugify import slugify
import attrs
from .enums import GeomType


@attrs.define
class Table:
    schema: str
    name: str


tables = [Table("public", "development_constraints"),
          Table("public", "constraint_categories"),
          Table("public", "priority_levels"),
          Table("public", "data_publishers"),
          Table("public", "data_licenses"),
          Table("public", "administrative_areas"),
          Table("public", "constraint_layers"),
          Table("public", "constraint_objects"),
          ]

files_to_load = [Path("priority_levels.sql"),
                 Path("constraint_categories.sql"),
                 Path("data_licenses.sql"),
                 Path("data_publishers.sql"),
                 Path("development_constraints.sql"),
                 Path("administrative_areas.sql"),
                 Path("constraint_layers.sql")
                 ]


def initialise_db_entries(conn: Connection, files_to_load: List[Path]) -> None:
    """This will execute a list of .sql files."""
    for path in files_to_load:
        with open(Path("src/db/sql") / path, encoding="utf-8") as f:
            conn.execute(text(f.read()))


def set_constraint_layer_names(engine: Engine, layer_ids: List[int]) -> None:
    session = Session(engine)
    for id in layer_ids:
        layer=session.scalar(select(ConstraintLayer).where(ConstraintLayer.id==id))
        if layer:
            area = layer.administrative_area.abbreviation
            name = layer.development_constraint.name
            layer_name = slugify(f"{area}_{name}").replace("-", "_").lower()
            layer.name = layer_name
    session.commit()


def set_table_identity_sequence(engine: Engine, tables: List[Table]) -> None:
    with engine.begin() as conn:
        for table in tables:
            table_name = table.name
            conn.execute(text(
                f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), "
                f"coalesce(MAX(id), 1)) from {table_name}"
            ))


def initialise_constraints_tables(engine: Engine) -> None:
    with engine.connect() as conn:
        for layer in conn.execute(select(ConstraintLayer.name, ConstraintLayer.id)):
            print(layer.name, layer.id)
            stmts = create_constraint_layer_table(
                layer.name, GeomType.MULTIPOLYGON, layer.id)
            for stmt in stmts:
                conn.execute(text(stmt))
        conn.commit()


if __name__ == "__main__":
    eng = engine(credentials_from_ini(Path("db_credentials.ini")), echo=True)

    #with eng.begin() as conn:
    #    initialise_db_entries(conn, files_to_load)
    

    #set_constraint_layer_names(eng, [1,2,3,11,16,17])

    
    #set_table_identity_sequence(tables, eng)

    initialise_constraints_tables(eng)
