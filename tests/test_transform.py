import pytest
import pandas as pd
from src.transform import clean_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'product_id': ['P001', 'P001', 'P002', None],
        'product_name': ['Product A ', 'product a', ' Product B', 'Product C'],
        'category': [' Electronics', 'electronics ', ' Home', ''],
        'discounted_price': ['₹1,299', '₹1,299', '₹0', None],
        'actual_price': ['₹1,499', '₹1,499', '₹999', '₹1,099'],
        'rating': [4.5, None, 6, -1],
        'rating_count': ['1,234', None, '123', ''],
        'review_title': [None, 'Great!', ' ', None],
        'review_content': ['Good product.', None, None, 'Bad experience.']
    })

def test_clean_data(sample_data):
    cleaned_df = clean_data(sample_data, '2023_10_01')

    # Check duplicates removed
    assert cleaned_df['product_id'].duplicated().sum() == 0

    # Check missing values filled
    assert cleaned_df['discounted_price'].isnull().sum() == 0
    assert cleaned_df['actual_price'].isnull().sum() == 0
    assert cleaned_df['rating'].isnull().sum() == 0
    assert cleaned_df['rating_count'].isnull().sum() == 0

    # Validate numeric conversions
    assert cleaned_df['discounted_price'].dtype == 'float'
    assert cleaned_df['actual_price'].dtype == 'float'

    # Validate text standardization
    assert all(cleaned_df['product_name'] == cleaned_df['product_name'].str.strip().str.lower())
    assert all(cleaned_df['category'] == cleaned_df['category'].str.strip().str.lower())

    # Validate rating boundaries
    assert cleaned_df['rating'].between(0, 5).all() 