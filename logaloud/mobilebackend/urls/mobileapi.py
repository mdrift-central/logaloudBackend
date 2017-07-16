from django.conf.urls import url
from mobilebackend.views import mobileapi as view



urlpatterns = [

    url(r'^api$', view.hi),
    url(r'^login$',view.mobile_login),
    url(r'^signup$',view.mobile_signup),
    url(r'^getlistings$',view.get_listings),
    url(r'^get_great_perks$',view.get_great_perks),
    url(r'^get_allies_perks$',view.get_allies_and_perks),
	# get_featured
	url(r'^get_featured$',view.get_featured),

]