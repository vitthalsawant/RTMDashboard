
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.equipment import Equipment
from app.models.alert import Alert
from app.schemas.dashboard import DashboardSummary

router = APIRouter()


@router.get("/dashboard", response_model=DashboardSummary)
def get_dashboard_summary(db: Session = Depends(get_db)):
    total   = db.query(Equipment).count()
    running = db.query(Equipment).filter(Equipment.status == "Running").count()
    stopped = db.query(Equipment).filter(Equipment.status == "Stopped").count()
    alerts  = db.query(Alert).count()

    return DashboardSummary(
        total_equipment=total,
        running_equipment=running,
        stopped_equipment=stopped,
        active_alerts=alerts
    )
