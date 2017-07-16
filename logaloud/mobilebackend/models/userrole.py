from django.db import models
from django.contrib.auth.models import User
from .role import Role


class UserRole(models.Model):
    user = models.OneToOneField(to=User)
    role = models.ForeignKey(to=Role)


    def __unicode__(self):
        return self.user.username

    def to_dct(self):
        dct = {}
        dct['userrole_id'] = self.userrole_id
        return dct