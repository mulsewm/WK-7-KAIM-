from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TransformedTelegramData(Base):
    __tablename__ = "transform_telegram"

    message_id = Column(Integer, primary_key=True, index=True)
    channel = Column(String)
    message_text = Column(String)
    message_date = Column(TIMESTAMP)
    media = Column(Boolean)
    image_path = Column(String)
