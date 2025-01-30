import os
import subprocess

# Define folder structure
folders = [
    "notebooks",
    "scripts",
    "data/raw",
    "data/processed",
    "logs",
    "models",
    "reports",
]

files = {
    "README.md": "# Ethiopian Medical Business Data Scraping\n\nThis project involves scraping Telegram channels to collect data on Ethiopian medical businesses.",
    "requirements.txt": "telethon\nrequests\npandas\nbeautifulsoup4\nscrapy\nselenium\nlogging\nopencv-python\ntorch torchvision", 
    "scripts/scraper.py": "# Script for Telegram Scraping\n\n# Add your scraping logic here.",
    "scripts/image_scraper.py": "# Script for Image Scraping\n\n# Add image extraction logic here.",
    "scripts/logger.py": "import logging\n\nlogging.basicConfig(filename='logs/scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\nlogger = logging.getLogger()\n\nlogger.info('Logger initialized.')",
    ".gitignore": "data/raw/*\ndata/processed/*\nlogs/*\nmodels/*",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file, content in files.items():
    with open(file, "w") as f:
        f.write(content)

# Initialize Git repository
subprocess.run(["git", "init"])

# Add all files to Git
subprocess.run(["git", "add", "."])

# Commit the changes
subprocess.run(["git", "commit", "-m", "Initial commit"])

print("Project setup completed. You can now start implementing the scrapers!")
