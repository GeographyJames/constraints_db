from src.db import sqlalchemy_config
from pathlib import Path
from sqlalchemy import text
import pytest
from src.db.exceptions import CredentialsError

db_credentials_ini = Path("db_credentials.ini")


class TestCredentialsFromIni:

    def test_should_return_database_credentials(self) -> None:
        assert isinstance(sqlalchemy_config.credentials_from_ini(Path(
            "tests/test_data/test_db_credentials/test_db_credentials_correct.ini"),
            password="password"), sqlalchemy_config.DbCredentiails)

    def test_should_raise_credentials_error(self) -> None:
        with pytest.raises(CredentialsError):
            sqlalchemy_config.credentials_from_ini(
                Path("tests/db_tests/test_data/test_db_credentials/test_db_credentials_error.ini"))
        with pytest.raises(
                CredentialsError,
                match="Unable to locate credentials .ini file"):
            sqlalchemy_config.credentials_from_ini(Path("fake/path.ini"))


@pytest.mark.db
def test_should_return_database_connection() -> None:
    engine = sqlalchemy_config.engine(sqlalchemy_config.credentials_from_ini(
        db_credentials_ini,))
    with engine.connect() as conn:
        assert conn.scalar(text("SELECT 'hello world'")) == "hello world"
