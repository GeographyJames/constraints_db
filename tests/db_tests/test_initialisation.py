from src.db.initialisation import set_constraint_layer_names
from src.db.sqlalchemy_config import *
from pathlib import Path
import pytest

engine = engine(credentials_from_ini(Path(f"db_credentials.ini")))


@pytest.mark.db
def test_initialise_constraints_tables():
    set_constraint_layer_names(engine)