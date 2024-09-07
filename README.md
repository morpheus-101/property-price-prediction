# Property Price Prediction API

This repository contains a FastAPI-based API for predicting house prices. The API is designed to be easily deployed using Docker, offering a scalable and efficient solution for real estate price predictions.

## Overview

This API provides property price predictions using features such as location, size, number of bedrooms, and other relevant factors. The predictive model is trained on a dataset from Kaggle's "House Prices - Advanced Regression Techniques" competition. For more information about the dataset, visit [the Kaggle competition page](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).



## Project Workflow

This project follows a comprehensive workflow to develop, package, and deploy a property price prediction model:

1. **Data Analysis and Model Development**
   - Conducted Exploratory Data Analysis (EDA) on the dataset
   - Preprocessed the data to prepare it for modeling
   - Built a regression model using scikit-learn

2. **API Development and Deployment**
   - Created a prediction endpoint using FastAPI
   - Implemented both Infrastructure as a Service (IaaS) and Platform as a Service (PaaS) deployment strategies

3. **Model Packaging and Distribution**
   - Converted the regression model into a Python package
   - Published the package to Gemfury, a private Python package repository (similar to PyPI)

4. **PaaS Deployment**
   - Containerized the API using Docker
   - Deployed the containerized application on Railway
   - Installed the regression model package from Gemfury

5. **IaaS Deployment**
   - Containerized the API using Docker
   - Deployed the container on an Amazon EC2 instance

6. **Continuous Integration and Deployment**
   - Used CircleCI for automated testing and deployment workflows
   - Ensured code quality and reliability through continuous integration practices

7. **Cross-Environment Testing**
   - Utilized Tox for running tests across multiple Python environments
   - Guaranteed compatibility and consistent behavior across different setups



## Technologies Used

- FastAPI: A modern, fast web framework for building APIs.
- Docker: Used for containerization and ensuring consistent environments.
- uvicorn: An ASGI server for running the FastAPI application.
- Pydantic: Employed for data validation and settings management.
- pandas and numpy: Used for data manipulation and analysis.
- scikit-learn: The machine learning library used for building the regression model.
- loguru: Used for efficient logging.
- Railway: The Platform as a Service (PaaS) used for deploying the containerized application.
- CircleCI: Utilized for continuous integration and deployment workflows.
- Tox: Used for running tests across multiple Python environments.
- Gemfury: A private Python package repository used for distributing the regression model package.
- AWS EC2: The Infrastructure as a Service (IaaS) platform used for deploying the containerized application.

## Project Structure

The project is meticulously organized as follows:

- `house-prices-api/`: Main API directory
  - `app/`: Contains the core FastAPI application
    - `api.py`: Defines API endpoints and request handling logic
    - `config.py`: Configuration settings for the API, including environment variables and logging setup
    - `main.py`: Main application entry point, sets up FastAPI app and includes routers
    - `schemas/`: Pydantic schemas for request/response models, ensuring type safety and validation
    - `tests/`: Comprehensive API tests to ensure reliability and correctness
  - `requirements.txt`: Detailed list of project dependencies with version specifications
  - `run.sh`: Bash script to run the API using uvicorn with proper settings
- `Dockerfile`: Instructions for building the Docker image, ensuring consistent environments
- `prod_model_package/`: Directory containing code for building, testing, packing the regression model.

## Setup

1. Clone the repository to your local machine.

2. Before building the Docker image, ensure you have access to the required model package. The model 'property-price-prediction-regression-model==0.0.1' is specified in the requirements.txt file and is sourced from a private package repository (Gemfury). You can find the exact model package in the 'prod_model_package/dist/' directory. Upload this package to your own Gemfury package repository before proceeding.

3. Build the Docker image using the provided Dockerfile.

4. Run the Docker container, which will start the API service.

## Usage

Once the API is running, you can access it at `http://localhost:8001`. The API provides the following endpoints:

- `/`: Basic HTML welcome page with links to documentation
- `/api/v1/health`: Health check endpoint to ensure the API is operational
- `/api/v1/predict`: POST endpoint for making house price predictions based on input features

For comprehensive API documentation, including request/response schemas and example usage, visit `http://localhost:8001/docs` after starting the server.