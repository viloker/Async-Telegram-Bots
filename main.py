from bots_client import create_clients
import asyncio

from telethon import TelegramClient
from handlers.register_handler import register_handler


async def start_bot(client: TelegramClient):
    await client.start()
    await register_handler(client)
    await client.run_until_disconnected()


async def main():
    tasks = [start_bot(client) for client in await create_clients()]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
