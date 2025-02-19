from datetime import datetime
from database.models import Message

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def add_message(session: AsyncSession,
                      message_id: int,
                      chat_id: int,
                      user_id: int,
                      text: str,
                      user_name: str | None = None,
                      time: datetime | None = None) -> Message:
    message = await get_message(session, message_id)
    if message:
        print(message)
        quit()

    message = Message(
        id=message_id,
        chat_id=chat_id,
        user_id=user_id,
        user_name=user_name,
        text=text,
        time=time if time else datetime.now()
    )

    session.add(message)
    try:
        await session.commit()
    except:
        await session.rollback()

    return message


async def get_message(session: AsyncSession, message_id: int) -> Message | None:
    message = await session.get(Message, message_id)

    return message if message else None


async def get_messages_for_chat(session: AsyncSession, chat_id: int, limit=10):
    query_messages = await session.execute(
        select(Message).where(Message.chat_id == chat_id).order_by(Message.time.desc()).limit(limit)
    )

    messages = query_messages.scalars().unique().all()

    return messages


async def update_message(session: AsyncSession, message_id: int, text: str) -> bool:
    message = await get_message(session, message_id)
    if not message:
        return False

    message.text = text
    await session.commit()
    return True
