import asyncio

from telethon import TelegramClient
from telethon.tl import custom
from telethon.tl.patched import Message  # reply message

from services import get_gpt_response
from services import calculate_typing_delay

from telethon.tl.types import User


async def reply_message(client: TelegramClient, message: custom.Message, replied_message: Message, me: User):
    response = await get_gpt_response(message.text, replied_message.chat_id, me.id)

    delay = calculate_typing_delay(len(response))
    async with client.action(replied_message.chat_id, 'typing'):
        await asyncio.sleep(delay)
        await message.reply(response)
