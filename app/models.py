#define the table schema

from sqlalchemy import Column, Integer, String, DateTime  # Column/Integer/String/DateTime describe table columns and their types
from sqlalchemy.sql import func  

from .db import Base 

class WatchItem(Base):

    __tablename__ = "watch_items" 

    id= Column(Integer, primary_key=True, index=True) #for faster lookup
    title= Column(String(200), nullable=False)
    type = Column(String(20), nullable=False) #movie or show
    status = Column(String (20), nullable=False) #planning, watching, completed, dropped
    notes = Column (String (500) ,nullable=True) # optional 
    created_at = Column(DateTime(timezone=True), server_default = func.now(), nullable=False) #automatic timestamp

