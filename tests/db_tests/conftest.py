import pytest


@pytest.fixture()
def my_fixture():
    return "some stuff"


def pytest_addoption(parser):
    parser.addoption(
        "--db_tests", action="store_true", default=False, help="Run tests that require database connection."
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "db: Mark test as requiring database connection.")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--db_tests"):
        return
    skip_db_tests = pytest.mark.skip(reason="Need --db_tests option to run.")
    for item in items:
        if "db" in item.keywords:
            item.add_marker(skip_db_tests)
