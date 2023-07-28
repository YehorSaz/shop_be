from core.enums.token_enum import TokenEnum
from core.tokens.action_token import ActionToken


class ActivateToken(ActionToken):
    token_type = TokenEnum.ACTIVATE.token_type
    lifetime = TokenEnum.ACTIVATE.life_time
