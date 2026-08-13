from fastapi import APIRouter, Depends, HTTPException
from discord.errors import NotFound, Forbidden

from src.utils.bot.api import return_json_about_channel
from src.entrypoints import KinetickBot

async def check_channel_for_requirements(channelID: int) -> None:
    try:
        await KinetickBot.fetch_channel(channelID)
    except NotFound:
        raise HTTPException(
            404,
            f"Канал с ID: {channelID} не был найден. Проверьте канал на существование"
        )
    except Forbidden:
        raise HTTPException(
            403,
            f"У бота нету доступа к каналу с ID: {channelID}. Убедитесь, что бот имеет доступ к указанному каналу"
        )

ChannelAPI = APIRouter(
    prefix = "/channel/{channelID}",
    dependencies=[Depends(check_channel_for_requirements)]
)

@ChannelAPI.get("/get_info")
async def get_info(channelID: int) -> dict:
    return await return_json_about_channel(channelID)