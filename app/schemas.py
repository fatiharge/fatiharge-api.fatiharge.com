from pydantic import BaseModel


class ContactBase(BaseModel):
    name: str
    mail: str
    phone: str
    subject: str
    message: str


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int

    class Config:
        orm_mode: True
