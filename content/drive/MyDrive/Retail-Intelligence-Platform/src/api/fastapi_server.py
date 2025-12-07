
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Retail Intelligence API Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
