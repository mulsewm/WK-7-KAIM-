from sqlalchemy.orm import Session
from models import TransformedTelegramData

def get_all_messages(db: Session, limit: int = 10):
    return db.query(TransformedTelegramData).limit(limit).all()

def get_message_by_id(db: Session, message_id: int):
    return db.query(TransformedTelegramData).filter(TransformedTelegramData.message_id == message_id).first()
