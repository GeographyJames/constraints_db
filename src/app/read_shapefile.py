from pathlib import Path
from osgeo import ogr

ogr.DontUseExceptions()


def read_shapefile(file_path: Path) -> int:
    if not file_path.is_file():
        raise Exception("Invalid file.")
    driver = ogr.GetDriverByName('ESRI Shapefile')
    datasource = driver.Open(file_path.as_posix())
    if not datasource:
        raise Exception("Could not open file")
    layer = datasource.GetLayer()
    feature_count = layer.GetFeatureCount()
    return int(feature_count)

