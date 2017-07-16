
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hi(request):
    return HttpResponse("Hello, world. You're at the mobilebackend index.")

