from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK
from src.lib.customresponse import CustomResponse

class StatusView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     mixins.ListModelMixin):

    def get(self, requests):
        Response = True
        return CustomResponse(message="Server Is Up and Running", payload=Response, code=HTTP_200_OK)
