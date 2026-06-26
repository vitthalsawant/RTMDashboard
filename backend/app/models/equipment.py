"""
Maps Python class attributes directly to PostgreSQL columns.

"""

from sqlalchemy import Column, Integer, String, Numeric
from app.database.db import Base


class Equipment(Base):
    
    __tablename__ = "equipment"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(100), nullable=False)
    status      = Column(String(50), nullable=False)   # Running, Stopped, Maintenance
    temperature = Column(Numeric(6, 2), nullable=True)
    production  = Column(Numeric(10, 2), nullable=True)
