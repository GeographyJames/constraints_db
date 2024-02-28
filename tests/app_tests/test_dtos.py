from src.app.dtos import (ConstraintLayerInputDTO,
                          DevelopmentConstraintOutputDTO,
                          AdministrativeAreaOutputDTO)
from datetime import date
from src.db.enums import GeomType


def test_should_retun_layer_name():
    layer = ConstraintLayerInputDTO(
        development_constraint=DevelopmentConstraintOutputDTO(
            1, "Site of Special Scientific Interest", "SSSI"),
        administrative_area=AdministrativeAreaOutputDTO(
            2, "Scotland", "SCO"
        ),
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
    assert layer.name() == "sco_sssi"
