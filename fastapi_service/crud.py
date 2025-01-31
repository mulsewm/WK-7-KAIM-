from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Schema for Creating a New Message
class TelegramMessageSchema(BaseModel):
    channel: str
    message_text: str
    message_date: datetime
    media: bool
    image_path: Optional[str] = None


# Schema for Updating an Existing Message
class UpdateTelegramMessageSchema(BaseModel):
    message_text: Optional[str] = None
    media: Optional[bool] = None
    image_path: Optional[str] = None
