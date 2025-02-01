from backend.db import Base
from sqlalchemy import Column, ForeignKey, String, Boolean, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
import os
import sys

# sys.path.append(os.getcwd())
class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique = True, index =True)
    is_active = Column(Boolean, default=True)
    
print(CreateTable(Category.__table__))