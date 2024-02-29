import attrs
from datetime import date
from slugify import slugify
from src.db.enums import GeomType


@attrs.define
class DevelopmentConstraintOutputDTO:
    id: int
    name: str
    abbreviation: str | None


@attrs.define
class AdministrativeAreaOutputDTO:
    id: int
    name: str
    abbreviation: str | None


@attrs.define
class ConstraintLayerFormOptionsDTO:
    development_constraints: dict[int, DevelopmentConstraintOutputDTO]
    administrative_areas: dict[int, AdministrativeAreaOutputDTO]
    data_publishers: dict[int, str]
    data_licenses: dict[int, str]


@attrs.define
class ConstraintLayerInputDTO:
    name: str
    development_constraint: DevelopmentConstraintOutputDTO
    administrative_area: AdministrativeAreaOutputDTO
    data_publisher_id: int
    data_license_id: int
    data_source: str | None
    update_cycle: str | None
    data_accessed_or_created: date
    data_last_updated: date | None
    data_next_updated: date | None
    data_expires: date | None
    notes: str | None
    geom_type: GeomType

    def generate_name(self) -> str:
        return slugify(f"{self.administrative_area.abbreviation}-{self.development_constraint.name}").replace("-", "_")
