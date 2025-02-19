from telethon import TelegramClient
from telethon.sessions import StringSession
from setting import set_bots_config, BOTS_CONFIG


async def create_clients() -> list[TelegramClient]:
    set_bots_config()

    clients = []

    for bot_config in BOTS_CONFIG:
        async with TelegramClient(StringSession(bot_config['SESSION']),
                                  api_id=bot_config['API_ID'],
                                  api_hash=bot_config['API_HASH']) as client:
            clients.append(client)

    return clients
