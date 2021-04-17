from rest_framework import permissions
from django.core.exceptions import ValidationError

HTTP_METHOD_POST        = 'POST'
HTTP_METHOD_GET         = 'GET'
HTTP_METHOD_OPTION      = 'OPTION'
HTTP_METHOD_PUT         = 'PUT'
HTTP_METHOD_HEAD        = 'HEAD'
HTTP_METHOD_DELETE      = 'DELETE'

class IsAuthenticatedOrCreate(permissions.BasePermission):
    SAFE_METHODS = [HTTP_METHOD_POST]
    def has_permission(self, request, view):
        return ( request.method in IsAuthenticatedOrCreate.SAFE_METHODS or request.user and request.user.is_authenticated() )


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if (str(request.user) == "AnonymousUser"):
            raise ValidationError("Authentication credentials were not provided.")
        else:
            return ( request.user and request.user.is_authenticated() )
