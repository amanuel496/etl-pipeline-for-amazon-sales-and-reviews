import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)  # Load environment variables from .env file

DATASET_NAME = "karkavelrajaj/amazon-sales-dataset"
SAVE_DIRECTORY = Path("data/raw")
CURRENT_DATE = pd.Timestamp.now().strftime('%Y_%m_%d')
CSV_FILE_PATH = SAVE_DIRECTORY / f"amazon_{CURRENT_DATE}.csv"

CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING')
if CONNECTION_STRING is None:
    raise ValueError("DB_CONNECTION_STRING is not set in the environment variables.")
TABLE_NAME = "amazon_sales_data"

APP_PASSWORD = os.getenv('APP_PASSWORD')  # Email password for sending alerts
if APP_PASSWORD is None:
    raise ValueError("APP_PASSWORD is not set in the environment variables.")

SENDER_EMAIL = os.getenv('SENDER_EMAIL')  # Sender email address for sending alerts
if SENDER_EMAIL is None:
    raise ValueError("SENDER_EMAIL is not set in the environment variables.")

RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')  # Receiver email address for sending alerts
if RECEIVER_EMAIL is None:
    raise ValueError("RECEIVER_EMAIL is not set in the environment variables.")

SUBJECT = "ETL Pipeline Failed 🚨"
# Add more configuration variables as needed