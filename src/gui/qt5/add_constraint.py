from PyQt5.QtWidgets import QApplication
from .dlgs.add_constraint import AddConstraintDlg
import logging
from src.app.postgres_repo import PostGresRepo
from src.db.sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = QApplication([])
    dlg = AddConstraintDlg(repo=PostGresRepo(
        engine(credentials_from_ini(Path("db_credentials.ini")), echo=True)))
    dlg.show()
    exitcode = app.exec()
