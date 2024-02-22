import enum


class GeomType(enum.StrEnum):
    MULTILINESTRING = enum.auto()
    POINT = enum.auto()
    MULTIPOLYGON = enum.auto()
