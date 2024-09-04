from typing import Generator
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import pandas as pd
import pytest
from fastapi.testclient import TestClient

import sys
import os
from contextlib import contextmanager

@contextmanager
def add_to_path(p):
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path

# Use the context manager to temporarily modify the path
with add_to_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))):
    from regression_model.config.core import config
    from regression_model.processing.data_manager import load_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return load_dataset(file_name=config.app_config.test_data_file)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
