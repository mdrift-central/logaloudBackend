
from django.db import models
from django.contrib.auth.models import User
from .address import Address
from .listing import Listing 


class BConnection(models.Model):
    created_by = models.ForeignKey(to=User)
    listing = models.ForeignKey(to=Listing)
    ally = models.ForeignKey(to=Listing,null=True, blank=True, related_name='+')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    additional_info = models.CharField(max_length=500)

    def __unicode__(self):
  		return self.listing.listing_name + '(listing) + (ally)' + self.ally.listing_name