from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.ParkingTransaction)
def create_parking_transaction(parking_transaction: schemas.ParkingTransactionCreate, db: Session = Depends(get_db)):
    return crud.create_parking_transaction(db=db, parking_transaction=parking_transaction)

@router.get("/", response_model=list[schemas.ParkingTransaction])
def read_parking_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    parking_transactions = crud.get_parking_transactions(db, skip=skip, limit=limit)
    return parking_transactions

@router.get("/durations", response_model=List[schemas.DurationHistogram])
def read_duration_histogram(db: Session = Depends(get_db)):
    results = crud.get_duration_histogram(db)
    
    if not results:
        raise HTTPException(status_code=404, detail="No data found")

    return results