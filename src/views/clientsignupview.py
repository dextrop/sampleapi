from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK
from src.lib.customresponse import CustomResponse
from src.lib.loggingmixin import LoggingMixin
from src.controllers import ClientSignupController

class ClientSignupView(LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     mixins.ListModelMixin):

    def post(self, requests):
        Response = ClientSignupController().signup(request_data=requests.data)
        return CustomResponse(message="Signup Api view", payload=Response, code=HTTP_200_OK)
