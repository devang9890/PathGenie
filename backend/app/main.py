from fastapi import FastAPI
from app.api.routes import resume, ats

app = FastAPI(title="PathGenie API")

app.include_router(resume.router, prefix="/api")
app.include_router(ats.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "PathGenie backend is running 🚀"}