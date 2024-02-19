from sqlalchemy import MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column




class Base(DeclarativeBase):
    pass

class Test(Base):
    __tablename__ = "test"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


if __name__ == "__main__":
    print("Running models file as main.")
    from src.db.sqlalchemy_config import engine, credentials_from_ini
    from pathlib import Path

    
    Base.metadata.create_all(engine(credentials_from_ini(Path("db_credentials.ini")), echo=True))