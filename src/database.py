# src/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base

# Configure SQLite database for lightweight data persistence
engine = create_engine('sqlite:///funds.db')
Session = sessionmaker(bind=engine)
session = Session()

# Automatically create tables if they don't exist
Base.metadata.create_all(engine)
