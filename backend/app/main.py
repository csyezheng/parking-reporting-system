from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import parking_lot, occupancy, revenue, transactions, turnover, peak_usage, utilization, revenue_distribution, comparative
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to match your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(parking_lot.router)
app.include_router(occupancy.router)
app.include_router(revenue.router)
app.include_router(transactions.router)
app.include_router(turnover.router)
app.include_router(peak_usage.router)
app.include_router(utilization.router)
app.include_router(revenue_distribution.router)
app.include_router(comparative.router)
