from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def simple(request):
    return HttpResponse("This is a response created by Zit!")