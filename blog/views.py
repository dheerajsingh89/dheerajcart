from django.shortcuts import render
from django.http import HttpResponse
def index(req):
    return HttpResponse("this is blog app")

# Create your views here.
