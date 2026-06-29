"""
app/models/alert.py
SQLAlchemy ORM model for the 'alerts' table.
Each alert is linked to an equipment record via a foreign key.

Matches SQL:
CREATE TABLE alerts (
    id           SERIAL PRIMARY KEY,
    equipment_id INTEGER NOT NULL,
    message      VARCHAR(255) NOT NULL,
    CONSTRAINT fk_equipment
        FOREIGN KEY (equipment_id)
        REFERENCES equipment(id)
        ON DELETE CASCADE
);
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base


class Alert(Base):
    """
    Represents an active alert for a piece of equipment.
    Maps to the 'alerts' table in PostgreSQL.
    """
    __tablename__ = "alerts"

    id           = Column(Integer, primary_key=True, index=True)
    equipment_id = Column(
        Integer,
        ForeignKey("equipment.id", ondelete="CASCADE"),
        nullable=False
    )
    message      = Column(String(255), nullable=False)
