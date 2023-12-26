from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models.account import AccountCreate, Account
from bson import ObjectId
import logging
import uvicorn
import os

app = FastAPI()
port = int(os.getenv("PORT-ACCOUNT", 8000))


def setup_mongo_client():
    try:
        client = MongoClient("mongodb://localhost:27017")
        db = client["online_banking"]
        accounts_collection = db["accounts"]
        logging.info("Connected to MongoDB successfully")
        return client, accounts_collection
    except Exception as e:
        logging.error(f"Error connecting to MongoDB: {e}")
        raise


# Call setup_mongo_client during app startup
@app.on_event("startup")
def startup_event():
    global client, accounts_collection
    client, accounts_collection = setup_mongo_client()


# Close the MongoDB client during app shutdown
@app.on_event("shutdown")
def shutdown_event():
    global client
    client.close()
    logging.info("Closed MongoDB connection during shutdown")


# Placeholder responses
to_be_implemented = {"message": "To be implemented"}


@app.get("/ping")
def ping():
    return {"status": "active"}


@app.get("/")
def ping():
    return {"status": "active"}

# Create Account


def create_account_instance(account_data: AccountCreate, account_id: ObjectId) -> Account:
    return Account(
        id=str(account_id),
        firstName=account_data.firstName,
        lastName=account_data.lastName,
        accountNumber=account_data.accountNumber,
    )


@app.post("/accounts", response_model=Account)
def create_account(account_data: AccountCreate):

    # Check if the accountNumber is already in use
    existing_account = accounts_collection.find_one(
        {"accountNumber": account_data.accountNumber})
    if existing_account:
        raise HTTPException(
            status_code=400, detail="AccountNumber already in use")

    # Save the account details to MongoDB
    result = accounts_collection.insert_one(account_data.dict())
    account_id = result.inserted_id

    # Convert to Account model for response
    created_account = create_account_instance(account_data, account_id)

    return created_account

# Delete Account


@app.delete("/accounts/{account_id}")
def delete_account(account_id: int):
    return to_be_implemented

# Update Account


@app.put("/accounts/{account_id}")
def update_account(account_id: int):
    return to_be_implemented

# Get All Accounts


@app.get("/accounts")
def get_all_accounts():
    return to_be_implemented

# Get One Account


@app.get("/accounts/{account_id}")
def get_one_account(account_id: int):
    return to_be_implemented


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
