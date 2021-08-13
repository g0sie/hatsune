from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"Hello": "World"}

@app.get('/numbers/{numbers}')
def number(numbers: int):
    return [{'number': number} for number in range(0, numbers + 1)]
