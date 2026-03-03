import os # lets environment vars to be read 

from sqlalchemy import create_engine #engine that talks to datebase
from sqlalchemy.orm import sessionmaker, declarative_base  # sessionmaker makes DB sessions; declarative_base is used to define models


#read url from environment else, use a local SQLite file
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./watchlist.db")


#SQLite has a thread-safety rule for connections.
# FastAPI can use multiple threads, so we set check_same_thread=False for SQLite.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

#create engine 
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

#create session factory: each request gets own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#class that all db models (tables) will inherit from. 
Base = declarative_base()