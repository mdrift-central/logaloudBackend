from django.conf.urls import url, include


urlpatterns = [
	url('', include('mobilebackend.urls.index')),
	url('', include('mobilebackend.urls.mobileapi')),
]