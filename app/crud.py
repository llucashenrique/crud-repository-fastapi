from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Customer
from .schemas import CustomerCreate, CustomerUpdate

def create_customer(db: Session, data: CustomerCreate) -> Customer:
    customer = Customer(name=data.name, email=str(data.email))
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def list_customers(db: Session, skip: int = 0, limit: int = 20) -> list[Customer]:
    stmt = select(Customer).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())

def get_customer(db: Session, customer_id: int) -> Customer | None:
    return db.get(Customer, customer_id)

def get_customer_by_email(db: Session, email: str) -> Customer | None:
    stmt = select(Customer).where(Customer.email == email)
    return db.scalars(stmt).first()

def update_customer(db: Session, customer: Customer, data: CustomerUpdate) -> Customer:
    if data.name is not None:
        customer.name = data.name
    if data.email is not None:
        customer.email = str(data.email)

    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer: Customer) -> None:
    db.delete(customer)
    db.commit()