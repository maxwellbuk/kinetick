from src.entrypoints import KinetickBot

async def return_json_about_channel(channelID: int) -> dict:
    channel = await KinetickBot.fetch_channel(channelID)