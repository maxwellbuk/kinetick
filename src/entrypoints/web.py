from uvicorn import Config, Server
from fastapi import FastAPI

KinetickAPI = FastAPI()

async def start_api():
    await Server(Config(
        KinetickAPI
    )).serve()