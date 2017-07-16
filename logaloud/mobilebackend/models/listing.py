#listing_id,business_name,listing_description,owner_id
#listing_location,listing_longitude,listing_latitude,category_id
#host_highlight,additional_info,created_date,modified_date
#featured,is_active


from django.db import models
from django.contrib.auth.models import User
from .address import Address

LISTING_TYPES = (('Normal','Normal'),('Ally','Ally'),('Admin_test','Admin_test'),('Great Perks','Great Perks'))


class Listing(models.Model):
    owner = models.ForeignKey(to=User)
    listing_type = models.CharField(choices=LISTING_TYPES, max_length=100)
    listing_short_title = models.CharField(max_length=100)
    listing_name = models.CharField(max_length=100)
    listing_address = models.ForeignKey(to=Address)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    additional_info = models.CharField(max_length=500)


    def __unicode__(self):
        return self.listing_name

    def to_dct(self):
        dct = {}
        dct['address_id'] = self.listing_name
        return dct


