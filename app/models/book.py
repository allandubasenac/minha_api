from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base

class Book(Base):
    __tablename__ = "empresa"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
