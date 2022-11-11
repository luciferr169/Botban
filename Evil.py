import logging
import asyncio
from decouple import config
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatBannedRights,
)

API_ID = config("API_ID", default=6, cast=int)
API_HASH = config("API_HASH", None)
BOT_TOKEN = config("BOT_TOKEN", None)
SUDO_USERS = list(map(int, getenv("SUDO").split()))

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


logging.basicConfig(level=logging.INFO)
Evil = TelegramClient('EVIL', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@Evil.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
        await event.delete()
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)
            except Exception as e:
                await asyncio.sleep(0.1)


print("TEAM LEGENDZ OP")

Evil.run_until_disconnected()
