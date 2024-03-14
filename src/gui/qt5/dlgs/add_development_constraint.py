from .qt_designer.add_development_constraint import Ui_AddDevelopmentConstraintDlg
from PyQt5.QtWidgets import QDialog, QMessageBox
from src.app.postgres_repo import PostGresRepo
from src.app.dtos import DevelopmentConstraintInputDTO


class AddDevelopmentConstraint(QDialog, # type: ignore
                               Ui_AddDevelopmentConstraintDlg):
    def __init__(self, repo: PostGresRepo) -> None:
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.repo = repo
        self.update_combo_boxes()

    def update_combo_boxes(self) -> None:
        form_options = self.repo.get_development_constraint_form_options()
        for id, name in form_options.categories.items():
            self.CategoryCB.addItem(name, id)

        for id, name in form_options.priority_levels.items():
            self.BatteryPriorityLevelCB.addItem(name, id)
            self.OnshoreWindPriorityLevelCB.addItem(name, id)
            self.SolarPriorityLevelCB.addItem(name, id)

    def populate_input_dto(self) -> DevelopmentConstraintInputDTO:
        return DevelopmentConstraintInputDTO(
            name=self.NameLE.text(),
            abbreviation=(self.AbbreviationLE.text() if self.AbbreviationLE.text() else None),
            table_name=(self.TableNameLE.text() if self.TableNameLE.text() else self.NameLE.text()),
            category_id=self.CategoryCB.currentData(),
            onshore_wind_priority_level_id=self.OnshoreWindPriorityLevelCB.currentData(),
            solar_priority_level_id=self.SolarPriorityLevelCB.currentData(),
            battery_priority_level_id=self.BatteryPriorityLevelCB.currentData(),
            description=(self.DescriptionTE.document().toPlainText() if self.DescriptionTE.document().toPlainText() else None),
            notes=(self.NotesTE.documen().toPlainText() if self.NotesTE.document().toPlainText() else None))
    
    def accept(self) -> None:
        if not self.NameLE.text():
            msg = QMessageBox.information(self, "Name required", "Please include a name")
            return
        try:
            self.repo.add_development_constraint(self.populate_input_dto())
        except Exception as e:
            msg = QMessageBox.information(self, "Error", f"Error adding constraint: {e}")
            return
        super().accept()
        


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    from src.db.sqlalchemy_config import engine, credentials_from_ini
    from pathlib import Path
    app = QApplication([])
    
    dlg = AddDevelopmentConstraint(repo=PostGresRepo(engine(credentials_from_ini(Path("db_credentials.ini")))))
    dlg.show()
    exitcode = app.exec()