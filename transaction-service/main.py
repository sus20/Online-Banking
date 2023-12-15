from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()
port = int(os.getenv("PORT-TRANSACTION", 8002))

@app.get("/ping")
def ping():
    return {"status": "active"}

@app.get("/")
def ping():
    return {"status": "active"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
