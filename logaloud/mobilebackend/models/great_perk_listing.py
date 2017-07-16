#listing_id,business_name,listing_description,owner_id
#listing_location,listing_longitude,listing_latitude,category_id
#host_highlight,additional_info,created_date,modified_date
#featured,is_active


from django.db import models
from django.contrib.auth.models import User
from .address import Address
from .listing import Listing
from .media import Media
from .business_connection import Connection


class GreatPerkListing(models.Model):
    owner = models.ForeignKey(to=User)
    listing = models.ForeignKey(to=Listing) # perk offered from
    cover_image = models.ForeignKey(to=Media)
    perk_image_url = models.CharField(max_length=200)
    additional_info = models.CharField(max_length=500)
