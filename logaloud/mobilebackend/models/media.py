from django.db import models
from django.contrib.auth.models import User
from .listing import Listing


MEDIA_TYPES = (('MobileHomePage','MobileHomePage'),('Gallery','Gallery'),('thumbnail','thumbnail'), 
    ('great_perks_cover',' great_perks_cover'), ('featured_cover','featured_cover'))


class Media(models.Model):
    image_path = models.CharField(max_length=500)
    listing = models.ForeignKey(to=Listing,default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    media_type  = models.CharField(choices=MEDIA_TYPES, max_length=100, default='Gallery')
    
    def __unicode__(self):
        return self.listing.listing_name + ' - ' + self.media_type

    def image_img(self):
        if self.image_path:
            return u'<img src="%s" height="120" width="120">' % self.image_path
    
    image_img.short_description = 'Image'
    image_img.allow_tags = True

            #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
