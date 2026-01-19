from fastapi import FastAPI
from app.api import v1

app = FastAPI(title="RasoiMate Backend", version="1.0")

app.include_router(v1.router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"system": "RasoiMate", "status": "online"}