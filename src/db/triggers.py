from sqlalchemy import DDL, Engine
from .sqlalchemy_config import engine, credentials_from_ini
import pathlib

tables = [("public", "development_constraints"),
          ("public", "constriaint_categories")]


def create_triggers(engine: Engine) -> None:
    with engine.connect() as conn:
        for (schema, table) in tables:
            func = DDL(
                f"CREATE OR REPLACE FUNCTION {schema}.{table}_update() "
                "RETURNS trigger as $$ "
                "BEGIN "
                "NEW.last_update := current_timestamp; "
                "NEW.last_update_by := current_user; "
                "RETURN NEW; "
                "END; "
                "$$ LANGUAGE plpgsql;"
            )

            trigger = DDL(
                f"CREATE OR REPLACE TRIGGER {
                    table}_update BEFORE UPDATE ON {table} "
                f"FOR EACH ROW EXECUTE FUNCTION {table}_update();"
            )
            conn.execute(func)
            conn.execute(trigger)
            conn.commit()


if __name__ == "__main__":
    create_triggers(engine(credentials_from_ini(
        pathlib.Path("db_credentials.ini")), echo=True))
