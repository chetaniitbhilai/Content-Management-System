from fastapi import FastAPI
from . import models
from .database import engine
from .routers import articles
from .routers import auth

app = FastAPI(title="Content Management System")

models.Base.metadata.create_all(bind=engine)

app.include_router(articles.router)
app.include_router(auth.router)  

@app.get("/")
def root():
    return {"message": "CMS Backend is running"}
