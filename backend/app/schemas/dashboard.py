"""
app/schemas/dashboard.py
Pydantic models that define the shape of API request/response data.
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


class TemperaturePoint(BaseModel):
    """A single data point for the temperature trend chart."""
    name:        str
    temperature: float


class StatusCount(BaseModel):
    """Equipment count grouped by status, used for the pie chart."""
    status: str
    count:  int


class ProductionItem(BaseModel):
    """Production value per machine, used for the bar chart."""
    name:       str
    production: float
