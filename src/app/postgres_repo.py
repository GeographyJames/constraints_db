from .dtos import (ConstraintLayerFormOptionsDTO,
                   DevelopmentConstraintOutputDTO,
                   AdministrativeAreaOutputDTO,
                   ConstraintLayerInputDTO)
from sqlalchemy import Engine, select, text
from src.db.models import (DevelopmentConstraint,
                           AdministrativeArea,
                           DataPublisher,
                           DataLicense,
                           create_constraint_layer_table,
                           ConstraintLayer
                           )
from sqlalchemy.engine import CursorResult
from sqlalchemy.orm import Session
from typing import Any


class PostGresRepo:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

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
                        abbreviation=row.abbreviation) for row in conn.execute(
                        select(DevelopmentConstraint.id,
                               DevelopmentConstraint.name,
                               DevelopmentConstraint.abbreviation))},
                administrative_areas={
                    row.id: AdministrativeAreaOutputDTO(
                        id=row.id,
                        name=row.name,
                        abbreviation=row.abbreviation) for row in conn.execute(
                            select(AdministrativeArea.id,
                                   AdministrativeArea.name,
                                   AdministrativeArea.abbreviation))},
                data_publishers=self._to_dict(conn.execute(select(
                    DataPublisher.id, DataPublisher.name))),
                data_licenses=self._to_dict(conn.execute(select(
                    DataLicense.id, DataLicense.name)))
            )
        return result

    def add_constraint_layer(self, layer: ConstraintLayerInputDTO) -> None:
        sql_layer = ConstraintLayer(
            name=layer.name(),
            development_constraint_id=layer.development_constraint.id,
            administrative_area_id=layer.administrative_area.id,
            data_publisher_id=layer.data_publisher_id,
            data_accessed_or_created=layer.data_accessed_or_created

        )
        with Session(self.engine) as session:
            session.add(sql_layer)
            session.commit()
            stmt1, stmt2 = create_constraint_layer_table(
                constraint_layer_name=layer.name(),
                geometry_type=layer.geom_type,
                constraint_layer_id=sql_layer.id)
            session.execute(text(stmt1))
            session.execute(text(stmt2))
            session.commit()
