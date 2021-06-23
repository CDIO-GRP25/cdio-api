# GRUPPE 21
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from os import environ as env

from cvengine.edge import CVEngine
from cvengine import serializer as im
from database.mongo import MongoDB

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db  = MongoDB(env['CDIO_MONGO_PASS'])
cv  = CVEngine

@app.post('/upload/')
async def upload(file: UploadFile = File(...)):
    img = im.save(im.load(file.file))
    return StreamingResponse(img, media_type='image/jpg')

@app.post('/board/')
async def upload(file: UploadFile = File(...)):
    gamestate = cv.gamestate_from_board(db, im.load(file.file))
    return JSONResponse(content=gamestate.json())
