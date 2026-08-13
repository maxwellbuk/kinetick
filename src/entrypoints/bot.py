from discord import Bot

from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")
KinetickBot = Bot()

async def start_bot():
    await KinetickBot.start(getenv("BOT_TOKEN"))