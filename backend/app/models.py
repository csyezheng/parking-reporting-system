from sqlalchemy import Column, Integer, String, Date, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import Base


class ParkingLot(Base):
    __tablename__ = "parking_lots"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    total_spaces = Column(Integer, nullable=False)
    occupancy_records = relationship("OccupancyRecord", back_populates="parking_lot")
    revenue_records = relationship("RevenueRecord", back_populates="parking_lot")
    transactions = relationship("ParkingTransaction", back_populates="parking_lot")
    turnover_records = relationship("TurnoverRecord", back_populates="parking_lot")
    peak_usage_records = relationship("PeakUsageRecord", back_populates="parking_lot")
    utilization_records = relationship("UtilizationRecord", back_populates="parking_lot")
    revenue_distribution_records = relationship("RevenueDistributionRecord", back_populates="parking_lot")
    comparative_records = relationship("ComparativeRecord", back_populates="parking_lot")

class OccupancyRecord(Base):
    __tablename__ = "occupancy_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    timestamp = Column(DateTime, nullable=False)
    occupied_spaces = Column(Integer, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="occupancy_records")

class RevenueRecord(Base):
    __tablename__ = "revenue_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    date = Column(Date, nullable=False)
    total_revenue = Column(DECIMAL, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="revenue_records")

class ParkingTransaction(Base):
    __tablename__ = "parking_transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    entry_time = Column(DateTime, nullable=False)
    exit_time = Column(DateTime)
    fee = Column(DECIMAL, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="transactions")

class TurnoverRecord(Base):
    __tablename__ = "turnover_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    timestamp = Column(DateTime, nullable=False)
    entries = Column(Integer, nullable=False)
    exits = Column(Integer, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="turnover_records")

class PeakUsageRecord(Base):
    __tablename__ = "peak_usage_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    timestamp = Column(DateTime, nullable=False)
    occupied_spaces = Column(Integer, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="peak_usage_records")

class UtilizationRecord(Base):
    __tablename__ = "utilization_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    timestamp = Column(DateTime, nullable=False)
    occupied_spaces = Column(Integer, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="utilization_records")

class RevenueDistributionRecord(Base):
    __tablename__ = "revenue_distribution_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    date = Column(Date, nullable=False)
    total_revenue = Column(DECIMAL, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="revenue_distribution_records")

class ComparativeRecord(Base):
    __tablename__ = "comparative_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"))
    date = Column(Date, nullable=False)
    occupancy_rate = Column(DECIMAL, nullable=False)
    total_revenue = Column(DECIMAL, nullable=False)
    parking_lot = relationship("ParkingLot", back_populates="comparative_records")
