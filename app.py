from fastapi import FastAPI

import fastapi

app = FastAPI()

print(fastapi.__file__)


@app.get("/hello")
async def hello():
    return "Hello"
