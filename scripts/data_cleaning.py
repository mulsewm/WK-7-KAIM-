import os
import json
import pandas as pd
import logging

# Setup logging
logging.basicConfig(filename='data_cleaning.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.info("Starting Data Cleaning Process")

# Load scraped data
input_file = "data/raw/telegram_data.json"
output_file = "data/processed/cleaned_telegram_data.csv"
os.makedirs("data/processed", exist_ok=True)

try:
    with open(input_file, "r") as f:
        data = json.load(f)
except Exception as e:
    logger.error(f"Error loading JSON file: {str(e)}")
    exit()

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Remove duplicates
df.drop_duplicates(subset=["message_id"], keep="first", inplace=True)

# Handle missing values
df.fillna("", inplace=True)

# Standardize text formats
df["text"] = df["text"].str.strip()

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Save cleaned data to CSV
df.to_csv(output_file, index=False)

logger.info("Data Cleaning Completed. Cleaned data saved to data/processed/cleaned_telegram_data.csv")
print("Data Cleaning Completed. Cleaned data saved to data/processed/cleaned_telegram_data.csv")
