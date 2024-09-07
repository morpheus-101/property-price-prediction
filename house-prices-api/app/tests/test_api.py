import math

import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    """
    Test the make_prediction endpoint of the API.

    This function tests the '/api/v1/predict' endpoint by sending a POST request
    with test data and verifying the response.

    Args:
        client (TestClient): The test client for the FastAPI application.
        test_data (pd.DataFrame): The test data to be used for prediction.

    Returns:
        None

    Raises:
        AssertionError: If any of the assertions fail.
    """
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200, "Expected status code 200"
    prediction_data = response.json()
    assert prediction_data["predictions"], "Predictions should not be empty"
    assert prediction_data["errors"] is None, "Errors should be None"
    assert math.isclose(prediction_data["predictions"][0], 113422, rel_tol=100), \
        "Prediction should be close to 113422 with a relative tolerance of 100"
