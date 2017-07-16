from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    role_name = models.CharField(max_length=30)
    role_description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.user.username

    def to_dct(self):
        dct = {}
        dct['role_id'] = self.role_id
        return dct
