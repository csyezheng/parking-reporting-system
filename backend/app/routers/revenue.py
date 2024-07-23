from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/revenue",
    tags=["revenue"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.RevenueRecord)
def create_revenue_record(revenue_record: schemas.RevenueRecordCreate, db: Session = Depends(get_db)):
    return crud.create_revenue_record(db=db, revenue_record=revenue_record)

@router.get("/", response_model=list[schemas.RevenueRecord])
def read_revenue_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    revenue_records = crud.get_revenue_records(db, skip=skip, limit=limit)
    return revenue_records
