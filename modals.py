from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    isbn = Column(String)
    price= Column(String)
    is_delete = Column(Boolean, default=False)

  