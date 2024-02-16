# This file must be in a directory above db_tests for reasons yet unknown.

import pytest


@pytest.fixture()
def my_fixture():
    return "some stuff"


def pytest_addoption(parser):
    parser.addoption(
        "--dbtests", action="store_true", default=False, help="Run tests that require database connection."
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "db: Mark test as requiring database connection.")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--dbtests"):
        return
    skip_db_tests = pytest.mark.skip(reason="Need --dbtests option to run.")
    for item in items:
        if "db" in item.keywords:
            item.add_marker(skip_db_tests)
