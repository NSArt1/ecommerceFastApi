from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase  # New

import sys

engine = create_engine('sqlite:///ecommerce.db', echo=True)
SessionLocal = sessionmaker(bind=engine)  # New
print(sys.path)

class Base(DeclarativeBase):
    pass