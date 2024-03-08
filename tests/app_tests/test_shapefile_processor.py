from pathlib import Path
from src.app.shapefile_processor import (verify_shapefile,
                                         verify_crs_is_ESPG27700,
                                         ShapefileProcessor)
import pytest
from src.app.exceptions import ShapefileError
from osgeo import ogr
import attrs
# import qgis


class TestVerifyShapefile:

    def test_should_raise_exception_for_path_not_a_file(self) -> None:
        path = Path("not/a/file.shp")
        assert not path.is_file()
        with pytest.raises(ShapefileError, match="not a file"):
            verify_shapefile(path)

    def test_should_raise_exception_for_file_not_shapefile(self) -> None:
        path = Path("tests/test_data/blank_text_file.txt")
        assert path.is_file()
        with pytest.raises(ShapefileError, match="not a shapefile"):
            verify_shapefile(path)

    def test_should_raise_exception_for_failing_to_open_file(self) -> None:
        path = Path("tests/test_data/blank_shapefile.shp")
        assert path.is_file()
        with pytest.raises(ShapefileError, match="Could not open file"):
            verify_shapefile(path)

    def test_should_read_shapefie_and_return_ogr_datasource(self) -> None:
        path = Path(
            "tests/test_data/test_shapefiles/1_valid_polygon_OSGB36.shp")
        assert path.is_file()
        assert isinstance(verify_shapefile(path), ogr.DataSource)


class TestVerifyCRS:
    def test_should_pass(self):
        path = Path(
            "tests/test_data/test_shapefiles/1_valid_point_OSGB36.shp")
        verify_shapefile(path)

    # @pytest.mark.skip
    def test_should_raise_exception_for_unaccepted_crs(self) -> None:
        path = Path(
            "tests/test_data/test_shapefiles/2_valid_polygons_WGS84.shp")
        datasource = verify_shapefile(path)
        with pytest.raises(ShapefileError, match="CRS not accepted"):
            verify_crs_is_ESPG27700(datasource)


@attrs.define()
class Input:
    name: str
    feature_count: int
    geom_type: str
    field_names: list[str]

    def path(self) -> Path:
        return Path(f"tests/test_data/test_shapefiles/{self.name}.shp")


@pytest.fixture
def cases():
    return [
        Input(
            "2_valid_multipolygons_OSGB36",
            2,
            "POLYGON",
            ["id", "Name", "Status", "Other"]),
        Input(
            "3_valid_linestrings_OSGB36",
            3,
            "LINESTRING",
            ["id", "new field"])
    ]


class TestShapefileProcessor:

    def test_should_return_feature_count(self, cases: list[Input]):
        for test_case in cases:
            assert ShapefileProcessor(
                test_case.path()).feature_count() == test_case.feature_count

    def test_should_return_geometry_type(self, cases: list[Input]):
        for test_case in cases:
            assert ShapefileProcessor(
                test_case.path()).geometry_type() == test_case.geom_type

    def test_should_return_field_names(self, cases: list[Input]):
        for test_case in cases:
            assert ShapefileProcessor(
                test_case.path()).field_names() == test_case.field_names
