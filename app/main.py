from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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


