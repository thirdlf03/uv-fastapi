from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from icecream import ic
import uvicorn


app = FastAPI()

class Cat(BaseModel):
    name: str
    num: int

@app.get("/")
def hello():
    try:
        return {"200": "hello"}
    except HTTPException:
        return {"500": "error"}
ic(hello())

@app.post("/")
def he():
    try:
        return {"200": "post hello"}
    except HTTPException:
        return {"500": "error"}

ic(he())

@app.get("/neko")
def neko(limit: int = 10):
    return {"200": "あれー"}

ic(neko())

@app.post("/neko")
def nek(cat: Cat):
    return {"200": cat}

ic(nek(Cat))

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
