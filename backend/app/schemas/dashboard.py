"""
These are separate from SQLAlchemy models — they handle validation and serialization.
"""

from pydantic import BaseModel


class DashboardSummary(BaseModel):
    """Response schema for GET /dashboard — KPI summary card data."""
    total_equipment:   int
    running_equipment: int
    stopped_equipment: int
    active_alerts:     int


class EquipmentOut(BaseModel):
    """Response schema for a single equipment record."""
    id:          int
    name:        str
    status:      str
    temperature: float | None
    production:  float | None

    class Config:
        from_attributes = True   # allows SQLAlchemy model -> Pydantic conversion
