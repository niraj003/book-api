from sqlalchemy.orm import Session
from modals import Book
from schemas import BookSchema

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()