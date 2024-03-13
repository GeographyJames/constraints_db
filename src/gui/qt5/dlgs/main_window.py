from .qt_designer.main_window import Ui_mainWindow
from .add_constraint import AddConstraintDlg
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialogButtonBox, QMessageBox, QDialog
import logging
from src.app.postgres_repo import PostGresRepo
from src.db.sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
from src.app.dtos import ConstraintLayerInfoDTO
import attrs


class MainWindow(QMainWindow,  # type: ignore
                 Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.repo = PostGresRepo(engine(credentials_from_ini(
            Path("db_credentials.ini")), echo=False), testing=False)
        self.RefreshPB.clicked.connect(self.update_table)
        # Toolbar actions
        self.actionAdd_New.triggered.connect(self.open_add_constraint_dlg)
        self.update_table()

    def update_table(self) -> None:
        field_names = [field.name for field in attrs.fields(ConstraintLayerInfoDTO)] 
        table_info = self.repo.get_constraint_layer_info()
        self.ConstraintsTW.setColumnCount(len(field_names))
        self.ConstraintsTW.setRowCount(len(table_info))

        for column, field_name in enumerate(field_names):
            self.ConstraintsTW.setHorizontalHeaderItem(
                column, QTableWidgetItem(field_name))

        for row_number, row in enumerate(table_info):
            for column, field_name in enumerate(field_names):
                if getattr(row, field_name):
                    self.ConstraintsTW.setItem(
                        row_number, column, QTableWidgetItem(str(getattr(row, field_name))))
        self.ConstraintsTW.resizeColumnsToContents()

    def open_add_constraint_dlg(self) -> None:
        dlg = AddConstraintDlg(repo=self.repo)
        result = dlg.exec()
        if result == QDialog.Accepted:
            self.update_table()
            QMessageBox.information(
                self, "Layer Added", "layer added successfully")
