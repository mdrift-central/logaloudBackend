from django.db import models
from django.contrib.auth.models import User
from .trip import Trip
from .listing import Listing


class TripItem(models.Model):
    trip = models.ForeignKey(to=Trip)
    listing = models.ForeignKey(to=Listing)
    tripItem_start_date = models.DateTimeField(auto_now=False)
    tripItem_end_date = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    tripItem_image = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username

    def to_dct(self):
        dct = {}
        dct['tripItem_id'] = self.trip_id
        return dct
