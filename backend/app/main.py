# app/main.py

from fastapi import FastAPI
from app.api.resume import router as resume_router

app = FastAPI(
    title="DreamCareer API"
)

app.include_router(
    resume_router,
    tags=["Resume"]
)


@app.get("/")
def home():
    return {
        "message": "DreamCareer Backend Running"
    }