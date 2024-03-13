from .dtos import (ConstraintLayerFormOptionsDTO,
                   DevelopmentConstraintOutputDTO,
                   AdministrativeAreaOutputDTO,
                   ConstraintLayerInputDTO,
                   ConstraintObjectInputDTO,
                   ConstraintLayerInfoDTO)
from sqlalchemy import Engine, select, text, insert, Connection, func
from src.db.models import (DevelopmentConstraint,
                           AdministrativeArea,
                           DataPublisher,
                           DataLicense,
                           create_constraint_layer_table,
                           ConstraintLayer,
                           constraint_objects_table
                           )
from sqlalchemy.engine import CursorResult
from sqlalchemy.orm import Session
from typing import Any
from src.db.enums import GeomType
import attrs
import datetime


class PostGresRepo:
    def __init__(self, engine: Engine, testing: bool = False) -> None:
        self.engine = engine
        self.testing = testing

    def _to_dict(self, result: CursorResult[Any]) -> dict[int, str]:
        return {row.id: row.name for row in result.all()}

    def get_constraint_layer_form_options(
            self) -> ConstraintLayerFormOptionsDTO:
        with self.engine.connect() as conn:
            result = ConstraintLayerFormOptionsDTO(
                development_constraints={
                    row.id: DevelopmentConstraintOutputDTO(
                        id=row.id,
                        name=row.name,
                        table_name=row.table_name,
                        abbreviation=row.abbreviation) for row in conn.execute(
                        select(DevelopmentConstraint.id,
                               DevelopmentConstraint.name,
                               DevelopmentConstraint.table_name,
                               DevelopmentConstraint.abbreviation).order_by(
                                   DevelopmentConstraint.name))},
                administrative_areas={
                    row.id: AdministrativeAreaOutputDTO(
                        id=row.id,
                        name=row.name,
                        abbreviation=row.abbreviation) for row in conn.execute(
                            select(AdministrativeArea.id,
                                   AdministrativeArea.name,
                                   AdministrativeArea.abbreviation))},
                data_publishers=self._to_dict(conn.execute(select(
                    DataPublisher.id, DataPublisher.name).order_by(
                        DataPublisher.name))),
                data_licenses=self._to_dict(conn.execute(select(
                    DataLicense.id, DataLicense.name).order_by(DataLicense.name)))
            )
        return result

    def add_constraint_layer(self, layer: ConstraintLayerInputDTO) -> None:
        layer_name = layer.name
        sql_layer = ConstraintLayer(
            name=layer_name,
            development_constraint_id=layer.development_constraint.id,
            administrative_area_id=layer.administrative_area.id,
            data_publisher_id=layer.data_publisher_id,
            data_accessed_or_created=layer.data_accessed_or_created,
            data_license_id=layer.data_license_id,
            data_source=layer.data_source,
            update_cycle=layer.update_cycle,
            data_last_updated=layer.data_last_updated,
            data_next_updated=layer.data_next_updated,
            data_expires=layer.data_expires,
            notes=layer.notes

        )
        if layer.geom_type in (GeomType.MULTILINESTRING, GeomType.LINESTRING):
            geom = GeomType.MULTILINESTRING
        elif layer.geom_type in (GeomType.POLYGON, GeomType.MULTIPOLYGON):
            geom = GeomType.MULTIPOLYGON
        else:
            geom = layer.geom_type

        with Session(self.engine) as session:
            session.add(sql_layer)
            if not self.testing:
                session.commit()
                for stmt in create_constraint_layer_table(
                        constraint_layer_name=layer_name,
                        geometry_type=geom,
                        constraint_layer_id=sql_layer.id):
                    session.execute(text(stmt))
                self.add_constraint_object(
                    session, layer, sql_layer.id)
                session.commit()

    def add_constraint_object(self, session: Session, layer: ConstraintLayerInputDTO, layer_id: int) -> None:
        for dto in layer.constraint_objects:
            stmt = text(
                "INSERT INTO constraint_objects (name, status, constraint_layer_id, geom) "
                "VALUES (:name, :status, "
                ":id, ST_Multi(:geom)) "
            ).bindparams(name=dto.name, status=dto.status, id=layer_id, geom=dto.geom)
            session.execute(stmt)

    def get_constraint_layer_info(self) -> list[ConstraintLayerInfoDTO]:
        result = []
        stmt = select(constraint_objects_table.c.constraint_layer_id, func.count(
            constraint_objects_table.c.id).label("count")).group_by(constraint_objects_table.c.constraint_layer_id)
        subq = stmt.subquery() 

        with Session(self.engine) as session:
            session.execute(stmt)
            for row in session.execute(select(ConstraintLayer, subq.c.count).join(subq, ConstraintLayer.id == subq.c.constraint_layer_id)).all():
                layer = row[0]
                count = row[1]
                result.append(ConstraintLayerInfoDTO(
                    id=layer.id,
                    layer_name=layer.name,
                    constraint=layer.development_constraint.name,
                    source=layer.data_source,
                    area=layer.administrative_area.name,
                    publisher=layer.data_publisher.name,
                    license=(
                        layer.data_license.name if layer.data_license else None),
                    update_cycle=layer.update_cycle,
                    accessed_or_created=datetime.datetime.strftime(layer.data_accessed_or_created, "%d/%m/%y"),
                    last_updated=datetime.datetime.strftime(layer.data_last_updated, "%d/%m/%y") if layer.data_last_updated else None,
                    next_updated=datetime.datetime.strftime(layer.data_next_updated, "%d/%m/%y")if layer.data_next_updated else None,
                    expires=datetime.datetime.strftime(layer.data_expires, "%d/%m/%y")if layer.data_expires else None,
                    notes=layer.notes,
                    created=datetime.datetime.strftime(layer.created, "%d/%m/%y %H:%M:%S"),
                    created_by=layer.created_by,
                    objects=count,
                    wind_priority=layer.development_constraint.onshore_wind_priority_level.name,
                    solar_priority=layer.development_constraint.solar_priority_level.name,
                    battery_priority=layer.development_constraint.battery_priority_level.name,
                    category=layer.development_constraint.constraint_category.name


                ))
        return result
