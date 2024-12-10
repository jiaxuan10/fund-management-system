# src/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create a base class for all SQLAlchemy ORM models
Base = declarative_base()

class InvestmentFund(Base):
    """
    Represents the structure of an investment fund in the database.
    Each fund has attributes such as:
    - id: A unique identifier for the fund (primary key).
    - name: The name of the fund (mandatory field).
    - manager: The name of the fund manager (mandatory field).
    - description: A short description of the fund (optional field).
    - nav: The Net Asset Value (NAV) of the fund (mandatory field).
    - creation_date: The date the fund was created (automatically set to the current timestamp).
    - performance: The fund's performance as a percentage (optional field).
    """
    __tablename__ = 'funds'  # Name of the table in the database
    id = Column(Integer, primary_key=True)  # Automatically increments
    name = Column(String, nullable=False)  # Must be provided when creating a fund
    manager = Column(String, nullable=False)  # Must be provided when creating a fund
    description = Column(String)  # Can be left empty if not provided
    nav = Column(Float, nullable=False)  # Must be provided when creating a fund
    creation_date = Column(DateTime, default=datetime.utcnow)  # Auto-generated timestamp
    performance = Column(Float)  # Can be updated later as needed

    def __repr__(self):
        """
        Provides a string representation of the fund object, useful for debugging.
        Example: <Fund(name=Global Fund, manager=John Doe, NAV=1000.0)>
        """
        return f"<Fund(name={self.name}, manager={self.manager}, NAV={self.nav})>"
