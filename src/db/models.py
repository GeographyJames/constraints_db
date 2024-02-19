from sqlalchemy import Identity, ForeignKey, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import TEXT
from typing import Optional

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
    __tablename__ = "development_constraints"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    constraint_category_id: Mapped[int] = mapped_column(ForeignKey("constraint_categories.id"))
    name: Mapped[str] = mapped_column(unique=True)
    abbreviation: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    notes: Mapped[Optional[str]]

    constraint_category: Mapped["ConstraintCategory"] = relationship(back_populates="development_constraints")


class ConstraintCategory(Base):
    __tablename__ = "constraint_categories"
    
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]

    constraint_categories: Mapped["DevelopmentConstraint"] = relationship(back_populates="constraint_category")