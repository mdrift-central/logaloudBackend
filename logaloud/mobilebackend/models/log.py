from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
    action = models.CharField(max_length=50)
    action_details = models.CharField(max_length=255)
    action_by = models.ForeignKey(to=User)
    created_date = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.action_by.username

    def to_dct(self):
        dct = {}
        dct['log_id'] = self.id
        return dct
