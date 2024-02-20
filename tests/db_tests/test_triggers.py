from pathlib import Path
from src.db import triggers
from src.db.sqlalchemy_config import engine, credentials_from_ini
import pytest

db_credentials_ini = Path("db_credentials.ini")


@pytest.mark.db
def test_trigger_function() -> None:
    with engine(credentials_from_ini(
            db_credentials_ini), echo=True).connect() as conn:
        triggers.create_triggers(conn, triggers.tables)
