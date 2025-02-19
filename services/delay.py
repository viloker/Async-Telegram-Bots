import random

TYPING_DELAY_RULES = [
    (1, 5, (2, 5)),
    (6, 20, (5, 20)),
    (21, 50, (15, 30)),
    (51, 100, (30, 50)),
    (101, 200, (40, 60)),
    (201, 500, (50, 120)),
    (501, 1000, (120, 240)),
]


def calculate_typing_delay(text_length: int, max_time_renge: list | tuple = (180, 300)) -> int:
    if text_length > 1000:
        return random.randrange(*max_time_renge)

    for min_len, max_len, time_range in TYPING_DELAY_RULES:
        if min_len <= text_length <= max_len:
            return random.randrange(*time_range)
