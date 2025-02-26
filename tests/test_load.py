import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.load import load_to_db

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        'product_id': ['P001'],
        'product_name': ['Sample Product'],
        'category': ['electronics'],
        'discounted_price': [999.0],
        'actual_price': [1299.0],
        'rating': [4.5],
        'rating_count': [100],
        'review_title': ['good'],
        'review_content': ['works well']
    })

@patch('src.load.psycopg2.connect')
@patch('src.load.execute_values')
def test_load_to_db_success(mock_execute_values, mock_connect, sample_dataframe):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.encoding = 'utf-8'
    mock_cursor.connection = mock_conn
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    connection_string = "dbname='testdb' user='user' password='pass' host='localhost'"
    table_name = "amazon_sales_data"

    load_to_db(sample_dataframe, connection_string, table_name)

    mock_connect.assert_called_once_with(connection_string)
    mock_execute_values.assert_called_once()
    mock_conn.commit.assert_called_once()

@patch('src.load.psycopg2.connect')
def test_load_to_db_database_error(mock_connect, sample_dataframe):
    mock_connect.side_effect = Exception("Database connection failed")

    connection_string = "invalid_connection_string"
    table_name = "amazon_sales_data"

    with pytest.raises(Exception) as exc_info:
        load_to_db(sample_dataframe, connection_string, table_name)

    assert "Database connection failed" in str(exc_info.value)
