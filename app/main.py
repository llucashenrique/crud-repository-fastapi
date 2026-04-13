from fastapi import FastAPI
from .db import engine
from .models import Customer
from .db import Base
from .routers.customers import router as customers_router

app = FastAPI(title="CRUD Customers - FastAPI + Postgres")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(customers_router)