

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from app.database.db import get_db
from app.models.equipment import Equipment
from app.schemas.dashboard import TemperaturePoint, StatusCount, ProductionItem, DashboardSummary

router = APIRouter()


@router.get("/temperature-trend", response_model=List[TemperaturePoint])
def get_temperature_trend(db: Session = Depends(get_db)):
    
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
    
    results = (
        db.query(Equipment.status, func.count(Equipment.id).label("count"))
        .group_by(Equipment.status)
        .all()
    )
    return [StatusCount(status=row.status, count=row.count) for row in results]


@router.get("/production-summary", response_model=List[ProductionItem])
def get_production_summary(db: Session = Depends(get_db)):
    
    records = db.query(Equipment).filter(Equipment.production.isnot(None)).all()
    return [
        ProductionItem(name=r.name, production=float(r.production))
        for r in records
    ]
