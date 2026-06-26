"""
Each alert is linked to an equipment record via a foreign key

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base


class Alert(Base):
    __tablename__ = "alerts"

    id           = Column(Integer, primary_key=True, index=True)
    equipment_id = Column(
        Integer,
        ForeignKey("equipment.id", ondelete="CASCADE"),
        nullable=False
    )
    message      = Column(String(255), nullable=False)
