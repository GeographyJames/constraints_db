import attrs
from datetime import date
from slugify import slugify
from src.db.enums import GeomType
import datetime


@attrs.define
class DevelopmentConstraintOutputDTO:
    id: int
    name: str
    table_name: str
    abbreviation: str | None


@attrs.define
class AdministrativeAreaOutputDTO:
    id: int
    name: str
    abbreviation: str


@attrs.define
class ConstraintLayerFormOptionsDTO:
    development_constraints: dict[int, DevelopmentConstraintOutputDTO]
    administrative_areas: dict[int, AdministrativeAreaOutputDTO]
    data_publishers: dict[int, str]
    data_licenses: dict[int, str]


@attrs.define
class ConstraintObjectInputDTO:
    name: str
    status: None|str
    geom: str


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
    geom_type: GeomType | None
    constraint_objects: None|list[ConstraintObjectInputDTO]

    @staticmethod
    def generate_name(admin_area_abbreviation: str, table_name: str) -> str:
        return slugify(f"{admin_area_abbreviation}-"
                       f"{table_name}"
                       ).replace("-", "_")


@attrs.define
class ShapfileInfoDTO:
    fields: list[str]
    feature_count: int
    geom_type: str

    def __repr__(self) -> str:
        return (
            f"feature count: {self.feature_count}\n"
            f"geometry type: {self.geom_type}\n"
            f"fields: {(", ").join(self.fields)}"
        )


@attrs.define
class ConstraintLayerInfoDTO:
    id: int
    layer_name: str
    constraint: str
    category: str
    objects: int
    wind_priority: int
    solar_priority: int
    battery_priority: int
    area: str
    publisher: str
    license: None|str
    update_cycle: None|str
    accessed_or_created: str
    last_updated: None|str
    next_updated: None|str
    expires: None|str
    layer_notes: None|str
    constraint_notes: None | str
    source: None|str
    created: str
    created_by: str


@attrs.define
class DevelopmentConstraintFormOptions:
    categories: dict[int, str]
    priority_levels: dict[int, str]

@attrs.define
class DevelopmentConstraintInputDTO:
    name: str
    abbreviation: str
    table_name: str
    category_id : int
    onshore_wind_priority_level_id: int
    solar_priority_level_id: int
    battery_priority_level_id: int
    description: None | str
    notes: None | str
