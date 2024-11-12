from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Herhangi bir kaynaktan gelen istekleri kabul et
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP metotlarına izin ver
    allow_headers=["*"],  # Tüm başlıklara izin ver
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.post("/contacts/", response_model=schemas.Contact)
def create_contact_endpoint(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db=db, contact=contact)


