import attrs



@attrs.define
class ConstraintLayerFormOptionsDTO:
    development_constraints: dict[int, str]
    administrative_areas: dict[int, str]
    data_publishers: dict[int, str]
    data_licenses: dict[int, str]