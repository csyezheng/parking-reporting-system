from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def get_parking_lot(db: Session, parking_lot_id: int):
    return db.query(models.ParkingLot).filter(models.ParkingLot.id == parking_lot_id).first()

def get_parking_lots(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ParkingLot).offset(skip).limit(limit).all()

def create_parking_lot(db: Session, parking_lot: schemas.ParkingLotCreate):
    db_parking_lot = models.ParkingLot(**parking_lot.dict())
    db.add(db_parking_lot)
    db.commit()
    db.refresh(db_parking_lot)
    return db_parking_lot

def get_occupancy_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.OccupancyRecord).offset(skip).limit(limit).all()

def create_occupancy_record(db: Session, occupancy_record: schemas.OccupancyRecordCreate):
    db_occupancy_record = models.OccupancyRecord(**occupancy_record.dict())
    db.add(db_occupancy_record)
    db.commit()
    db.refresh(db_occupancy_record)
    return db_occupancy_record

def get_revenue_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.RevenueRecord).offset(skip).limit(limit).all()

def create_revenue_record(db: Session, revenue_record: schemas.RevenueRecordCreate):
    db_revenue_record = models.RevenueRecord(**revenue_record.dict())
    db.add(db_revenue_record)
    db.commit()
    db.refresh(db_revenue_record)
    return db_revenue_record

def get_parking_transactions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ParkingTransaction).offset(skip).limit(limit).all()

def create_parking_transaction(db: Session, parking_transaction: schemas.ParkingTransactionCreate):
    db_parking_transaction = models.ParkingTransaction(**parking_transaction.dict())
    db.add(db_parking_transaction)
    db.commit()
    db.refresh(db_parking_transaction)
    return db_parking_transaction

def get_duration_histogram(db: Session, skip: int = 0, limit: int = 10):
    results = db.query(
        models.ParkingTransaction.parking_lot_id,
        func.date_part('hour', models.ParkingTransaction.duration).label('hours'),
        func.count(models.ParkingTransaction.id).label('count')
    ).group_by('hours').all()
    return results

def get_turnover_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TurnoverRecord).offset(skip).limit(limit).all()

def create_turnover_record(db: Session, turnover_record: schemas.TurnoverRecordCreate):
    db_turnover_record = models.TurnoverRecord(**turnover_record.dict())
    db.add(db_turnover_record)
    db.commit()
    db.refresh(db_turnover_record)
    return db_turnover_record

def get_peak_usage_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PeakUsageRecord).offset(skip).limit(limit).all()

def create_peak_usage_record(db: Session, peak_usage_record: schemas.PeakUsageRecordCreate):
    db_peak_usage_record = models.PeakUsageRecord(**peak_usage_record.dict())
    db.add(db_peak_usage_record)
    db.commit()
    db.refresh(db_peak_usage_record)
    return db_peak_usage_record

def get_utilization_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.UtilizationRecord).offset(skip).limit(limit).all()

def create_utilization_record(db: Session, utilization_record: schemas.UtilizationRecordCreate):
    db_utilization_record = models.UtilizationRecord(**utilization_record.dict())
    db.add(db_utilization_record)
    db.commit()
    db.refresh(db_utilization_record)
    return db_utilization_record

def get_revenue_distribution_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.RevenueDistributionRecord).offset(skip).limit(limit).all()

def create_revenue_distribution_record(db: Session, revenue_distribution_record: schemas.RevenueDistributionRecordCreate):
    db_revenue_distribution_record = models.RevenueDistributionRecord(**revenue_distribution_record.dict())
    db.add(db_revenue_distribution_record)
    db.commit()
    db.refresh(db_revenue_distribution_record)
    return db_revenue_distribution_record

def get_comparative_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ComparativeRecord).offset(skip).limit(limit).all()

def create_comparative_record(db: Session, comparative_record: schemas.ComparativeRecordCreate):
    db_comparative_record = models.ComparativeRecord(**comparative_record.dict())
    db.add(db_comparative_record)
    db.commit()
    db.refresh(db_comparative_record)
    return db_comparative_record
