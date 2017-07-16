# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mobilebackend.models import Listing, Address, Log, Media, Role, UserProfile
from mobilebackend.models import UserRole, Listing, Trip, TripItem, Perk, BConnection

admin.site.register(Listing)
admin.site.register(Address)
admin.site.register(Log)


admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.register(UserRole)
admin.site.register(Trip)
admin.site.register(TripItem)
admin.site.register(Perk)
admin.site.register(BConnection)

class MediaAdmin(admin.ModelAdmin):
	fields = ('listing', 'media_type','image_path')
	list_display= ('listing', 'media_type','image_img')

admin.site.register(Media, MediaAdmin)

# Register your models here.
""" from .userprofile import UserProfile
from .address import Address
from .log import Log
from .media import Media
from .role import Role
from .userprofile import UserProfile
from .userrole import UserRole
from .listing import Listing
from .trip import Trip
from .trip_item import TripItem
from .listing import Listing
from .perk import Perk
from .business_connection import Connection """