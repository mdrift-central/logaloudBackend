#listing_id,business_name,listing_description,owner_id
#listing_location,listing_longitude,listing_latitude,category_id
#host_highlight,additional_info,created_date,modified_date
#featured,is_active


from django.db import models
from django.contrib.auth.models import User
from .address import Address
from .listing import Listing
from .business_connection import BConnection


class Perk(models.Model):
    owner = models.ForeignKey(to=User)
    from_listing = models.ForeignKey(to=Listing) # perk offered from
    ally = models.ForeignKey(to=Listing,null=True, blank=True, related_name='+') #perk offered to
    perk_name = models.CharField(max_length=100)
    perk_description = models.CharField(max_length=200)
    perk_coupon_code = models.CharField(max_length=7)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    perk_image_url = models.CharField(max_length=200)
    additional_info = models.CharField(max_length=500)

