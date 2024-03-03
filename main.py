from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, Path
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
import modals
from database import engine
import service

description = """
ChimichangApp API helps you do awesome stuff. 🚀
"""

app = FastAPI(
     
    title="Book-API"
)

modals.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books", tags=["Books"])
async def root():
    return {"message": "all books"}

@app.get('/books/{id}')
async def method_name(id, db: Session = Depends(get_db)):
     
     return service.get_book_by_id(db,id)

@app.get('/books/search')
async def method_name(title:str):
      return {"message": "all books",
            "title": title}

@app.put("/books/{id}")
def update_item(id:int):
     return {"message": "book updata",
            "id": id}

@app.delete("/books/{id}")
def delete_item(
   id:int
): 
     return {"message": "book delete",
            "id": id}
    