import binascii, os
from src.models import Users
from django.db import models
from django.core import exceptions as django_exc
TOKEN_LENGTH = 40

class UsersTokenManager(models.Manager):

    def generate_access_token(self):
        return binascii.hexlify(os.urandom(int(TOKEN_LENGTH / 2))).decode()

    def get_access_token(self, user_id=None, access_token=None):
        if Users:
            return UsersToken.objects.get(user_id=user_id)
        elif access_token:
            return UsersToken.objects.get(access_token=access_token)
        raise django_exc.ObjectDoesNotExist('access token object does not exists')


class UsersToken(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    # access token should be unique
    access_token = models.CharField(max_length=TOKEN_LENGTH, db_index=True, unique=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, unique=True)
    objects = UsersTokenManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = UsersToken.objects.generate_access_token()
        return super(UsersToken, self).save(*args, **kwargs)

    def updateAccessToken(self, *args, **kwargs):
        new_token = binascii.hexlify(os.urandom(int(TOKEN_LENGTH / 2))).decode()
        self.access_token = new_token
        self.save()

    def __unicode__(self):
        return self.access_token

    class Meta:
        db_table = 'users_access_token'
        app_label = 'src'
