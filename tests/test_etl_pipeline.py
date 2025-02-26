import pytest
from unittest.mock import patch, MagicMock
from src.etl_pipeline import etl_pipeline
from unittest.mock import ANY


@patch('src.etl_pipeline.download_dataset')
@patch('src.etl_pipeline.load_csv')
@patch('src.etl_pipeline.clean_data')
@patch('src.etl_pipeline.load_to_db')
def test_etl_pipeline_success(mock_load_to_db, mock_clean_data, mock_load_csv, mock_download_dataset):
    mock_load_csv.return_value = MagicMock()
    mock_clean_data.return_value = MagicMock()

    etl_pipeline()

    # Verify each step was called
    mock_download_dataset.assert_called()
    mock_load_csv.assert_called_once()
    mock_clean_data.assert_called_once_with(mock_load_csv.return_value)
    mock_load_to_db.assert_called_once_with(mock_clean_data.return_value, ANY, ANY)

@patch('src.etl_pipeline.load_csv', side_effect=Exception("Failed to load CSV"))
def test_etl_pipeline_extract_failure(mock_load_csv):
    with pytest.raises(Exception) as exc_info:
        etl_pipeline()

    assert "Failed to load CSV" in str(exc_info.value)

@patch('src.etl_pipeline.clean_data', side_effect=Exception("Failed to clean data"))
@patch('src.etl_pipeline.load_csv')
def test_etl_pipeline_transform_failure(mock_load_csv, mock_clean_data):
    mock_load_csv.return_value = MagicMock()

    with pytest.raises(Exception) as exc_info:
        etl_pipeline()

    assert "Failed to clean data" in str(exc_info.value)

@patch('src.etl_pipeline.load_to_db', side_effect=Exception("Failed to load data"))
@patch('src.etl_pipeline.clean_data')
@patch('src.etl_pipeline.load_csv')
def test_etl_pipeline_load_failure(mock_load_csv, mock_clean_data, mock_load_to_db):
    mock_load_csv.return_value = MagicMock()
    mock_clean_data.return_value = MagicMock()

    with pytest.raises(Exception) as exc_info:
        etl_pipeline()

    assert "Failed to load data" in str(exc_info.value)
