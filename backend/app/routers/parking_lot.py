from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/parking_lots",
    tags=["parking_lots"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.ParkingLot)
def create_parking_lot(parking_lot: schemas.ParkingLotCreate, db: Session = Depends(get_db)):
    return crud.create_parking_lot(db=db, parking_lot=parking_lot)

@router.get("/", response_model=list[schemas.ParkingLot])
def read_parking_lots(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    parking_lots = crud.get_parking_lots(db, skip=skip, limit=limit)
    return parking_lots

@router.get("/{parking_lot_id}", response_model=schemas.ParkingLot)
def read_parking_lot(parking_lot_id: int, db: Session = Depends(get_db)):
    db_parking_lot = crud.get_parking_lot(db, parking_lot_id=parking_lot_id)
    if db_parking_lot is None:
        raise HTTPException(status_code=404, detail="Parking lot not found")
    return db_parking_lot
