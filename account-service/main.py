from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()
port = int(os.getenv("PORT-ACCOUNT", 8000))

# Placeholder responses
to_be_implemented = {"message": "To be implemented"}

@app.get("/ping")
def ping():
    return {"status": "active"}

@app.get("/")
def ping():
    return {"status": "active"}

# Create Account
@app.post("/accounts")
def create_account():
    return to_be_implemented

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
