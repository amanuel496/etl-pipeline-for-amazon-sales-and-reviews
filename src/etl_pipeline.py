import logging
from extract import load_csv, download_dataset
from transform import clean_data
from load import load_to_db
from config import DATASET_NAME, SAVE_DIRECTORY, CURRENT_DATE, CSV_FILE_PATH, \
     CONNECTION_STRING, TABLE_NAME, APP_PASSWORD, SENDER_EMAIL, RECEIVER_EMAIL, \
        SUBJECT
import smtplib 
from email.mime.text import MIMEText # For creating email content

def send_alert(error_message): 
    """Sends an email alert with the error message."""

    msg = MIMEText(f"Your ETL pipeline failed with the following error:\n\n{error_message}")
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    # Set up the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD) 
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        logging.info("Alert email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")
        raise

def etl_pipeline():
    """Runs the full ETL pipeline."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting ETL pipeline...")

    try:
        # Extract
        if not CSV_FILE_PATH.exists():
            download_dataset(DATASET_NAME, SAVE_DIRECTORY, CURRENT_DATE)
        raw_data = load_csv(str(CSV_FILE_PATH))
        logging.info("Data extraction completed.")

        # Transform
        cleaned_data = clean_data(raw_data, CURRENT_DATE)
        logging.info("Data transformation completed.")

        # Load
        load_to_db(cleaned_data, CONNECTION_STRING, TABLE_NAME)
        logging.info("Data loading completed.")

        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")
        send_alert(str(e)) # Send alert email with the error message
        raise

if __name__ == "__main__":
    etl_pipeline()
