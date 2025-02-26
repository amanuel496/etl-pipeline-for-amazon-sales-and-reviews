import pytest
import pandas as pd
from unittest.mock import patch
from pathlib import Path
from src.extract import download_dataset, load_csv

@pytest.fixture
def mock_kaggle_download(tmpdir):
    mock_path = tmpdir.mkdir("mock_dataset")
    mock_csv_path = mock_path.join("amazon.csv")

    # Create a mock CSV file
    df = pd.DataFrame({
        'product_id': ['P001'],
        'product_name': ['Sample Product'],
        'category': ['Electronics'],
        'discounted_price': ['₹999'],
        'actual_price': ['₹1299'],
        'rating': [4.5],
        'rating_count': ['100'],
        'review_title': ['Good'],
        'review_content': ['Works well']
    })
    df.to_csv(mock_csv_path, index=False)

    with patch('src.extract.kh.dataset_download') as mock_download:
        mock_download.return_value = Path(mock_path)
        yield mock_download

def test_download_dataset(mock_kaggle_download, tmpdir):
    dataset_name = "karkavelrajaj/amazon-sales-dataset"
    save_path = tmpdir.mkdir("raw_data")
    date = "2024_02_22"

    download_dataset(dataset_name, str(save_path), date)

    expected_file = Path(save_path) / f"amazon_{date}.csv"
    assert expected_file.exists()
    df = pd.read_csv(expected_file)
    assert df.iloc[0]['product_id'] == 'P001'

def test_load_csv(tmpdir):
    csv_path = tmpdir.join("amazon.csv")
    df = pd.DataFrame({
        'product_id': ['P001'],
        'product_name': ['Sample Product'],
        'category': ['Electronics'],
        'discounted_price': ['₹999'],
        'actual_price': ['₹1299'],
        'discount_percentage': ['23%'],
        'rating': [4.3],
        'rating_count': ['100'],
        'review_title': ['Good'],
        'review_content': ['Good product']
    })
    df.to_csv(csv_path, index=False)

    loaded_df = load_csv(str(csv_path))
    assert not loaded_df.empty
    assert 'product_id' in loaded_df.columns
    assert loaded_df.iloc[0]['product_id'] == 'P001'
