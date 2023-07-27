from typing import Type

from rest_framework_simplejwt.tokens import BlacklistMixin, Token


ActionTokenType = Type[BlacklistMixin | Token]


class ActionToken(BlacklistMixin, Token):
    pass


