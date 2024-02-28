from .qt_designer.add_constraint import Ui_AddConstraintDlg
from PyQt5.QtWidgets import QDialog
import logging
from src.app.dtos import ConstraintLayerInputDTO, ConstraintLayerFormOptionsDTO
from src.app.postgres_repo import PostGresRepo
from PyQt5.QtCore import QDate
from src.db.enums import GeomType


class AddConstraintDlg(QDialog,  # type: ignore
                       Ui_AddConstraintDlg):
    def __init__(self, repo: PostGresRepo) -> None:
        logging.info("Initiating add constraint dlg")
        super().__init__()
        self.repo = repo
        self.setupUi(self)  # type: ignore
        self.update_combo_boxes()
        self.set_date_edits()
        self.buttonBox.accepted.connect(self.add_layer)
        self.DevelopmentConstraintCB.currentIndexChanged.connect(
            self.update_layer_name)
        self.AdministrativeAreaCB.currentIndexChanged.connect(
            self.update_layer_name
        )
        self.form_options: None | ConstraintLayerFormOptionsDTO = None

    def update_combo_boxes(self) -> None:
        self.form_options = self.repo.get_constraint_layer_form_options()
        for area in self.form_options.administrative_areas.values():
            self.AdministrativeAreaCB.addItem(area.name, area.id)

        for id, name in self.form_options.data_licenses.items():
            self.LicenseCB.addItem(name, id)

        for id, name in self.form_options.data_publishers.items():
            self.DataPublisherCB.addItem(name, id)

        for constraint in self.form_options.development_constraints.values():
            self.DevelopmentConstraintCB.addItem(
                constraint.name, constraint.id)

        for value in GeomType.__members__:
            self.GeomTypeCB.addItem(value)

    def set_date_edits(self) -> None:
        self.NextUpdateDE.setDate(QDate.currentDate())
        self.AccessedCreatedDE.setDate(QDate.currentDate())
        self.LastUpdatedDE.setDate(QDate.currentDate())
        self.ExpiresDE.setDate(QDate.currentDate())

    def populate_input_dto(self) -> ConstraintLayerInputDTO:
        if not self.form_options:
            raise Exception
        return ConstraintLayerInputDTO(
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
            geom_type=GeomType[self.GeomTypeCB.currentText()]
        )

    def update_layer_name(self) -> None:
        self.LayerNameLE.setText(self.populate_input_dto().name())

    def add_layer(self) -> None:
        logging.info("submit button pressed")
        print(self.LayerNameLE.text(), type(self.LayerNameLE.text())),
        print(self.NotesTE.document().toPlainText()), type(
            self.NotesTE.document().toPlainText())
        input_dto = self.populate_input_dto()
        self.repo.add_constraint_layer(input_dto)
        logging.info(input_dto)
