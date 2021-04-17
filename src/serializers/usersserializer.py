from rest_framework import serializers
from src.helpers import password_hashing
from django.core.exceptions import ValidationError
from src.models import Users, UsersToken

model_fields = ["email", "password", "name", "type"]

class UsersBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        exclude = ('salt', 'password')

class UsersSerializer():
    def validate_email_password(self, email, password):        
        obj = self.check_if_user_exits(email=email)
        if obj == None:
            raise ValidationError("Email Does not exits")
        
        password_req, _ = password_hashing(password, obj.salt)
        if password_req != obj.password:
            raise ValidationError("Invalid Password")
        
        return True
    
    def check_if_user_exits(self, email):
        objects = Users.objects.filter(email=email)
        if (objects.count() < 1):
            return None
        return objects[0]
            
    def generate_session(self, object):        
        token, created = UsersToken.objects.get_or_create(user_id=object)
        user_info = UsersBaseSerializer(object, many=False).data
        user_info["token"] = token.access_token
        return user_info
    
    def modify(self, data):
        # Modify an object based on ID.
        if "_id" not in data:
            raise ValidationError("Missing Object ID")
        obj = self.get(id=data["_id"])
        if obj == None:
            raise ValidationError("Object does not exits check if id is correct")
        for key in model_fields:
            if key != "_id" and key in data:
                setattr(obj, key, data[key])

        obj.save()
        obj = self.get(id=obj._id)
        return UsersBaseSerializer(obj, many=False).data

    def delete(self, data):
        # Delete an object based on ID.
        if "_id" not in data:
            raise ValidationError("Missing Object ID")
        Users.objects.filter(_id=data["_id"]).delete()
        return "Object Deleted Successfully"
