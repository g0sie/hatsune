from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestData(BaseModel):
    text: str


@app.get('/')
def index():
    return {"Hello": "World"}


@app.get('/test')
def test_echo():
    return {'data': 'testing'}


@app.post('/ping')
async def ping_echo(data: RequestData):
    print(data)
    return data


@app.get('/numbers/{numbers}')
def number(numbers: int):
    return [{'number': number} for number in range(0, numbers + 1)]


# http://127.0.0.1:8000/login?username=admin&password=admin
@app.get('/login')
def login(username: Optional[str] = None, password: Optional[str] = None):
    logged = True if username == 'admin' and password == 'admin' else False
    return {'logged': logged}


class User(BaseModel):
    username: str
    password: str


@app.post('/register')
def register(user: User):
    return {user.username: 'registered'}
