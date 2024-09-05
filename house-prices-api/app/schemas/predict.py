from typing import Any, List, Optional
from pydantic import BaseModel

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
with add_to_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))):
    from regression_model.processing.validation import HouseDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "MSSubClass": 20,
                        "MSZoning": "RH",
                        "LotFrontage": 80.0,
                        "LotArea": 11622,
                        "Street": "Pave",
                        "Alley": None,
                        "LotShape": "Reg",
                        "LandContour": "Lvl",
                        "Utilities": "AllPub",
                        "LotConfig": "Inside",
                        "LandSlope": "Gtl",
                        "Neighborhood": "NAmes",
                        "Condition1": "Feedr",
                        "Condition2": "Norm",
                        "BldgType": "1Fam",
                        "HouseStyle": "1Story",
                        "OverallQual": 5,
                        "OverallCond": 6,
                        "YearBuilt": 1961,
                        "YearRemodAdd": 1961,
                        "RoofStyle": "Gable",
                        "RoofMatl": "CompShg",
                        "Exterior1st": "VinylSd",
                        "Exterior2nd": "VinylSd",
                        "MasVnrType": "None",
                        "MasVnrArea": 0.0,
                        "ExterQual": "TA",
                        "ExterCond": "TA",
                        "Foundation": "CBlock",
                        "BsmtQual": "TA",
                        "BsmtCond": "TA",
                        "BsmtExposure": "No",
                        "BsmtFinType1": "Rec",
                        "BsmtFinSF1": 468.0,
                        "BsmtFinType2": "LwQ",
                        "BsmtFinSF2": 144.0,
                        "BsmtUnfSF": 270.0,
                        "TotalBsmtSF": 882.0,
                        "Heating": "GasA",
                        "HeatingQC": "TA",
                        "CentralAir": "Y",
                        "Electrical": "SBrkr",
                        "FirstFlrSF": 896,
                        "SecondFlrSF": 0,
                        "LowQualFinSF": 0,
                        "GrLivArea": 896,
                        "BsmtFullBath": 0.0,
                        "BsmtHalfBath": 0.0,
                        "FullBath": 1,
                        "HalfBath": 0,
                        "BedroomAbvGr": 2,
                        "KitchenAbvGr": 1,
                        "KitchenQual": "TA",
                        "TotRmsAbvGrd": 5,
                        "Functional": "Typ",
                        "Fireplaces": 0,
                        "FireplaceQu": None,
                        "GarageType": "Attchd",
                        "GarageYrBlt": 1961.0,
                        "GarageFinish": "Unf",
                        "GarageCars": 1.0,
                        "GarageArea": 730.0,
                        "GarageQual": "TA",
                        "GarageCond": "TA",
                        "PavedDrive": "Y",
                        "WoodDeckSF": 140,
                        "OpenPorchSF": 0,
                        "EnclosedPorch": 0,
                        "ThreeSsnPortch": 0,
                        "ScreenPorch": 120,
                        "PoolArea": 0,
                        "PoolQC": None,
                        "Fence": "MnPrv",
                        "MiscFeature": None,
                        "MiscVal": 0,
                        "MoSold": 6,
                        "YrSold": 2010,
                        "SaleType": "WD",
                        "SaleCondition": "Normal",
                    }
                ]
            }
        }
