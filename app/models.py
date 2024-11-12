from sqlalchemy import  Column, Integer, String

from database import Base


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    mail = Column(String)
    phone = Column(String)
    subject = Column(String)
    message = Column(String)
    createDate = Column(String)

