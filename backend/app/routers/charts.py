"""
app/routers/charts.py
Handles chart data endpoints:
  - GET /temperature-trend  -> Line chart (last 10 records)
  - GET /equipment-status   -> Pie chart (status distribution)
  - GET /production-summary -> Bar chart (per machine production)
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from app.database.db import get_db
from app.models.equipment import Equipment
from app.schemas.dashboard import TemperaturePoint, StatusCount, ProductionItem

router = APIRouter()


@router.get("/temperature-trend", response_model=List[TemperaturePoint])
def get_temperature_trend(db: Session = Depends(get_db)):
    """
    Returns temperature data for the last 10 equipment records.
    Used to render the Trend Line Chart in Angular.
    """
    records = (
        db.query(Equipment)
        .filter(Equipment.temperature.isnot(None))
        .order_by(Equipment.id.desc())
        .limit(10)
        .all()
    )
    records = list(reversed(records))  # oldest -> newest, left to right
    return [
        TemperaturePoint(name=r.name, temperature=float(r.temperature))
        for r in records
    ]


@router.get("/equipment-status", response_model=List[StatusCount])
def get_equipment_status(db: Session = Depends(get_db)):
    """
    Returns count of equipment grouped by status.
    Used to render the Pie Chart (Running / Stopped / Maintenance).
    """
    results = (
        db.query(Equipment.status, func.count(Equipment.id).label("count"))
        .group_by(Equipment.status)
        .all()
    )
    return [StatusCount(status=row.status, count=row.count) for row in results]


@router.get("/production-summary", response_model=List[ProductionItem])
def get_production_summary(db: Session = Depends(get_db)):
    """
    Returns production values for each machine.
    Used to render the Bar Chart in Angular.
    """
    records = db.query(Equipment).filter(Equipment.production.isnot(None)).all()
    return [
        ProductionItem(name=r.name, production=float(r.production))
        for r in records
    ]
