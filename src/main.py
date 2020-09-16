from fastapi import FastAPI
from api import get_data

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api")
def get_all_data():
    d = get_data()
    return d    