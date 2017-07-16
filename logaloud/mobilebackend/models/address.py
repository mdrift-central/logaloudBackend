from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.ForeignKey(to=User)
    type = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.street + '  ' + self.city + ' ' + self.country

    def to_dct(self):
        dct = {}
        dct['address_id'] = self.address_id
        return dct

    