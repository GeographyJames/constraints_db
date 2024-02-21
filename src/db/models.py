from sqlalchemy import Identity, ForeignKey, MetaData
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import TEXT
from typing import Optional, List
from datetime import datetime
from geoalchemy2 import WKBElement, Geometry


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

    def __repr__(self) -> str:
        return f"<geographical_areas: {self.id}, {self.name}>"
