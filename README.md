cci-setup5 testing!
testing deployment to railway job!

# Property Price Prediction Regression Model

This repository contains a production-ready regression model package for predicting house prices. The package is designed to be easily integrated into larger projects or deployed as a standalone service.

## Project Structure

The project is organized as follows:

- `regression_model/`: Main package directory
  - `datasets/`: Contains train.csv and test.csv datasets for model training and evaluation
  - `trained_models/`: Stores trained model pickle files for easy loading and deployment
  - `train_pipeline.py`: Script for training the model and creating the prediction pipeline
  - `config.yml`: Configuration file for model parameters and feature engineering steps
  - `VERSION`: Version information for the package, used for tracking changes
- `tests/`: Directory containing unit and integration tests
- `requirements/`: Directory containing requirement files
  - `requirements.txt`: Main project dependencies for production use
  - `test_requirements.txt`: Additional dependencies for running tests
  - `typing_requirements.txt`: Dependencies for static type checking
- `tox.ini`: Configuration file for tox, used for automating testing and quality checks across different environments
- `MANIFEST.in`: Specifies additional files to include in the package distribution
- `setup.py`: Setup script for packaging and distribution

## Setup and Installation

1. Clone this repository:
   ```
   git clone https://github.com/morpheus-101/property-price-prediction.git
   cd property-price-prediction
   ```
2. Create a virtual environment (recommended):
   ```
   python -m venv hpp-env
   source hpp-env/bin/activate  # On Windows, use `hpp-env\Scripts\activate`
   ```
3. Install the required packages:
   ```
   pip install -r requirements/requirements.txt
   ```

## Usage

To train the model:
