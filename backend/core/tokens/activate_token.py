from .action_token import ActionToken
from ..enums.token_enum import TokenEnum


class ActivateToken(ActionToken):
    token_type = TokenEnum.ACTIVATE.token_type
    lifetime = TokenEnum.ACTIVATE.life_time
