from datetime import datetime
from sqlalchemy.orm import Session
import models
import schemas


def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(
        name=contact.name,
        mail=contact.mail,
        phone=contact.phone,
        subject=contact.subject,
        message=contact.message,
        createDate=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact
