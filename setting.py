import os
from dotenv import load_dotenv

load_dotenv()

BOTS_CONFIG = []


def _create_bot_config_dict(api_id: str, api_hash: str, session: str) -> dict:
    return {
        "API_ID": api_id,
        "API_HASH": api_hash,
        "SESSION": session
    }


def set_bots_config():
    for number in range(len(os.environ)):
        if os.getenv(f'bot_api_id_{number}') and os.getenv(f"bot_api_hash_{number}") and os.getenv(f"session_{number}"):
            bot_config = _create_bot_config_dict(
                os.getenv(f"bot_api_id_{number}"),
                os.getenv(f"bot_api_hash_{number}"),
                os.getenv(f"session_{number}")
            )

            BOTS_CONFIG.append(bot_config)



