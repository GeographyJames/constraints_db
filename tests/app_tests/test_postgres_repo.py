from src.app.postgres_repo import PostGresRepo
from src.db.sqlalchemy_config import engine, credentials_from_ini
import pytest
from pathlib import Path


@pytest.mark.db
def test_postgres_repo():
    repo = PostGresRepo(engine=engine(
        credentials_from_ini(Path("db_credentials.ini")), echo=True))
    dto = repo.get_constraint_layer_info()
    print(dto)

if __name__ == "__main__":
    test_postgres_repo()