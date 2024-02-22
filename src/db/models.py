from sqlalchemy import Identity, ForeignKey, MetaData, Table,  Column, Integer, Connection, DateTime, text
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import TEXT, JSONB, ENUM
from typing import Optional, List, Tuple
from datetime import datetime, date
from geoalchemy2 import WKBElement, Geometry
from .sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
from .enums import GeomType


class Base(DeclarativeBase):
    type_annotation_map = {
        str: TEXT
    }
    metadata_obj = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })


class DevelopmentConstraint(Base):
    """This defines the table of development constraints."""
    __tablename__ = "development_constraints"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    constraint_category_id: Mapped[int] = mapped_column(
        ForeignKey("constraint_categories.id"))
    name: Mapped[str] = mapped_column(unique=True)
    abbreviation: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    notes: Mapped[Optional[str]]
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())
    onshore_wind_priority_level_id: Mapped[int] = mapped_column(
        ForeignKey("priority_levels.id"))
    solar_priority_level_id: Mapped[int] = mapped_column(
        ForeignKey("priority_levels.id"))

    constraint_category: Mapped["ConstraintCategory"] = relationship(
        back_populates="development_constraints")
    onshore_wind_priority_level: Mapped["PriorityLevel"] = relationship(
        back_populates="onshore_wind_constraints")
    solar_priority_level: Mapped["PriorityLevel"] = relationship(
        back_populates="solar_constrints")
    constraint_layers: Mapped[List["ConstraintLayer"]] = relationship(
        back_populates="development_constraint")

    def __repr__(self) -> str:
        return f"<development constraint: {self.id}, {self.name}>"


class ConstraintCategory(Base):
    __tablename__ = "constraint_categories"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())

    development_constraints: Mapped[
        List["DevelopmentConstraint"]] = relationship(
        back_populates="constraint_category")

    def __repr__(self) -> str:
        return f"<constraint category: {self.id}, {self.name}>"


class PriorityLevel(Base):
    __tablename__ = "priority_levels"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())

    onshore_wind_constraints: Mapped[
        List["DevelopmentConstraint"]] = relationship(
        back_populates="onshore_wind_priority_level")
    solar_constraints: Mapped[List["DevelopmentConstraint"]] = relationship(
        back_populates="solar_priority_level")

    def __repr__(self) -> str:
        return f"<priority level: {self.id}, {self.name}>"


class DataPublisher(Base):
    __tablename__ = "data_publishers"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    abbreviation: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())

    constraint_layers: Mapped[List["ConstraintLayer"]] = relationship(
        back_populates="data_publisher")

    def __repr__(self) -> str:
        return f"<data publisher: {self.id}, {self.name}>"


class DataLicense(Base):
    __tablename__ = "data_licenses"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())

    constraint_layers: Mapped[List["ConstraintLayer"]] = relationship(
        back_populates="data_license")

    def __repr__(self) -> str:
        return f"<data licenses: {self.id}, {self.name}>"


class AdministrativeLevel(Base):
    __tablename__ = "administrative_levels"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    level: Mapped[int]
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())

    administrative_areas: Mapped[list["AdministrativeArea"]] = relationship(
        back_populates="administrative_levele")
    constraint_layers: Mapped[List["ConstraintLayer"]] = relationship(
        back_populates="administrative_level")

    def __repr__(self) -> str:
        return f"<admin level: {self.id}, {self.name}>"


class AdministrativeArea(Base):
    __tablename__ = "administrative_areas"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    parent_area_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("administrative_areas.id"))
    administrative_level_id: Mapped[int] = mapped_column(
        ForeignKey("administrative_levels.id"))
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())
    geom: Mapped[WKBElement] = mapped_column(
        Geometry(geometry_type="MULTIPOLYGON", srid=27700))

    administrative_level: Mapped["AdministrativeLevel"] = relationship(
        back_populates="administrative_areas")
    parent_area: Mapped["AdministrativeArea"] = relationship(
        back_populates="child_areas")
    child_areas: Mapped[List["AdministrativeArea"]
                        ] = relationship(back_populates="parent_area")
    constraint_layers: Mapped[List["ConstraintLayer"]] = relationship(
        back_populates="administrative_area")

    def __repr__(self) -> str:
        return f"<geographical_areas: {self.id}, {self.name}>"


class ConstraintLayer(Base):
    __tablename__ = "constraint_layers"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    development_constraint_id: Mapped[int] = mapped_column(
        ForeignKey("development_constraints.id"))
    administrative_level_id: Mapped[int] = mapped_column(
        ForeignKey("administrative_levels.id"))
    administrative_area_id: Mapped[int] = mapped_column(
        ForeignKey("administrative_areas.id"))
    data_publisher_id: Mapped[int] = mapped_column(
        ForeignKey("data_publishers.id"))
    data_license_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("data_licenses.id"))
    data_source: Mapped[Optional[str]]
    update_cycle: Mapped[Optional[str]]

    data_accessed_or_created: Mapped[Optional[date]]
    data_last_updated: Mapped[Optional[date]]
    data_next_updated: Mapped[Optional[date]]
    data_expires: Mapped[Optional[date]]
    notes: Mapped[Optional[str]]

    created: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[str] = mapped_column(server_default=func.current_user())
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now())
    last_updated_by: Mapped[str] = mapped_column(
        server_default=func.current_user())

    development_constraint: Mapped["DevelopmentConstraint"] = relationship(
        back_populates="constraint_layers")
    administrative_level: Mapped["AdministrativeLevel"] = relationship(
        back_populates="constraint_layers")
    administrative_area: Mapped["AdministrativeArea"] = relationship(
        back_populates="constraint_layers")
    data_publisher: Mapped["DataPublisher"] = relationship(
        back_populates="constraint_layers")
    data_license: Mapped["DataLicense"] = relationship(
        back_populates="constraint_layers")

    def __repr__(self) -> str:
        return f"<constraint layer: {self.id}, {self.name}>"


constraint_objects_table = Table(
    "constraint_objects",
    Base.metadata,

    Column("id", Integer, Identity()),
    Column("name", TEXT, nullable=False),
    Column("status", TEXT),
    Column("constraint_layer_id", Integer,  ForeignKey(
        "constraint_layers.id"), nullable=False,),
    Column("created", DateTime, server_default=func.now(), nullable=False),
    Column("created_by", TEXT, server_default=func.current_user(),
           nullable=False),
    Column("last_updated", DateTime, server_default=func.now(),
           nullable=False),
    Column("last_updated_by", TEXT, nullable=False,
           server_default=func.current_user()),
    Column("geom", Geometry(srid=27700), nullable=False,),
    postgresql_partition_by="LIST(GeometryType(geom))",
)


def create_prtitioned_tables(conn: Connection, parent_table: Table) -> None:
    """To my current knowledge, Alembic does not support table partitioning.
    Therefore to create the partitioned tables, run this function.
    """
    for geometry_type in GeomType:
        conn.execute(text(
            f"CREATE TABLE IF NOT EXISTS {parent_table}_{geometry_type} "
            f"  PARTITION OF {parent_table.name} "
            f"  FOR VALUES IN ('{geometry_type.name}') "
        ))


if __name__ == "__main__":
    with engine(credentials_from_ini(Path("db_credentials.ini")),
                echo=True).begin() as conn:
        create_prtitioned_tables(conn, constraint_objects_table)
