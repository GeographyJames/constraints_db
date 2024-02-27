from .qt_designer.main_window import Ui_mainWindow
from .add_constraint import AddConstraintDlg
from PyQt5.QtWidgets import QMainWindow
import logging
from src.app.postgres_repo import PostGresRepo
from src.db.sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path


class MainWindow(QMainWindow, # type: ignore
                 Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self) # type: ignore
        self.repo = PostGresRepo(engine(credentials_from_ini(Path("db_credentials.ini")), echo=False))


        # Toolbar actions
        self.actionAdd_New.triggered.connect(self.open_add_constraint_dlg)

    def open_add_constraint_dlg(self) -> None:
        logging.info("add constraint button clicked")
        dlg = AddConstraintDlg(repo=self.repo)
        dlg.exec()