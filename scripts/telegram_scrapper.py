import os
import json
import logging
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv


load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

# Define target Telegram channels
CHANNELS = [
    'DoctorsET',
    'Chemed Telegram Channel',
    'Lobelia4cosmetics',
    'Yetenaweg',
    'EAHCI'
]

# Setup logging
logging.basicConfig(filename='telegram_scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.info("Starting Telegram Scraper")

# Create output directory if not exists
os.makedirs("data/raw", exist_ok=True)

# Initialize Telegram Client
client = TelegramClient('telegram_session', API_ID, API_HASH)

async def scrape_telegram():
    await client.start()
    all_messages = []
    
    for channel in CHANNELS:
        try:
            entity = await client.get_entity(channel)
            messages = await client.get_messages(entity, limit=100)
            
            for message in messages:
                msg_data = {
                    'channel': channel,
                    'message_id': message.id,
                    'text': message.text,
                    'date': str(message.date),
                    'media': False,
                    'image_path': None
                }
                
                # Save image if present
                if message.media and isinstance(message.media, MessageMediaPhoto):
                    file_path = f"data/raw/{channel}_{message.id}.jpg"
                    await client.download_media(message, file=file_path)
                    msg_data['media'] = True
                    msg_data['image_path'] = file_path
                    
                all_messages.append(msg_data)
            
            logger.info(f"Scraped {len(messages)} messages from {channel}")
        except Exception as e:
            logger.error(f"Error scraping {channel}: {str(e)}")
    
    # Save data to JSON
    with open('data/raw/telegram_data.json', 'w') as f:
        json.dump(all_messages, f, indent=4)

    print("Scraping completed. Data saved to data/raw/telegram_data.json")
    logger.info("Scraping completed successfully")

with client:
    client.loop.run_until_complete(scrape_telegram())
