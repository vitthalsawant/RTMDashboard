
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models.equipment import Equipment
from app.schemas.dashboard import EquipmentOut

router = APIRouter()


@router.get("/equipment", response_model=List[EquipmentOut])
def get_all_equipment(db: Session = Depends(get_db)):
    equipment_list = db.query(Equipment).all()
    return equipment_list
