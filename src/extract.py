import os
import logging
import pandas as pd
import kagglehub as kh
import shutil
from pathlib import Path

def download_dataset(dataset: str, save_path: str, date: str) -> None:
    """Downloads a dataset from Kaggle to the specified path."""
    try:
        source = kh.dataset_download(dataset)

        # Copy the downloaded file to the ./data/raw directory
        source_files = list(Path(source).glob("*.csv"))
        if not source_files:
            raise FileNotFoundError("No CSV file found in the downloaded dataset.")
        
        Path(save_path).mkdir(parents=True, exist_ok=True)
        shutil.copy(Path(source)/"amazon.csv", Path(save_path)/f"amazon_{date}.csv")
        logging.info(f"Dataset saved as {Path(save_path)/f'amazon_{date}.csv'}")
    except Exception as e:
        logging.error(f"Error downloading dataset: {e}")
        raise

def load_csv(file_path: str) -> pd.DataFrame:
    """Loads a CSV file into a DataFrame."""
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError(f"Empty DataFrame: {file_path}")
        
        required_columns = [
            "product_id", "product_name", "category", "discounted_price", "actual_price",
            "discount_percentage", "rating", "rating_count", "review_title", "review_content"
        ]

        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        # Ensure the DataFrame contains only the required columns
        df = df[required_columns]
        
        logging.info(f"Successfully loaded data from {file_path}")
        return df
    
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        raise

if __name__ == "__main__":
    dataset_name = "karkavelrajaj/amazon-sales-dataset"
    save_directory = "data/raw"
    current_date = pd.Timestamp.now().strftime('%Y_%m_%d')
    csv_file_path = Path(save_directory)/f"amazon{current_date}.csv"

    # Download dataset if not available
    if not Path(csv_file_path).exists():
        download_dataset(dataset_name, save_directory, current_date)
    
    # Load CSV file 
    df = load_csv(csv_file_path)
    print(df.head())
