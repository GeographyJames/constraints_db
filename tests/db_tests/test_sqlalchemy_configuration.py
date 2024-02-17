from src.db import sqlalchemy_config
from pathlib import Path
from sqlalchemy import text
import pytest
from src.db.exceptions import DatabaseError
import os

db_credentials_ini = Path("db_credentials.ini")

def test_should_return_database_credentials_from_ini() -> None:
    db_credentials_ini = Path("tests/db_tests/test_data/test_db_credentials1.ini")
    assert db_credentials_ini.is_file()
    assert isinstance(sqlalchemy_config.credentials_from_ini(db_credentials_ini), sqlalchemy_config.DbCredentiails)


def test_credentials_from_ini_should_raise_database_error() -> None:
    db_credentials_ini = Path("tests/db_tests/test_data/test_db_credentials2.ini")
    assert db_credentials_ini.is_file()
    with pytest.raises(DatabaseError) as e_info:
        sqlalchemy_config.credentials_from_ini(db_credentials_ini)


@pytest.mark.db
def test_should_return_database_connection() -> None:
    engine = sqlalchemy_config.engine(sqlalchemy_config.credentials_from_ini(
        db_credentials_ini, os.environ.get("POSTGRESQL")))
    with engine.connect() as conn:
        assert conn.scalar(text("SELECT 'hello world'")) == "hello world"


def test_fixturs(my_fixture) -> None:
    assert my_fixture == "some stuff"
