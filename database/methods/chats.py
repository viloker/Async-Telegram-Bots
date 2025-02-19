from database.models import Chat

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def add_chat(session: AsyncSession, chat_id: int, prompt: str, name: str) -> Chat:

    chat = Chat(
        id=chat_id,
        prompt=prompt,
        name=name
    )
    session.add(chat)
    await session.commit()

    return chat


async def get_chat(session: AsyncSession, chat_id: int) -> Chat | None:
    chat = await session.get(Chat, chat_id)

    return chat


async def get_prompt(session: AsyncSession, chat_id: int) -> str:
    chat = await get_chat(session, chat_id)

    if not chat:
        raise "Chat id {} not exists. May you forget about '-' for id chat".format(chat)

    return chat.prompt


async def set_prompt(session: AsyncSession, chat_id: int, prompt: str) -> Chat:
    chat = await get_chat(session, chat_id)

    if not chat:
        chat = await add_chat(session, chat_id, prompt)

    else:
        chat.prompt = prompt
        await session.commit()

    return chat


async def get_all_chats(session: AsyncSession):
    chats = await session.execute(select(Chat))
    chats = chats.scalars().all()
    return chats
