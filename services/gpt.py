import os
from dotenv import load_dotenv

from openai import OpenAI

from database.methods import get_prompt, get_messages_for_chat, get_bot_role

from database.db_config import async_session


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

GPT = OpenAI(api_key=OPENAI_API_KEY)


async def get_gpt_response(user_message: str,
                           chat_id: int,
                           bot_id: int,
                           limit: int = 5) -> str:
    async with async_session() as session:
        chat_history = await get_messages_for_chat(session, chat_id=chat_id, limit=limit)
        role = await get_bot_role(session, bot_id=bot_id)
        system_prompt = await get_prompt(session, chat_id)

    messages = [{'role': 'system', 'content': role + "\n" + system_prompt},
                {'role': 'user', 'content': user_message}]

    messages += [
        {'role': 'user',
         f'content': f'User({message.user_name if message.user_name else message.user_id}) : {message.text}'}
        for message in chat_history[::-1]]

    try:
        response = GPT.chat.completions.create(
            model='gpt-4o-mini',
            messages=messages
        )
        return response.choices[0].message.content

    except Exception:
        raise Exception("Some error with GPT")
