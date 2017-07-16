from django.conf.urls import url
from mobilebackend.views import index as view



urlpatterns = [

    url(r'^new$', view.hi),

]