from pydantic import BaseModel


class AccountCreate(BaseModel):
    firstName: str
    lastName: str
    accountNumber: int


class Account(BaseModel):
    id: str
    firstName: str
    lastName: str
    accountNumber: int
