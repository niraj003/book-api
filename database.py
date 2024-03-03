from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql://postgres:Niraj\@2002@localhost:5432/Books-api'

engine = create_engine("postgresql://postgres:%s@localhost:5432/Book-api"% quote_plus("Niraj@2002"))
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()