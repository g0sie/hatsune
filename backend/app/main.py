from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RequestData

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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/test')
def test_echo():
    return {'data': 'testing'}


@app.post('/ping')
async def ping_echo(data: RequestData):
    print(data)
    return data
