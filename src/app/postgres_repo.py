from .dtos import ConstraintLayerFormOptionsDTO
from sqlalchemy import Engine, select, Connection
from src.db.models import DevelopmentConstraint, AdministrativeArea, DataPublisher, DataLicense
from sqlalchemy.engine import CursorResult
from typing import Any


class PostGresRepo:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def _to_dict(self, result: CursorResult[Any]) -> dict[int, str]:
        return {row.id: row.name for row in result.all()}

    def get_constraint_layer_form_options(self) -> ConstraintLayerFormOptionsDTO:
        with self.engine.connect() as conn:
            result = ConstraintLayerFormOptionsDTO(
                development_constraints=self._to_dict(conn.execute(select(
                    DevelopmentConstraint.id, DevelopmentConstraint.name))),
                administrative_areas=self._to_dict(conn.execute(select(
                    AdministrativeArea.id, AdministrativeArea.name))),
                data_publishers=self._to_dict(conn.execute(select(
                    DataPublisher.id, DataPublisher.name))),
                data_licenses=self._to_dict(conn.execute(select(
                    DataLicense.id, DataLicense.name)))
            )
        return result
