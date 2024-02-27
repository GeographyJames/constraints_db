import attrs
from datetime import date


@attrs.define
class ConstraintLayerFormOptionsDTO:
    development_constraints: dict[int, str]
    administrative_areas: dict[int, str]
    data_publishers: dict[int, str]
    data_licenses: dict[int, str]


@attrs.define
class ConstraintLayerInputDTO:
    name: str
    development_constraint_id: int
    administrative_area_id: int
    data_publisher_id: int
    data_license_id: int
    data_source: str | None
    update_cycle: str | None
    data_accessed_or_created: date
    data_last_updated: date | None
    data_next_updated: date | None
    data_expires: date | None
    notes: str | None
    
