import enum


class GeomType(enum.StrEnum):
    LINESTRING = enum.auto()
    POINT = enum.auto()
    MULTIPOLYGON = enum.auto()
