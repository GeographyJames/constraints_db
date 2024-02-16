from src.db import sqlalchemy_config
from pathlib import Path
from sqlalchemy import text
import pytest

db_credentials_ini = Path("db_credentials.ini")

@pytest.mark.db
def test_should_return_database_credentials_from_ini() -> None:
    assert db_credentials_ini.is_file()
    assert isinstance(sqlalchemy_config.credentials_from_ini(db_credentials_ini), sqlalchemy_config.DbCredentiails)


@pytest.mark.db
def test_should_return_database_connection() -> None:
    engine = sqlalchemy_config.engine(sqlalchemy_config.credentials_from_ini(db_credentials_ini), echo=True)
    with engine.connect() as conn:
        assert conn.scalar(text("SELECT 'hello world'")) == "hello world"


def test_fixturs(my_fixture) -> None:
    assert my_fixture == "some stuff"
