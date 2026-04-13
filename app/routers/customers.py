from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import get_db
from .. import crud
from ..schemas import CustomerCreate, CustomerUpdate, CustomerOut

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create(data: CustomerCreate, db: Session = Depends(get_db)):
    exists = crud.get_customer_by_email(db, str(data.email))
    if exists:
        raise HTTPException(status_code=409, detail="Email já cadastrado.")
    return crud.create_customer(db, data)

@router.get("", response_model=list[CustomerOut])
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.list_customers(db, skip=skip, limit=limit)

@router.get("/{customer_id}", response_model=CustomerOut)
def get_one(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return customer

@router.put("/{customer_id}", response_model=CustomerOut)
def update(customer_id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

    if data.email is not None:
        other = crud.get_customer_by_email(db, str(data.email))
        if other and other.id != customer_id:
            raise HTTPException(status_code=409, detail="Email já cadastrado por outro cliente.")

    return crud.update_customer(db, customer, data)

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    crud.delete_customer(db, customer)
    return None