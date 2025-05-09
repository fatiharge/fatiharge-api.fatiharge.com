import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
import crud
from database import SessionLocal, engine
import mail_service

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
async def create_contact_endpoint(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    try:
        RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
        body = f"""
         A new contact has been added:

         Name: {contact.name}
         Email: {contact.mail}
         Phone: {contact.phone}
         Subject: {contact.subject}
         Message: 
         {contact.message}
         """
        await mail_service.send_email(
            recipient=RECIPIENT_EMAIL,
            subject=f"New Contact Information - {contact.subject}",
            body=body,
        )
    except Exception as e:
        print(f"create_contact_endpoint: {str(e)}")

    return crud.create_contact(db=db, contact=contact)
