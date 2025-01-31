from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TelegramMessageSchema(BaseModel):
    message_id: int
    channel: str
    message_text: str
    message_date: datetime
    media: bool
    image_path: Optional[str] = None
    
class DetectionResultSchema(BaseModel):
    image_name: str
    object_class: str
    confidence: float
    bounding_box: str
    detected_at: datetime
