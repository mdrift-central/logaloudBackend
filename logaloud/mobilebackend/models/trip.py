from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    trip_name = models.CharField(max_length=30)
    trip_description = models.CharField(max_length=255)
    trip_start_date = models.DateTimeField(auto_now=False)
    trip_end_date = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    trip_image = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username

    def to_dct(self):
        dct = {}
        dct['trip_id'] = self.trip_id
        return dct
