from .qt_designer.select_geom_type import Ui_SelectGeomTypeDlg
from PyQt5.QtWidgets import QDialog
from src.db.enums import GeomType
from src.app.dtos import ConstraintLayerInputDTO

class SelectGeomType(QDialog,  # type: ignore
                     Ui_SelectGeomTypeDlg):
    def __init__(self, input_dto: ConstraintLayerInputDTO) -> None:
        super().__init__()
        self.input_dto = input_dto
        self.setupUi(self)  # type: ignore
        self.GeometryTypeCB.addItems(
            [GeomType.MULTIPOLYGON, GeomType.MULTILINESTRING, GeomType.POINT])
        
    def accept(self) -> None:
        self.input_dto.geom_type=GeomType(self.GeometryTypeCB.currentText())
        super().accept()


