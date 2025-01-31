from fastapi import FastAPI, Depends, HTTPException
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


# GET: Fetch all messages
@app.get("/messages/", response_model=list[schemas.TelegramMessageSchema])
def read_messages(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_messages(db, limit)


# GET: Fetch a specific message by ID
@app.get("/messages/{message_id}", response_model=schemas.TelegramMessageSchema)
def read_message(message_id: int, db: Session = Depends(get_db)):
    message = crud.get_message_by_id(db, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


# POST: Create a new message
@app.post("/messages/", response_model=schemas.TelegramMessageSchema)
def create_message(message: schemas.TelegramMessageSchema, db: Session = Depends(get_db)):
    return crud.create_message(db, message)


# PUT: Update an existing message
@app.put("/messages/{message_id}", response_model=schemas.TelegramMessageSchema)
def update_message(message_id: int, updated_data: schemas.UpdateTelegramMessageSchema, db: Session = Depends(get_db)):
    updated_message = crud.update_message(db, message_id, updated_data)
    if not updated_message:
        raise HTTPException(status_code=404, detail="Message not found")
    return updated_message

@app.get("/detections/", response_model=list[schemas.DetectionResultSchema])
def read_detections(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_detection_results(db, limit)
