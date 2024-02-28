import enum


class GeomType(enum.StrEnum):
    MULTIPOLYGON = enum.auto()
    MULTILINESTRING = enum.auto()
    POINT = enum.auto()
