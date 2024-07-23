from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/comparative",
    tags=["comparative"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.ComparativeRecord)
def create_comparative_record(comparative_record: schemas.ComparativeRecordCreate, db: Session = Depends(get_db)):
    return crud.create_comparative_record(db=db, comparative_record=comparative_record)

@router.get("/", response_model=list[schemas.ComparativeRecord])
def read_comparative_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comparative_records = crud.get_comparative_records(db, skip=skip, limit=limit)
    return comparative_records
