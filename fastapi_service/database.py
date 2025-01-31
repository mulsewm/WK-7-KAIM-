from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database Configuration
DB_NAME = os.getenv("DB_NAME", "telegram_db")
DB_USER = os.getenv("DB_USER", "telegram_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Define Detection Results Table
class DetectionResult(Base):
    __tablename__ = "detection_results"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_name = Column(String, nullable=False)
    object_class = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    bounding_box = Column(String, nullable=False)
    detected_at = Column(TIMESTAMP, nullable=False)

# Create the table in the database
Base.metadata.create_all(engine)
