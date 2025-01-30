import logging

logging.basicConfig(filename='logs/scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

logger.info('Logger initialized.')