from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()
port = int(os.getenv("PORT-NOTIFICATION", 8001))

to_be_implemented = {"message": "To be implemented"}

@app.get("/ping")
def ping():
    return {"status": "active"}

@app.get("/")
def ping():
    return {"status": "active"}

@app.get("/notifications")
def get_notifications():
    return to_be_implemented

# Get Specific Notification
@app.get("/notifications/{notification_id}")
def get_specific_notification(notification_id: int):
    return to_be_implemented

# Post Notification
@app.post("/notifications")
def post_notification(message: str):
    return to_be_implemented

if __name__ == "__main__":    
    uvicorn.run(app, host="0.0.0.0", port=port)