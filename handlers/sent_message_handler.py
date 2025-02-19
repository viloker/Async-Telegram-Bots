import asyncio


from telethon.tl.custom import Message
from telethon import TelegramClient

from services import get_gpt_response
from services import calculate_typing_delay

from telethon.tl.types import User


async def sent_message_to_chat(client: TelegramClient, message: Message, me: User):
    response = await get_gpt_response(message.text, message.chat_id, me.id)
    await client.send_read_acknowledge(message.chat_id, message)
    delay = calculate_typing_delay(len(response))
    async with client.action(message.chat_id, 'typing'):
        await asyncio.sleep(delay)
        await client.send_message(message.chat_id, response)
