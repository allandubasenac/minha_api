from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Borrow(Base):
    __tablename__ = "borrow"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_copy_id = Column(Integer, ForeignKey("book_copy.id"), nullable=False)
    borrower_id = Column(Integer, ForeignKey("user.id"), nullable=False)  
    lender_id = Column(Integer, ForeignKey("user.id"), nullable=False) 

    borrow_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=False)
    return_date = Column(DateTime(timezone=True), nullable=True)

    book_copy = relationship("BookCopy", back_populates="borrows", foreign_keys=[book_copy_id])
    
    borrower = relationship("User", foreign_keys=[borrower_id], back_populates="borrowed_items")

    lender = relationship("User", foreign_keys=[lender_id], back_populates="processed_loans")

