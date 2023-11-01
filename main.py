from fastapi import FastAPI, Body
import logging
from pydantic import BaseModel, Field


class MessageBody(BaseModel):
    message: str = Field(max_length=300)


app = FastAPI()


@app.get("/")
def hello():
    return {"hello": "world"}


@app.post("/message")
def create_message(body: MessageBody = Body(...)):
    print("PRINT", body.message)
    logging.info("LOG", body.message)
    return {"message": body.message, "saved_to_db": False}
