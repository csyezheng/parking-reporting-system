from datetime import date, datetime
from pydantic import BaseModel

class ParkingLotBase(BaseModel):
    name: str
    location: str
    total_spaces: int

class ParkingLotCreate(ParkingLotBase):
    pass

class ParkingLot(ParkingLotBase):
    id: int

    class Config:
        orm_mode = True

class OccupancyRecordBase(BaseModel):
    parking_lot_id: int
    timestamp: datetime
    occupied_spaces: int

class OccupancyRecordCreate(OccupancyRecordBase):
    pass

class OccupancyRecord(OccupancyRecordBase):
    id: int

    class Config:
        orm_mode = True

class RevenueRecordBase(BaseModel):
    parking_lot_id: int
    date: date
    total_revenue: float

class RevenueRecordCreate(RevenueRecordBase):
    pass

class RevenueRecord(RevenueRecordBase):
    id: int

    class Config:
        orm_mode = True

class ParkingTransactionBase(BaseModel):
    parking_lot_id: int
    entry_time: datetime
    exit_time: datetime
    fee: float

class ParkingTransactionCreate(ParkingTransactionBase):
    pass

class ParkingTransaction(ParkingTransactionBase):
    id: int

    class Config:
        orm_mode = True

class TurnoverRecordBase(BaseModel):
    parking_lot_id: int
    timestamp: datetime
    entries: int
    exits: int

class TurnoverRecordCreate(TurnoverRecordBase):
    pass

class TurnoverRecord(TurnoverRecordBase):
    id: int

    class Config:
        orm_mode = True

class PeakUsageRecordBase(BaseModel):
    parking_lot_id: int
    timestamp: datetime
    occupied_spaces: int

class PeakUsageRecordCreate(PeakUsageRecordBase):
    pass

class PeakUsageRecord(PeakUsageRecordBase):
    id: int

    class Config:
        orm_mode = True

class UtilizationRecordBase(BaseModel):
    parking_lot_id: int
    timestamp: datetime
    occupied_spaces: int

class UtilizationRecordCreate(UtilizationRecordBase):
    pass

class UtilizationRecord(UtilizationRecordBase):
    id: int

    class Config:
        orm_mode = True

class RevenueDistributionRecordBase(BaseModel):
    parking_lot_id: int
    date: date
    total_revenue: float

class RevenueDistributionRecordCreate(RevenueDistributionRecordBase):
    pass

class RevenueDistributionRecord(RevenueDistributionRecordBase):
    id: int

    class Config:
        orm_mode = True

class ComparativeRecordBase(BaseModel):
    parking_lot_id: int
    date: date
    occupancy_rate: float
    total_revenue: float

class ComparativeRecordCreate(ComparativeRecordBase):
    pass

class ComparativeRecord(ComparativeRecordBase):
    id: int

    class Config:
        orm_mode = True
