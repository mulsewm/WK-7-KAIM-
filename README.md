# Ethiopian Medical Business Data Scraping

This project involves scraping Telegram channels to collect data on Ethiopian medical businesses. The data is processed and transformed using dbt (data build tool) to provide insights and analytics.

## Project Structure

- **notebooks/**: Jupyter notebooks for data exploration and analysis.
- **scripts/**: Python scripts for scraping and data processing.
  - `scraper.py`: Script for scraping Telegram channels.
  - `image_scraper.py`: Script for extracting images from messages.
  - `data_cleaning.py`: Script for cleaning and processing raw data.
  - `store_db.py`: Script for storing cleaned data into a PostgreSQL database.
  - `logger.py`: Script for setting up logging.
- **data/**: Directory for storing raw and processed data.
  - `raw/`: Contains raw data files.
  - `processed/`: Contains cleaned data files.
- **logs/**: Directory for log files.
- **models/**: dbt models for transforming data.
- **reports/**: Directory for generated reports.
- **telegram_dbt/**: dbt project directory.
  - `models/`: Contains SQL models for data transformation.
  - `analyses/`, `macros/`, `seeds/`, `snapshots/`, `tests/`: dbt directories for additional functionalities.

## Setup

1. **Install Requirements**: Ensure you have Python and PostgreSQL installed. Install Python dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**: Create a `.env` file with the following variables:
   ```
   API_ID=<your_telegram_api_id>
   API_HASH=<your_telegram_api_hash>
   DB_NAME=<your_database_name>
   DB_USER=<your_database_user>
   DB_PASSWORD=<your_database_password>
   DB_HOST=<your_database_host>
   DB_PORT=<your_database_port>
   ```

3. **Initialize dbt**: Navigate to the `telegram_dbt` directory and run:
   ```bash
   dbt init
   ```

## Usage

1. **Run Scraper**: Execute the Telegram scraper to collect data:
   ```bash
   python scripts/telegram_scrapper.py
   ```

2. **Clean Data**: Clean the raw data using:
   ```bash
   python scripts/data_cleaning.py
   ```

3. **Store Data**: Store the cleaned data into the database:
   ```bash
   python scripts/store_db.py
   ```

4. **Run dbt Models**: Transform the data using dbt:
   ```bash
   cd telegram_dbt
   dbt run
   ```

5. **Test dbt Models**: Run tests to ensure data quality:
   ```bash
   dbt test
   ```

## Resources

- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.