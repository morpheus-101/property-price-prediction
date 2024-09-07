from pydantic import BaseModel


class Health(BaseModel):
    """
    Pydantic model for the health check response.

    Attributes:
        name (str): The name of the API.
        api_version (str): The version of the API.
        model_version (str): The version of the prediction model being used.
    """

    name: str
    api_version: str
    model_version: str
