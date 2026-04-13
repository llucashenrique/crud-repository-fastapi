from pydantic import BaseModel, EmailStr, ConfigDict

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr

class CustomerUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class CustomerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr