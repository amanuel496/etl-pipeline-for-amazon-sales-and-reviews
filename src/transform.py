import pandas as pd
import logging

def clean_data(df: pd.DataFrame, date: str) -> pd.DataFrame:
    """Cleans and preprocesses the dataset."""
    initial_count = len(df)
    logging.info(f"Initial rows: {initial_count}")

    try:
        # Drop duplicates based product_id
        df.drop_duplicates(subset='product_id', inplace=True)

        # Fill missing values
        df['discounted_price'].fillna(0, inplace=True)
        df['actual_price'].fillna(0, inplace=True)
        df['rating'].fillna(0, inplace=True)
        df['rating_count'].fillna(0, inplace=True)
        df['review_title'].fillna('No review', inplace=True)
        df['review_content'].fillna('No review', inplace=True)
        
        # Convert prices to numeric format (remove currency symbols and commas)
        df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
        df['actual_price'] = df['actual_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)

        # Validate prices and ratings
        df = df[(df['discounted_price'] >= 0) & (df['actual_price'] > 0)]
        df = df[(df['rating'] >= 0) & (df['rating'] <= 5)]

        # Log how many rows were dropped
        logging.info(f"Rows after cleaning: {len(df)}")

        # Convert rating_count to integer (removing commas if present)
        df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '').astype(int)

        # Standardize text columns
        df['product_name'] = df['product_name'].str.strip().str.lower()
        df['category'] = df['category'].str.strip().str.lower()
        df['review_title'] = df['review_title'].str.strip().str.lower()
        df['review_content'] = df['review_content'].str.strip().str.lower()

        logging.info("Data cleaning successful.")
        return df
    
    except Exception as e:
        logging.error(f"Error cleaning data: {e}")
        raise

if __name__ == "__main__":
    date = pd.Timestamp.now().strftime('%Y_%m_%d')
    file_path = f"data/raw/amazon_{date}.csv"
    df = pd.read_csv(file_path)
    cleaned_df = clean_data(df, date)
    print(cleaned_df.head())