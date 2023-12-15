from fastapi import FastAPI
from dotenv import dotenv_values
import uvicorn

# Create an instance of the FastAPI class
app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "active"}

@app.get("/")
def ping():
    return {"status": "active"}

if __name__ == "__main__":
    env_vars = dotenv_values(".env")

    port = int(env_vars.get("PORT_ACCOUNT", 8000))

    
    uvicorn.run(app, host="0.0.0.0", port=port)
