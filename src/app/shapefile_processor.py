from pathlib import Path
from osgeo import ogr
from .exceptions import ShapefileError
from .dtos import ShapfileInfoDTO


ogr.UseExceptions()


class ShapefileProcessor:
    def __init__(self, file_path: Path) -> None:
        self.datasource = verify_shapefile(file_path)
        # verify_crs_is_ESPG27700(self.datasource)

    def feature_count(self) -> int:
        return int(self.datasource.GetLayer().GetFeatureCount())

    def geometry_type(self) -> str:
        geom = self.datasource.GetLayer().GetGeomType()
        return str(ogr.GeometryTypeToName(geom).upper().replace(" ", ""))

    def field_names(self) -> list[str]:
        layer_def = self.datasource.GetLayer().GetLayerDefn()
        return [layer_def.GetFieldDefn(i).GetName() for i in range(
            layer_def.GetFieldCount())]

    def shapefile_info(self) -> ShapfileInfoDTO:
        return ShapfileInfoDTO(
            fields=self.field_names(),
            geom_type=self.geometry_type(),
            feature_count=self.feature_count()
        )


def read_shapefile(file_path: Path) -> int:
    if not file_path.is_file():
        raise ShapefileError(f"{file_path} not a file.")
    driver = ogr.GetDriverByName('ESRI Shapefile')
    datasource = driver.Open(file_path.as_posix())
    print(datasource)
    if not datasource:
        raise Exception("Could not open file")
    layer = datasource.GetLayer()
    feature_count = layer.GetFeatureCount()
    return int(feature_count)


def verify_shapefile(file_path: Path) -> ogr.DataSource:
    if not file_path.is_file():
        raise ShapefileError(f"{file_path} not a file.")
    if not file_path.suffix == ".shp":
        raise ShapefileError(f"{file_path} not a shapefile.")
    driver = ogr.GetDriverByName("ESRI Shapefile")
    datasource = driver.Open(file_path.as_posix())
    if not datasource:
        raise ShapefileError(f"Could not open file {file_path}.")
    return datasource


def verify_crs_is_ESPG27700(datasource: ogr.DataSource) -> None:
    osr = datasource.GetLayer().GetSpatialRef()
    authority_code = f"{osr.GetAttrValue(
        'AUTHORITY')}:{osr.GetAttrValue('AUTHORITY', 1)}"
    if not authority_code == "EPSG:27700":
        raise ShapefileError(
            f"CRS not accepted. Convert to EPSG:27700 (British National Grid) "
            f"and try again. CRS of layer EPSG:{authority_code}")


if __name__ == "__main__":
    path = Path(r"tests\test_data\test_shapefiles\1_valid_point_OSGB36.shp")
    sp = ShapefileProcessor(path)
    print(sp.geometry_type())
