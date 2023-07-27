from enum import Enum
from datetime import timedelta


class TokenEnum(Enum):
    ACTIVATE = (
        'activate',
        timedelta(days=1)
    )

    def __init__(self, token_type, life_time):
        self.token_type = token_type
        self.life_time = life_time
