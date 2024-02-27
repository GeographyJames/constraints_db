from .qt_designer.add_constraint import Ui_AddConstraintDlg
from PyQt5.QtWidgets import QDialog
import logging
from src.app.dtos import ConstraintLayerInputDTO
from src.app.postgres_repo import PostGresRepo


class AddConstraintDlg(QDialog, # type: ignore
                       Ui_AddConstraintDlg):
    def __init__(self, repo: PostGresRepo) -> None:
        logging.info("Initiating add constraint dlg")        
        super().__init__()
        self.repo = repo
        self.setupUi(self) # type: ignore
        self.update_spin_boxes()
        self.buttonBox.accepted.connect(self.add_layer)

    def update_spin_boxes(self) -> None:
        form_options = self.repo.get_constraint_layer_form_options()
        for key, value in form_options.administrative_areas.items():
            self.AdministrativeAreaCB.addItem(value, key)
        for key, value in form_options.data_licenses.items():
            self.LicenseCB.addItem(value, key)
        for key, value in form_options.data_publishers.items():
            self.DataPublisherCB.addItem(value, key)
        for key, value in form_options.development_constraints.items():
            self.DevelopmentConstraintCB.addItem(value, key)

    def populate_input_dto(self) -> ConstraintLayerInputDTO:
        return ConstraintLayerInputDTO(
            name=self.LayerNameLE.text(),
            development_constraint_id=self.DevelopmentConstraintCB.currentData(),
            administrative_area_id=self.AdministrativeAreaCB.currentData(),
            data_publisher_id=self.DataPublisherCB.currentData(),
            data_license_id=self.LicenseCB.currentData(),
            data_source=self.SourceLE.text(),
            update_cycle=self.UpdateCycleLE.text(),
            data_accessed_or_created=self.AccessedCreatedDE.date().toPyDate(),
            data_last_updated=self.LastUpdatedDE.date().toPyDate(),
            data_next_updated=self.NextUpdateDE.date().toPyDate(),
            data_expires=self.ExpiresDE.date().toPyDate(),
            notes=self.NotesTE.document().toPlainText()
            )

    def add_layer(self) -> None:
        logging.info("submit button pressed")
        print(self.LayerNameLE.text(), type(self.LayerNameLE.text())),
        print(self.NotesTE.document().toPlainText()), type(self.NotesTE.document().toPlainText())
        input_dto = self.populate_input_dto()




