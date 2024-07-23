from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/revenue_distribution",
    tags=["revenue_distribution"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.RevenueDistributionRecord)
def create_revenue_distribution_record(revenue_distribution_record: schemas.RevenueDistributionRecordCreate, db: Session = Depends(get_db)):
    return crud.create_revenue_distribution_record(db=db, revenue_distribution_record=revenue_distribution_record)

@router.get("/", response_model=list[schemas.RevenueDistributionRecord])
def read_revenue_distribution_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    revenue_distribution_records = crud.get_revenue_distribution_records(db, skip=skip, limit=limit)
    return revenue_distribution_records
