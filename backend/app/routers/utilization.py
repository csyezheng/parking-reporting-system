from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/utilization",
    tags=["utilization"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.UtilizationRecord)
def create_utilization_record(utilization_record: schemas.UtilizationRecordCreate, db: Session = Depends(get_db)):
    return crud.create_utilization_record(db=db, utilization_record=utilization_record)

@router.get("/", response_model=list[schemas.UtilizationRecord])
def read_utilization_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    utilization_records = crud.get_utilization_records(db, skip=skip, limit=limit)
    return utilization_records
