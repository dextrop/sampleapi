from src.helpers import *
from src.serializers import UsersSerializer
from src.models import Users

model_fields = ["email", "password", "name", "type"]
class ClientSignupController():
    def __init__(self):
        self.serializer = UsersSerializer()

    def signup(self, request_data):
        """
        Validate API request
        check if user already exits in db
        hash password and create salt
        add object to db and return session
        """
        validate_request(model_fields, request_data)
        user = self.serializer.check_if_user_exits(
            email= request_data["email"]
        )
        
        if user != None:
            raise ValidationError("User already exits, Try login in")
        request_data["password"], request_data["salt"] = password_hashing(request_data["password"])
        created = Users.objects.create(**request_data)
        return UsersSerializer().generate_session(created)
