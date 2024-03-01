from pathlib import Path
from src.app.read_shapefile import read_shapefile
import pytest

def test_should_raise_exception_for_path_not_a_file() -> None:
        path = Path("not/a/file.shp")
        assert not path.is_file()
        with pytest.raises(Exception):
            read_shapefile(path)


def test_should_raise_exception_for_file_not_shapefile() -> None:
       path = Path("tests/test_data/blank_text_file.txt")
       assert path.is_file()
       with pytest.raises(Exception):
              read_shapefile(path)
       
        
def test_should_read_shapefie_and_return_details() -> None:
        test_file = Path("tests/test_data/test_shapefiles/1_valid_polygon_OSGB36.shp")
        assert test_file.is_file()
        assert read_shapefile(test_file) == 1 
