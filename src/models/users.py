from django.db import models

class Users(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)

    email = models.CharField(default="", max_length=200)
    password = models.CharField(default="", max_length=200)
    salt = models.CharField(default="", max_length=16)
    name = models.CharField(default="", max_length=200)
    type = models.IntegerField(default=0)
    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Users, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self._id)

    class Meta:
        db_table = 'users'
        app_label = 'src'
