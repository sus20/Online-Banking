from fastapi import FastAPI
from dotenv import dotenv_values
import uvicorn

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the GET method at /ping
@app.get("/ping")
def ping():
    return {"status": "active"}

@app.get("/")
def ping():
    return {"status": "active"}

if __name__ == "__main__":
    # Load environment variables from .env file
    env_vars = dotenv_values(".env")

    # Get the port number from the environment variable or use a default port (8000)
    port = int(env_vars.get("PORT_TRANSACTION", 8002))

    
    uvicorn.run(app, host="0.0.0.0", port=port)
