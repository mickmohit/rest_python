from fastapi import FastAPI, APIRouter
from routes.note import note
from fastapi.staticfiles import StaticFiles


app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
#to call route class with all restendpoints
app.include_router(note)
