from src.app.dtos import (ConstraintLayerInputDTO,
                          DevelopmentConstraintOutputDTO,
                          AdministrativeAreaOutputDTO)
from datetime import date
from src.db.enums import GeomType


def test_should_retun_layer_name():
    administrative_area = AdministrativeAreaOutputDTO(
        2, "Scotland", "SCO")
    development_constraint = DevelopmentConstraintOutputDTO(
        id=1,
      name="Site of Special Scientific Interest",
      abbreviation="SSSI",
    table_name="SSSI")
    name = ConstraintLayerInputDTO.generate_name(
        administrative_area, development_constraint)
    layer = ConstraintLayerInputDTO(
        name=name,
        administrative_area=administrative_area,
        development_constraint=development_constraint,
        data_license_id=1,
        data_publisher_id=1,
        data_source=None,
        update_cycle=None,
        data_accessed_or_created=date.today(),
        data_last_updated=None,
        data_expires=None,
        data_next_updated=None,
        notes=None,
        geom_type=GeomType.MULTIPOLYGON)
    assert layer.name == "sco_SSSI"
