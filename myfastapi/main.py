from fastapi import FastAPI, Body
import logging
from pydantic import BaseModel, Field
from beanie import init_beanie, Document
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
import os


class MessageBody(BaseModel):
    message: str = Field(max_length=300)


class MessageDB(Document, MessageBody):
    pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(os.environ["DB_CONNECTION_URI"])
    # db_name is anything
    await init_beanie(database=client.myfastapi, document_models=[MessageDB])
    yield
    print("shutting down")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def hello():
    return {"hello": "world"}


@app.get("/messages", response_model=List[MessageBody])
async def list_messages():
    messages = await MessageDB.find().to_list()
    return messages


@app.post("/messages")
async def create_message(body: MessageBody = Body(...)):
    print("PRINT", body.message)
    logging.info("LOG", body.message)
    message_db = MessageDB(message=body.message)
    message_db = await message_db.create()
    if message_db:
        return {"message": body.message, "saved_to_db": True}
    else:
        return {"message": body.message, "saved_to_db": False}
