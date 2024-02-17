from pathlib import Path
import attrs
from sqlalchemy import URL, create_engine, Engine
import configparser
import os
import logging
from .exceptions import DatabaseError


@attrs.define
class DbCredentiails:
    username: str
    password: str
    host: str
    database: str
    drivername: str = "postgresql"

def credentials_from_ini(db_credentials: Path, password: str = None) -> DbCredentiails:
    config = configparser.ConfigParser()
    config.read(db_credentials)
    db_dict = dict(config.items(section="DATABASE"))
    if "password" not in db_dict.keys():
        db_dict["password"] = password
    try:
        return DbCredentiails(**db_dict)
    except TypeError as e:
        raise DatabaseError(e)


def url_obj(db_credentials: DbCredentiails):
    return URL.create(**attrs.asdict(db_credentials))


def engine(db_credentials: DbCredentiails, echo: bool=False) -> Engine:
    return create_engine(url_obj(db_credentials), echo=echo)


