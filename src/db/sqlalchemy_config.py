from pathlib import Path
import attrs
from sqlalchemy import URL, create_engine, Engine
import configparser
from .exceptions import CredentialsError
import os


@attrs.define
class DbCredentiails:
    username: str
    password: str
    host: str
    database: str
    drivername: str = "postgresql"


def credentials_from_ini(
        db_credentials: Path, password: str | None = None) -> DbCredentiails:
    """Builds database credentials from an ini file."""

    if not db_credentials.is_file():
        raise CredentialsError(
            f"Unable to locate credentials .ini file ({
                db_credentials}). Check file path is valid file.")

    config = configparser.ConfigParser()
    config.read(db_credentials)
    try:
        db_dict = dict(config.items(section="DATABASE"))
    except configparser.NoSectionError as e:
        raise CredentialsError(
            f"Error with database credentials .ini file: {e}")
    if "password" not in db_dict.keys():
        if not password:
            postgres_env_varialbl_name = "POSTGRESQL"
            password = os.environ.get(postgres_env_varialbl_name)
        if not password:
            raise CredentialsError(
                f"No password provided. No environment variable set for "
                f"{postgres_env_varialbl_name}.")
        db_dict["password"] = password
    try:
        return DbCredentiails(**db_dict)
    except TypeError as e:
        raise CredentialsError(f"Error with database credentials: {e}")


def url_obj(db_credentials: DbCredentiails) -> URL:
    return URL.create(**attrs.asdict(db_credentials))


def engine(db_credentials: DbCredentiails, echo: bool = False) -> Engine:
    return create_engine(url_obj(db_credentials), echo=echo)
