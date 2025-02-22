import logging
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def etl_pipeline():
    """Runs the full ETL pipeline."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s %(message)s')
    logging.info('Starting ETL pipeline...')

    try:
        # Extract
        raw_data = extract_data()
        logging.info('Data extracted successfully.')

        # Transform
        cleaned_data = transform_data(raw_data)
        logging.info('Data transformed successfully.')

        # Load
        load_data(cleaned_data)
        logging.info('Data loaded successfully.')
    except Exception as e:
        logging.error(f'Error during ETL pipeline: {e}')
        raise

if __name__ == '__main__':
    etl_pipeline()