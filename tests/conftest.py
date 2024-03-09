# This file must be in a directory above db_tests for reasons yet unknown.

from typing import Any
import pytest


def pytest_addoption(parser: Any) -> None:
    parser.addoption(
        "--dbtests",
        action="store_true",
        default=False,
        help="Run tests that require database connection."
    )
    parser.addoption(
        "--gui",
        action="store_true",
        default=False,
        help="Run tests that require gui"

    )


def pytest_configure(config: Any) -> None:
    config.addinivalue_line(
        "markers",
        "db: Mark test as requiring database connection.")
    config.addinivalue_line(
        "markers",
        "gui: Mark test as requiring gui"
    )


def pytest_collection_modifyitems(config: Any, items: Any) -> None:
    if not config.getoption("--dbtests"):
        skip_db_tests = pytest.mark.skip(
            reason="Need --dbtests option to run.")
        for item in items:
            if "db" in item.keywords:
                item.add_marker(skip_db_tests)

    if not config.getoption("--gui"):
        skip_gui_tests = pytest.mark.skip(
            reason="Need --gui option to run"
        )
        for item in items:
            if "gui" in item.keywords:
                item.add_marker(skip_gui_tests)
