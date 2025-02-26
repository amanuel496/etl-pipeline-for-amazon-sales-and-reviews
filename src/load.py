import psycopg2
import logging
import pandas as pd
from psycopg2 import excute_values

def load_to_db(df: pd.DataFrame, connection_string: str, table_name: str) -> None:
    """Loads the given DataFrame into the specified PostgreSQL database table."""
    try:
        # Establish a database connection
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()

        # Create insert query
        columns = ", ".join(df.columns)
        values_template = "%s" # Placeholder for values
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_template})"

        # Execute insert operation
        records = df.to_records(index=False)
        excute_values(cursor, insert_query, records)

        # Commit and close 
        conn.commit()
        logging.info(f"Data successfully loaded into {table_name} table.")
    
    except psycopg2.DatabaseError as e:
        logging.error(f"Database error: {e}")
        conn.rollback()
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

    finally:
        cursor.close()
        conn.close()

# Example usage
if __name__ == "__main__":
    connection_string = "dbname='amazon_sales' user='username' password='password' host='localhost'"
    table_name = "amazon_sales_data"

    # Load some sample data for testing
    df_sample = pd.DataFrame({
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

    load_to_db(df_sample, connection_string, table_name)