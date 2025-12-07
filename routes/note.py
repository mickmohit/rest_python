from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schema.note import noteEntity, notesEntity
from fastapi import FastAPI, Request
from typing import Union
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note=APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    newDocs = []
    docs=conn.notes.notes.find({})
    print(docs)
    # Now you can access fields
    for doc in docs:
        print(doc['_id'])
        newDocs.append({
            "id":doc['_id'],
            "title":doc['title'],
            "description":doc['description'],
            "important":doc['important']
        })
       
    return templates.TemplateResponse("index.html", {"request": request, "newdocs" : newDocs})


@note.get("/item/{item_id}")
def read_item(item_id: int, q: str | None=None):
   return {"item_id": item_id, "q":q}


@note.post("/",response_class=HTMLResponse)
async def add_note(note: Note):
    inserted_note = conn.notes.notes.insert_one(dict(note))
    return noteEntity(inserted_note)
