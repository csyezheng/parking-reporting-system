from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/peak_usage",
    tags=["peak_usage"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PeakUsageRecord)
def create_peak_usage_record(peak_usage_record: schemas.PeakUsageRecordCreate, db: Session = Depends(get_db)):
    return crud.create_peak_usage_record(db=db, peak_usage_record=peak_usage_record)

@router.get("/", response_model=list[schemas.PeakUsageRecord])
def read_peak_usage_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    peak_usage_records = crud.get_peak_usage_records(db, skip=skip, limit=limit)
    return peak_usage_records
