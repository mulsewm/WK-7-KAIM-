from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud
import schemas

# Initialize FastAPI app
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency: Get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/messages/", response_model=list[schemas.TelegramMessageSchema])
def read_messages(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_messages(db, limit)

@app.get("/messages/{message_id}", response_model=schemas.TelegramMessageSchema)
def read_message(message_id: int, db: Session = Depends(get_db)):
    message = crud.get_message_by_id(db, message_id)
    if not message:
        return {"error": "Message not found"}
    return message
