"""
This module contains pytest fixtures and utility functions for testing the House Price Prediction API.
"""

from typing import Generator
import pandas as pd
import pytest
from fastapi.testclient import TestClient

import sys
import os
from contextlib import contextmanager

@contextmanager
def add_to_path(p: str) -> Generator[None, None, None]:
    """
    A context manager to temporarily add a path to sys.path.

    Args:
        p (str): The path to be added to sys.path.

    Yields:
        None
    """
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path

# Use the context manager to temporarily modify the path
with add_to_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))):
    from regression_model.config.core import config
    from regression_model.processing.data_manager import load_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    """
    Pytest fixture to load test data.

    Returns:
        pd.DataFrame: The loaded test dataset.
    """
    return load_dataset(file_name=config.app_config.test_data_file)


@pytest.fixture()
def client() -> Generator:
    """
    Pytest fixture to create a test client for the FastAPI app.

    Yields:
        TestClient: A test client for the FastAPI app.
    """
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
