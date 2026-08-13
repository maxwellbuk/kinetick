from asyncio import gather, run

from src.entrypoints import start_api, start_bot

async def start_all_services():
    await gather(start_bot(), start_api())

try:
    run(start_all_services())
except KeyboardInterrupt:
    pass