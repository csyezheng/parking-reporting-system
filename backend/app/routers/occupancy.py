from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/occupancy",
    tags=["occupancy"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.OccupancyRecord)
def create_occupancy_record(occupancy_record: schemas.OccupancyRecordCreate, db: Session = Depends(get_db)):
    return crud.create_occupancy_record(db=db, occupancy_record=occupancy_record)

@router.get("/", response_model=list[schemas.OccupancyRecord])
def read_occupancy_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    occupancy_records = crud.get_occupancy_records(db, skip=skip, limit=limit)
    return occupancy_records
