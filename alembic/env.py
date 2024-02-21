from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context
from geoalchemy2 import alembic_helpers

from src.db import sqlalchemy_config, models

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

target_metadata = models.Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = sqlalchemy_config.url_obj(
        sqlalchemy_config.credentials_from_ini(Path("db_credentials.ini"))
    ).render_as_string()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def include_name(name, type_, parent_names):
    if type_ == "table":
        return name in target_metadata.tables
    else:
        return True


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(sqlalchemy_config.url_obj(
        sqlalchemy_config.credentials_from_ini(Path("db_credentials.ini"))),
        poolclass=pool.NullPool,
        echo=True)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_server_default=True,
            include_name=include_name,
            render_item=alembic_helpers.render_item,
            include_object=alembic_helpers.include_object,
            process_revision_directives=alembic_helpers.writer
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
