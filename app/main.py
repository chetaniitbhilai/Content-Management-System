from fastapi import FastAPI
from .database import engine

app = FastAPI(title="Content Management System")

@app.get("/")
def root():
    return {"message": "CMS Backend is running"}
