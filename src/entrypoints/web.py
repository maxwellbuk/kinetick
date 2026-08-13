from src.api import ChannelAPI

from uvicorn import Config, Server
from fastapi import FastAPI

KinetickAPI = FastAPI()

KinetickAPI.include_router(ChannelAPI)

async def start_api():
    await Server(Config(
        KinetickAPI
    )).serve()