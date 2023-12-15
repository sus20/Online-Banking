from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()
port = int(os.getenv("PORT-TRANSACTION", 8002))

to_be_implemented = {"message": "To be implemented"}

@app.get("/ping")
def ping():
    return {"status": "active"}

@app.get("/")
def ping():
    return {"status": "active"}

@app.post("/transfers/from/{from_account_id}/to/{to_account_id}")
def transfer_amount(from_account_id: int, to_account_id: int, amount: float):
    return to_be_implemented

@app.get("/transfers")
def get_all_transfers():
    return to_be_implemented

@app.get("/transfers/{transfer_id}")
def get_specific_transfer(transfer_id: int):
    return to_be_implemented

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
