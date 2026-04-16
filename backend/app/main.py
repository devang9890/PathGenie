from fastapi import FastAPI

app = FastAPI(title="PathGenie API")

@app.get("/")
def root():
    return {"message": "PathGenie backend is running 🚀"}