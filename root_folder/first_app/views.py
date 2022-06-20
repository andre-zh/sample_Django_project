from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def simple(request):
    return HttpResponse("This is a response created by Zit!")

def temp(request):
    return render(request, 'first_app/example.html') # connect html in template/first_app folder