from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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

@app.post("/")
def hello():
    try:
        return {"200": "post hello"}
    except HTTPException:
        return {"500": "error"}

@app.get("/neko")
def neko(limit: int = 10):
    return {"200": "あれー"}

@app.post("/neko")
def neko(cat: Cat):
    return {"200": cat}


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)