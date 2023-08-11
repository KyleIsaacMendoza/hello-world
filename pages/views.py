# pages/views.py
from django.shortcuts import render
from django.http import HttpResponse  # import HttpResponse from http


# Create your views here.
def homePageView(request):
    return HttpResponse("Hello, World!")
