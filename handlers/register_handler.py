from telethon import events
from telethon.tl.custom import Message
from telethon import TelegramClient
from telethon.tl.types import User

from database.methods import add_message
from database.methods import bot_is_main, bot_is_signal, get_bot_name
from database.db_config import async_session

from handlers.reply_handler import reply_message
from handlers.sent_message_handler import sent_message_to_chat

TEST_CHANNEL_ID = 00000


async def register_handler(client: TelegramClient):
    me: User = (await client.get_me())
    async with async_session() as session:
        me.commit = await bot_is_main(session, me.id)


    @client.on(events.NewMessage(chats=TEST_CHANNEL_ID))
    async def message_handler(event: events.NewMessage.Event) -> None:
        message: Message = event.message
        async with async_session() as session:
            user_name = await get_bot_name(session, message.from_id.user_id)
        message.user_name = user_name

        if me.commit:
            async with async_session() as session:
                await add_message(session,
                                  message_id=message.id,
                                  chat_id=message.chat_id,
                                  user_id=message.from_id.user_id,
                                  user_name=message.user_name,
                                  text=message.text,
                                  time=message.date)

        if message.is_reply:
            replied_message = await message.get_reply_message()

            if replied_message.sender_id == me.id:
                await reply_message(client, message, replied_message, me)

        if await bot_is_signal(session, message.from_id.user_id):
            await sent_message_to_chat(client, message, me)

        else:
            print('Невідома дія')
