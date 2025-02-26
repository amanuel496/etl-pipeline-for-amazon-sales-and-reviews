import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

DATASET_NAME = "karkavelrajaj/amazon-sales-dataset"
SAVE_DIRECTORY = Path("data/raw")
CURRENT_DATE = pd.Timestamp.now().strftime('%Y_%m_%d')
CSV_FILE_PATH = SAVE_DIRECTORY / f"amazon_{CURRENT_DATE}.csv"
CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING')
TABLE_NAME = "amazon_sales_data"
# Add more configuration variables as needed