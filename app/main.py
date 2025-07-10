from fastapi import FastAPI
from . import models
from .database import engine

app = FastAPI(title="Content Management System")

# Create tables on startup
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "CMS Backend is running"}
