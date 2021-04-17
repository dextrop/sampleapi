from src.models import Users, UsersToken
from rest_framework import authentication
from rest_framework import exceptions

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        _token = request.META.get("HTTP_TOKEN", False)
        if _token:
            try:
                tokens = UsersToken.objects.filter(access_token=_token)
                if tokens.count() < 1:
                    raise exceptions.AuthenticationFailed('Invalid access token')
                token = tokens[0]
            except Exception as e:
                raise exceptions.AuthenticationFailed('Invalid access token')
            user_id = token.user_id            
            user = Users.objects.get(_id=user_id._id)
            return (user, token)

    def authenticate_header(self, request):
        return ['token']