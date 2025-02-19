from database.models import Bot

from sqlalchemy.ext.asyncio import AsyncSession


async def add_bot(session: AsyncSession, bot_id: int, name: str, role: str, signal: bool = False,
                  main: bool = False) -> Bot:
    bot = Bot(
        id=bot_id,
        name=name,
        role=role,
        signal=signal,
        main=main
    )
    session.add(bot)
    await session.commit()
    return bot


async def get_bot(session: AsyncSession, bot_id: int) -> Bot | None:
    bot = await session.get(Bot, bot_id)
    return bot


async def get_bot_name(session: AsyncSession, bot_id: int) -> str:
    bot = await get_bot(session, bot_id)
    if not bot:
        return ''

    return bot.name


async def get_bot_role(session: AsyncSession, bot_id: int) -> str:
    bot = await get_bot(session, bot_id)
    if not bot:
        raise f"Bot with id -> {bot_id} doesn't exists"

    return bot.role


async def bot_is_signal(session: AsyncSession, bot_id: int) -> bool:
    bot = await get_bot(session, bot_id)
    if not bot:
        raise f"Bot with id -> {bot_id} doesn't exists"

    return bot.signal


async def bot_is_main(session: AsyncSession, bot_id: int) -> bool:
    bot = await get_bot(session, bot_id)
    if not bot:
        raise f"Bot with id -> {bot_id} doesn't exists"

    return bot.main


async def delete_bot(session: AsyncSession, bot_id: int) -> bool:
    bot = await get_bot(session, bot_id)

    if not bot:
        raise f"Bot with id -> {bot_id} doesn't exists"

    await session.delete(bot)
    await session.commit()
    return True


async def update_bot(session: AsyncSession,
                     bot_id: int,
                     name: str | None = None,
                     role: str | None = None,
                     signal: bool | None = None,
                     main: bool | None = None) -> bool:
    bot = await get_bot(session, bot_id)

    if not bot:
        raise f"Bot with id -> {bot_id} doesn't exists"

    bot.name = name if name else bot.name
    bot.role = role if role else bot.role
    bot.signal = signal if signal else bot.signal
    bot.main = main if main else bot.main

    session.add(bot)
    await session.commit()

    return True



