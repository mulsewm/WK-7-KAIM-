import os
import pandas as pd
import psycopg2
import logging
from sqlalchemy import create_engine

# Setup logging
logging.basicConfig(filename='db_ingestion.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.info("Starting Database Ingestion")

# Database Configuration
DB_NAME = "telegram_data"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
TABLE_NAME = "telegram_data"

# Load cleaned data
input_file = "data/processed/cleaned_telegram_data.csv"
if not os.path.exists(input_file):
    logger.error("Cleaned data file not found.")
    exit()

df = pd.read_csv(input_file)

# Establish connection to PostgreSQL
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def create_table():
    try:
        with engine.connect() as connection:
            connection.execute(f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    message_id BIGINT PRIMARY KEY,
                    channel TEXT,
                    text TEXT,
                    date TIMESTAMP,
                    media BOOLEAN,
                    image_path TEXT
                );
            ''')
        logger.info("Database table created successfully.")
    except Exception as e:
        logger.error(f"Error creating table: {str(e)}")

# Insert Data
def insert_data():
    try:
        df.to_sql(TABLE_NAME, engine, if_exists='append', index=False)
        logger.info("Data inserted into PostgreSQL successfully.")
        print("Data successfully stored in PostgreSQL database.")
    except Exception as e:
        logger.error(f"Error inserting data: {str(e)}")

if __name__ == "__main__":
    create_table()
    insert_data()
