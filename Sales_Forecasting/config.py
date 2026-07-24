import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "sales_forecasting_dashboard_2026"

    DATASET_PATH = os.path.join(
        BASE_DIR,
        "dataset",
        "train.csv"
    )

    FORECAST_PERIOD = 4500

    DEBUG = True