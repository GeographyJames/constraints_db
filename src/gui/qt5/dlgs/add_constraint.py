from .qt_designer.add_constraint import Ui_AddConstraintDlg
from PyQt5.QtWidgets import QDialog, QMessageBox
from src.app.dtos import ConstraintLayerInputDTO, ConstraintLayerFormOptionsDTO
from src.app.postgres_repo import PostGresRepo
from PyQt5.QtCore import QDate
from src.db.enums import GeomType
from src.app.shapefile_processor import ShapefileProcessor
from pathlib import Path
from src.app.exceptions import ShapefileError


class AddConstraintDlg(QDialog,  # type: ignore
                       Ui_AddConstraintDlg):
    def __init__(self, repo: PostGresRepo) -> None:
        super().__init__()
        self.repo = repo
        self.setupUi(self)  # type: ignore
        self.form_options = self.repo.get_constraint_layer_form_options()
        self.update_combo_boxes()
        self.set_date_edits()
        self.DevelopmentConstraintCB.currentIndexChanged.connect(
            self.update_layer_name)
        self.AdministrativeAreaCB.currentIndexChanged.connect(
            self.update_layer_name
        )
        self.SelectShapefileQgsFileWidget.setDefaultRoot(
            r"C:\Users\jcampbell\Downloads")
        self.SelectShapefileQgsFileWidget.fileChanged.connect(
            self.file_changed)
        self.shapefile_processor: ShapefileProcessor | None = None

    def file_changed(self) -> None:
        try:
            self.shapefile_processor = ShapefileProcessor(
                Path(self.SelectShapefileQgsFileWidget.filePath()))
            file_info = self.shapefile_processor.shapefile_info()
        except ShapefileError as e:
            QMessageBox.information(
                self, "Shapefile Error", f"Error opening shapefile: {e}")
            return
        self.ShapefileInfoTE.setText(str(file_info))
        self.FeatureNameCB.clear()
        self.FeatureNameCB.addItems(file_info.fields)
        self.FeatureStatusCB.clear()
        self.FeatureStatusCB.addItem("NONE")
        self.FeatureStatusCB.addItems(file_info.fields)

    def update_combo_boxes(self) -> None:

        self.AdministrativeAreaCB.clear()
        for area in self.form_options.administrative_areas.values():
            self.AdministrativeAreaCB.addItem(
                f"{area.name} ({area.abbreviation})", area.id)

        self.LicenseCB.clear()
        for id, name in self.form_options.data_licenses.items():
            self.LicenseCB.addItem(name, id)

        self.DataPublisherCB.clear()
        for id, name in self.form_options.data_publishers.items():
            self.DataPublisherCB.addItem(name, id)

        self.DevelopmentConstraintCB.clear()
        for constraint in self.form_options.development_constraints.values():
            self.DevelopmentConstraintCB.addItem(
                constraint.name, constraint.id)

    def set_date_edits(self) -> None:
        self.NextUpdateDE.setDate(QDate.currentDate())
        self.AccessedCreatedDE.setDate(QDate.currentDate())
        self.LastUpdatedDE.setDate(QDate.currentDate())
        self.ExpiresDE.setDate(QDate.currentDate())

    def populate_input_dto(self) -> None | ConstraintLayerInputDTO:
        self.update_layer_name()
        if not self.shapefile_processor:
            QMessageBox.information(
                self, "Select Shapefile", "No Shapefile selected")
            return None
        if not self.form_options:
            raise Exception
        return ConstraintLayerInputDTO(
            name=self.LayerNameLE.text(),
            development_constraint=self.form_options.development_constraints[
                self.DevelopmentConstraintCB.currentData()],
            administrative_area=self.form_options.administrative_areas[
                self.AdministrativeAreaCB.currentData()],
            data_publisher_id=self.DataPublisherCB.currentData(),
            data_license_id=self.LicenseCB.currentData(),
            data_source=(self.SourceLE.text()
                         if self.SourceLE.text() else None),
            update_cycle=(self.UpdateCycleLE.text()
                          if self.UpdateCycleLE.text() else None),
            data_accessed_or_created=self.AccessedCreatedDE.date().toPyDate(),
            data_last_updated=(self.LastUpdatedDE.date().toPyDate(
            ) if self.LastUpdatedCB.isChecked() else None),
            data_next_updated=(self.NextUpdateDE.date().toPyDate(
            ) if self.NextUpdateCB.isChecked() else None),
            data_expires=(self.ExpiresDE.date().toPyDate()
                          if self.ExpiresCB.isChecked() else None),
            notes=(self.NotesTE.document().toPlainText()
                   if self.NotesTE.document().toPlainText() else None),
            geom_type=self.shapefile_processor.geometry_type(),
            constraint_objects=self.shapefile_processor.constraint_object_input_dto(
                name_field=self.FeatureNameCB.currentText(),
                status_field=(self.FeatureStatusCB.currentText()
                              if self.FeatureStatusCB.currentText() != "NONE" else None)
            )

        )

    def update_layer_name(self) -> None:
        if not self.form_options:
            raise Exception
        self.LayerNameLE.setText(ConstraintLayerInputDTO.generate_name(
            admin_area_abbreviation=self.form_options.administrative_areas[
                self.AdministrativeAreaCB.currentData()].abbreviation,
            table_name=self.form_options.development_constraints[
                self.DevelopmentConstraintCB.currentData()].table_name)
        )

    def accept(self) -> None:
        input_dto = self.populate_input_dto()

        if not input_dto:
            return

        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setWindowTitle("Add layer")
        msg.setText(
            f"Confirm details\n\n"
            f"layer name: {input_dto.name}\n"
            f"administrativ area: {input_dto.administrative_area.name}\n")
        result = msg.exec()

        if result != QMessageBox.Ok:
            return
        try:
            self.repo.add_constraint_layer(input_dto)
        except Exception as e:
            QMessageBox.information(
                self, "Error", f"Error adding data to database: {e}")
            return
        super().accept()


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    from src.app.postgres_repo import PostGresRepo
    from src.db.sqlalchemy_config import engine, credentials_from_ini
    from pathlib import Path

    if __name__ == "__main__":
        app = QApplication([])
        dlg = AddConstraintDlg(repo=PostGresRepo(
            engine(credentials_from_ini(Path("db_credentials.ini")),
                   echo=True), testing=True))
        dlg.show()
        dlg.SelectShapefileQgsFileWidget.setDefaultRoot(
            r"tests\test_data\test_shapefiles")
        exitcode = app.exec()
