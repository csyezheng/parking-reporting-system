from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/turnover",
    tags=["turnover"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.TurnoverRecord)
def create_turnover_record(turnover_record: schemas.TurnoverRecordCreate, db: Session = Depends(get_db)):
    return crud.create_turnover_record(db=db, turnover_record=turnover_record)

@router.get("/", response_model=list[schemas.TurnoverRecord])
def read_turnover_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    turnover_records = crud.get_turnover_records(db, skip=skip, limit=limit)
    return turnover_records
