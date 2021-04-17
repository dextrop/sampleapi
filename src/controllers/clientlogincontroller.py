from src.helpers import *
from src.serializers import UsersSerializer
from src.models import Users

model_fields = ["email", "password"]

class ClientLoginController():
    def __init__(self):
        self.serializer = UsersSerializer()

    def login(self, request_data):
        """
        :param request_data: {"email": "", "password"}
        :return: {"user_info": "token": ""}
        """
        validate_request(model_fields, request_data)

        user = self.serializer.check_if_user_exits(
            email= request_data["email"]
        )

        self.serializer.validate_email_password(
            email=request_data["email"], password=request_data["password"]
        )

        return UsersSerializer().generate_session(user)
