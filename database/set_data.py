import asyncio
from database.db_config import async_session
from datetime import datetime
from methods import add_bot, get_bot, delete_bot, update_bot
from methods import add_chat, get_chat, get_prompt, set_prompt
from methods import add_message, get_message, update_message, get_messages_for_chat


async def add_bots():
    async with async_session() as session:
        while True:
            bot_id: int = int(input("Enter bot id: "))
            name: str = input("Enter name bot's here: ")
            role: str = input("Enter role bot's here: ")
            signal: bool = bool(input("Enter 1 if bot does signal, or 0 if bot doesn't signal: "))
            main: bool = bool(int(input("Enter 1 if bot is main, or 0 if bot isn't main: ")))
            await add_bot(session,bot_id, name, role, signal, main)
            q: str = input("Enter q for ending: ")

            if q == 'q':
                break


async def add_chats():
    async with async_session() as session:
        while True:
            chat_id: int = int(input("Enter chat id: "))
            prompt: str = input("Enter promtp for chat: ")
            name: str = input("Enter name chat's here: ")

            await add_chat(session, chat_id, prompt, name)

            q: str = input("Enter q for ending: ")

            if q == 'q':
                break


async def update_bots():
    async with async_session() as session:
        while True:
            bot_id: int = int(input("Enter bot id: "))
            main: bool = bool(int(input("Enter 1 if bot is main, or 0 if bot isn't main: ")))
            role: str = input("Enter role bots here: ")
            await update_bot(session, bot_id=bot_id, role=role, main=main)
            q: str = input("Enter q for ending: ")

            if q == 'q':
                break


asyncio.run(add_chats())
