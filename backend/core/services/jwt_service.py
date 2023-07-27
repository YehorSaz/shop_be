from rest_framework.generics import get_object_or_404

from core.exceptions.jwt_exception import JWTException
from core.tokens.action_token import ActionTokenType

from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class JWTService:
    @staticmethod
    def create_token(user, token_class: ActionTokenType):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: ActionTokenType):
        try:
            token = token_class(token)
            token.check_blacklist()
        except (Exception,):
            raise JWTException

        token.blacklist()
        user_id = token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
