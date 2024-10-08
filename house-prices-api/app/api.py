import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger

import sys
import os
from contextlib import contextmanager

@contextmanager
def add_to_path(p):
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
with add_to_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))):
    from regression_model import __version__ as model_version
    from regression_model.predict import make_prediction

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Endpoint to check the health of the API.

    Returns:
        dict: A dictionary containing the project name, API version, and model version.
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
    """
    Endpoint to make house price predictions using the TID regression model.

    Args:
        input_data (schemas.MultipleHouseDataInputs): The input data for prediction.

    Returns:
        Any: The prediction results.

    Raises:
        HTTPException: If there are validation errors in the prediction.
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results
