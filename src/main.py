from fastapi import FastAPI
from api import *
import uvicorn
import logging

""" Define and setup logger for app. """
log = logging.getLogger(__file__)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api")
def get_all_data():
    d = get_data()
    return d    

@app.get("/api/team/{team}")
def get_team_data(team: str):
    d = get_team(team)
    return d    


if __name__ == '__main__':

    log.info('Starting app...')
    uvicorn.run(app, host='0.0.0.0', port=5000)