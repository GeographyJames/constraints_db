from pathlib import Path
import attrs
from sqlalchemy import URL, create_engine, Engine
import configparser

@attrs.define
class DbCredentiails:
    username: str
    password: str
    host: str
    database: str
    drivername: str = "postgresql"

def credentials_from_ini(db_credentials: Path) -> DbCredentiails:
    config = configparser.ConfigParser()
    config.read(db_credentials)
    return DbCredentiails(**dict(config.items(section="DATABASE")))


def url_obj(db_credentials: DbCredentiails):
    return URL.create(**attrs.asdict(db_credentials))


def engine(db_credentials: DbCredentiails, echo: bool=False) -> Engine:
    return create_engine(url_obj(db_credentials), echo=echo)


