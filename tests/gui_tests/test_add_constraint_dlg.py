from src.gui.qt5.dlgs.add_constraint import AddConstraintDlg
from PyQt5.QtWidgets import QApplication
from src.app.postgres_repo import PostGresRepo
from src.db.sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
import pytest


class TestAddConstraintUI:

    app = QApplication([])

    @pytest.mark.db
    def test_ui(self):
        AddConstraintDlg(PostGresRepo(engine(credentials_from_ini(
            Path("db_credentials.ini")), echo=True), testing=True))
